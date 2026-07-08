"""SQLite access for Rubber Duck Pizzeria.

NOTE: This module intentionally contains insecure helpers used by the lab API.
Do not treat this as production code.
"""
from __future__ import annotations

import hashlib
import os
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "pizzeria.db"


def get_connection() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def _md5(password: str) -> str:
    # Intentional weak hash (FLAG path RD_WEAK_HASH)
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def init_db(force: bool = False) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if force and DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except OSError:
            # Windows may briefly lock the file during Flask reload — fall through idempotently
            pass

    conn = get_connection()
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'staff',
            is_admin INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            customer_code TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            location TEXT,
            total_spent REAL DEFAULT 0,
            last_order REAL DEFAULT 0,
            join_date TEXT,
            is_admin INTEGER NOT NULL DEFAULT 0,
            notes TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            description TEXT,
            image_path TEXT,
            sales_count INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_code TEXT UNIQUE NOT NULL,
            customer_id INTEGER,
            status TEXT NOT NULL,
            amount REAL NOT NULL,
            location TEXT,
            created_at TEXT,
            coupon_blob BLOB,
            note TEXT DEFAULT '',
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );

        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            menu_item_id INTEGER,
            item_name TEXT NOT NULL,
            qty INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY(order_id) REFERENCES orders(id)
        );

        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            review_code TEXT UNIQUE NOT NULL,
            customer_name TEXT NOT NULL,
            body TEXT NOT NULL,
            rating REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'published',
            created_at TEXT,
            avatar_path TEXT
        );

        CREATE TABLE IF NOT EXISTS app_settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        """
    )

    # Already seeded — safe to exit after schema ensure
    if cur.execute("SELECT COUNT(*) AS c FROM staff").fetchone()[0] > 0 and not force:
        conn.commit()
        conn.close()
        return

    staff = [
        ("admin", _md5("admin123"), "manager", 1),
        ("kitchen", _md5("kitchen"), "staff", 0),
        ("demo", _md5("demo"), "staff", 0),
    ]
    cur.executemany(
        "INSERT INTO staff(username, password_hash, role, is_admin) VALUES (?,?,?,?)",
        staff,
    )

    customers = [
        ("#5552351", "James Witwicky", "james@example.com", "Corner Street 5th London", 164.52, 14.89, "12 January 2026, 12:42 AM", 0, "VIP Friday regular"),
        ("#5552375", "Emilia Johanson", "emilia@example.com", "67 St. John's Road London", 251.16, 32.10, "08 February 2026, 02:12 AM", 0, ""),
        ("#5552456", "Peter Parkur", "peter@example.com", "South Corner St 41256 London", 89.40, 22.20, "18 March 2026, 01:05 PM", 0, ""),
        ("#5552488", "Cindy Alexa", "cindy@example.com", "32 The Green London", 120.00, 8.20, "02 April 2026, 06:20 PM", 0, ""),
        ("#5552501", "Alexzander Queqe", "alex@example.com", "Long Horn Ave London", 410.00, 55.00, "15 May 2026, 11:11 AM", 0, "Loyal customer"),
        ("#5552510", "Bella Simatupang", "bella@example.com", "Harbor Row London", 302.11, 41.50, "21 May 2026, 09:40 AM", 0, ""),
        ("#5552522", "Robertos Jr.", "robertos@rdp.local", "HQ Desk", 0.0, 0.0, "01 January 2026, 09:00 AM", 1, "Internal staff mirror — should not be public"),
    ]
    cur.executemany(
        """INSERT INTO customers(customer_code,name,email,location,total_spent,last_order,join_date,is_admin,notes)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        customers,
    )

    menu = [
        ("Chicken curry special with cucumber", "main", 5.60, "Rich curry bowl", "menu/Untitled-1.jpg", 890),
        ("Italiano Pizza With Garlic", "pizza", 8.20, "Garlic mozzarella pizza", "menu/Untitled-2.jpg", 1204),
        ("Watermelon juice with ice", "drink", 3.50, "Iced watermelon", "menu/Untitled-3.jpg", 640),
        ("Tuna Soup spinach with himalaya salt", "soup", 6.10, "Warm spinach tuna soup", "menu/Untitled-4.jpg", 412),
        ("Medium Spicy Spagethi Italiano", "pasta", 7.40, "Spicy tomato spaghetti", "menu/Untitled-5.jpg", 733),
        ("Chicken Kebab from Turkish with Garlic", "main", 9.90, "Grilled kebab platter", "card/chicken-kebab.jpg", 512),
        ("Orange Juice Special Smoothy with Sugar", "drink", 4.20, "Fresh orange smoothie", "card/orange-juice.jpg", 388),
    ]
    cur.executemany(
        """INSERT INTO menu_items(name,category,price,description,image_path,sales_count)
           VALUES (?,?,?,?,?,?)""",
        menu,
    )

    orders = [
        ("#INV-0012456", 3, "DELIVERED", 63.29, "South Corner St 41256 London", "08 July 2026, 12:42 AM", "Leave at door", 1),
        ("#5552375", 2, "PENDING", 251.16, "67 St. John's Road London", "08 July 2026, 02:12 AM", "", 2),
        ("#5552401", 4, "ON PROGRESS", 44.97, "32 The Green London", "07 July 2026, 07:33 PM", "Extra napkins", 3),
        ("#5552410", 1, "DELIVERED", 14.89, "Corner Street 5th London", "06 July 2026, 01:15 PM", "", 4),
        ("#5552422", 5, "PENDING", 55.00, "Long Horn Ave London", "06 July 2026, 08:05 PM", "Ring bell", 5),
    ]
    for code, cid, status, amount, loc, created, note, _ in orders:
        cur.execute(
            """INSERT INTO orders(order_code,customer_id,status,amount,location,created_at,note)
               VALUES (?,?,?,?,?,?,?)""",
            (code, cid, status, amount, loc, created, note),
        )

    order_items = [
        (1, 1, "Chicken curry special with cucumber", 1, 4.12),
        (1, 3, "Watermelon juice with ice", 3, 14.99),
        (1, 2, "Italiano pizza with garlic", 1, 8.20),
        (2, 5, "Medium Spicy Spagethi Italiano", 2, 7.40),
        (3, 3, "Watermelon juice with ice", 2, 3.50),
    ]
    cur.executemany(
        """INSERT INTO order_items(order_id,menu_item_id,item_name,qty,unit_price)
           VALUES (?,?,?,?,?)""",
        order_items,
    )

    reviews = [
        ("#RD-1042", "James Sitepu", "Ordered the garlic pizza after work — crust was crispy, cheese pulled perfectly, and it was still hot when it arrived.", 4.2, "published", "26/04/2026, 12:42 PM", "table/Untitled-1.jpg"),
        ("#RD-1188", "John Doe", "Spaghetti was tasty but a bit too mild for me. Delivery was on time though. Would try a spicier option next visit.", 3.0, "published", "15/02/2026, 02:42 PM", "table/Untitled-2.jpg"),
        ("#RD-1215", "Maria Stan", "Came with the kids for dinner. Watermelon juice was icy-cold and fresh — they asked for a second glass before dessert.", 4.5, "published", "15/05/2026, 01:50 PM", "table/Untitled-3.jpg"),
        ("#RD-1307", "Karry Doe", "Chicken curry portions were huge and the sauce was rich. Staff even swapped my side when I asked. Felt looked after.", 4.5, "published", "07/08/2026, 10:42 AM", "table/Untitled-4.jpg"),
        ("#RD-1420", "Carry Kondy", "Asked for extra mozzarella mid-order and they handled it without fuss. Ticket time was about 11 minutes. Smooth.", 4.2, "published", "12/06/2026, 08:42 AM", "table/Untitled-5.jpg"),
    ]
    cur.executemany(
        """INSERT INTO reviews(review_code,customer_name,body,rating,status,created_at,avatar_path)
           VALUES (?,?,?,?,?,?,?)""",
        reviews,
    )

    cur.executemany(
        "INSERT INTO app_settings(key,value) VALUES (?,?)",
        [
            ("kitchen_target", "1000"),
            ("discount_mode", "legacy"),
            ("report_cmd_template", "echo kitchen-report"),
            ("config_snippet", "settings = {'promo': True}"),
        ],
    )

    conn.commit()
    conn.close()


