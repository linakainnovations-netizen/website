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
