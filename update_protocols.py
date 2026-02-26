import os
import re

base_path = r"d:\Documents\Antigravity\YehoshamaFoundation\YehoshamaFoundationWebsite\protocols"

data = {
    "arc.html": {
        "title": "Indestructible Archives (ARC)",
        "subtitle": "Protocol 02: ARC",
        "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">Hardware fails. Hard drives crash. We are developing a way to save your most critical information so that it survives extreme damage. We are designing it so your digital files can be printed onto regular paper and perfectly restored decades later.</p>
                        
                        <h3 style="margin-top: 2rem;">Built for the worst-case scenario</h3>
                        <p>Standard files break completely if a single piece of data is corrupted. Indestructible Archives fundamentally change this approach. Our protocol assumes that storage drives will eventually fail, and it weaves your data with advanced recovery patterns. If a portion of your archive is damaged, the system is designed to gracefully recover and reconstruct the missing pieces.</p>
                        
                        <h3 style="margin-top: 2rem;">The Analogue Fallback</h3>
                        <p>Data that requires electricity to survive is inherently at risk. True to the foundation's philosophy, Indestructible Archives can be translated directly into high-density patterns printed on standard paper. If a user needs absolute, cold-storage sovereignty over a dataset, paper can outlast electronic memory by decades. A standard optical scanner can later perfectly reconstruct your digital files from those printed pages.</p>
                        
                        <h3 style="margin-top: 2rem;">Sovereignty through survival</h3>
                        <p>Information that can easily be lost cannot be truly owned. By engineering a system that fights physical corruption and survives the transition to physical paper, we ensure that your data remains your property, regardless of hardware failure or technological obsolescence.</p>
                    </div>"""
    },
    "shroomdb.html": {
        "title": "Personal Data Vaults (ShroomDB)",
        "subtitle": "Protocol 01: ShroomDB",
        "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">We are building secure, self-organizing digital vaults. Instead of handing your data over to a corporation, you keep everything perfectly organized and protected in a space that only you control.</p>
                        
                        <h3 style="margin-top: 2rem;">A vault that organizes itself</h3>
                        <p>Over time, standard data storage becomes cluttered and slow. Personal Data Vaults are designed to be self-healing and self-organizing. During idle times, the system naturally rearranges your information to ensure lightning-fast access, entirely automatically. You don't need a database administrator or technical knowledge; the vault takes care of itself.</p>
                        
                        <h3 style="margin-top: 2rem;">Infinite compartments</h3>
                        <p>Because of our unique architectural approach, a vault can effortlessly hold entire other vaults inside of it. This creates infinite possibilities for perfectly organizing your digital life, allowing you to completely compartmentalize different users, applications, or security levels without complex setups.</p>
                        
                        <h3 style="margin-top: 2rem;">Absolute security</h3>
                        <p>Our most advanced protective measure ensures that anything running inside your vault is strictly isolated. The system is mathematically walled off so that no uninvited process can reach out to the internet or access unauthorized information, placing sovereign data control firmly back into your hands.</p>
                    </div>"""
    },
    "rune.html": {
        "title": "A Visual Language for Security (Rune)",
        "subtitle": "Protocol 03: Rune",
        "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">We are creating a system of intuitive symbols that bridge the gap between human thought and computer code. It will allow you to process secure information simply by looking at shapes—no complex math or computer required.</p>
                        
                        <h3 style="margin-top: 2rem;">Visual logic over complex math</h3>
                        <p>Standard computer language (zeros and ones) is perfect for machines but impossible for humans to process quickly. Our Visual Language replaces this abstract math with distinct geometric shapes. This structure allows a human to look at two symbols and perform complex operations purely through straightforward spatial reasoning.</p>
                        
                        <h3 style="margin-top: 2rem;">Perfectly readable by machines</h3>
                        <p>While designed for the human mind, this system maintains absolute digital efficiency. The geometries are strictly defined for maximum contrast, meaning a standard smartphone camera or basic digital scanner can instantly and flawlessly read these written symbols back into digital information.</p>
                        
                        <h3 style="margin-top: 2rem;">Empowerment without a processor</h3>
                        <p>By creating a language that both the human brain and the silicon processor can "read" at native speed, we remove the machine's monopoly on data processing. This allows an individual to act as their own secure processing unit, fulfilling our promise of universal accessibility regardless of the technology you have on hand.</p>
                    </div>"""
    },
    "protocol-4.html": {
        "title": "Privacy Without Computers",
        "subtitle": "Protocol 04: Low-Tech Crypto",
        "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">We believe privacy is a fundamental right, even when the internet is entirely unreachable. We are designing methods for proving who you are and securing your messages using nothing more than a pen, paper, and a basic calculator.</p>
                        
                        <h3 style="margin-top: 2rem;">Cryptography for the analogue layer</h3>
                        <p>While massive servers focus on global encrypted traffic, we focus on securing communication between real people in constrained physical environments. This system provides undeniable privacy and verification in spaces where high-tech devices fail or simply cannot exist.</p>
                        
                        <h3 style="margin-top: 2rem;">Message signing & off-the-grid security</h3>
                        <p>Individuals can generate mathematical proof of their identity attached to physical letters or offline transactions. Anyone receiving the message can verify the sender using simple guidelines—often utilizing our visual symbol system for immediate recognition.</p>
                        
                        <h3 style="margin-top: 2rem;">The democratic cipher</h3>
                        <p>By proving that secure communication does not require a modern processor or an internet connection, this system ensures that privacy remains a universal human right, wieldable by anyone capable of basic reasoning.</p>
                    </div>"""
    },
    "protocol-5.html": {
        "title": "Community Trade Off-the-Grid",
        "subtitle": "Protocol 05: Offline Ledger",
        "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">What happens to local markets when the internet fails? We are engineering a system that allows communities to maintain secure, verifiable ledgers and make transactions while completely disconnected from the worldwide web.</p>
                        
                        <h3 style="margin-top: 2rem;">Flawless detection vs. impossible prevention</h3>
                        <p>Modern decentralized finance requires massive computational power and constant internet connectivity to prevent unauthorized transactions. In disconnected environments, that is impossible. Our system shifts the paradigm entirely: instead of trying to prevent physical fraud offline, our mathematics guarantee that any fraudulent alteration to your community's ledger is instantly and irrefutably exposed the moment records are compared.</p>
                        
                        <h3 style="margin-top: 2rem;">Operating in the void</h3>
                        <p>By abandoning the requirement for a global, "always-on" internet connection, communities can maintain complex economic ledgers or voting records through intermittent, local connections—or simply by physically handing off data drives. The system functions smoothly whether running over fiber-optics or carried across a geographical divide by a person.</p>
                        
                        <h3 style="margin-top: 2rem;">Sovereignty beyond the grid</h3>
                        <p>We are proving that community consensus and financial trust do not require a server farm. This tool empowers disconnected regions to govern themselves and manage value locally, returning the power of community record-keeping back to the people.</p>
                    </div>"""
    },
    "protocol-6.html": {
        "title": "Drawing Ideas, Not Typing Code",
        "subtitle": "Protocol 06: M# (Sharp Mind)",
        "vision": """
                    <div class="section-header">
                        <h2>Vision</h2>
                        <div class="accent-line"></div>
                    </div>
                    <div class="prose">
                        <p class="lead">We are fundamentally changing how software is built. Instead of typing endless lines of complex text, our "Sharp Mind" system will allow creators to build secure applications by drawing visual, geometric logic.</p>
                        
                        <h3 style="margin-top: 2rem;">The two-dimensional canvas</h3>
                        <p>Traditional programming relies on pages of complex text. We are replacing that with a deeply intuitive visual grid. Logic flows through spatial relationships and geometric structures instead of written code, fundamentally lowering the barrier to entry while maintaining rigorous application logic.</p>
                        
                        <h3 style="margin-top: 2rem;">Universal creation</h3>
                        <p>Because the logic is structurally visual rather than based on English syntax, the language is universally accessible. It empowers brilliant problem-solvers around the world to architect software without first mastering the archaic syntax of traditional programming.</p>
                        
                        <h3 style="margin-top: 2rem;">Enterprise power, visual simplicity</h3>
                        <p>Despite its visual nature, this is not a toy. It leverages the power of industry-leading computation beneath the hood, providing creators with enterprise-level processing capability driven entirely by a geometric, accessible interface.</p>
                    </div>"""
    },
    "protocol-7.html": {
        "title": "Ultimate Creator Protection",
        "subtitle": "Protocol 08: IP Protection (Name TBD)",
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
    },
    "protocol-8.html": {
        "title": "Universal Language of Understanding",
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
}

for filename, content_data in data.items():
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Title string inside <title></title> if needed:
    html = re.sub(r'<title>.*?</title>', f'<title>{content_data["title"]} &mdash; Yehoshama Foundation</title>', html)

    # Replace <h1>Title</h1> with new title
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{content_data["title"]}</h1>', html, count=1)
    
    # Replace the subtitle
    html = re.sub(r'<p class="subpage-subtitle">.*?</p>', f'<p class="subpage-subtitle">{content_data["subtitle"]}</p>', html, count=1)

    # Replace everything inside <div class="protocol-detail"> ... </div> (excluding the div itself if possible, or replacing its contents)
    # We'll regex replace from the first <div class="section-header"> inside <section id="vision"> up to the end of the section
    start_match = r'<div class="protocol-detail">([\s\S]*?)</div>\s*</div>\s*</section>'
    
    # The replacement will inject the new Vision content, but keep it cleanly enclosed
    html = re.sub(start_match, f'<div class="protocol-detail">\n{content_data["vision"]}\n                </div>\n            </div>\n        </section>', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print(f"Updated {filename}")
