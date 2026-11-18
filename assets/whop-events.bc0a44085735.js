// Whop custom events for Unbanz. Does not alter the base pixel snippet.
// view_content: once on the homepage and /instagram-account-recovery/.
// contact: any mailto / email CTA that opens the onboarding modal (not the in-modal "Write the email" link).
// submit_application + schedule: successful completion of the onboarding modal ("Write the email").
(function () {
  'use strict';
  if (window.__unbanzWhopEvents) return;
  window.__unbanzWhopEvents = true;

  function track(name) {
    var tries = 0;
    var max = 40;
    function fire() {
      tries += 1;
      try {
        if (typeof whop !== 'undefined' && whop && typeof whop.track === 'function') {
          whop.track(name);
          return true;
        }
      } catch (err) {}
      return false;
    }
    if (fire()) return;
    var id = setInterval(function () {
      if (fire() || tries >= max) clearInterval(id);
    }, 100);
  }

  var path = (location.pathname || '/').replace(/\/+$/, '') || '/';
  if (path === '/' || path === '/index.html' || path === '/instagram-account-recovery') {
    track('view_content');
  }

  document.addEventListener('click', function (event) {
    if (event.button !== 0) return;
    var node = event.target && event.target.closest ? event.target.closest('a[href]') : null;
    if (!node) return;
    var href = node.getAttribute('href') || '';
    if (!/^mailto:/i.test(href)) return;
    if (node.classList.contains('mp-go') || node.closest('.cm-dialog') || node.closest('.mp-sheet')) return;
    track('contact');
  }, true);

  document.addEventListener('click', function (event) {
    if (event.button !== 0) return;
    var node = event.target && event.target.closest ? event.target.closest('a.mp-go') : null;
    if (!node) return;
    if (node.getAttribute('aria-disabled') === 'true' || node.classList.contains('mp-off')) return;
    track('submit_application');
    track('schedule');
  }, true);
})();
