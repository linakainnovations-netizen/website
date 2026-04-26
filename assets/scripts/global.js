/* D:\linaka_innovations\website\assets\scripts\global.js */
function toggleMenu(btn) {
  document.getElementById('navLinks').classList.toggle('active');
  if (btn) {
    btn.classList.toggle('open');
  } else {
    var toggle = document.querySelector('.menu-toggle');
    if (toggle) toggle.classList.toggle('open');
  }
}

/* PWA Service Worker Registration */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    const swPath = window.location.pathname.includes('/pages/') ? '../sw.js' : 'sw.js';
    navigator.serviceWorker.register(swPath)
      .then(reg => console.log('LINAKA PWA: Service Worker Registered'))
      .catch(err => console.error('LINAKA PWA: Service Worker Error', err));
  });
}
