import os
import re

base_dir = r'c:\Users\ADMIN\Ecommerce FinalProjectBenjWorkspace'

# HTML file processing
html_file = os.path.join(base_dir, 'eCommerceMainScratch2.html')
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

def replace_html_comment(match):
    # Extract the inner text, strip whitespace and newlines, collapse multiple spaces
    inner = match.group(1)
    inner = re.sub(r'\s+', ' ', inner).strip()
    return f'<!-- ~~~~ {inner} ~~~~ -->'

html_pattern = re.compile(r'<!--\s*=============================================\s*(.*?)\s*=============================================\s*-->', re.DOTALL)
html_content = html_pattern.sub(replace_html_comment, html_content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# CSS file processing
css_file = os.path.join(base_dir, 'styles.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

def replace_css_comment(match):
    inner = match.group(1)
    inner = re.sub(r'\s+', ' ', inner).strip()
    return f'/* ~~~~ {inner} ~~~~ */'

css_pattern = re.compile(r'/\*\s*=============================================\s*(.*?)\s*=============================================\s*\*/', re.DOTALL)
css_content = css_pattern.sub(replace_css_comment, css_content)

# Also replace single line block comments if any
css_pattern_single = re.compile(r'/\*\s*(.*?)\s*\*/')
# actually wait, let's just stick to the big blocks or also format the smaller ones.
# The user said "all the comments", let's check what other comments there are in CSS.

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# JS file processing
js_file = os.path.join(base_dir, 'script.js')
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

def replace_js_comment(match):
    inner = match.group(1)
    inner = re.sub(r'\s+', ' ', inner).strip()
    return f'/* ~~~~ {inner} ~~~~ */'

js_pattern = re.compile(r'/\*\s*----\s*(.*?)\s*----\s*\*/', re.DOTALL)
js_content = js_pattern.sub(replace_js_comment, js_content)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Comment formatting completed.")
