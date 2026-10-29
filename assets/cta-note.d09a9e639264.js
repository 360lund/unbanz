// Human-only qualifier near the contact buttons for countries where most contacts are not a fit for a paid service.
// Never runs for crawlers or automation, never changes indexable content, never hides or blocks anything.
(function () {
  try {
    if (!/^en/i.test(document.documentElement.lang || '')) return;
    if (navigator.webdriver || /bot\b|bot[\/ ;)]|crawl|spider|slurp|bingpreview|googlebot|google-|facebookexternalhit|gptbot|chatgpt|claude|perplexity|amazonbot|applebot|bytespider|ccbot|duckduck|yandex|baidu|preview|lighthouse|headless|python|curl|wget/i.test(navigator.userAgent || '')) return;
    var LOW = ['IN', 'PK', 'BD', 'NG', 'KE', 'NP', 'LK', 'GH'];
    var TEXT = 'Unbanz is a paid professional service. If you only need the official steps, our guides list them.';
    var KEY = 'ubz_c';
    var run = function (c) {
      if (LOW.indexOf(c) < 0) return;
      var apply = function () {
        document.querySelectorAll('.cm-hint:not(.cta-note)').forEach(function (h) {
          if (h.nextElementSibling && h.nextElementSibling.classList.contains('cta-note')) return;
          var p = document.createElement('p'); p.className = 'cm-hint cta-note'; p.textContent = TEXT; h.parentNode.insertBefore(p, h.nextSibling);
        });
        document.querySelectorAll('.inline-cta').forEach(function (b) {
          if (b.querySelector('.cta-note')) return;
          var p = document.createElement('p'); p.className = 'cta-note'; p.style.cssText = 'font-size:.85em;opacity:.8;margin:.6rem 0 0'; p.textContent = TEXT; b.appendChild(p);
        });
      };
      apply();
      var raf = 0;
      new MutationObserver(function () { if (!raf) raf = requestAnimationFrame(function () { raf = 0; apply(); }); }).observe(document.body, { childList: true, subtree: true });
    };
    var c = null; try { c = sessionStorage.getItem(KEY); } catch (e) {}
    if (c !== null) return run(c);
    fetch('/api/geo/', { credentials: 'omit', cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (j) {
      var v = (j && j.c) || ''; try { sessionStorage.setItem(KEY, v); } catch (e) {}
      run(v);
    }).catch(function () {});
  } catch (e) {}
})();
