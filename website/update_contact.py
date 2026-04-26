import re

new_main = """  <main>
    <section class="section" style="background: linear-gradient(135deg, var(--color-green) 0%, #0d2b1e 100%); color: white; padding: 100px 0;">
      <div class="container text-center">
        <h1 style="color: var(--color-gold); font-size: 3rem; margin-bottom: 1rem;">Let's Build Together</h1>
        <p style="font-size: 1.2rem; max-width: 600px; margin: 0 auto; color: rgba(255,255,255,0.9);">
          Have a project in mind? Reach out today and let's turn your vision into a digital reality.
        </p>
      </div>
    </section>

    <section class="section" style="padding: 60px 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
          
          <div class="card" style="text-align: center; padding: 3rem 2rem;">
            <div style="width: 80px; height: 80px; border-radius: 50%; background: rgba(37, 211, 102, 0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2.5rem; color: #25D366;">
              <i class="fab fa-whatsapp">💬</i>
            </div>
            <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">WhatsApp Us</h3>
            <p style="color: var(--color-charcoal); margin-bottom: 1.5rem;">For quick responses and direct messaging.</p>
            <a href="https://wa.me/260979400243" target="_blank" class="btn btn-primary" style="background: #25D366; width: 100%;">Message Now</a>
          </div>
          
          <div class="card" style="text-align: center; padding: 3rem 2rem;">
            <div style="width: 80px; height: 80px; border-radius: 50%; background: rgba(234, 67, 53, 0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2.5rem; color: #EA4335;">
              <i class="fas fa-envelope">✉️</i>
            </div>
            <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Email Us</h3>
            <p style="color: var(--color-charcoal); margin-bottom: 1.5rem;">For formal inquiries and proposal requests.</p>
            <a href="mailto:linakainnovations@gmail.com" class="btn btn-primary" style="background: #EA4335; width: 100%;">Send Email</a>
          </div>
          
          <div class="card" style="text-align: center; padding: 3rem 2rem;">
            <div style="width: 80px; height: 80px; border-radius: 50%; background: rgba(51, 51, 51, 0.1); display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2.5rem; color: #333;">
              <i class="fab fa-github">💻</i>
            </div>
            <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">GitHub</h3>
            <p style="color: var(--color-charcoal); margin-bottom: 1.5rem;">Explore our open-source contributions.</p>
            <a href="https://github.com/" target="_blank" class="btn btn-primary" style="background: #333; width: 100%;">View Profile</a>
          </div>

        </div>

        <div class="card" style="padding: 0; overflow: hidden;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; min-height: 500px;">
            <div style="padding: 4rem;">
              <h3 style="font-size: 2rem; margin-bottom: 1rem;">Send a Message</h3>
              <form>
                <div style="margin-bottom: 1.5rem;">
                  <label style="display: block; font-weight: 600; margin-bottom: 0.5rem;">Full Name</label>
                  <input type="text" style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 4px; font-size: 1rem;" placeholder="Your Name">
                </div>
                <div style="margin-bottom: 1.5rem;">
                  <label style="display: block; font-weight: 600; margin-bottom: 0.5rem;">Email Address</label>
                  <input type="email" style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 4px; font-size: 1rem;" placeholder="Your Email">
                </div>
                <div style="margin-bottom: 1.5rem;">
                  <label style="display: block; font-weight: 600; margin-bottom: 0.5rem;">Message</label>
                  <textarea rows="5" style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 4px; font-size: 1rem; resize: vertical;" placeholder="How can we help you?"></textarea>
                </div>
                <button type="button" class="btn btn-primary" style="width: 100%; font-size: 1.1rem; padding: 1rem;">Submit Message</button>
              </form>
            </div>
            <div style="background: #eee; position: relative;">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d123164.7179040994!2d28.19632822184918!3d-15.416805820359873!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1940f35db6fcebfd%3A0xeab50d4fc8b9fdf6!2sLusaka%2C%20Zambia!5e0!3m2!1sen!2sus!4v1714151240212!5m2!1sen!2sus" width="100%" height="100%" style="border:0; position: absolute; top:0; left:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>"""

with open('pages/contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = re.sub(r'<main>.*?</main>', new_main, html, flags=re.DOTALL)
new_html = new_html.replace('  <style>', '  <style>\n@media(max-width: 768px){ .card > div { grid-template-columns: 1fr !important; } .card > div > div:last-child { min-height: 300px; } }')

if '@media(max-width: 768px)' not in new_html:
    new_html = new_html.replace('</head>', '<style>@media(max-width: 768px){ .card > div { grid-template-columns: 1fr !important; } .card > div > div:last-child { min-height: 300px; } }</style>\n</head>')

with open('pages/contact.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
