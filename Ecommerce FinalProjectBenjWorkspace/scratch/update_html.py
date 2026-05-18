import re

with open("eCommerceMainScratch2.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'<span class="productBadge([^"]*)">\s*([^<]+?)\s*</span>\s*<div class="productCardImgWrap">\s*<img src="([^"]*)" alt="([^"]*)" />\s*</div>', re.DOTALL)
replacement = r'''<div class="productCardImgWrap">
                    <img src="\3" alt="\4" />
                    <div class="productBadge\1">\2</div>
                </div>'''

content = pattern.sub(replacement, content)

with open("eCommerceMainScratch2.html", "w", encoding="utf-8") as f:
    f.write(content)
