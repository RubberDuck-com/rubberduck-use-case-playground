from pathlib import Path

root = Path(r"C:\Projects\Rubberduck\Workspace")
files = [
    root / "demo project/package/rubber_duck_pizzeria/templates/rubber_duck_pizzeria/index.html",
    root / "demo project/package/rubber_duck_pizzeria/templates/rubber_duck_pizzeria/index-2.html",
    root / "demo project/package/rubber_duck_pizzeria/templates/rubber_duck_pizzeria/analytics.html",
    root / "demo project/package/rubber_duck_pizzeria/templates/rubber_duck_pizzeria/bootstrap/ui-typography.html",
    root / "demo project/package/rubber_duck_pizzeria/templates/rubber_duck_pizzeria/bootstrap/ui-popover.html",
    root / "demo project/package/rubber_duck_pizzeria/templates/rubber_duck_pizzeria/plugins/uc-select2.html",
]
repls = {
    "Today’s kitchen performance amet, consectetur": "See trends across orders and guests",
    "Today’s kitchen performance amet, consectetur adipisicing elit, sed do eiusmod tempor.": "Orders update live as kitchen tickets finish.",
    "Today’s kitchen performance amet": "Fresh daily specials",
    '<option value="BY">Lorem</option>': '<option value="BY">Lunch Combo</option>',
}
for p in files:
    t = p.read_text(encoding="utf-8")
    for a, b in repls.items():
        t = t.replace(a, b)
    p.write_text(t, encoding="utf-8")
    print("fixed", p.name)
