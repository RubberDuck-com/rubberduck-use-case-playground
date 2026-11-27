"""Order exports for the kitchen dashboard."""
from __future__ import annotations

import os
import subprocess
import urllib.request

from .db import get_connection

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "data", "exports")


def sorted_orders(column: str, direction: str):
    conn = get_connection()
    try:
        query = "SELECT id, customer_name, total FROM orders ORDER BY " + column + " " + direction
        return [dict(r) for r in conn.execute(query).fetchall()]
    finally:
        conn.close()


def read_export(name: str) -> str:
    path = os.path.join(EXPORT_DIR, name)
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def compress_export(name: str) -> int:
    archive = name + ".tar.gz"
    return subprocess.call("tar -czf " + archive + " -C " + EXPORT_DIR + " " + name, shell=True)


def notify(callback: str, payload: bytes) -> int:
    req = urllib.request.Request(callback, data=payload, method="POST")
    with urllib.request.urlopen(req, timeout=5) as resp:
        return resp.status


