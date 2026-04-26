import re

new_main = """  <style>
    /* Premium Home Animations & Styles */
    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .animate-up { animation: fadeInUp 0.8s ease forwards; opacity: 0; }
    .delay-1 { animation-delay: 0.2s; }
    .delay-2 { animation-delay: 0.4s; }
    .delay-3 { animation-delay: 0.6s; }
    
    .hero { position: relative; overflow: hidden; color: white; padding: 12rem 0; text-align: center; }
    .hero video { position: absolute; top: 50%; left: 50%; min-width: 100%; min-height: 100%; width: auto; height: auto; transform: translateX(-50%) translateY(-50%); object-fit: cover; z-index: 0; }
    .hero-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(27, 67, 50, 0.9) 0%, rgba(19, 48, 36, 0.7) 100%); z-index: 1; }
    .hero .container { position: relative; z-index: 2; }
    
    .masonry-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; grid-auto-rows: 250px; }
    .masonry-item { position: relative; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); cursor: pointer; transition: transform 0.3s; }
    .masonry-item:hover { transform: translateY(-10px); }
    .masonry-item img, .masonry-item video { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
    .masonry-item:hover img, .masonry-item:hover video { transform: scale(1.05); }
    .masonry-overlay { position: absolute; bottom: 0; left: 0; right: 0; padding: 2rem; background: linear-gradient(to top, rgba(27,67,50,0.9) 0%, transparent 100%); color: white; }
    
    .masonry-large { grid-row: span 2; }
    
    .feature-card { padding: 3rem 2rem; border-radius: 12px; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: all 0.3s; border-bottom: 4px solid transparent; }
    .feature-card:hover { transform: translateY(-10px); border-bottom-color: var(--color-gold); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
  </style>

  <main>
    <!-- Hero Section -->
    <section class="hero">
      <video autoplay loop muted playsinline>
        <source src="https://assets.mixkit.co/videos/preview/mixkit-business-team-in-a-meeting-5108-large.mp4" type="video/mp4">
      </video>
      <div class="hero-overlay"></div>
      <div class="container">
        <h1 class="animate-up" style="font-size: 4.5rem; color: var(--color-gold); margin-bottom: 1.5rem; font-weight: 800; letter-spacing: -1px; text-shadow: 0 4px 15px rgba(0,0,0,0.3);">LINAKA INNOVATIONS</h1>
        <p class="animate-up delay-1" style="font-size: 1.4rem; color: rgba(255,255,255,0.9); margin-bottom: 3rem; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">
          Designing the future of enterprise software and web solutions.<br><strong>Rooted in Zambia. Built for the world.</strong>
        </p>
        <div class="animate-up delay-2" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
          <a href="pages/services.html" class="btn btn-primary" style="padding: 1.2rem 3rem; font-size: 1.1rem; border-radius: 50px; background: var(--color-gold); color: white; box-shadow: 0 10px 20px rgba(197,160,89,0.3);">Explore Services</a>
          <a href="pages/quote-tool.html" class="btn btn-outline" style="padding: 1.2rem 3rem; font-size: 1.1rem; border-radius: 50px; border: 2px solid white; color: white;">Generate Quote</a>
        </div>
      </div>
    </section>

    <!-- Visual Showcase -->
    <section class="section" style="padding: 8rem 0; background: var(--color-bg);">
      <div class="container">
        <div class="text-center animate-up" style="margin-bottom: 4rem;">
          <h2 style="font-size: 2.8rem; color: var(--color-green);">Our Creative Edge</h2>
          <p style="font-size: 1.1rem; color: var(--color-charcoal); max-width: 600px; margin: 0 auto;">Immersive visual experiences engineered for modern enterprises.</p>
        </div>
        
        <div class="masonry-grid">
          <div class="masonry-item masonry-large animate-up delay-1">
            <video autoplay loop muted playsinline>
              <source src="https://assets.mixkit.co/videos/preview/mixkit-hacker-in-a-dark-room-with-several-monitors-4171-large.mp4" type="video/mp4">
            </video>
            <div class="masonry-overlay">
              <h3 style="color: var(--color-gold); margin:0;">Cybersecurity</h3>
              <p style="margin:0; font-size: 0.9rem;">Robust enterprise protection</p>
            </div>
          </div>
          
          <div class="masonry-item animate-up delay-2">
            <img src="website/assets/images/services_hero.png" alt="Services">
            <div class="masonry-overlay">
              <h3 style="color: var(--color-gold); margin:0;">Cloud Solutions</h3>
              <p style="margin:0; font-size: 0.9rem;">Scalable architecture</p>
            </div>
          </div>
          
          <div class="masonry-item animate-up delay-3">
            <video autoplay loop muted playsinline>
              <source src="https://assets.mixkit.co/videos/preview/mixkit-software-developer-working-on-code-4174-large.mp4" type="video/mp4">
            </video>
            <div class="masonry-overlay">
              <h3 style="color: var(--color-gold); margin:0;">Development</h3>
              <p style="margin:0; font-size: 0.9rem;">Custom software engineering</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Highlights Section -->
    <section class="section" style="padding: 6rem 0; background: white;">
      <div class="container text-center">
        <h2 class="animate-up" style="color: var(--color-green); margin-bottom: 3rem; font-size: 2.8rem;">Empowering Your Business</h2>
        <div class="grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem;">
          <div class="feature-card animate-up delay-1">
            <div style="font-size: 3.5rem; margin-bottom: 1.5rem;">💻</div>
            <h3 style="margin-bottom: 1rem; color: var(--color-green); font-size: 1.5rem;">End-to-end Development</h3>
            <p style="color: var(--color-charcoal); line-height: 1.7;">From initial design to final deployment, we build custom software that scales with your ambition.</p>
          </div>
          <div class="feature-card animate-up delay-2">
            <div style="font-size: 3.5rem; margin-bottom: 1.5rem;">⚙️</div>
            <h3 style="margin-bottom: 1rem; color: var(--color-green); font-size: 1.5rem;">Digital Transformation</h3>
            <p style="color: var(--color-charcoal); line-height: 1.7;">Modernize your workflow with intelligent automated systems and progressive web applications.</p>
          </div>
          <div class="feature-card animate-up delay-3">
            <div style="font-size: 3.5rem; margin-bottom: 1.5rem;">🔒</div>
            <h3 style="margin-bottom: 1rem; color: var(--color-green); font-size: 1.5rem;">Enterprise Tools</h3>
            <p style="color: var(--color-charcoal); line-height: 1.7;">Explore our secure internal platforms, including our dedicated high-res Quote Generator.</p>
          </div>
        </div>
      </div>
    </section>
  </main>"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = re.sub(r'<main>.*?</main>', new_main, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
