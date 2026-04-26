import re

new_main = """  <main>
    <section class="section" style="padding-top: 80px;">
      <div class="container">
        <h1 class="section-title">Our Services</h1>
        <p class="text-center" style="max-width: 700px; margin: 0 auto 4rem; font-size: 1.1rem;">We provide a comprehensive suite of digital services designed to help your business operate efficiently and scale rapidly.</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem;">
          
          <div class="card" style="padding: 0; overflow: hidden; border-radius: 12px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="width: 100%; height: 220px; overflow: hidden;">
              <img src="../website/assets/images/web_app_dev.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" alt="Web App Development">
            </div>
            <div style="padding: 2rem;">
              <h3 style="color: var(--color-green); font-size: 1.4rem; margin-bottom: 1rem;">Web App Development</h3>
              <p style="color: var(--color-charcoal); line-height: 1.6; margin: 0;">End-to-end development of custom, scalable, and responsive web applications tailored to your specific business requirements.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden; border-radius: 12px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="width: 100%; height: 220px; overflow: hidden;">
              <img src="../website/assets/images/mobile_app.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" alt="Mobile App Development">
            </div>
            <div style="padding: 2rem;">
              <h3 style="color: var(--color-green); font-size: 1.4rem; margin-bottom: 1rem;">Mobile App Development</h3>
              <p style="color: var(--color-charcoal); line-height: 1.6; margin: 0;">High-performance native and cross-platform mobile applications that provide seamless user experiences on iOS and Android.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden; border-radius: 12px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="width: 100%; height: 220px; overflow: hidden;">
              <img src="../website/assets/images/automation_sys.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" alt="Automated Systems">
            </div>
            <div style="padding: 2rem;">
              <h3 style="color: var(--color-green); font-size: 1.4rem; margin-bottom: 1rem;">Automated Systems</h3>
              <p style="color: var(--color-charcoal); line-height: 1.6; margin: 0;">Streamline your operations with intelligent automation, reducing manual workloads and increasing organizational efficiency.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden; border-radius: 12px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="width: 100%; height: 220px; overflow: hidden;">
              <img src="../website/assets/images/digital_marketing.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" alt="Digital Marketing">
            </div>
            <div style="padding: 2rem;">
              <h3 style="color: var(--color-green); font-size: 1.4rem; margin-bottom: 1rem;">Digital Marketing</h3>
              <p style="color: var(--color-charcoal); line-height: 1.6; margin: 0;">Data-driven marketing strategies, SEO, and campaign management to enhance your online presence and reach your target audience effectively.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden; border-radius: 12px; border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="width: 100%; height: 220px; overflow: hidden;">
              <img src="../website/assets/images/graphic_design.png" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" alt="Graphic Design">
            </div>
            <div style="padding: 2rem;">
              <h3 style="color: var(--color-green); font-size: 1.4rem; margin-bottom: 1rem;">Graphic Design</h3>
              <p style="color: var(--color-charcoal); line-height: 1.6; margin: 0;">Professional branding, UI/UX design, and creative visual assets that ensure your brand stands out in a crowded digital landscape.</p>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>"""

with open('pages/services.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = re.sub(r'<main>.*?</main>', new_main, html, flags=re.DOTALL)

with open('pages/services.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
