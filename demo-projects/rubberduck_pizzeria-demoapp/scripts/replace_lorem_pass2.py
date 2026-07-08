"""Second pass: fix broken partial replacements and remaining dummy Latin."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "package" / "rubber_duck_pizzeria" / "templates"

FIXES = [
    # Broken fragments from partial short replacements
    (
        "Today’s kitchen performance amet, consectetur adipiscing elit, sed do ",
        "On track for today’s revenue target from lunch and dinner rush. ",
    ),
    (
        "Today’s kitchen performance amet,consecteture",
        "Track top dishes and loyal guests",
    ),
    (
        "Today’s kitchen performance amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
        "The crust was perfectly crispy and the garlic pizza smelled amazing. We’ll definitely order again tonight.",
    ),
    (
        "Today’s kitchen performance amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  ",
        "Delivery arrived hot and on time. The spicy spaghetti had great flavor — just the right amount of heat.",
    ),
    (
        "Today’s kitchen performance amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad m",
        "Loved the watermelon juice with ice. Fresh, cold, and perfect with our family pizza night.",
    ),
    (
        "Today’s kitchen performance amet, consectetur adipiscing elit.",
        "Handmade dough, slow-simmered sauces, and pies hot from the oven.",
    ),
    (
        "Today’s kitchen performance amet, consectetur adipiscing elit. Integer posuere erat a ante.",
        "Fresh dough daily. Bold sauces. Pizzas that actually taste like a restaurant.",
    ),
    (
        "Today’s kitchen performance amet consectetur adipisicing elit. A, minima! Eligendi minima illum itaque harum aliquam vel, sunt magni dolorem! Cum quaerat est cupiditate saepe quidem, fugiat in at magni ad provident distinctio",
        "Rubber Duck Pizzeria keeps tickets moving fast so every order leaves hot and ready.",
    ),
    (
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's.",
        "Please leave the order at the door and ring the bell. Extra napkins requested.",
    ),
    (
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
        "Daily specials from the Rubber Duck Pizzeria kitchen.",
    ),
    (
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Has been the industry's standard text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimencenturies.",
        "From first proof to a perfect bake — our kitchen story starts with dough, fire, and guests who come back weekly.",
    ),
    ("<h5>Lorem Ipsum</h5>", "<h5>Kitchen Notes</h5>"),
    ("Integer molestie lorem at massa", "Seasonal pizza of the week"),
    (
        "Almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.",
        "Tonight’s delivery route is busy — keep oven tickets under 12 minutes for peak orders.",
    ),
    (
        "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for\n                                                    the far World of Grammar. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.",
        "Reminder: Rubber Duck Pizzeria weekend promo starts Friday. Double-check topping inventory for garlic pizza and spicy spaghetti.",
    ),
    (
        "Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut",
        "Please confirm courier ETAs before marking large catered orders as ready for dispatch.",
    ),
]

REVIEW_CYCLE = [
    "The crust was perfectly crispy and the garlic pizza smelled amazing. We’ll definitely order again tonight.",
    "Delivery arrived hot and on time. The spicy spaghetti had great flavor — just the right amount of heat.",
    "Loved the watermelon juice with ice. Fresh, cold, and perfect with our family pizza night.",
    "Chicken curry was rich and comforting. Service was friendly and the portion sizes were generous.",
    "Great place for kids. The small pizza meal was fun and tasty. Five stars from our table.",
    "Staff checked in quickly and fixed our extra-cheese request without hassle. Smooth experience overall.",
    "Italiano pizza with garlic is now our usual. Cheese was stretchy and toppings were fresh.",
    "Loyal customer here — weeknight takeouts never disappoint. Keep those best-seller menus coming!",
    "Ordering was easy and the kitchen ticket showed up correctly. Food quality matched the photos.",
    "Slight wait at peak hour, but the food made up for it. Warm bread and a solid marinara.",
]


def scrub_latin_paragraphs(text: str) -> str:
    # Broad scrub for remaining latin dummy paragraphs (bootstrap demos)
    patterns = [
        re.compile(r"(?:>|^)([^<]*(?:Lorem|Cupidatat|Cillum ad ut|Fugiat id quis|Velit aute mollit|Ut ut do pariatur|Lorem,)[^<]{10,})", re.I | re.M),
    ]
    for pat in patterns:
        def sub(m: re.Match) -> str:
            whole = m.group(0)
            body = m.group(1)
            # Keep short option values
            if len(body) < 12:
                return whole
            replacement = "Rubber Duck Pizzeria keeps orders moving with clear tickets, hot pies, and happy guests."
            return whole.replace(body, replacement)
        text = pat.sub(sub, text)
    return text


def fix_reviews_file(path: Path) -> None:
    if path.name != "review.html":
        return
    text = path.read_text(encoding="utf-8")
    # Replace remaining broken review <p class="mb-0 text-dark">...</p>
    pattern = re.compile(r'(<p class="mb-0 text-dark">)(.*?)(</p>)', re.S)
    i = 0

    def sub(m: re.Match) -> str:
        nonlocal i
        inner = m.group(2)
        if "Today’s kitchen" in inner or "Lorem" in inner or "consectetur" in inner or "eiusmod" in inner:
            out = REVIEW_CYCLE[i % len(REVIEW_CYCLE)]
            i += 1
            return f"{m.group(1)}{out}{m.group(3)}"
        return m.group(0)

    new = pattern.sub(sub, text)
    path.write_text(new, encoding="utf-8")


def main() -> None:
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        orig = text
        for old, new in FIXES:
            text = text.replace(old, new)
        text = scrub_latin_paragraphs(text)
        text = text.replace("(454 revies)", "(454 reviews)")
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("updated", path.relative_to(ROOT))
        fix_reviews_file(path)

    left = []
    for path in ROOT.rglob("*.html"):
        t = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"Lorem|ipsum dolor|consectetur adipiscing|eiusmod|Today’s kitchen performance amet", t, re.I):
            # ignore select option 'Lorem' if any tiny remnants we want to report
            left.append(str(path.relative_to(ROOT)))
    print("remaining", len(left))
    for x in left:
        print("!", x)


if __name__ == "__main__":
    main()
