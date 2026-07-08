import urllib.request
import re

html = urllib.request.urlopen("http://127.0.0.1:5000/review", timeout=5).read().decode("utf-8", "replace")
paras = re.findall(r'<p class="mb-0 text-dark">(.*?)</p>', html)
print("count", len(paras))
for i, p in enumerate(paras, 1):
    print(i, p[:140])
print("has_broken", "kitchen performance amet" in html)
print("has_distinct_curry", "Chicken curry was rich" in html)
