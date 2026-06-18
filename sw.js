const CACHE_NAME = 'linaka-v2';
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
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
