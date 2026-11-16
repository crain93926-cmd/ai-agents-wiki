// 教學簡報的換頁與縮放。不依賴任何外部函式庫。
(function () {
  var stage = document.getElementById('stage');
  var slides = Array.prototype.slice.call(document.querySelectorAll('section.slide'));
  var bar = document.getElementById('bar');
  var count = document.getElementById('count');
  var hint = document.getElementById('hint');
  var current = 0;

  function fit() {
    var box = stage.parentElement.getBoundingClientRect();
    var scale = Math.min(box.width / 1280, box.height / 720);
    stage.style.transform = 'scale(' + scale + ')';
  }

  function go(i, keepHash) {
    current = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (s, n) { s.classList.toggle('active', n === current); });
    bar.style.width = ((current + 1) / slides.length * 100) + '%';
    count.textContent = (current + 1) + ' / ' + slides.length;
    if (!keepHash) { history.replaceState(null, '', '#' + (current + 1)); }
  }

  function fromHash() {
    var n = parseInt(location.hash.replace('#', ''), 10);
    return isNaN(n) ? 0 : n - 1;
  }

  // 小測驗：答案預設蓋住，點一下才顯示
  document.querySelectorAll('.layout-quiz blockquote').forEach(function (q) {
    q.classList.add('hidden');
    q.setAttribute('tabindex', '0');
    q.setAttribute('role', 'button');
    q.setAttribute('aria-label', '顯示答案');
    function reveal(e) { q.classList.remove('hidden'); e.stopPropagation(); }
    q.addEventListener('click', reveal);
    q.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { reveal(e); e.preventDefault(); } });
  });

  document.getElementById('prev').addEventListener('click', function () { go(current - 1); });
  document.getElementById('next').addEventListener('click', function () { go(current + 1); });
  document.addEventListener('keydown', function (e) {
    if (e.target && e.target.getAttribute && e.target.getAttribute('role') === 'button') { return; }
    if (['ArrowRight', 'PageDown', ' ', 'Enter'].indexOf(e.key) !== -1) { go(current + 1); e.preventDefault(); }
    else if (['ArrowLeft', 'PageUp', 'Backspace'].indexOf(e.key) !== -1) { go(current - 1); e.preventDefault(); }
    else if (e.key === 'Home') { go(0); }
    else if (e.key === 'End') { go(slides.length - 1); }
  });

  var startX = null;
  document.addEventListener('touchstart', function (e) { startX = e.touches[0].clientX; }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (startX === null) { return; }
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) { go(current + (dx < 0 ? 1 : -1)); }
    startX = null;
  });

  window.addEventListener('resize', fit);
  window.addEventListener('hashchange', function () { go(fromHash(), true); });

  window.__deck = { go: function (i) { go(i, true); }, count: slides.length };
  fit();
  go(fromHash(), true);
})();
