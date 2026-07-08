"""Replace Lorem ipsum / dummy Latin copy with Rubber Duck Pizzeria-relevant text."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "package" / "rubber_duck_pizzeria" / "templates"

# Short captions used under section titles
SHORT = {
    "Lorem ipsum dolor sit": "Today’s kitchen performance",
    "Lorem ipsum dolor": "Updated live from the kitchen",
    " Lorem ipsum dolor": " Updated from today’s sales",
    "Lorem ipsum dolor sit amet, conse": "Real-time snapshot for your pizzeria",
    "Lorem ipsum dolor sit amet,consecteture": "Track top dishes and loyal guests",
    "Lorem ipsum dolor sit amet, consectetur": "See trends across orders and guests",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do ": "On track for today’s revenue target based on lunch and dinner rush. ",
    "Lorem ipsum dolor sit amet, consecteture": "Keep guests happy with faster tickets",
}

# Longer review-style bodies (cycled)
REVIEWS = [
    "The crust was perfectly crispy and the garlic pizza smelled amazing. We’ll definitely order again tonight.",
    "Delivery arrived hot and on time. The spicy spaghetti had great flavor — just the right amount of heat.",
    "Loved the watermelon juice with ice. Fresh, cold, and perfect with our family pizza night.",
    "Chicken curry was rich and comforting. Service was friendly and the portion sizes were generous.",
    "Great place for kids. The small pizza meal was fun and tasty. Five stars from our table.",
    "Staff checked in quickly and fixed our extra-cheese request without hassle. Smooth experience overall.",
    "Italiano pizza with garlic is now our usual. Cheese was stretchy and toppings were fresh.",
    "Loyal customer here — weeknight takesouts never disappoint. Keep those best-seller menus coming!",
    "Ordering was easy and the kitchen ticket showed up correctly. Food quality matched the photos.",
    "Slight wait at peak hour, but the food made up for it. Warm bread and a solid marinara.",
]

# Generic paragraph replacements for longer lorem/lipsum-ish blocks on product/email/cms pages
GENERIC_PARAS = [
    "Rubber Duck Pizzeria serves wood-fired pizzas, house pastas, and cold drinks made fresh every shift.",
    "Our kitchen team tracks ticket times so every order leaves hot, boxed, and ready for pickup or delivery.",
    "Guests can browse best-sellers, leave reviews, and reorder favorites from the customer app in minutes.",
]


def replace_exact(text: str, mapping: dict[str, str]) -> str:
    for old, new in mapping.items():
        text = text.replace(old, new)
    return text


def replace_reviews_in_file(text: str) -> str:
    # Replace full classic lorem review paragraphs with cycling review copy
    pattern = re.compile(
        r"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua\.[^<]*",
        re.I,
    )
    i = 0

    def _sub(_: re.Match) -> str:
        nonlocal i
        out = REVIEWS[i % len(REVIEWS)]
        i += 1
        return out

    return pattern.sub(_sub, text)


def replace_long_dummy(text: str) -> str:
    # Catch leftover long latinish paragraphs commonly used in templates
    patterns = [
        re.compile(r"Lorem ipsum dolor sit amet[^<]{20,400}", re.I),
        re.compile(r"Culpa dolor voluptate do laboris[^<]{20,600}", re.I),
        re.compile(r"Eu dolore ea ullamco dolore Lorem[^<]{20,600}", re.I),
        re.compile(r"Cras mattis consectetur purus sit amet fermentum\.[^<]*", re.I),
        re.compile(r"Praesent commodo cursus magna, vel scelerisque nisl consectetur[^<]*", re.I),
        re.compile(r"Aenean lacinia bibendum nulla sed consectetur\.[^<]*", re.I),
        re.compile(r"Porta ac consectetur ac", re.I),
        re.compile(r"There are many variations of passages of Lorem Ipsum available[^<]*", re.I),
    ]
    counter = {"i": 0}
    for pat in patterns:
        def _sub(m: re.Match, counter=counter) -> str:
            if m.group(0).lower().startswith("porta ac"):
                return "Fresh daily specials"
            out = GENERIC_PARAS[counter["i"] % len(GENERIC_PARAS)]
            counter["i"] += 1
            return out
        text = pat.sub(_sub, text)
        counter["i"] = 0
    return text


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8", errors="ignore")
    text = original
    text = replace_exact(text, SHORT)
    text = replace_reviews_in_file(text)
    text = replace_long_dummy(text)

    # Order / note specific leftovers
    extras = {
        "Lorem ipsum dolor sit amet,consecteture": "Track top dishes and loyal guests",
        "Note Order": "Note Order",  # keep label
    }
    text = replace_exact(text, extras)

    # Fix common typo left in template near reviews count
    text = text.replace("(454 revies)", "(454 reviews)")
    text = text.replace("(454 revies)", "(454 reviews)")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for path in ROOT.rglob("*.html"):
        # Skip pure bootstrap showcase pages if desired? User said all places — include them.
        if process_file(path):
            changed.append(str(path.relative_to(ROOT)))
    print(f"Updated {len(changed)} files")
    for c in changed:
        print(" -", c)

    # Sanity: remaining Lorem?
    left = []
    for path in ROOT.rglob("*.html"):
        t = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"Lorem ipsum|lorem ipsum|consectetur adipiscing", t, re.I):
            left.append(str(path.relative_to(ROOT)))
    print(f"Remaining with Lorem-like text: {len(left)}")
    for c in left[:40]:
        print(" !", c)


if __name__ == "__main__":
    main()
