import os
import re

base_dir = r'c:\Users\ADMIN\Ecommerce FinalProjectBenjWorkspace'

# HTML file processing
html_file = os.path.join(base_dir, 'eCommerceMainScratch2.html')
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

def replace_html_all_comments(match):
    inner = match.group(1).strip()
    # Remove existing ~~~~ if they somehow got in
    inner = re.sub(r'^~+|~+$', '', inner).strip()
    if not inner:
        return match.group(0) # skip empty
    # Collapse multiple spaces and newlines into single space
    inner = re.sub(r'\s+', ' ', inner)
    return f'<!-- ~~~~ {inner} ~~~~ -->'

html_pattern_all = re.compile(r'<!--(.*?)-->', re.DOTALL)
html_content = html_pattern_all.sub(replace_html_all_comments, html_content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)


# CSS file processing
css_file = os.path.join(base_dir, 'styles.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

def replace_css_all_comments(match):
    inner = match.group(1).strip()
    inner = re.sub(r'^~+|~+$', '', inner).strip()
    if not inner:
        return match.group(0)
    inner = re.sub(r'\s+', ' ', inner)
    return f'/* ~~~~ {inner} ~~~~ */'

css_pattern_all = re.compile(r'/\*(.*?)\*/', re.DOTALL)
css_content = css_pattern_all.sub(replace_css_all_comments, css_content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)


# JS file processing
js_file = os.path.join(base_dir, 'script.js')
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = css_pattern_all.sub(replace_css_all_comments, js_content)

# We also need to handle // comments in JS?
def replace_js_line_comments(match):
    inner = match.group(1).strip()
    inner = re.sub(r'^~+|~+$', '', inner).strip()
    if not inner:
        return match.group(0)
    return f'/* ~~~~ {inner} ~~~~ */'

js_line_pattern = re.compile(r'//(.*)$', re.MULTILINE)
js_content = js_line_pattern.sub(replace_js_line_comments, js_content)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("All comments formatted!")
