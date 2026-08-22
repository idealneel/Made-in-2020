/* ===== SKELETON LOADER ===== */
window.addEventListener('load', function() {
  document.body.classList.add('loaded');
});

if (document.readyState === 'complete') {
  document.body.classList.add('loaded');
}

/* ===== NAVBAR & HAMBURGER ===== */
document.addEventListener('DOMContentLoaded', function() {
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function() {
      mobileMenu.classList.toggle('hidden');
    });
  }
});

/* ===== MENU PAGE — Category Tab Scrolling ===== */
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.category-tab');
  tabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
      const target = document.getElementById(this.dataset.target);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});
