const CACHE_NAME = 'linaka-v1';
const ASSETS = [
  './',
  './index.html',
  './assets/styles/global.css',
  './assets/scripts/global.js',
  './assets/icons/logo.png',
  './pages/about.html',
  './pages/services.html',
  './pages/projects.html',
  './pages/contact.html',
  './pages/quote-tool.html'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
