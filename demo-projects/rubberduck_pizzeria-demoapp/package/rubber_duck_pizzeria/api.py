"""Kitchen API — intentionally insecure for RubberDuck MCP labs.

UI looks normal; vulns are in handlers and helpers.
"""
from __future__ import annotations

import os
import pickle
import subprocess
from functools import wraps

from flask import Blueprint, jsonify, request, session, make_response, render_template_string

from . import db as dbmod

api = Blueprint("kitchen_api", __name__, url_prefix="/api")


def _cors(resp):
    # Overly permissive CORS — FLAG{RD_CORS_WILDCARD}
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Role, X-Debug"
    return resp


@api.after_request
def add_cors(resp):
    return _cors(resp)


def login_optional(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@api.route("/health")
def health():
    from .services import kitchen_target, promo_enabled, timezone_label

    return jsonify(
        {
            "ok": True,
            "service": "rubber-duck-pizzeria-api",
            "kitchen_target": kitchen_target(),
            "promo_enabled": promo_enabled(),
            "timezone": timezone_label(),
        }
    )


@api.route("/search")
def search():
    """SQLi via q= … FLAG{RD_SQLI_SEARCH}
    Also reflected XSS if format=html … FLAG{RD_XSS_SEARCH}
    """
    q = request.args.get("q", "")
    fmt = request.args.get("format", "json")
    rows = dbmod.search_customers_raw(q)

    # Loud marker for SQL injection discovery
    flag = None
    if "FLAG{RD_SQLI_SEARCH}" in q or "' OR " in q.upper() or "1=1" in q.replace(" ", ""):
        flag = "FLAG{RD_SQLI_SEARCH}"
    # Also reveal when union/injection dumped notes of admin mirror
    for r in rows:
        if r.get("is_admin") == 1 or "Internal staff" in (r.get("notes") or ""):
            flag = "FLAG{RD_SQLI_SEARCH}"
            r["secret_note"] = "FLAG{RD_SQLI_SEARCH}"

    if fmt == "html":
        # Reflected XSS sink — intentionally unescaped
        html = f"""
        <section class="search-results">
          <h4>Results for: {q}</h4>
          <ul>
            {''.join(f"<li>{r.get('name')} — {r.get('location')}</li>" for r in rows) or '<li>No matches</li>'}
          </ul>
          <!-- kitchen search widget -->
        </section>
        """
        if "<script>" in q.lower() or "onerror=" in q.lower():
            html += "<!-- FLAG{RD_XSS_SEARCH} -->"
        resp = make_response(html)
        resp.headers["Content-Type"] = "text/html; charset=utf-8"
        return resp

    payload = {"query": q, "count": len(rows), "results": rows}
    if flag:
        payload["flag"] = flag
    return jsonify(payload)


@api.route("/reviews", methods=["GET", "POST"])
def reviews():
    if request.method == "GET":
        status = request.args.get("status", "published")
        return jsonify({"reviews": dbmod.list_reviews(status)})

    data = request.get_json(silent=True) or request.form
    name = data.get("customer_name") or data.get("name") or "Guest"
    body = data.get("body") or data.get("review") or ""
    rating = float(data.get("rating") or 5)
    # Stored XSS — body stored & later rendered unsafe — FLAG{RD_XSS_STORED}
    code = dbmod.add_review(name, body, rating)
    out = {"ok": True, "review_code": code}
    if "<script>" in body.lower() or "onerror=" in body.lower():
        out["flag"] = "FLAG{RD_XSS_STORED}"
    return jsonify(out)


@api.route("/orders/<int:order_id>")
def order_detail(order_id: int):
    """IDOR — no auth / ownership check. FLAG{RD_IDOR_ORDER}"""
    data = dbmod.get_order_by_id(order_id)
    if not data:
        return jsonify({"error": "not found"}), 404
    return jsonify(data)


@api.route("/customers/<int:customer_id>", methods=["PATCH", "POST"])
def customer_update(customer_id: int):
    """Mass assignment. FLAG{RD_MASS_ASSIGN}"""
    payload = request.get_json(silent=True) or {}
    updated = dbmod.update_customer(customer_id, payload)
    if not updated:
        return jsonify({"error": "not found"}), 404
    return jsonify(updated)


@api.route("/login", methods=["POST"])
def login():
    """Weak MD5 passwords — FLAG{RD_WEAK_HASH}
    Hardcoded debug bypass — FLAG{RD_HARDCODED_BYPASS}
    """
    data = request.get_json(silent=True) or request.form
    username = data.get("username", "")
    password = data.get("password", "")

    # Debug backdoor
    if username == "debug" and password == "rd-debug-2026":
        session["user"] = {"username": "debug", "role": "manager", "is_admin": 1}
        return jsonify(
            {
                "ok": True,
                "user": session["user"],
                "flag": "FLAG{RD_HARDCODED_BYPASS}",
                "hash_algo": "md5",
            }
        )

    user = dbmod.verify_staff(username, password)
    if not user:
        return jsonify({"ok": False, "error": "invalid credentials"}), 401

    session["user"] = {
        "username": user["username"],
        "role": user["role"],
        "is_admin": user["is_admin"],
    }
    out = {"ok": True, "user": session["user"], "hash_algo": "md5"}
    if user["username"] == "admin":
        out["flag"] = "FLAG{RD_WEAK_HASH}"
    return jsonify(out)


@api.route("/admin/stats")
def admin_stats():
    """Broken access control — trusts client header. FLAG{RD_BAC_HEADER}"""
    role = request.headers.get("X-Role", session.get("user", {}).get("role", "guest"))
    if role.lower() in {"manager", "admin", "staff"}:  # staff should not see admin
        conn = dbmod.get_connection()
        try:
            orders = conn.execute("SELECT COUNT(*) AS c FROM orders").fetchone()["c"]
            revenue = conn.execute("SELECT SUM(amount) AS s FROM orders").fetchone()["s"] or 0
            customers = conn.execute("SELECT COUNT(*) AS c FROM customers").fetchone()["c"]
        finally:
            conn.close()
        payload = {
            "role": role,
            "orders": orders,
            "revenue": float(revenue),
            "customers": customers,
        }
        if role.lower() != "manager" or request.headers.get("X-Role"):
            payload["flag"] = "FLAG{RD_BAC_HEADER}"
        return jsonify(payload)
    return jsonify({"error": "forbidden"}), 403


@api.route("/report")
def kitchen_report():
    """Command injection via name= … FLAG{RD_CMDI_REPORT}"""
    name = request.args.get("name", "daily")
    # Intentionally unsafe
    cmd = f"echo Kitchen report for {name}"
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=3)
        text = output.decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        text = str(exc)
    out = {"command": cmd, "output": text}
    if any(x in name for x in [";", "|", "&", "`", "$("]):
        out["flag"] = "FLAG{RD_CMDI_REPORT}"
    return jsonify(out)


