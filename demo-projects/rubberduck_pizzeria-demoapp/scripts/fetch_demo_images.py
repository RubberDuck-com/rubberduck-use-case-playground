"""Download matching food/people images and wire them to the correct placeholder files."""
from __future__ import annotations

import json
import shutil
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "package" / "rubber_duck_pizzeria" / "static" / "rubber_duck_pizzeria" / "images"
UA = {"User-Agent": "Mozilla/5.0 RubberDuckPizzeriaDemo/1.0"}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def save(rel: str, data: bytes) -> None:
    dest = BASE / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print(f"OK {rel} ({len(data)//1024} KB)")


def foodish(cat: str) -> bytes:
    meta = json.loads(get(f"https://foodish-api.com/api/images/{cat}"))
    return get(meta["image"])


def unsplash(photo_id: str, w: int = 500) -> bytes:
    return get(f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w={w}&q=85")


def copy(src_rel: str, dest_rel: str) -> None:
    src = BASE / src_rel
    dest = BASE / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"COPY {src_rel} -> {dest_rel}")


def main() -> None:
    # Keep user-provided menu images. Download only missing dishes.
    # Orange juice (dedicated file — was wrongly sharing pizza image)
    save("card/orange-juice.jpg", unsplash("photo-1600271886742-f049cd451bba", 500))
    # Chicken kebab / grilled meat
    save("card/chicken-kebab.jpg", unsplash("photo-1544025162-d76694265947", 500))
    # Extra mozzarella-style pizza from Foodish (fresh download, not reuse of kids meal)
    save("card/mozarella-pizza.jpg", foodish("pizza"))
    save("card/deluxe-pizza.jpg", foodish("pizza"))

    # Exact filename mapping by dish meaning
    mapping = {
        # Dashboard recent orders
        "card/Untitled-1.jpg": "card/Untitled-9.jpg",          # kids pizza meal
        "card/Untitled-2.jpg": "menu/Untitled-4.jpg",          # tuna soup
        "card/Untitled-3.jpg": "card/deluxe-pizza.jpg",        # extreme deluxe pizza
        # Order detail items
        "card/Untitled-4.jpg": "menu/Untitled-3.jpg",          # watermelon juice
        "card/Untitled-5.jpg": "menu/Untitled-2.jpg",          # italiano pizza
        "card/Untitled-6.jpg": "menu/Untitled-1.jpg",          # chicken curry
        # Most favorites
        "card/Untitled-10.jpg": "card/mozarella-pizza.jpg",    # mozzarella pizza
        "card/Untitled-11.jpg": "card/deluxe-pizza.jpg",       # extreme deluxe pizza ONLY
        "card/Untitled-12.jpg": "menu/Untitled-3.jpg",         # watermelon juice
        "card/Untitled-13.jpg": "card/chicken-kebab.jpg",      # chicken kebab
        "card/Untitled-14.jpg": "card/Untitled-7.jpg",         # medium spicy pizza (hero)
        "card/Untitled-15.jpg": "card/orange-juice.jpg",       # orange juice/smoothie
        # Shop products
        "product/1.jpg": "menu/Untitled-2.jpg",
        "product/2.jpg": "card/deluxe-pizza.jpg",
        "product/3.jpg": "card/Untitled-9.jpg",
        "product/4.jpg": "card/Untitled-7.jpg",
        "product/5.jpg": "menu/Untitled-1.jpg",
        "product/6.jpg": "menu/Untitled-4.jpg",
        "product/7.jpg": "menu/Untitled-3.jpg",
    }
    for dest, src in mapping.items():
        copy(src, dest)

    # People portraits (randomuser CDN)
    portraits = {
        "profile/Untitled-10.jpg": "https://randomuser.me/api/portraits/men/32.jpg",
        "profile/Untitled-11.jpg": "https://randomuser.me/api/portraits/women/44.jpg",
        "profile/Untitled-12.jpg": "https://randomuser.me/api/portraits/men/75.jpg",
        "profile/Untitled-13.jpg": "https://randomuser.me/api/portraits/men/22.jpg",
        "profile/Untitled-1.jpg": "https://randomuser.me/api/portraits/men/11.jpg",  # delivery
        "profile/Untitled-2.jpg": "https://randomuser.me/api/portraits/men/41.jpg",  # customer
        "profile/pic1.jpg": "https://randomuser.me/api/portraits/men/36.jpg",       # admin header
        "avatar/1.jpg": "https://randomuser.me/api/portraits/men/36.jpg",
        "avatar/2.jpg": "https://randomuser.me/api/portraits/women/44.jpg",
        "avatar/3.jpg": "https://randomuser.me/api/portraits/men/32.jpg",
        "avatar/4.jpg": "https://randomuser.me/api/portraits/women/68.jpg",
        "avatar/5.jpg": "https://randomuser.me/api/portraits/men/75.jpg",
        "table/Untitled-1.jpg": "https://randomuser.me/api/portraits/men/32.jpg",
        "table/Untitled-2.jpg": "https://randomuser.me/api/portraits/men/41.jpg",
        "table/Untitled-3.jpg": "https://randomuser.me/api/portraits/women/44.jpg",
        "table/Untitled-4.jpg": "https://randomuser.me/api/portraits/women/68.jpg",
        "table/Untitled-5.jpg": "https://randomuser.me/api/portraits/men/22.jpg",
    }
    for rel, url in portraits.items():
        save(rel, get(url))

    # PNG avatar variants used by ecommerce customers page
    for i, src in [("1.png", "avatar/1.jpg"), ("5.png", "avatar/5.jpg")]:
        copy(src, f"avatar/{i}")

    # Small profile pics for tables
    small = BASE / "profile" / "small"
    small.mkdir(parents=True, exist_ok=True)
    for idx, src_name in enumerate(
        ["Untitled-10.jpg", "Untitled-11.jpg", "Untitled-12.jpg", "Untitled-13.jpg",
         "Untitled-1.jpg", "Untitled-2.jpg", "pic1.jpg", "Untitled-10.jpg",
         "Untitled-11.jpg", "Untitled-12.jpg"],
        start=1,
    ):
        copy(f"profile/{src_name}", f"profile/small/pic{idx}.jpg")

    print("DONE")


if __name__ == "__main__":
    main()
