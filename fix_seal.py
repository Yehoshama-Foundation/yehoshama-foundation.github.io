import os
import re
import glob

base_path = r"d:\Documents\Antigravity\YehoshamaFoundation\YehoshamaFoundationWebsite"
protocols_path = os.path.join(base_path, "protocols")
old_p8_path = os.path.join(protocols_path, "protocol-8.html")
new_p8_path = os.path.join(protocols_path, "seal.html")

# 1. Rename the file
if os.path.exists(old_p8_path):
    os.rename(old_p8_path, new_p8_path)
    print("Renamed protocol-8.html to seal.html")

# 2. Update protocol-7.html and seal.html with the correct content since they were flipped
p7_data = {
    "title": "Universal Concept Language",
    "subtitle": "Protocol 07: Universal Concept Language",
    "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">Looking to the distant future, we are laying the groundwork for a language that can perfectly explain anything in the universe. It will allow humans and machines to communicate complex concepts deeply and accurately, putting an end to misunderstandings caused by artificial intelligence.</p>
                        
                        <h3 style="margin-top: 2rem;">A language of absolute explanations</h3>
                        <p>This initiative moves beyond simple digital commands. It is engineered to structure human thought and expression in a manner that is deeply nuanced for us, while being flawlessly parsable by a machine. From complex physical mechanisms to abstract societal structures, this language maps absolute conceptual relationships.</p>
                        
                        <h3 style="margin-top: 2rem;">The end of statistical guessing</h3>
                        <p>Today's artificial intelligence relies on statistical "guessing" to understand what humans want, often failing spectacularly. By speaking a structured language of understanding, machines will not have to guess at your meaning—they will fundamentally comprehend the logical relationships you've mapped out.</p>
                        
                        <h3 style="margin-top: 2rem;">Protecting human truth</h3>
                        <p>In an age where AI-generated content dilutes reality, this universal system ensures that genuine human logic and knowledge can be forever documented and perfectly understood, safeguarding our shared intellectual legacy for generations to come.</p>
                    </div>"""
}

seal_data = {
    "title": "Ultimate Creator Protection (Seal)",
    "subtitle": "Protocol 08: Seal",
    "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">We are building a dual-layered shield for artists, writers, and inventors. It allows creators to mathematically prove they were the first to invent an idea—and detect if it was stolen—without ever having to reveal their hidden secrets to the public.</p>
                        
                        <h3 style="margin-top: 2rem;">Establishing a timeline of genesis</h3>
                        <p>When you originate a groundbreaking concept, this system provides you with an irrefutable, unalterable digital timeline. You receive undeniable mathematical proof that you possessed the complete idea before any competitor, locking your ownership in place chronologically.</p>
                        
                        <h3 style="margin-top: 2rem;">Detecting theft without exposure</h3>
                        <p>The true genius of this protective shield lies in how it detects infringement. Using advanced conceptual mapping, our system can detect if another party has stolen and subtly altered your work. Crucially, it achieves this mathematical comparison without you ever needing to present your original work to a central authority or upload it to the public internet.</p>
                        
                        <h3 style="margin-top: 2rem;">Emancipation for the creator</h3>
                        <p>By combining timeline locking with invisible theft detection, we offer creators the ultimate defense. Brilliant individuals and small teams can finally architect world-changing concepts without fear of exploitation by massively funded conglomerates.</p>
                    </div>"""
}

def update_page_content(filepath, data):
    if not os.path.exists(filepath):
        print(f"File not found to update content: {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Title string inside <title></title> if needed:
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} &mdash; Yehoshama Foundation</title>', html)
    # Replace <h1>Title</h1> with new title
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{data["title"]}</h1>', html, count=1)
    # Replace the subtitle
    html = re.sub(r'<p class="subpage-subtitle">.*?</p>', f'<p class="subpage-subtitle">{data["subtitle"]}</p>', html, count=1)

    start_match = r'<div class="protocol-detail">([\s\S]*?)</div>\s*</div>\s*</section>'
    html = re.sub(start_match, f'<div class="protocol-detail">\n{data["vision"]}\n                </div>\n            </div>\n        </section>', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated content of {filepath}")

update_page_content(os.path.join(protocols_path, "protocol-7.html"), p7_data)
update_page_content(new_p8_path, seal_data)


# 3. Global Find and Replace for navigation strings across all HTML files
html_files = glob.glob(os.path.join(base_path, '**', '*.html'), recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False

    # Standardize links
    if 'href="protocols/protocol-8.html"' in content:
        content = content.replace('href="protocols/protocol-8.html"', 'href="protocols/seal.html"')
        changed = True
        
    if 'href="protocol-8.html"' in content:
        content = content.replace('href="protocol-8.html"', 'href="seal.html"')
        changed = True

    # Standardize dropdown display text
    if '>Protocol #8<' in content:
        content = content.replace('>Protocol #8<', '>Seal<')
        changed = True

    # A safety check for anything that hardcoded older naming
    if '>Protocol 08<' in content:
        content = content.replace('>Protocol 08<', '>Seal<')
        changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated nav references in {os.path.basename(file_path)}")

print("Done with Seal updates.")
