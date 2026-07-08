"""Update branding to RubberDuck team and bump all years to 2026."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "package" / "rubber_duck_pizzeria"

META_DESC = (
    "Rubber Duck Pizzeria is a demo restaurant admin app built by the RubberDuck team "
    "to test RubberDuck’s 10 MCP use cases."
)

REPLACEMENTS = [
    ("DexignZone", "RubberDuck Team"),
    ("dexignzone.com", "rubberduck.com"),
    ("alt=\"DexignZone\"", "alt=\"Rubber Duck Pizzeria\""),
    ("Partner with RubberDuck Team to create an impressive online presence for your Restaurant. Start driving more traffic and growing your business today", META_DESC),
    # after DexignZone -> RubberDuck Team, clean meta author leftovers remaining from old marketing blurb
    (
        "Boost your Restaurant business with Rubber Duck Pizzeria. Our professionally designed admin templates cater specifically to the needs of Food, admin and cafe business, offering visually stunning and functional designs. Choose from a variety of Rubber Duck Pizzeria website templates that are perfect for showcasing your menu, promoting your services, and attracting Factory  customers. Partner with RubberDuck Team to create an impressive online presence for your Restaurant. Start driving more traffic and growing your business today",
        META_DESC,
    ),
]

# Year bumps: prefer longer/more specific first
YEAR_PATTERNS = [
    (re.compile(r"\b2025\b"), "2026"),
    (re.compile(r"\b2024\b"), "2026"),
    (re.compile(r"\b2023\b"), "2026"),
    (re.compile(r"\b2022\b"), "2026"),
    (re.compile(r"\b2021\b"), "2026"),
    (re.compile(r"\b2020\b"), "2026"),
    (re.compile(r"\b2019\b"), "2026"),
]


def process_text(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    for pat, repl in YEAR_PATTERNS:
        text = pat.sub(repl, text)
    # fix weird typo year if any
    text = text.replace("20226", "2026")
    text = text.replace("20224", "2026")
    return text


def main() -> None:
    changed = 0
    for path in list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.js")) + list(ROOT.rglob("*.py")):
        if "node_modules" in str(path) or "vendor" in str(path):
            continue
        try:
            original = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        updated = process_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print("updated", path.relative_to(ROOT))
    print("files_changed", changed)


if __name__ == "__main__":
    main()
