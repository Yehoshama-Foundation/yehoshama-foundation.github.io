import os
import glob

# HTML snippet to inject before closing </body>
BANNER_HTML = """
    <!-- Under Construction Banner -->
    <div class="construction-banner">
        <span>🚧 We are currently building this site. Everything is under construction. 🚧</span>
    </div>
"""

files = glob.glob('d:\\Documents\\Antigravity\\YehoshamaFoundation\\YehoshamaFoundationWebsite\\**\\*.html', recursive=True)

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid injecting multiple times
    if 'class="construction-banner"' not in content:
        # Add banner right before closing body tag
        if '</body>' in content:
            content = content.replace('</body>', f'{BANNER_HTML}\n</body>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Added banner to {file_path}")

print("Done injecting banner.")
