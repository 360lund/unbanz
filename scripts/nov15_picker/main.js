// Email topic picker v3 (Nov 15 2026): two-step sheet. Step 1 = topic cards (grouped, icons), step 2 = username +
// optional "how did you hear" + sticky "Write the email". Mobile: bottom sheet with drag handle; desktop: centered modal.
// Same output as v2: intercepts team@unbanz.com mailto clicks, same topic values, same subject/body template, and
// "How I heard about Unbanz: …" appended to the body (what hear-source.js did). Tracking: the dialog keeps .cm-dialog,
// the topic cards keep .cm-pill[data-group="service"][aria-pressed] and the final link keeps data-service/data-platform.
// The plain mailto href stays as the no-JS fallback. Email is the only contact channel.
(function () {
  try {
    if (document.body && document.body.classList.contains('cta-hold')) return;
    var lang = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);
/*STRINGS*/
    var L = LANGS[lang];
    if (!L) return;
    var MAIL = 'team@unbanz.com';
    var HEAR_VALUES = ['', 'ChatGPT or another AI assistant', 'Google or another search engine', 'A person I know', 'Instagram, Facebook or another app', 'Somewhere else'];
    var GROUPS = [['gIg', ['ig_disabled', 'ig_hacked', 'username']], ['gFb', ['fb', 'page']], ['gAds', ['ad', 'bm']], ['gOther', ['tiktok', 'snap', 'youtube', 'whatsapp', 'other']]];
    var S = function (d) { return '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + d + '</svg>'; };
    var ICON = {
      ig_disabled: S('<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.8"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/>'),
      ig_hacked: S('<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 7.6-1.7"/><path d="M12 14.5v2.5"/>'),
      username: S('<circle cx="12" cy="12" r="3.6"/><path d="M15.6 12v1.4a2.6 2.6 0 0 0 5.2 0V12a8.8 8.8 0 1 0-3.5 7"/>'),
      fb: S('<path d="M14.5 21v-7.5h2.6l.4-3.1h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4a21 21 0 0 0-2.4-.1c-2.4 0-4 1.4-4 4.1v2h-2.6v3.1h2.6V21"/>'),
      page: S('<path d="M5 21V4"/><path d="M5 4.5h11.5l-2 4 2 4H5"/>'),
      ad: S('<path d="M4 10.5v3a1.5 1.5 0 0 0 1.5 1.5H7l9 4.5V4.5L7 9H5.5A1.5 1.5 0 0 0 4 10.5Z"/><path d="M8.5 15.2 10 20"/><path d="M19 9.5a3.5 3.5 0 0 1 0 5"/>'),
      bm: S('<rect x="3.5" y="7.5" width="17" height="12" rx="2.5"/><path d="M9 7.5V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.5"/><path d="M3.5 12.5h17"/>'),
      tiktok: S('<path d="M13.5 3.5v11.2a3.3 3.3 0 1 1-3.3-3.3"/><path d="M13.5 3.5c.4 2.6 2.2 4.4 4.8 4.6"/>'),
      snap: S('<path d="M12 3.6c2.9 0 4.6 2.1 4.6 4.8v2.2l1.9-.5c.5 0 .7.6.3.9l-2 1.2c.6 1.7 1.9 3 3.6 3.5-.3.8-1.4 1-2.4 1.2l-.4 1.3-1.6-.2c-1 0-1.8 1.4-4 1.4s-3-1.4-4-1.4l-1.6.2-.4-1.3c-1-.2-2.1-.4-2.4-1.2 1.7-.5 3-1.8 3.6-3.5l-2-1.2c-.4-.3-.2-.9.3-.9l1.9.5V8.4c0-2.7 1.7-4.8 4.6-4.8Z"/>'),
      youtube: S('<rect x="2.8" y="5.5" width="18.4" height="13" rx="4"/><path d="m10.2 9.2 4.8 2.8-4.8 2.8Z" fill="currentColor"/>'),
      whatsapp: S('<path d="M4.2 19.8 5.4 16A8 8 0 1 1 8.4 18.8Z"/><path d="M9.3 8.6c.2-.4.6-.5.9-.4l.6 1.5c.1.3 0 .5-.2.7l-.4.5c.5 1 1.3 1.8 2.3 2.3l.5-.4c.2-.2.5-.3.7-.2l1.5.6c.2.3 0 .8-.4 1-1 .7-2.6.3-4.3-1.3-1.6-1.6-2.1-3.3-1.2-4.3Z"/>'),
      other: S('<circle cx="12" cy="12" r="8.5"/><path d="M9.7 9.6a2.4 2.4 0 1 1 3.3 2.2c-.6.3-1 .8-1 1.5v.4"/><circle cx="12" cy="16.6" r=".5" fill="currentColor"/>')
    };
    var CHECK = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>';
    var CHEV = '<svg class="mp-chev" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m9 6 6 6-6 6"/></svg>';
    var BACK = '<svg class="mp-flip" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m15 6-6 6 6 6"/></svg>';
    var X = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>';
    var CSS = '/*CSS*/';
    var modal, sheet, lastFocus, topic = null, input, hear, go, step = 1, busy = false, scrollY = 0;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    var find = function (k) { for (var i = 0; i < L.t.length; i++) if (L.t[i][0] === k) return L.t[i]; return null; };
    var infer = function () {
      var s = location.pathname.toLowerCase();
      if (/snapchat/.test(s)) return 'snap';
      if (/tiktok/.test(s)) return 'tiktok';
      if (/youtube/.test(s)) return 'youtube';
      if (/whatsapp/.test(s)) return 'whatsapp';
      if (/username|gebruikersnaam|pseudo|one-letter|\/og-/.test(s)) return 'username';
      if (/business-portfolio|business-manager|business-suite/.test(s)) return 'bm';
      if (/ad-account|ads-|meta-ad|advertentie|publicit|pixel/.test(s)) return 'ad';
      if (/instagram/.test(s)) return /hack|pirat|gehackt/.test(s) ? 'ig_hacked' : 'ig_disabled';
      if (/facebook/.test(s)) return /facebook-page|page-recovery|-page-|pagina-facebook|page-facebook|facebookpagina/.test(s) ? 'page' : 'fb';
      return null;
    };
    var href = function () {
      var t = find(topic) || find('other'), u = (input.value || '').replace(/[\r\n]+/g, ' ').trim().slice(0, 120);
      var body = L.hi + '\n\n' + L.f[0] + ': ' + t[3] + '\n' + L.f[1] + ': ' + u + '\n' + L.f[2] + ': \n' + L.f[3] + ': \n' + L.f[4] + ': \n\n' + L.bye;
      if (hear && hear.value) body += '\nHow I heard about Unbanz: ' + hear.value;
      return 'mailto:' + MAIL + '?subject=' + encodeURIComponent(t[2]) + '&body=' + encodeURIComponent(body);
    };
    var update = function () {
      var t = find(topic);
      go.href = href();
      go.setAttribute('aria-disabled', String(!t));
      go.classList.toggle('mp-off', !t);
      go.dataset.service = t ? t[0] : '';
      if (t && t[4]) go.dataset.platform = t[4]; else delete go.dataset.platform;
      modal.querySelectorAll('.cm-pill').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.value === topic)); });
      if (t) {
        modal.querySelector('.mp-sel-ic').innerHTML = ICON[t[0]] || '';
        modal.querySelector('.mp-sel-tx').textContent = t[1];
      }
    };
    var card = function (k) {
      var t = find(k); if (!t) return '';
      return '<button type="button" class="cm-pill mp-card" data-group="service" data-value="' + t[0] + '" aria-pressed="false">' +
        '<span class="mp-ic">' + (ICON[k] || '') + '</span><span class="mp-tx">' + esc(t[1]) + '</span><span class="mp-ck">' + CHECK + '</span></button>';
    };
    var build = function () {
      var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
      var groups = GROUPS.map(function (g, i) {
        return '<div class="mp-group"><p class="mp-gl" id="mp-g' + i + '">' + esc(L[g[0]]) + '</p><div class="mp-grid" role="group" aria-labelledby="mp-g' + i + '">' + g[1].map(card).join('') + '</div></div>';
      }).join('');
      var opts = HEAR_VALUES.map(function (v, i) { return '<option value="' + esc(v) + '">' + esc(L.hear[i + 1]) + '</option>'; }).join('');
      modal = document.createElement('div');
      modal.className = 'cm-backdrop mp-backdrop mp3';
      modal.hidden = true;
      modal.innerHTML = '<div class="cm-dialog mp-dialog mp-sheet" role="dialog" aria-modal="true" aria-labelledby="mp-title" tabindex="-1" data-step="1">' +
        '<div class="mp-drag"><span class="mp-grab" aria-hidden="true"></span>' +
        '<div class="mp-bar"><button type="button" class="mp-back" aria-label="' + esc(L.back) + '">' + BACK + '</button>' +
        '<div class="mp-prog" role="img" aria-label="' + esc(L.step.replace('%s', '1')) + '"><i class="on"></i><i></i></div>' +
        '<button type="button" class="cm-close mp-x" aria-label="' + esc(L.close) + '">' + X + '</button></div></div>' +
        '<div class="mp-body"><div class="mp-steps">' +
        '<section class="mp-step mp-s1" aria-labelledby="mp-title"><p class="eyebrow cm-eyebrow mp-eye">' + esc(L.eyebrow) + '</p>' +
        '<h2 id="mp-title">' + esc(L.title) + '</h2><p class="cm-hint mp-hint">' + esc(L.hint) + '</p>' + groups + '</section>' +
        '<section class="mp-step mp-s2" aria-labelledby="mp-sel-l" hidden>' +
        '<button type="button" class="mp-sel" aria-describedby="mp-sel-c"><span class="mp-ic mp-sel-ic"></span><span class="mp-sel-txw"><span class="mp-sel-tx" id="mp-sel-l"></span>' +
        '<span class="mp-sel-c" id="mp-sel-c">' + esc(L.change) + '</span></span>' + CHEV + '</button>' +
        '<label class="mp-label" for="mp-user">' + esc(L.user) + ' <span>' + esc(L.opt) + '</span></label>' +
        '<input id="mp-user" class="mp-input" type="text" maxlength="120" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="send" dir="auto" placeholder="' + esc(L.ph) + '">' +
        '<label class="mp-label" for="ubz-hear-mail">' + esc(L.hear[0]) + ' <span>' + esc(L.opt) + '</span></label>' +
        '<div class="mp-selwrap"><select id="ubz-hear-mail" class="mp-input mp-select">' + opts + '</select></div>' +
        '</section></div></div>' +
        '<div class="mp-foot"><div class="cm-actions mp-act"><a class="button button-blue mp-go" href="mailto:' + MAIL + '">' + esc(L.go) + ' <span aria-hidden="true">↗︎</span></a></div>' +
        '<p class="cm-note mp-note">' + esc(L.note) + '</p></div></div>';
      document.body.appendChild(modal);
      sheet = modal.querySelector('.mp-sheet');
      input = modal.querySelector('#mp-user');
      hear = modal.querySelector('#ubz-hear-mail');
      go = modal.querySelector('.mp-go');
      modal.addEventListener('click', function (e) {
        var pill = e.target.closest('.cm-pill');
        if (pill) { topic = pill.dataset.value; update(); setTimeout(function () { show(2); }, reduce ? 0 : 160); return; }
        if (e.target.closest('.mp-back') || e.target.closest('.mp-sel')) { show(1); return; }
        if (e.target === modal || e.target.closest('.cm-close')) close();
      });
      input.addEventListener('input', update);
      hear.addEventListener('change', update);
      input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go.click(); } });
      go.addEventListener('click', function (e) {
        if (!find(topic)) { e.preventDefault(); e.stopImmediatePropagation(); show(1); return; }
        update(); setTimeout(close, 60);
      }, true);
      modal.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { e.preventDefault(); close(); return; }
        if (e.key === 'Tab') {
          var f = Array.prototype.filter.call(modal.querySelectorAll('button, a[href], input, select'), function (el) { return el.offsetParent !== null && !el.closest('[hidden]'); });
          if (!f.length) return;
          var first = f[0], last = f[f.length - 1];
          if (e.shiftKey && (document.activeElement === first || document.activeElement === sheet)) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      });
      drag();
    };
    // Switch steps with a height morph and a short slide. Hidden step gets [hidden] so it is out of tab order and AT.
    var show = function (n, instant) {
      if (busy && !instant) return;
      var from = modal.querySelector('.mp-s' + step), to = modal.querySelector('.mp-s' + n);
      var prog = modal.querySelector('.mp-prog');
      prog.children[1].classList.toggle('on', n === 2);
      prog.setAttribute('aria-label', L.step.replace('%s', String(n)));
      sheet.setAttribute('data-step', String(n));
      if (n === step || instant || reduce) {
        from.hidden = n !== step; to.hidden = false; step = n; after(n); return;
      }
      busy = true;
      var h0 = sheet.offsetHeight;
      var dir = n > step ? 1 : -1;
      from.hidden = true; to.hidden = false;
      var h1 = sheet.offsetHeight;
      to.style.setProperty('--mp-dx', (dir * 28) + 'px');
      to.classList.add('mp-in');
      sheet.style.height = h0 + 'px'; void sheet.offsetHeight;
      sheet.classList.add('mp-morph'); sheet.style.height = h1 + 'px';
      step = n;
      setTimeout(function () { sheet.classList.remove('mp-morph'); sheet.style.height = ''; to.classList.remove('mp-in'); busy = false; }, 340);
      after(n);
    };
    var after = function (n) {
      modal.querySelector('.mp-body').scrollTop = 0;
      if (n === 2) {
        setTimeout(function () { try { input.focus({ preventScroll: true }); } catch (e) { input.focus(); } }, reduce ? 0 : 260);
      } else {
        var b = modal.querySelector('.cm-pill[aria-pressed="true"]');
        if (b && document.activeElement && modal.contains(document.activeElement)) b.focus({ preventScroll: false });
      }
    };
    // Drag the handle/top bar down to dismiss (touch + mouse). Small drags spring back.
    var drag = function () {
      var area = modal.querySelector('.mp-drag'), y0 = null, t0 = 0, dy = 0;
      area.addEventListener('pointerdown', function (e) {
        if (e.target.closest('button') || !matchMedia('(max-width: 640px)').matches) return;
        e.preventDefault(); y0 = e.clientY; t0 = Date.now(); dy = 0; sheet.classList.add('mp-dragging');
        try { area.setPointerCapture(e.pointerId); } catch (x) {}
      });
      area.addEventListener('pointermove', function (e) {
        if (y0 === null) return;
        dy = Math.max(0, e.clientY - y0);
        sheet.style.transform = 'translate3d(0,' + dy + 'px,0)';
      });
      var end = function () {
        if (y0 === null) return;
        var v = dy / Math.max(1, Date.now() - t0);
        y0 = null; sheet.classList.remove('mp-dragging'); sheet.style.transform = '';
        if (dy > 110 || (dy > 30 && v > 0.6)) close();
      };
      area.addEventListener('pointerup', end); area.addEventListener('pointercancel', end);
    };
    var lock = function (on) {
      var de = document.documentElement, b = document.body;
      if (on) {
        scrollY = window.scrollY || 0;
        de.classList.add('cm-lock');
        b.style.position = 'fixed'; b.style.top = (-scrollY) + 'px'; b.style.left = '0'; b.style.right = '0'; b.style.width = '100%';
      } else {
        de.classList.remove('cm-lock');
        b.style.position = ''; b.style.top = ''; b.style.left = ''; b.style.right = ''; b.style.width = '';
        var se = de.style.scrollBehavior; de.style.scrollBehavior = 'auto'; window.scrollTo(0, scrollY); de.style.scrollBehavior = se;
      }
    };
    var open = function (preset) {
      if (!modal) build();
      if (!modal.hidden && modal.classList.contains('is-open')) return;
      var pre = (preset && find(preset)) ? preset : null;
      topic = pre || infer();
      if (pre === 'other') pre = null; // a generic "Other" link still starts at the topic cards, with Other preselected
      input.value = ''; hear.value = '';
      update();
      step = pre ? 1 : 2; show(pre ? 2 : 1, true);
      lastFocus = document.activeElement;
      modal.hidden = false;
      lock(true);
      void modal.offsetWidth; modal.classList.add('is-open');
      if (pre) setTimeout(function () { input.focus({ preventScroll: true }); }, reduce ? 0 : 320);
      else sheet.focus({ preventScroll: true });
    };
    var close = function () {
      if (!modal || modal.hidden) return;
      modal.classList.remove('is-open');
      lock(false);
      setTimeout(function () { modal.hidden = true; }, reduce ? 0 : 320);
      if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) {}
    };
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
      if (!a || a.closest('.cm-dialog') || !/^mailto:team@unbanz\.com/i.test(a.getAttribute('href') || '')) return;
      e.preventDefault();
      open(a.getAttribute('data-topic'));
    });
    window.unbanzMailPick = { open: open, close: close };
  } catch (e) {}
})();
