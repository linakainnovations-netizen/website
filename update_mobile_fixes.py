import re
import glob

# 1. Update global.css to make mobile menu scrollable
with open('website/assets/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    "box-shadow: -5px 0 15px rgba(0,0,0,0.1); transition: right 0.4s cubic-bezier(0.77, 0, 0.175, 1); z-index: 1000; display: flex !important;",
    "box-shadow: -5px 0 15px rgba(0,0,0,0.1); transition: right 0.4s cubic-bezier(0.77, 0, 0.175, 1); z-index: 1000; display: flex !important; overflow-y: auto;"
)

with open('website/assets/styles/global.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html hero for mobile view
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

if "@media (max-width: 768px)" not in index_html.split("/* Premium Home Animations & Styles */")[1]:
    index_html = index_html.replace(
        "/* Premium Home Animations & Styles */",
        "/* Premium Home Animations & Styles */\n    @media (max-width: 768px) { .hero { padding: 6rem 0 !important; } .hero h1 { font-size: 2.8rem !important; } .hero p { font-size: 1.1rem !important; } }"
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# 3. Add background image to Contact page hero
with open('pages/contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

contact_html = contact_html.replace(
    'style="background: linear-gradient(135deg, var(--color-green) 0%, #0d2b1e 100%); color: white; padding: 100px 0;"',
    'style="background: linear-gradient(rgba(27,67,50,0.85), rgba(19,48,36,0.95)), url(\'../website/assets/images/hero_tech_bg.png\') center/cover no-repeat; color: white; padding: 100px 0; background-attachment: fixed;"'
)

with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

# Let's apply it to about, services, and projects too if they have a similar hero
pages = ['pages/about.html', 'pages/services.html', 'pages/projects.html']
for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Their hero might be using just "class="section" and no background. 
        # For example, services.html has <section class="section" style="padding-top: 80px;">
        html = html.replace(
            '<section class="section" style="padding-top: 80px;">',
            '<section class="section" style="background: linear-gradient(rgba(27,67,50,0.9), rgba(19,48,36,0.95)), url(\'../website/assets/images/hero_tech_bg.png\') center/cover no-repeat; padding: 60px 0; color: white;">'
        )
        html = html.replace(
            '<h1 class="section-title">',
            '<h1 class="section-title" style="color: var(--color-gold);">'
        )
        html = html.replace(
            '<p class="text-center" style="max-width: 700px; margin: 0 auto 4rem; font-size: 1.1rem;">',
            '<p class="text-center" style="max-width: 700px; margin: 0 auto 4rem; font-size: 1.1rem; color: rgba(255,255,255,0.9);">'
        )
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(html)
    except:
        pass
