import os
import glob
import re

base_path = r"d:\Documents\Antigravity\YehoshamaFoundation\YehoshamaFoundationWebsite"

html_files = glob.glob(os.path.join(base_path, '**', '*.html'), recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False

    # Update dropdown text
    replacements = {
        '>Protocol #4<': '>Low-Tech Crypto<',
        '>Protocol #5<': '>Offline Ledger<',
        '>Protocol #6<': '>M# (Sharp Mind)<',
        '>Protocol #7<': '>Universal Concept<',
    }

    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated menus in {os.path.basename(file_path)}")

print("Done updating dropdown menus.")
