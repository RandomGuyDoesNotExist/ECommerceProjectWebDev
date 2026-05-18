import os

with open('eCommerceMainScratch2.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False

for i in range(len(lines)):
    line = lines[i]
    
    # CSS exclusion
    if 'MICROGRAPHIC FRAMING — section dividers' in line:
        skip = True
        # remove the preceding /* ==== line too
        if len(new_lines) > 0 and '/* ====' in new_lines[-1]:
            new_lines.pop()
            
    if 'RESPONSIVE — TABLET' in line:
        skip = False
        new_lines.append('        /* =============================================\n')
        
    # HTML exclusion
    if 'FRAMING DIVIDER — decorative section separator' in line:
        skip = True
        # remove preceding <!-- ====
        if len(new_lines) > 0 and '<!-- ====' in new_lines[-1]:
            new_lines.pop()
            
    if 'JAVASCRIPT — carousel logic' in line:
        skip = False
        new_lines.append('    <!-- =============================================\n')

    if not skip:
        new_lines.append(line)

with open('eCommerceHeroScratch3.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