def search_customers_raw(q: str):
    """VULN: SQL injection via string format. FLAG{RD_SQLI_SEARCH}"""
    conn = get_connection()
    sql = f"SELECT * FROM customers WHERE name LIKE '%{q}%' OR location LIKE '%{q}%' OR customer_code LIKE '%{q}%' OR notes LIKE '%{q}%'"
    try:
        rows = conn.execute(sql).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


def get_order_by_id(order_id: int):
    """No ownership check — IDOR sink. FLAG{RD_IDOR_ORDER}"""
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
        items = conn.execute("SELECT * FROM order_items WHERE order_id = ?", (order_id,)).fetchall()
    finally:
        conn.close()
    if not row:
        return None
    data = dict(row)
    data["items"] = [dict(i) for i in items]
    # Leak secret note for internal order discovery
    if data.get("order_code") == "#INV-0012456":
        data["internal_token"] = "FLAG{RD_IDOR_ORDER}"
    return data


def list_reviews(status: str = "published"):
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM reviews WHERE status = ? ORDER BY id DESC",
            (status,),
        ).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


def add_review(customer_name: str, body: str, rating: float = 5.0):
    import datetime
    import secrets

    conn = get_connection()
    code = f"#RD-{secrets.randbelow(9000)+1000}"
    created = datetime.datetime.now().strftime("%d/%m/%Y, %I:%M %p")
    try:
        conn.execute(
            """INSERT INTO reviews(review_code,customer_name,body,rating,status,created_at,avatar_path)
               VALUES (?,?,?,?,?,?,?)""",
            (code, customer_name, body, rating, "published", created, "table/Untitled-1.jpg"),
        )
        conn.commit()
    finally:
        conn.close()
    return code


