import os
import glob

files = glob.glob('d:\\Documents\\Antigravity\\YehoshamaFoundation\\YehoshamaFoundationWebsite\\**\\*.html', recursive=True)

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace css/style.css with css/style.css?v=1.1
    # Be careful to handle files in root vs protocols/
    content = content.replace('css/style.css"', 'css/style.css?v=1.1"')
    content = content.replace('js/main.js"', 'js/main.js?v=1.1"')
    
    # In case already modified
    content = content.replace('?v=1.1?v=1.1', '?v=1.1')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated all HTML files with cache-busting query strings.")
