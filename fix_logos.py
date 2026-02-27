import os
import glob
import re

base_path = r"d:\Documents\Antigravity\YehoshamaFoundation\YehoshamaFoundationWebsite"
html_files = glob.glob(os.path.join(base_path, '**', '*.html'), recursive=True)

for file_path in html_files:
    rel_path = os.path.relpath(file_path, base_path)
    depth = rel_path.count(os.sep)
    prefix = "../" * depth if depth > 0 else ""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The HTML-escaped version: { &gt;&lt;((('&gt; }
    
    # 1. Header Logo
    # <a href="..." class="ascii-logo">{ &gt;&lt;((('&gt; }</a>
    content = re.sub(r'<a([^>]+)class="ascii-logo"[^>]*>\s*\{\s*&gt;&lt;\(\(\(\'&gt;\s*\}\s*</a>', 
                     rf'<a\1class="logo-link"><img src="{prefix}Logo.png" alt="Yehoshama Foundation Logo" class="site-logo"></a>',
                     content)

    # 2. Hero Logo (in index.html)
    # <div class="hero-logo ascii">{ &gt;&lt;((('&gt; }</div>
    content = re.sub(r'<div class="hero-logo ascii">\s*\{\s*&gt;&lt;\(\(\(\'&gt;\s*\}\s*</div>',
                     rf'<div class="hero-logo"><img src="{prefix}Logo.png" alt="Yehoshama Foundation Logo"></div>',
                     content)
    
    # 3. Footer Logo or generic span
    # <span class="ascii-logo">{ &gt;&lt;((('&gt; }</span>
    content = re.sub(r'<span class="ascii-logo">\s*\{\s*&gt;&lt;\(\(\(\'&gt;\s*\}\s*</span>',
                     rf'<img src="{prefix}Logo.png" alt="Yehoshama Foundation Logo" class="site-logo">',
                     content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replaced ASCII logos with image Logo.png using HTML entity matching.")
