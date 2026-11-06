// Email topic picker: intercepts team@unbanz.com mailto clicks and opens a small "What do you need help with?"
// dialog (same look as the WhatsApp popup). The chosen topic prefills the subject and a short body template.
// The plain mailto href stays as the no-JS fallback; the tracker still logs the first click (k=email) and logs
// the final "Write the email" click again with the topic in data-service.
(function () {
  try {
    if (document.body && document.body.classList.contains('cta-hold')) return;
    var lang = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);
    var L = {
      en: {
        eyebrow: 'EMAIL US', title: 'What do you need help with?',
        hint: 'Pick one and your email opens with a short template ready to fill in.',
        user: 'Your username or profile link', opt: '(optional)', ph: '@username or link',
        go: 'Write the email', note: 'Never send passwords or login codes.', close: 'Close',
        hi: 'Hi Unbanz', f: ['My issue', 'My username or profile link', 'What the notice says', 'Did I already appeal', 'Country'], bye: 'Thanks',
        t: [
          ['ig_disabled', 'Instagram disabled / suspended', 'Instagram disabled - help', 'Instagram account disabled', 'Instagram'],
          ['ig_hacked', 'Instagram hacked', 'Instagram hacked - help', 'Instagram account hacked', 'Instagram'],
          ['fb', 'Facebook disabled / hacked', 'Facebook account - help', 'Facebook account disabled or hacked', 'Facebook'],
          ['ad', 'Ad account restricted', 'Ad account restricted - help', 'Ad account restricted or disabled', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - help', 'Business Portfolio / Business Manager restricted', 'Facebook'],
          ['username', 'Username', 'Username claim - help', 'Username claim', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat account - help', 'Snapchat account locked or banned', 'Snapchat'],
          ['other', 'Other', 'Account help', 'Other', '']
        ]
      },
      fr: {
        eyebrow: 'ÉCRIVEZ-NOUS', title: 'Pour quoi avez-vous besoin d’aide ?',
        hint: 'Choisissez une option : votre e-mail s’ouvre avec un court modèle à compléter.',
        user: 'Votre nom d’utilisateur ou lien du profil', opt: '(facultatif)', ph: '@pseudo ou lien',
        go: 'Écrire l’e-mail', note: 'N’envoyez jamais de mot de passe ni de code de connexion.', close: 'Fermer',
        hi: 'Bonjour Unbanz', f: ['Mon problème', 'Mon nom d’utilisateur ou lien du profil', 'Ce que dit la notification', 'Ai-je déjà fait appel', 'Pays'], bye: 'Merci',
        t: [
          ['ig_disabled', 'Instagram désactivé / suspendu', 'Instagram désactivé - aide', 'Compte Instagram désactivé', 'Instagram'],
          ['ig_hacked', 'Instagram piraté', 'Instagram piraté - aide', 'Compte Instagram piraté', 'Instagram'],
          ['fb', 'Facebook désactivé / piraté', 'Compte Facebook - aide', 'Compte Facebook désactivé ou piraté', 'Facebook'],
          ['ad', 'Compte publicitaire restreint', 'Compte publicitaire restreint - aide', 'Compte publicitaire restreint ou désactivé', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - aide', 'Business Portfolio / Business Manager restreint', 'Facebook'],
          ['username', 'Nom d’utilisateur', 'Nom d’utilisateur - aide', 'Récupérer un nom d’utilisateur', 'Instagram'],
          ['snap', 'Snapchat', 'Compte Snapchat - aide', 'Compte Snapchat bloqué ou banni', 'Snapchat'],
          ['other', 'Autre', 'Aide pour un compte', 'Autre', '']
        ]
      },
      nl: {
        eyebrow: 'MAIL ONS', title: 'Waar heb je hulp bij nodig?',
        hint: 'Kies er één en je e-mail opent met een kort sjabloon om in te vullen.',
        user: 'Je gebruikersnaam of profiellink', opt: '(optioneel)', ph: '@gebruikersnaam of link',
        go: 'Schrijf de e-mail', note: 'Stuur nooit wachtwoorden of inlogcodes.', close: 'Sluiten',
        hi: 'Hoi Unbanz', f: ['Mijn probleem', 'Mijn gebruikersnaam of profiellink', 'Wat er in de melding staat', 'Heb ik al bezwaar gemaakt', 'Land'], bye: 'Bedankt',
        t: [
          ['ig_disabled', 'Instagram uitgeschakeld / geschorst', 'Instagram uitgeschakeld - hulp', 'Instagram-account uitgeschakeld', 'Instagram'],
          ['ig_hacked', 'Instagram gehackt', 'Instagram gehackt - hulp', 'Instagram-account gehackt', 'Instagram'],
          ['fb', 'Facebook uitgeschakeld / gehackt', 'Facebook-account - hulp', 'Facebook-account uitgeschakeld of gehackt', 'Facebook'],
          ['ad', 'Advertentieaccount beperkt', 'Advertentieaccount beperkt - hulp', 'Advertentieaccount beperkt of uitgeschakeld', 'Facebook'],
          ['bm', 'Business Portfolio / Business Manager', 'Business Portfolio - hulp', 'Business Portfolio / Business Manager beperkt', 'Facebook'],
          ['username', 'Gebruikersnaam', 'Gebruikersnaam - hulp', 'Gebruikersnaam claimen', 'Instagram'],
          ['snap', 'Snapchat', 'Snapchat-account - hulp', 'Snapchat-account geblokkeerd of verbannen', 'Snapchat'],
          ['other', 'Anders', 'Hulp met mijn account', 'Anders', '']
        ]
      }
    }[lang];
    if (!L) return;
    var MAIL = 'team@unbanz.com';
    var modal, lastFocus, topic = null, input, go;
    var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    var find = function (k) { for (var i = 0; i < L.t.length; i++) if (L.t[i][0] === k) return L.t[i]; return null; };
    var infer = function () {
      var s = location.pathname.toLowerCase();
      if (/snapchat/.test(s)) return 'snap';
      if (/username|gebruikersnaam|pseudo|one-letter|\/og-/.test(s)) return 'username';
      if (/business-portfolio|business-manager|business-suite/.test(s)) return 'bm';
      if (/ad-account|ads-|meta-ad|advertentie|publicit|pixel/.test(s)) return 'ad';
      if (/instagram/.test(s)) return /hack|pirat|gehackt/.test(s) ? 'ig_hacked' : 'ig_disabled';
      if (/facebook/.test(s)) return 'fb';
      return null;
    };
    var href = function () {
      var t = find(topic) || find('other'), u = (input.value || '').replace(/[\r\n]+/g, ' ').trim().slice(0, 120);
      var body = L.hi + '\n\n' + L.f[0] + ': ' + t[3] + '\n' + L.f[1] + ': ' + u + '\n' + L.f[2] + ': \n' + L.f[3] + ': \n' + L.f[4] + ': \n\n' + L.bye;
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
    };
    var build = function () {
      var st = document.createElement('style');
      st.textContent = '.mp-dialog .cm-pills{margin-bottom:16px}.mp-dialog input{display:block;box-sizing:border-box;width:100%;min-height:46px;padding:11px 14px;border:1px solid #d6e5f0;border-radius:16px;background:#fff;color:var(--ink,#111);font:inherit;font-size:16px;margin:0 0 16px}.mp-dialog input:focus{outline:2px solid var(--blue,#2a7fd4);outline-offset:2px}.mp-dialog .mp-off{opacity:.5}';
      document.head.appendChild(st);
      modal = document.createElement('div');
      modal.className = 'cm-backdrop mp-backdrop';
      modal.hidden = true;
      modal.innerHTML = '<div class="cm-dialog mp-dialog" role="dialog" aria-modal="true" aria-labelledby="mp-title" tabindex="-1">' +
        '<button type="button" class="cm-close" aria-label="' + esc(L.close) + '">×</button>' +
        '<p class="eyebrow cm-eyebrow">' + esc(L.eyebrow) + '</p>' +
        '<h2 id="mp-title">' + esc(L.title) + '</h2>' +
        '<p class="cm-hint">' + esc(L.hint) + '</p>' +
        '<div class="cm-pills" role="group" aria-labelledby="mp-title">' + L.t.map(function (t) { return '<button type="button" class="cm-pill" data-group="service" data-value="' + t[0] + '" aria-pressed="false">' + esc(t[1]) + '</button>'; }).join('') + '</div>' +
        '<label class="cm-label" for="mp-user">' + esc(L.user) + ' <span>' + esc(L.opt) + '</span></label>' +
        '<input id="mp-user" type="text" maxlength="120" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="' + esc(L.ph) + '">' +
        '<div class="cm-actions"><a class="button button-blue mp-go" href="mailto:' + MAIL + '">' + esc(L.go) + ' <span aria-hidden="true">↗︎</span></a></div>' +
        '<p class="cm-note">' + esc(L.note) + '</p></div>';
      document.body.appendChild(modal);
      input = modal.querySelector('#mp-user');
      go = modal.querySelector('.mp-go');
      modal.addEventListener('click', function (e) {
        var pill = e.target.closest('.cm-pill');
        if (pill) { topic = pill.dataset.value; update(); }
        if (e.target === modal || e.target.closest('.cm-close')) close();
      });
      input.addEventListener('input', update);
      input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go.click(); } });
      go.addEventListener('click', function (e) {
        if (!find(topic)) { e.preventDefault(); e.stopImmediatePropagation(); var f = modal.querySelector('.cm-pill'); if (f) f.focus(); return; }
        update(); setTimeout(close, 60);
      }, true);
      modal.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { e.preventDefault(); close(); }
        if (e.key === 'Tab') {
          var f = Array.prototype.slice.call(modal.querySelectorAll('button, a[href], input'));
          var first = f[0], last = f[f.length - 1];
          if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      });
    };
    var open = function () {
      if (!modal) build();
      topic = infer();
      update();
      lastFocus = document.activeElement;
      modal.hidden = false;
      document.documentElement.classList.add('cm-lock');
      void modal.offsetWidth; modal.classList.add('is-open');
      modal.querySelector('.cm-dialog').focus();
    };
    var close = function () {
      if (!modal || modal.hidden) return;
      modal.classList.remove('is-open');
      document.documentElement.classList.remove('cm-lock');
      setTimeout(function () { modal.hidden = true; }, 220);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    };
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
      if (!a || a.closest('.cm-dialog') || !/^mailto:team@unbanz\.com/i.test(a.getAttribute('href') || '')) return;
      e.preventDefault();
      open();
    });
    window.unbanzMailPick = { open: open, close: close };
  } catch (e) {}
})();
