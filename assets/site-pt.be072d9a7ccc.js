// Unbanz first-party analytics: one row per browser session plus a persistent anonymous visitor id
// (random, localStorage 'ubzv'), so returning visitors group together. No cookies, no IPs, no personal data.
// Also builds the "(via ChatGPT)"-style source tag used in WhatsApp/email prefills.
(() => {
  const AI = [['chatgpt.com', 'ChatGPT'], ['chat.openai.com', 'ChatGPT'], ['openai.com', 'ChatGPT'], ['perplexity.ai', 'Perplexity'], ['gemini.google.com', 'Gemini'], ['bard.google.com', 'Gemini'], ['claude.ai', 'Claude'], ['anthropic.com', 'Claude'], ['copilot.microsoft.com', 'Copilot'], ['copilot.cloud.microsoft', 'Copilot'], ['meta.ai', 'Meta AI'], ['grok.com', 'Grok'], ['x.ai', 'Grok'], ['deepseek.com', 'DeepSeek'], ['you.com', 'You.com'], ['phind.com', 'Phind']];
  const SEARCH = [['google.', 'Google'], ['bing.com', 'Bing'], ['duckduckgo.com', 'DuckDuckGo'], ['yahoo.', 'Yahoo'], ['yandex.', 'Yandex'], ['ecosia.org', 'Ecosia'], ['search.brave.com', 'Brave Search'], ['baidu.com', 'Baidu']];
  const SOCIAL = [['instagram.com', 'Instagram'], ['facebook.com', 'Facebook'], ['fb.com', 'Facebook'], ['fb.me', 'Facebook'], ['messenger.com', 'Facebook'], ['threads.net', 'Threads'], ['reddit.com', 'Reddit'], ['redd.it', 'Reddit'], ['tiktok.com', 'TikTok'], ['youtube.com', 'YouTube'], ['youtu.be', 'YouTube'], ['t.co', 'X'], ['x.com', 'X'], ['twitter.com', 'X'], ['snapchat.com', 'Snapchat'], ['linkedin.com', 'LinkedIn'], ['lnkd.in', 'LinkedIn'], ['pinterest.', 'Pinterest'], ['pin.it', 'Pinterest'], ['quora.com', 'Quora']];
  const MSG = [['whatsapp.com', 'WhatsApp'], ['wa.me', 'WhatsApp'], ['l.wl.co', 'WhatsApp'], ['t.me', 'Telegram'], ['telegram.org', 'Telegram'], ['discord.com', 'Discord'], ['discord.gg', 'Discord'], ['mail.google.com', 'Email'], ['outlook.live.com', 'Email'], ['outlook.office.com', 'Email'], ['mail.yahoo.com', 'Email'], ['mail.proton.me', 'Email']];
  const UTM = { chatgpt: 'ChatGPT', 'chatgpt.com': 'ChatGPT', openai: 'ChatGPT', perplexity: 'Perplexity', 'perplexity.ai': 'Perplexity', gemini: 'Gemini', claude: 'Claude', 'claude.ai': 'Claude', copilot: 'Copilot', 'meta.ai': 'Meta AI', metaai: 'Meta AI', grok: 'Grok', deepseek: 'DeepSeek', you: 'You.com', 'you.com': 'You.com', phind: 'Phind', google: 'Google', bing: 'Bing', ig: 'Instagram', instagram: 'Instagram', fb: 'Facebook', facebook: 'Facebook', meta: 'Facebook', reddit: 'Reddit', tiktok: 'TikTok', youtube: 'YouTube', yt: 'YouTube', x: 'X', twitter: 'X', snapchat: 'Snapchat', snap: 'Snapchat', telegram: 'Telegram', discord: 'Discord', linkedin: 'LinkedIn', pinterest: 'Pinterest', quora: 'Quora', whatsapp: 'WhatsApp', wa: 'WhatsApp', email: 'Email', newsletter: 'Email' };
  const GROUP = {};
  AI.forEach(([, n]) => (GROUP[n] = 'AI')); SEARCH.forEach(([, n]) => (GROUP[n] = 'Search')); SOCIAL.forEach(([, n]) => (GROUP[n] = 'Social')); MSG.forEach(([, n]) => (GROUP[n] = 'Messaging'));
  const match = (host, list) => { for (const [d, n] of list) if (host === d || host.endsWith('.' + d) || (d.endsWith('.') && (host.startsWith(d) || host.includes('.' + d)))) return n; return null; };

  function classify(href, referrer) {
    const p = new URL(href).searchParams;
    const us = (p.get('utm_source') || '').toLowerCase().trim(), um = (p.get('utm_medium') || '').toLowerCase().trim();
    let host = ''; try { host = new URL(referrer).hostname.replace(/^www\./, '').toLowerCase(); } catch {}
    if (host === location.hostname.replace(/^www\./, '')) host = '';
    const paidMedium = /^(cpc|ppc|paid|paid_?social|paidsocial|ads?|display|cpm|sponsored)$/.test(um);
    const metaAd = paidMedium && /^(ig|instagram|fb|facebook|meta)$/.test(us) || p.has('ad_id') || p.has('adset_id') || p.has('h_ad_id') || /^(fb|ig|meta)_?ads?$/.test(us);
    let s = null, g = null, m = 'organic';
    if (p.has('gclid') || p.has('gbraid') || p.has('wbraid') || (paidMedium && us === 'google')) { s = 'Google Ads'; g = 'Ads'; m = 'paid'; }
    else if (p.has('msclkid') || (paidMedium && us === 'bing')) { s = 'Bing Ads'; g = 'Ads'; m = 'paid'; }
    else if (metaAd || (p.has('fbclid') && paidMedium)) { const ig = /^ig|instagram/.test(us) || /instagram/.test(host); s = ig ? 'Instagram Ads' : (/^fb|facebook/.test(us) || /facebook/.test(host)) ? 'Facebook Ads' : 'Meta Ads'; g = 'Ads'; m = 'paid'; }
    else if (p.has('ttclid') || (paidMedium && us === 'tiktok')) { s = 'TikTok Ads'; g = 'Ads'; m = 'paid'; }
    else if (p.has('sccid') || (paidMedium && /snap/.test(us))) { s = 'Snapchat Ads'; g = 'Ads'; m = 'paid'; }
    else if (p.has('li_fat_id') && paidMedium) { s = 'LinkedIn Ads'; g = 'Ads'; m = 'paid'; }
    else if (paidMedium) { s = (UTM[us] || us || 'Other') + ' Ads'; g = 'Ads'; m = 'paid'; }
    else if (um === 'email' || us === 'email' || us === 'newsletter') { s = 'Email'; g = 'Messaging'; }
    else if (host && (s = match(host, AI))) g = 'AI';
    else if (us && UTM[us] && GROUP[UTM[us]] === 'AI') { s = UTM[us]; g = 'AI'; }
    else if (host && (s = match(host, SEARCH))) g = 'Search';
    else if (host && (s = match(host, SOCIAL))) g = 'Social';
    else if (host && (s = match(host, MSG))) g = 'Messaging';
    else if (us && UTM[us]) { s = UTM[us]; g = GROUP[s] || (s === 'Email' ? 'Messaging' : 'Other'); }
    else if (p.has('fbclid')) { s = 'Facebook'; g = 'Social'; }
    else if (us) { s = us.slice(0, 40); g = 'Other'; }
    else if (host) { s = host; g = 'Other'; }
    else { s = 'Direct'; g = 'Direct'; m = 'none'; }
    let q = p.get('utm_term') || '';
    try { if (!q && host) q = new URL(referrer).searchParams.get('q') || new URL(referrer).searchParams.get('p') || ''; } catch {}
    return { s, g, m, d: host || null, us: us || null, um: um || null, uc: p.get('utm_campaign') || null, q: q || null };
  }

  const KEY = 'ubz1';
  let st = null;
  try { st = JSON.parse(sessionStorage.getItem(KEY) || 'null'); } catch {}
  if (!st || !st.id) {
    const c = classify(location.href, document.referrer);
    st = { id: Math.random().toString(36).slice(2, 12) + Date.now().toString(36), ...c };
    try { sessionStorage.setItem(KEY, JSON.stringify(st)); } catch {}
  }
  let vid = null;
  try { vid = localStorage.getItem('ubzv'); if (!/^[a-z0-9]{8,40}$/.test(vid || '')) { vid = Math.random().toString(36).slice(2, 12) + Date.now().toString(36); localStorage.setItem('ubzv', vid); } } catch { vid = null; }
  const camp = (st.uc || '').replace(/[\r\n]/g, ' ').slice(0, 60);
  window.unbanzSrc = st;
  window.unbanzViaTag = st.g === 'Direct' ? '' : `(via ${st.s}${camp ? ' / ' + camp : ''})`;

  if (location.pathname.startsWith('/users')) return;
  const send = (o) => {
    let tz; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone; } catch {}
    let tst; try { tst = localStorage.getItem('ubz_test') === '1' ? 1 : undefined; } catch {}
    const body = JSON.stringify({ id: st.id, v: vid || undefined, tz: tz || undefined, x: tst, ...o });
    try { if (navigator.sendBeacon && navigator.sendBeacon('/api/t/', new Blob([body], { type: 'application/json' }))) return; } catch {}
    fetch('/api/t/', { method: 'POST', body, keepalive: true, headers: { 'Content-Type': 'application/json' } }).catch(() => {});
  };
  const view = () => { send({ e: 'view', p: location.pathname, s: st.s, g: st.g, m: st.m, d: st.d, us: st.us, um: st.um, uc: st.uc, q: st.q }); engReady(); };
  if (document.readyState === 'complete') setTimeout(view, 0); else addEventListener('load', () => setTimeout(view, 0), { once: true });
  addEventListener('pageshow', (e) => { if (e.persisted) view(); });
  // Presence heartbeat for the live 'Online now' counter: every ~20s while the tab is visible.
  const hb = () => { if (document.visibilityState === 'visible') send({ e: 'hb', p: location.pathname }); };
  setInterval(hb, 20000);
  document.addEventListener('visibilitychange', hb);

  // Engagement beats ('eng'): a WhatsApp CTA was on screen, furthest scroll % and active seconds.
  // Sent only after the 'view' beat, so the visit row already exists. The sticky bar and popup do not count as "CTA seen".
  let engOn = false, seenCta = 0, maxSc = 0, sentSc = 0, actSum = 0, actFrom = document.visibilityState === 'visible' ? Date.now() : 0;
  const scrolled = () => { const d = document.documentElement; maxSc = Math.max(maxSc, Math.min(100, Math.round(((window.scrollY || d.scrollTop || 0) + window.innerHeight) / Math.max(d.scrollHeight, 1) * 100))); };
  const engSend = (force) => {
    if (!engOn) return;
    scrolled();
    const now = Date.now();
    if (actFrom) { actSum += (now - actFrom) / 1000; actFrom = now; }
    const t = Math.floor(actSum);
    if (!force && maxSc <= sentSc && t < 1) return;
    send({ e: 'eng', c: seenCta, sc: maxSc, t });
    actSum -= t; sentSc = maxSc;
  };
  function engReady() {
    if (engOn) return;
    engOn = true;
    engSend(true);
    addEventListener('scroll', scrolled, { passive: true });
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') { engSend(); actFrom = 0; } else actFrom = Date.now(); });
    addEventListener('pagehide', () => engSend());
    setInterval(() => { if (document.visibilityState === 'visible') engSend(); }, 60000);
  }
  const watchCtas = () => {
    if (!('IntersectionObserver' in window)) return;
    const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { io.disconnect(); seenCta = 1; engSend(true); } }, { threshold: 0.6 });
    document.querySelectorAll('a[href^="https://wa.me/"]').forEach((a) => { if (!a.closest('.mobile-contact, .cm-dialog')) io.observe(a); });
  };
  if (document.readyState === 'loading') addEventListener('DOMContentLoaded', watchCtas, { once: true }); else watchCtas();

  document.addEventListener('click', (e) => {
    const a = e.target.closest && e.target.closest('a[href^="https://wa.me/"], a[href^="mailto:"]');
    if (!a) return;
    const dlg = a.closest('.cm-dialog');
    const pick = (grp) => dlg && dlg.querySelector(`.cm-pill[data-group="${grp}"][aria-pressed="true"]`)?.dataset.value || a.dataset.platform || null;
    const wa = a.href.startsWith('https://wa.me/');
    const k = wa ? (dlg || e.metaKey || e.ctrlKey || e.shiftKey ? 'whatsapp' : 'popup') : 'email';
    send({ e: 'click', k, pl: pick('platform'), sv: pick('service') || a.dataset.service || null });
  }, true);
})();
(() => {
  'use strict';

  const one = (selector, root = document) => root.querySelector(selector);
  const all = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const mobile = window.matchMedia('(max-width: 650px)');
  const year = one('#year');
  if (year) year.textContent = String(new Date().getFullYear());

  // Native details remains the fallback when JavaScript is unavailable.
  // Enhanced answers use a reversible CSS grid transition, with no measured heights.
  all('.simple-faq details').forEach((details, index) => {
    const summary = one('summary', details);
    if (!summary) return;

    const entry = document.createElement('div');
    entry.className = 'faq-entry';
    const heading = document.createElement('h3');
    heading.className = 'faq-question';
    const trigger = document.createElement('button');
    trigger.className = 'faq-trigger';
    trigger.type = 'button';
    trigger.id = `faq-question-${index}`;
    trigger.innerHTML = summary.innerHTML;
    trigger.setAttribute('aria-controls', `faq-answer-${index}`);

    const answer = document.createElement('div');
    answer.className = 'faq-answer';
    answer.id = `faq-answer-${index}`;
    answer.setAttribute('role', 'region');
    answer.setAttribute('aria-labelledby', trigger.id);
    const inner = document.createElement('div');
    inner.className = 'faq-answer-inner';
    Array.from(details.childNodes).forEach(node => {
      if (node !== summary) inner.appendChild(node);
    });
    answer.appendChild(inner);
    heading.appendChild(trigger);
    entry.append(heading, answer);

    const setOpen = open => {
      trigger.setAttribute('aria-expanded', String(open));
      entry.classList.toggle('is-open', open);
      answer.setAttribute('aria-hidden', String(!open));
      answer.inert = !open;
    };
    setOpen(details.open);
    details.replaceWith(entry);
    trigger.addEventListener('click', () => {
      setOpen(trigger.getAttribute('aria-expanded') !== 'true');
    });
  });

  const menu = one('.menu-button');
  const nav = one('#mobile-nav');
  const setMenu = open => {
    if (!menu || !nav) return;
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    nav.classList.toggle('is-open', open);
    nav.setAttribute('aria-hidden', String(!open));
    nav.inert = !open;
  };
  if (menu && nav) {
    nav.classList.add('nav-ready');
    setMenu(false);
    nav.hidden = false;
    menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
    all('a', nav).forEach(link => link.addEventListener('click', () => setMenu(false)));
    document.addEventListener('click', event => {
      if (!nav.contains(event.target) && !menu.contains(event.target)) setMenu(false);
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        menu.focus();
      }
    });
    mobile.addEventListener('change', () => setMenu(false));
  }

  // Real page links keep native navigation, including back/forward and open-in-new-tab.
  // Only a plain click to an anchor in this document receives a smooth scroll.
  document.addEventListener('click', event => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('a[href]');
    if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
    const url = new URL(link.href, location.href);
    if (!url.hash || url.origin !== location.origin || url.pathname !== location.pathname || url.search !== location.search) return;
    let id;
    try { id = decodeURIComponent(url.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    event.preventDefault();
    if (location.hash !== url.hash) history.pushState(null, '', url.hash);
    target.scrollIntoView({ behavior: motion.matches ? 'auto' : 'smooth', block: 'start' });
    if (link.classList.contains('skip-link')) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    }
  });

  const contact = one('.mobile-contact');
  const hero = one('.hero') || one('.service-hero') || one('main > section');
  // The sticky bar stays out of the way while any in-page WhatsApp CTA is on screen (rendered ones only; some are hidden on mobile).
  // Returns null when the page has no rendered CTA, so the old hero-based rule applies.
  const ctaState = () => {
    const links = all('main a[href^="https://wa.me/"]').filter(link => link.getClientRects().length);
    if (!links.length) return null;
    return links.some(link => { const r = link.getBoundingClientRect(); return r.bottom > 0 && r.top < window.innerHeight - 40; });
  };
  let contactVisible = null;
  let frame = 0;
  const updateContact = () => {
    frame = 0;
    if (!contact) return;
    const cta = ctaState();
    const show = mobile.matches && (cta !== null ? !cta : hero ? hero.getBoundingClientRect().bottom <= 0 : window.scrollY > 220);
    if (show === contactVisible) return;
    contactVisible = show;
    contact.classList.toggle('is-visible', show);
    contact.setAttribute('aria-hidden', String(!show));
    contact.inert = !show;
    all('a', contact).forEach(link => { link.tabIndex = show ? 0 : -1; });
  };
  const scheduleContact = () => {
    if (!frame) frame = requestAnimationFrame(updateContact);
  };
  updateContact();
  window.addEventListener('scroll', scheduleContact, { passive: true });
  window.addEventListener('resize', scheduleContact, { passive: true });
  mobile.addEventListener('change', scheduleContact);
  window.addEventListener('pagehide', () => {
    setMenu(false);
    if (frame) cancelAnimationFrame(frame);
    frame = 0;
  });
  window.addEventListener('pageshow', event => {
    setMenu(false);
    const navigation = performance.getEntriesByType('navigation')[0];
    // A new route starts at the top, without carrying the old long page's offset.
    // Cached back/forward pages retain their natural scroll restoration.
    if (!event.persisted && navigation?.type === 'navigate' && !location.hash) {
      window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
    }
    scheduleContact();
  });
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) scheduleContact();
  });

  // Campaign labels are included only in the visitor's outgoing message draft.
  const params = new URLSearchParams(location.search);
  const campaign = ['utm_source', 'utm_campaign']
    .map(key => params.get(key)?.replace(/[\r\n]/g, ' ').slice(0, 100))
    .filter(Boolean).join(' / ');
  if (window.unbanzViaTag) all('a[href^="https://wa.me/"]').forEach(link => {
    const url = new URL(link.href);
    url.searchParams.set('text', `${url.searchParams.get('text') || 'Hi Unbanz'} ${window.unbanzViaTag}`);
    link.href = url.toString();
  });
})();

