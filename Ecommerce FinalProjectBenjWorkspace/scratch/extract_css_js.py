import os
import re

base_dir = r'c:\Users\ADMIN\Ecommerce FinalProjectBenjWorkspace'
html_file = os.path.join(base_dir, 'eCommerceMainScratch2.html')
css_file = os.path.join(base_dir, 'styles.css')
js_file = os.path.join(base_dir, 'script.js')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract and replace style
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    style_content = style_match.group(1).strip()
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(style_content)
    content = content[:style_match.start()] + '<link rel="stylesheet" href="styles.css" />' + content[style_match.end():]

# Extract and replace script
script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if script_match:
    script_content = script_match.group(1).strip()
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(script_content)
    content = content[:script_match.start()] + '<script src="script.js"></script>' + content[script_match.end():]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Extraction and replacement completed.")
