import re
import os

files = ['home.html', 'about.html', 'menu.html', 'contact.html']

head_addition = """<link rel="stylesheet" href="styles.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
"""

iframe_replacement = """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3768.558!2d73.1876!3d19.1209!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7952b29c8e6e3%3A0x3e5d6f7a4c9b2f1a!2sCafe%20Made%20In%202020!5e0!3m2!1sen!2sin!4v1" width="100%" height="440" style="border:none; border-radius:16px; display:block;" allowfullscreen="" loading="lazy"></iframe>"""

for f in files:
    filepath = os.path.join(r"d:\idealneel\Made-in-2020", f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Remove all <style> tags and their content
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    
    # 2. Remove all <script> tags and their content
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)

    # 3. Add to <head> if not present
    if 'href="styles.css"' not in content:
        content = content.replace('</head>', f'{head_addition}</head>')

    # 4. Add script to bottom of <body> (before </body>)
    if 'script.js' not in content:
        content = content.replace('</body>', '<script src="script.js"></script>\n</body>')

    # 5. Fix navigation links
    content = re.sub(r'href="[^"]*"([^>]*)>\s*Home\s*</a>', r'href="home.html"\1>Home</a>', content)
    content = re.sub(r'href="[^"]*"([^>]*)>\s*Menu\s*</a>', r'href="menu.html"\1>Menu</a>', content)
    content = re.sub(r'href="[^"]*"([^>]*)>\s*About Us\s*</a>', r'href="about.html"\1>About Us</a>', content)
    content = re.sub(r'href="[^"]*"([^>]*)>\s*Contact\s*</a>', r'href="contact.html"\1>Contact</a>', content)
    
    # Buttons
    content = re.sub(r'<button([^>]*)>(.*?)(Reserve a Table|Order Now|ORDER ONLINE)(.*?)</button>', r'<a\1 href="contact.html">\2\3\4</a>', content, flags=re.DOTALL)

    # 6. Fix contact page map
    if f == 'contact.html':
        content = re.sub(r'<iframe .*?</iframe>', iframe_replacement, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print("HTML refactoring complete.")