@api.route("/promo/import", methods=["POST"])
def promo_import():
    """Insecure pickle deserialization. FLAG{RD_PICKLE_PROMO}"""
    raw = request.get_data()
    if not raw:
        return jsonify({"error": "empty body — send pickled coupon blob"}), 400
    try:
        obj = pickle.loads(raw)  # noqa: S301
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": f"pickle failed: {exc}"}), 400
    return jsonify({"ok": True, "promo": obj, "flag": "FLAG{RD_PICKLE_PROMO}"})


@api.route("/config/eval", methods=["POST"])
def config_eval():
    """Unsafe eval / exec of config snippet. FLAG{RD_EXEC_CONFIG}"""
    data = request.get_json(silent=True) or {}
    snippet = data.get("snippet") or data.get("config") or ""
    local_ns: dict = {}
    # Intentional
    exec(snippet, {}, local_ns)  # noqa: S102
    return jsonify({"ok": True, "locals": {k: str(v) for k, v in local_ns.items()}, "flag": "FLAG{RD_EXEC_CONFIG}"})


@api.route("/path")
def read_kitchen_file():
    """Path traversal via file= … FLAG{RD_PATH_TRAVERSAL}"""
    rel = request.args.get("file", "menu_note.txt")
    base = dbmod.DATA_DIR
    # Intentionally joins without sanitizing ..
    target = os.path.normpath(os.path.join(str(base), rel))
    try:
        with open(target, "r", encoding="utf-8", errors="replace") as fh:
            content = fh.read()
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": str(exc), "path": target}), 404
    out = {"path": target, "content": content}
    if ".." in rel or "flag_path.txt" in rel.replace("\\", "/"):
        out["flag"] = "FLAG{RD_PATH_TRAVERSAL}"
    return jsonify(out)


