import os
import glob
import re

footer_template = """<!-- SITE FOOTER -->
<footer style="position: relative; overflow: hidden; padding: 80px 0 30px; color: #fff; margin-top: 4rem;">
  <video autoplay loop muted playsinline style="position: absolute; top: 50%; left: 50%; min-width: 100%; min-height: 100%; width: auto; height: auto; transform: translateX(-50%) translateY(-50%); object-fit: cover; z-index: 0; opacity: 0.5;">
    <source src="https://assets.mixkit.co/videos/preview/mixkit-software-developer-working-on-code-4174-large.mp4" type="video/mp4">
  </video>
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(27, 67, 50, 0.95) 0%, rgba(19, 48, 36, 0.85) 100%); z-index: 1;"></div>
  
  <div class="container" style="position: relative; z-index: 2;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem; margin-bottom: 3rem;">
      
      <div>
        <h3 style="color: var(--color-gold, #C5A059); margin-bottom: 1rem; font-size: 1.5rem;">LINAKA INNOVATIONS</h3>
        <p style="font-size: 1.05rem; line-height: 1.6; color: rgba(255,255,255,0.9);">
          Custom web & software solutions.<br>Rooted in Zambia. Built for the world.
        </p>
        <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
          <a href="https://wa.me/260979400243" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; transition: all 0.3s; color: #fff; text-decoration: none;" onmouseover="this.style.background='var(--color-gold)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">💬</a>
          <a href="mailto:linakainnovations@gmail.com" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; transition: all 0.3s; color: #fff; text-decoration: none;" onmouseover="this.style.background='var(--color-gold)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">✉️</a>
          <a href="https://github.com/" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; transition: all 0.3s; color: #fff; text-decoration: none;" onmouseover="this.style.background='var(--color-gold)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">💻</a>
        </div>
      </div>

      <div>
        <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.2rem;">Quick Links</h4>
        <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.8rem;">
          <li><a href="{home_path}" style="color: rgba(255,255,255,0.8); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--color-gold)'" onmouseout="this.style.color='rgba(255,255,255,0.8)'">Home</a></li>
          <li><a href="{about_path}" style="color: rgba(255,255,255,0.8); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--color-gold)'" onmouseout="this.style.color='rgba(255,255,255,0.8)'">About</a></li>
          <li><a href="{services_path}" style="color: rgba(255,255,255,0.8); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--color-gold)'" onmouseout="this.style.color='rgba(255,255,255,0.8)'">Services</a></li>
          <li><a href="{projects_path}" style="color: rgba(255,255,255,0.8); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--color-gold)'" onmouseout="this.style.color='rgba(255,255,255,0.8)'">Projects</a></li>
          <li><a href="{contact_path}" style="color: rgba(255,255,255,0.8); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--color-gold)'" onmouseout="this.style.color='rgba(255,255,255,0.8)'">Contact</a></li>
        </ul>
      </div>

      <div>
        <h4 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.2rem;">Our Location</h4>
        <div style="width: 100%; height: 200px; border-radius: 8px; overflow: hidden; border: 2px solid rgba(255,255,255,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d123164.7179040994!2d28.19632822184918!3d-15.416805820359873!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1940f35db6fcebfd%3A0xeab50d4fc8b9fdf6!2sLusaka%2C%20Zambia!5e0!3m2!1sen!2sus!4v1714151240212!5m2!1sen!2sus" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>

    </div>
    
    <div style="text-align: center; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 20px; font-size: 0.95rem; color: rgba(255,255,255,0.7);">
      <p>&copy; 2026 LINAKA INNOVATIONS. All Rights Reserved.</p>
    </div>
  </div>
</footer>
"""

html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'includes' in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    is_root = '/' not in filepath and '\\' not in filepath
    
    if is_root:
        f_html = footer_template.format(
            home_path="index.html",
            about_path="pages/about.html",
            services_path="pages/services.html",
            projects_path="pages/projects.html",
            contact_path="pages/contact.html"
        )
    else:
        f_html = footer_template.format(
            home_path="../index.html",
            about_path="about.html",
            services_path="services.html",
            projects_path="projects.html",
            contact_path="contact.html"
        )
        
    new_html = re.sub(r'<footer.*?</footer>', f_html, html, flags=re.DOTALL | re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