// Contact modal: intercepts WhatsApp CTAs; plain wa.me href stays as no-JS fallback.
(() => {
  const WA = 'https://wa.me/19342012490', MAIL = 'team@unbanz.com';
  const services = [['unban', 'Recuperar minha conta'], ['ban', 'Denunciar uma conta'], ['username', 'Nome de usuário'], ['ad', 'Conta de anúncios'], ['other', 'Outra coisa']];
  const platforms = ['Instagram', 'Facebook', 'Snapchat'];
  const p = new URLSearchParams(location.search);
  const campaign = ['utm_source', 'utm_campaign'].map(k => p.get(k)?.replace(/[\r\n]/g, ' ').slice(0, 100)).filter(Boolean).join(' / ');
  let modal, lastFocus, state = { service: 'unban', platform: 'Instagram' };
  const pills = (name, items) => items.map(([v, l], i) => `<button type="button" class="cm-pill" data-group="${name}" data-value="${v}" aria-pressed="${i === 0}">${l}</button>`).join('');
  const sentence = () => {
    const pl = state.platform, s = state.service;
    const base = s === 'unban' ? `Quero recuperar minha conta do ${pl}`
      : s === 'ban' ? `Quero denunciar uma conta do ${pl}`
      : s === 'username' ? `Quero reivindicar um nome de usuário do ${pl}`
      : s === 'ad' ? (pl === 'Instagram' || pl === 'Facebook' ? `Preciso de ajuda com minha conta de anúncios da Meta (${pl})` : `Preciso de ajuda com uma conta de anúncios no ${pl}`)
      : `Preciso de ajuda com minha conta do ${pl}`;
    const reason = modal.querySelector('#cm-reason').value.replace(/\s+/g, ' ').trim();
    return `Olá Unbanz, ${base}.` + (reason ? ` Motivo: ${reason}` : '') + ' (PT)' + (window.unbanzViaTag ? ` ${window.unbanzViaTag}` : '');
  };
  // When a CTA carries no preset, guess service/platform from the page so the popup starts on the right answer.
  const infer = () => {
    const s = location.pathname.toLowerCase().replace(/^\/(fr|nl|es|pt|pt-br)\//, '/');
    const platform = /snapchat/.test(s) ? 'Snapchat' : /facebook|meta-|business-manager/.test(s) ? 'Facebook' : 'Instagram';
    const service = /^\/(ban|fake-account-takedown|harassment-account-removal|impersonation-account-removal|scammer-account-removal|report-)/.test(s) ? 'ban'
      : /username|one-letter|\/og-|-og-/.test(s) ? 'username'
      : /ad-account|ads-account|meta-ad|meta-business|business-manager|meta-agency|meta-special|ads-/.test(s) ? 'ad'
      : /sextortion|scam|fake|harass|impersonat|copyright/.test(s) ? 'other' : 'unban';
    return { service, platform };
  };
  const build = () => {
    modal = document.createElement('div');
    modal.className = 'cm-backdrop';
    modal.hidden = true;
    modal.innerHTML = `<div class="cm-dialog" role="dialog" aria-modal="true" aria-labelledby="cm-title" tabindex="-1">
      <button type="button" class="cm-close" aria-label="Fechar">×</button>
      <p class="eyebrow cm-eyebrow">FALE COM A GENTE</p>
      <h2 id="cm-title">Com o que você precisa de ajuda?</h2>
      <p class="cm-hint">Tudo aqui é opcional. Toque em Continuar para abrir o WhatsApp com a mensagem pronta.</p>
      <fieldset class="cm-group"><legend>Serviço</legend><div class="cm-pills">${pills('service', services)}</div></fieldset>
      <fieldset class="cm-group"><legend>Plataforma</legend><div class="cm-pills">${pills('platform', platforms.map(x => [x, x]))}</div></fieldset>
      <label class="cm-label" for="cm-reason">Motivo resumido <span>(opcional)</span></label>
      <textarea id="cm-reason" maxlength="200" rows="2" placeholder="ex.: desativada depois de entrar num celular novo"></textarea>
      <p class="cm-count" aria-live="polite"><span>0</span>/200</p>
      <div class="cm-actions"><a class="button button-blue cm-wa" href="${WA}" target="_blank" rel="noopener">Continuar no WhatsApp <span aria-hidden="true">↗︎</span></a><a class="button button-light cm-mail" href="mailto:${MAIL}">Prefiro e-mail</a></div>
      <p class="cm-note">Nunca envie senhas nem códigos de acesso.</p></div>`;
    document.body.appendChild(modal);
    modal.addEventListener('click', e => {
      const pill = e.target.closest('.cm-pill');
      if (pill) {
        state[pill.dataset.group] = pill.dataset.value;
        modal.querySelectorAll(`.cm-pill[data-group="${pill.dataset.group}"]`).forEach(b => b.setAttribute('aria-pressed', b === pill));
        update();
      }
      if (e.target === modal || e.target.closest('.cm-close')) close();
    });
    const ta = modal.querySelector('#cm-reason');
    ta.addEventListener('input', () => { modal.querySelector('.cm-count span').textContent = ta.value.length; update(); });
    modal.querySelector('.cm-wa').addEventListener('click', () => { update(); setTimeout(close, 50); });
    modal.querySelector('.cm-mail').addEventListener('click', update);
    modal.addEventListener('keydown', e => {
      if (e.key === 'Escape') { e.preventDefault(); close(); }
      if (e.key === 'Tab') {
        const f = [...modal.querySelectorAll('button, a[href], textarea')];
        const first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  };
  const update = () => {
    const text = sentence();
    modal.querySelector('.cm-wa').href = `${WA}?text=${encodeURIComponent(text)}`;
    modal.querySelector('.cm-mail').href = `mailto:${MAIL}?subject=${encodeURIComponent('Ajuda com minha conta')}&body=${encodeURIComponent(text)}`;
  };
  const open = (preset = {}) => {
    if (!modal) build();
    const guess = infer(), svc = preset.service || guess.service, plt = preset.platform || guess.platform;
    if (services.some(([v]) => v === svc)) state.service = svc;
    if (platforms.includes(plt)) state.platform = plt;
    modal.querySelectorAll('.cm-pill').forEach(b => b.setAttribute('aria-pressed', String(state[b.dataset.group] === b.dataset.value)));
    lastFocus = document.activeElement;
    update();
    modal.hidden = false;
    document.documentElement.classList.add('cm-lock');
    void modal.offsetWidth; modal.classList.add('is-open');
    modal.querySelector('.cm-dialog').focus();
  };
  const close = () => {
    if (!modal || modal.hidden) return;
    modal.classList.remove('is-open');
    document.documentElement.classList.remove('cm-lock');
    setTimeout(() => { modal.hidden = true; }, 220);
    lastFocus?.focus?.();
  };
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="https://wa.me/"]');
    if (!a || a.closest('.cm-dialog') || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    open({ service: a.dataset.service, platform: a.dataset.platform });
  });
  window.unbanzContact = { open, close };
})();

// CTA helpers: trust line in the sticky bar, and one inline CTA after the first section of guides.
(() => {
  const lang = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);
  const T = {
    en: { sub: 'Nothing is charged for asking', subUser: '100% refund if a username claim fails', title: 'Want us to handle this for you?', btn: 'Message us on WhatsApp', note: 'Nothing is charged for asking. We’re an independent service, not affiliated with Meta, and we work through Meta’s official process.' },
    fr: { sub: 'Poser la question ne coûte rien', subUser: 'Remboursé à 100 % si le pseudo échoue', title: 'Vous voulez qu’on s’en occupe pour vous ?', btn: 'Écrivez-nous sur WhatsApp', note: 'Poser la question ne coûte rien. Nous sommes un service indépendant, non affilié à Meta, et nous passons par le processus officiel de Meta.' },
    nl: { sub: 'Vragen kost niets', subUser: '100% terug als je claim mislukt', title: 'Wil je dat wij dit voor je regelen?', btn: 'Stuur ons een bericht op WhatsApp', note: 'Vragen kost niets. We zijn een onafhankelijke dienst, niet verbonden aan Meta, en werken via het officiële proces van Meta.' },
    es: { sub: 'Preguntar no cuesta nada', subUser: 'Reembolso del 100 % si el reclamo falla', title: '¿Quieres que nos encarguemos por ti?', btn: 'Escríbenos por WhatsApp', note: 'Preguntar no cuesta nada. Somos un servicio independiente, sin afiliación con Meta, y trabajamos por el proceso oficial de Meta.' },
    pt: { sub: 'Perguntar não custa nada', subUser: '100% de reembolso se a solicitação falhar', title: 'Quer que a gente cuide disso para você?', btn: 'Mande uma mensagem no WhatsApp', note: 'Perguntar não custa nada. Somos um serviço independente, sem afiliação com a Meta, e trabalhamos pelo processo oficial da Meta.' }
  }[lang] || null;
  if (!T) return;
  const isGuide = document.body.classList.contains('guide-page');
  // Sticky bar: small trust line under the label. The username refund line only on username service pages (the refund policy covers username claims).
  const first = document.querySelector('.mobile-contact a:first-child');
  if (first && !first.querySelector('.mc-sub')) {
    const sub = document.createElement('small');
    sub.className = 'mc-sub';
    sub.textContent = first.dataset.service === 'username' && !isGuide ? T.subUser : T.sub;
    first.appendChild(sub);
  }
  // Inline CTA after the first section of a guide, written in the guide's own language.
  const h2s = isGuide ? Array.from(document.querySelectorAll('.guide-body h2')) : [];
  if (h2s.length >= 3 && !document.querySelector('.inline-cta')) {
    const WA = 'https://wa.me/19342012490';
    const greet = { en: 'Hey Unbanz, I need help with an account', fr: 'Hey Unbanz, j’ai besoin d’aide avec un compte', nl: 'Hey Unbanz, ik heb hulp nodig met een account', es: 'Hola Unbanz, necesito ayuda con una cuenta', pt: 'Olá Unbanz, preciso de ajuda com uma conta' }[lang];
    const box = document.createElement('aside');
    box.className = 'inline-cta';
    box.setAttribute('aria-label', T.title);
    const tt = document.createElement('p'); tt.className = 'inline-cta-title'; tt.textContent = T.title;
    const a = document.createElement('a'); a.className = 'button button-blue'; a.href = `${WA}?text=${encodeURIComponent(greet + (window.unbanzViaTag ? ' ' + window.unbanzViaTag : ''))}`;
    a.append(T.btn + ' ');
    const ar = document.createElement('span'); ar.setAttribute('aria-hidden', 'true'); ar.textContent = '↗︎'; a.appendChild(ar);
    const nt = document.createElement('p'); nt.className = 'inline-cta-note'; nt.textContent = T.note;
    box.append(tt, a, nt);
    h2s[1].parentNode.insertBefore(box, h2s[1]);
  }
})();