@api.route("/discount/preview", methods=["POST"])
def discount_preview():
    """Logic bug in aggregation. FLAG{RD_LOGIC_DISCOUNT}"""
    data = request.get_json(silent=True) or {}
    ids = data.get("order_ids") or [1, 2, 3]
    result = dbmod.get_discount_totals(list(ids))
    return jsonify(result)


@api.route("/redirect")
def open_redirect():
    """Open redirect (support sink; used for impact analysis labs)."""
    from flask import redirect

    next_url = request.args.get("next", "/")
    return redirect(next_url)


@api.route("/render")
def ssti_preview():
    """SSTI via template query param. FLAG{RD_SSTI_RENDER}"""
    tmpl = request.args.get("template", "Hello {{ name }}")
    name = request.args.get("name", "Kitchen")
    html = render_template_string(tmpl, name=name)
    marker = request.args.get("template", "")
    if "{{" in marker and ("config" in marker.lower() or ".__" in marker or "lipsum" in marker.lower()):
        html += "<!-- FLAG{RD_SSTI_RENDER} -->"
    return html


@api.route("/debug/info")
def debug_info():
    """Verbose debug endpoint left enabled. FLAG{RD_DEBUG_EXPOSE}"""
    return jsonify(
        {
            "debug": True,
            "secret_key_hint": "oJew_hVN9dv46ZkLReHCVw",
            "db_path": str(dbmod.DB_PATH),
            "flag": "FLAG{RD_DEBUG_EXPOSE}",
        }
    )


@api.route("/token")
def issue_token():
    """Predictable token helper used by legacy devices."""
    import hashlib

    user = request.args.get("user", "guest")
    token = hashlib.md5(f"{user}:rd-kitchen".encode()).hexdigest()
    return jsonify({"user": user, "token": token})


@api.route("/orders")
def list_orders():
    conn = dbmod.get_connection()
    try:
        rows = conn.execute(
            """SELECT o.*, c.name AS customer_name
               FROM orders o LEFT JOIN customers c ON c.id = o.customer_id
               ORDER BY o.id DESC"""
        ).fetchall()
    finally:
        conn.close()
    return jsonify({"orders": [dict(r) for r in rows]})


@api.route("/menu")
def list_menu():
    conn = dbmod.get_connection()
    try:
        rows = conn.execute("SELECT * FROM menu_items ORDER BY sales_count DESC").fetchall()
    finally:
        conn.close()
    return jsonify({"items": [dict(r) for r in rows]})


@api.route("/customers")
def list_customers():
    # Missing auth — sensitive fields (email/notes/is_admin) exposed. FLAG{RD_PII_LEAK}
    conn = dbmod.get_connection()
    try:
        rows = conn.execute("SELECT * FROM customers").fetchall()
    finally:
        conn.close()
    data = [dict(r) for r in rows]
    out = {"customers": data}
    if any(int(r.get("is_admin") or 0) == 1 for r in data):
        out["warning"] = "internal records included"
        out["flag"] = "FLAG{RD_PII_LEAK}"
    return jsonify(out)
