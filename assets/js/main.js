(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Menu */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  function setMenu(open) {
    nav.classList.toggle('open', open);
    document.body.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', open);
    toggle.textContent = open ? 'Sluiten' : 'Menu';
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Stagger siblings in grids */
  var groups = '.countries, .tiles, .ventures, .principles, .steps, .facts, .legal-grid, .services, .timeline';
  Array.prototype.forEach.call(document.querySelectorAll(groups), function (g) {
    var kids = Array.prototype.filter.call(g.children, function (c) { return c.classList.contains('reveal'); });
    kids.forEach(function (c, k) { c.style.setProperty('--stagger', (k % 4) * 120 + 'ms'); });
  });

  /* Images: fade in with a gentle zoom-out */
  if (!reduce) {
    Array.prototype.forEach.call(document.querySelectorAll('.split__img, .portrait'), function (el) { el.classList.add('media'); });
  }

  /* Reveal on scroll */
  var items = document.querySelectorAll('.reveal, .media');
  if (!('IntersectionObserver' in window) || reduce) {
    Array.prototype.forEach.call(items, function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    Array.prototype.forEach.call(items, function (el) { io.observe(el); });
  }

  /* Timeline: draw the line, fill the circles one by one */
  var lines = document.querySelectorAll('.steps');
  Array.prototype.forEach.call(lines, function (ol) {
    var items = ol.querySelectorAll('li');
    Array.prototype.forEach.call(items, function (li, i) {
      li.style.setProperty('--fill-delay', Math.round(200 + (items.length > 1 ? i / (items.length - 1) : 0) * 1700) + 'ms');
    });
  });
  if (reduce || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(lines, function (ol) { ol.classList.add('is-drawn'); });
  } else {
    var lio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-drawn'); lio.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -20% 0px' });
    Array.prototype.forEach.call(lines, function (ol) { lio.observe(ol); });
  }

  /* Header becomes solid after scrolling */
  var header = document.querySelector('.header');
  function onScroll() {
    if (!header || document.body.classList.contains('menu-open')) return;
    var stuck = window.scrollY > 120;
    header.classList.toggle('stuck', stuck);
    document.body.classList.toggle('header-shown', stuck);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

