from pathlib import Path
import re

path = Path(r"C:\Projects\Rubberduck\Workspace\demo project\package\rubber_duck_pizzeria\templates\rubber_duck_pizzeria\review.html")
text = path.read_text(encoding="utf-8")

# Distinct review per customer entry (10 reviews across tabs)
reviews = [
    "Ordered the garlic pizza after work — crust was crispy, cheese pulled perfectly, and it was still hot when it arrived.",
    "Spaghetti was tasty but a bit too mild for me. Delivery was on time though. Would try a spicier option next visit.",
    "Came with the kids for dinner. Watermelon juice was icy-cold and fresh — they asked for a second glass before dessert.",
    "Chicken curry portions were huge and the sauce was rich. Staff even swapped my side when I asked. Felt looked after.",
    "Brought my nephew for a birthday treat. Kids meal pizza was adorable and he finished every bite. Easy five stars.",
    "Asked for extra mozzarella mid-order and they handled it without fuss. Ticket time was about 11 minutes. Smooth.",
    "This is our Friday-night usual now. Garlic Italiano stays consistent — stretchy cheese, bright tomato, no soggy base.",
    "Weeknight takeout regular here. Best-sellers never disappoint and packaging keeps everything hot. Keep them coming!",
    "App checkout was simple and the kitchen matched the order exactly. Food looked like the photos for once. Nice.",
    "Saturday peak had a short wait, but warm bread and solid marinara made it worth it. Will come earlier next time.",
]

ids = [
    "#RD-1042",
    "#RD-1188",
    "#RD-1215",
    "#RD-1307",
    "#RD-1420",
    "#RD-1503",
    "#RD-1631",
    "#RD-1719",
    "#RD-1844",
    "#RD-1902",
]

pattern = re.compile(r'(<p class="mb-0 text-dark">)(.*?)(</p>)', re.S)
idx = {"i": 0}

def replace_review(m: re.Match) -> str:
    i = idx["i"]
    idx["i"] += 1
    return f"{m.group(1)}{reviews[i % len(reviews)]}{m.group(3)}"

text = pattern.sub(replace_review, text)

# unique ticket ids in order
parts = text.split("#C01234")
out = []
for j, part in enumerate(parts):
    out.append(part)
    if j < len(parts) - 1:
        out.append(ids[j % len(ids)])
text = "".join(out)

text = text.replace('alt="DexignZone"', 'alt="Customer review"')
# also scrub any leftover broken fragment if still present
text = re.sub(
    r"Today.?s kitchen performance amet,[^<]*",
    "Fresh feedback from a Rubber Duck Pizzeria guest.",
    text,
)

path.write_text(text, encoding="utf-8")
print("reviews_written", idx["i"], "id_slots", len(parts) - 1)
