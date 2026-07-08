from pathlib import Path
import re

p = Path(r"C:\Projects\Rubberduck\Workspace\demo project\package\rubber_duck_pizzeria\templates\rubber_duck_pizzeria\analytics.html")
t = p.read_text(encoding="utf-8")
pat = re.compile(
    r"(images/card/Untitled-11\.jpg)([\s\S]{0,500}?Orange Juice Special Smoothy)",
    re.M,
)
nt, n = pat.subn(r"images/card/Untitled-15.jpg\2", t)
p.write_text(nt, encoding="utf-8")
print("replacements", n)
