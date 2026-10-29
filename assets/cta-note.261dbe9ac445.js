// Human-only qualifier for countries where most contacts are not a fit for a paid service.
// Never runs for crawlers or automation, never touches the homepages, never changes indexable content
// (added client-side after load), never hides or blocks anything.
(function () {
  try {
    var path = location.pathname || '/';
    var HOME = /^\/(?:(?:fr|es|nl|pt-br)\/)?(?:index\.html)?$/i.test(path);
    var lang = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);
    var TEXTS = {
      en: 'Unbanz is a paid professional service. If you only need the official steps, our guides list them.',
      fr: 'Unbanz est un service professionnel payant. Si vous voulez seulement les étapes officielles, nos guides les présentent.',
      es: 'Unbanz es un servicio profesional de pago. Si solo necesitas los pasos oficiales, nuestras guías los explican.',
      pt: 'A Unbanz é um serviço profissional pago. Se você só precisa dos passos oficiais, nossos guias os explicam.',
      nl: 'Unbanz is een betaalde professionele dienst. Als je alleen de officiële stappen nodig hebt, staan die in onze gidsen.'
    };
    var TEXT = TEXTS[lang];
    var MAILS = { en: 'Email us', fr: 'Écrivez-nous', es: 'Escríbenos', pt: 'Envíe-nos un e-mail', nl: 'Mail ons' };
    MAILS.pt = 'Envie um e-mail';
    var MAIL_LABEL = MAILS[lang] || MAILS.en;
    var MAIL_HREF = 'mailto:team@unbanz.com?subject=Account%20help';
    if (navigator.webdriver || /bot\b|bot[\/ ;)]|crawl|spider|slurp|bingpreview|googlebot|google-|facebookexternalhit|gptbot|chatgpt|claude|perplexity|amazonbot|applebot|bytespider|ccbot|duckduck|yandex|baidu|preview|lighthouse|headless|python|curl|wget/i.test(navigator.userAgent || '')) return;
    var LOW = ['IN', 'PK', 'BD', 'NG', 'KE', 'NP', 'LK', 'GH', 'EG', 'IQ', 'DZ', 'MA', 'PH', 'ID',
      'SO', 'VN', 'AF', 'ET', 'UG', 'TZ', 'ZW', 'MM', 'KH', 'YE', 'SD', 'TN', 'CM', 'ZM', 'MW', 'RW', 'SN', 'CI', 'LR', 'SL',
      'SS', 'NE', 'ML', 'BF', 'HT', 'LA', 'TJ', 'UZ', 'KG', 'SY', 'MZ'];
    var KEY = 'ubz_c';
    var mk = function (cls, style) {
      var p = document.createElement('p'); p.className = cls; p.textContent = TEXT; if (style) p.style.cssText = style; return p;
    };
    var run = function (c) {
      if (LOW.indexOf(c) < 0) return;
      var isBtn = function (a) { return /\bbutton\b/.test(a.className || ''); };
      // WhatsApp off for these countries: drop it where an email button sits next to it, otherwise turn it into the email link.
      var noWa = function () {
        document.querySelectorAll('a[href*="wa.me/"]:not([data-ubz-wa])').forEach(function (a) {
          a.setAttribute('data-ubz-wa', '1');
          var box = a.parentNode, mails = [];
          for (var i = 0; box && i < 2 && !mails.length; i++, box = box.parentNode) {
            if (box.querySelectorAll) mails = Array.prototype.slice.call(box.querySelectorAll('a[href^="mailto:"]'));
          }
          if (isBtn(a) && mails.some(isBtn)) { a.style.display = 'none'; return; }
          if (!isBtn(a) && mails.length && !/header-contact/.test(a.className || '')) { a.style.display = 'none'; return; }
          var arrow = a.querySelector('span[aria-hidden]');
          a.href = MAIL_HREF; a.removeAttribute('target'); a.removeAttribute('data-service');
          a.textContent = MAIL_LABEL + ' ';
          if (arrow) a.appendChild(arrow);
          mails.forEach(function (m) { if (!isBtn(m) && /hero-email/.test(m.className || '')) m.style.display = 'none'; });
        });
      };
      var apply = function () {
        noWa();
        if (HOME || !TEXT) return;
        // Contact popup hint.
        document.querySelectorAll('.cm-hint:not(.cta-note)').forEach(function (h) {
          if (h.nextElementSibling && h.nextElementSibling.classList.contains('cta-note')) return;
          h.parentNode.insertBefore(mk('cm-hint cta-note'), h.nextSibling);
        });
        // Inline CTA box in guides.
        document.querySelectorAll('.inline-cta').forEach(function (b) {
          if (b.querySelector('.cta-note')) return;
          b.appendChild(mk('cta-note', 'font-size:.85em;opacity:.8;margin:.6rem 0 0'));
        });
        // Page body note: once per page, under the main contact buttons, or under the page lead as a fallback.
        if (document.querySelector('.cta-note-page') || document.querySelector('.inline-cta')) return;
        var main = document.querySelector('main') || document.body;
        var host = main.querySelector('.hero-cta'), anchor = null;
        if (host) {
          anchor = host;
        } else {
          var h1 = main.querySelector('h1');
          if (!h1) return;
          anchor = h1;
          var n = h1.nextElementSibling;
          if (n && n.tagName === 'P') anchor = n;
        }
        if (!anchor.parentNode) return;
        var p = mk('cta-note cta-note-page', 'font-size:14px;line-height:1.5;opacity:.85;margin:14px 0 0;max-width:36em;color:inherit');
        if (anchor.parentNode.classList && anchor.parentNode.classList.contains('hero-cta')) anchor = anchor.parentNode;
        anchor.parentNode.insertBefore(p, anchor.nextSibling);
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
