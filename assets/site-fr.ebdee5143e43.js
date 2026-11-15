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
    menu.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
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
  let contactVisible = null;
  let frame = 0;
  const updateContact = () => {
    frame = 0;
    if (!contact) return;
    const show = mobile.matches && (hero ? hero.getBoundingClientRect().bottom <= 0 : window.scrollY > 220);
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

// WhatsApp contact modal removed (Nov 15 2026): contact is email only.
window.unbanzContact = { open() {}, close() {} };