def update_customer(customer_id: int, payload: dict):
    """VULN: mass assignment — accepts is_admin. FLAG{RD_MASS_ASSIGN}"""
    conn = get_connection()
    allowed_any = payload  # intentional: no allowlist
    sets = []
    values = []
    for k, v in allowed_any.items():
        if k in {"id"}:
            continue
        sets.append(f"{k} = ?")
        values.append(v)
    if not sets:
        return None
    values.append(customer_id)
    sql = f"UPDATE customers SET {', '.join(sets)} WHERE id = ?"
    try:
        conn.execute(sql, values)
        conn.commit()
        row = conn.execute("SELECT * FROM customers WHERE id = ?", (customer_id,)).fetchone()
    finally:
        conn.close()
    data = dict(row) if row else None
    if data and int(data.get("is_admin") or 0) == 1 and data.get("email") != "robertos@rdp.local":
        data["flag"] = "FLAG{RD_MASS_ASSIGN}"
    return data


def get_discount_totals(order_ids: list[int]) -> dict:
    """Business-logic bug: mutates incoming list/mask while aggregating.
    FLAG{RD_LOGIC_DISCOUNT} surfaced when callers inspect returned breakdown.
    """
    conn = get_connection()
    try:
        rows = conn.execute(
            f"SELECT id, amount FROM orders WHERE id IN ({','.join(str(i) for i in order_ids) or 'NULL'})"
        ).fetchall()
    finally:
        conn.close()

    # Intentional mutation of caller-provided structure style bug
    mask = {"subtotal": True, "discount": True, "total": True}
    subtotal = 0.0
    for r in rows:
        subtotal += float(r["amount"])
        # Bug: wipe discount eligibility after first item
        if "discount" in mask:
            mask.pop("discount")

    discount = 0.0
    if "discount" in mask:  # never true after first loop when rows exist
        discount = round(subtotal * 0.1, 2)

    total = round(subtotal - discount, 2)
    result = {
        "subtotal": round(subtotal, 2),
        "discount": discount,
        "total": total,
        "mask": mask,
        "note": "kitchen promo engine v1",
    }
    # Evidence marker for agents tracing mutation
    if rows and "discount" not in mask and discount == 0.0 and subtotal > 0:
        result["debug_hint"] = "FLAG{RD_LOGIC_DISCOUNT}"
    return result


def verify_staff(username: str, password: str):
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT * FROM staff WHERE username = ? AND password_hash = ?",
            (username, _md5(password)),
        ).fetchone()
    finally:
        conn.close()
    return dict(row) if row else None
