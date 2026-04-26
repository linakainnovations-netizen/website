import os
import glob

# 1. Update global.js
js_code = """/* D:\\linaka_innovations\\website\\assets\\scripts\\global.js */
function toggleMenu(btn) {
  document.getElementById('navLinks').classList.toggle('active');
  if (btn) {
    btn.classList.toggle('open');
  } else {
    var toggle = document.querySelector('.menu-toggle');
    if (toggle) toggle.classList.toggle('open');
  }
}
"""
with open('website/assets/scripts/global.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

# 2. Update global.css
with open('website/assets/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_menu_toggle = ".menu-toggle { display: none; background: none; border: none; font-size: 1.5rem; color: var(--color-green); cursor: pointer; }"
new_menu_toggle = """/* Animated Hamburger */
.menu-toggle {
  display: none; background: none; border: none; width: 30px; height: 24px; position: relative; cursor: pointer; z-index: 1001;
}
.menu-toggle span {
  display: block; position: absolute; height: 3px; width: 100%; background: var(--color-green); border-radius: 3px; transition: var(--transition);
}
.menu-toggle span:nth-child(1) { top: 0px; }
.menu-toggle span:nth-child(2) { top: 10px; }
.menu-toggle span:nth-child(3) { top: 20px; }
.menu-toggle.open span:nth-child(1) { top: 10px; transform: rotate(45deg); }
.menu-toggle.open span:nth-child(2) { opacity: 0; }
.menu-toggle.open span:nth-child(3) { top: 10px; transform: rotate(-45deg); }"""

css = css.replace(old_menu_toggle, new_menu_toggle)

old_media_query = """@media (max-width: 768px) {
  .nav-links { display: none; flex-direction: column; position: absolute; top: 80px; left: 0; width: 100%; background: var(--color-white); padding: 1rem 0; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
  .nav-links.active { display: flex; }
  .menu-toggle { display: block; }
}"""

new_media_query = """@media (max-width: 768px) {
  .menu-toggle { display: block; margin-left: auto; }
  .nav-links {
    position: fixed; top: 0; right: -100%; width: 280px; height: 100vh;
    background: var(--color-white); flex-direction: column; padding-top: 100px;
    box-shadow: -5px 0 15px rgba(0,0,0,0.1); transition: right 0.4s cubic-bezier(0.77, 0, 0.175, 1); z-index: 1000; display: flex !important;
  }
  .nav-links.active { right: 0; }
  .nav-links li { margin: 1rem 0; width: 100%; text-align: center; }
  .nav-links a { display: block; width: 100%; padding: 0.5rem; font-size: 1.2rem; }
}"""

css = css.replace(old_media_query, new_media_query)
with open('website/assets/styles/global.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update all HTML files with new button
html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('<button class="menu-toggle" onclick="toggleMenu()">☰</button>', '<button class="menu-toggle" onclick="toggleMenu(this)"><span></span><span></span><span></span></button>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
