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
        
    # extract clean title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1).replace(' &mdash; Yehoshama Foundation', '').replace(' — The Yehoshama Foundation', '') if title_match else "Yehoshama Foundation"
    
    # extract meta description
    desc_match = re.search(r'<meta name="description"\s+(?:content="([^"]*)"[^>]*|[^>]*content="([^"]*)")>', content)
    desc = desc_match.group(1) if desc_match and desc_match.group(1) else (desc_match.group(2) if desc_match else "Yehoshama Foundation")

    # The seo block with the dynamic prefix for Logo.png
    seo_block = f'''
    <!-- Favicon & Social Meta Tags -->
    <link rel="icon" type="image/png" href="{prefix}Logo.png">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{prefix}Logo.png">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Yehoshama Foundation">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{prefix}Logo.png">
'''

    # Ensure we don't duplicate injection
    if 'og:site_name' not in content:
        content = content.replace('</head>', seo_block + '</head>')
        
    # Replace the ascii logo in the navigation header
    content = content.replace('class="ascii-logo">{ ><((\'> }', f'class="logo-link"><img src="{prefix}Logo.png" alt="Yehoshama Foundation" class="site-logo">')
    content = content.replace('class="ascii-logo">{ ><(((\'> }', f'class="logo-link"><img src="{prefix}Logo.png" alt="Yehoshama Foundation" class="site-logo">')
    
    # Replace ascii logo in the hero section (index.html)
    content = content.replace('<div class="hero-logo ascii">{ ><(((\'> }</div>', f'<div class="hero-logo"><img src="{prefix}Logo.png" alt="Yehoshama Foundation Logo"></div>')

    # Replace ascii logo in the footer
    content = content.replace('<span class="ascii-logo">{ ><(((\'> }</span>', f'<img src="{prefix}Logo.png" alt="Yehoshama Foundation" class="site-logo">')
    content = content.replace('<span class="ascii-logo">{ ><((\'> }</span>', f'<img src="{prefix}Logo.png" alt="Yehoshama Foundation" class="site-logo">')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected SEO meta tags and transformed ASCII logos into the image Logo.")
