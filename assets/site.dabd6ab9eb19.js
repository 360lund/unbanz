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
    menu.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
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
  if (campaign) all('a[href^="https://wa.me/"]').forEach(link => {
    const url = new URL(link.href);
    url.searchParams.set('text', `${url.searchParams.get('text') || 'Hi Unbanz'}\nCampaign: ${campaign}`);
    link.href = url.toString();
  });
})();

// Contact modal: intercepts WhatsApp CTAs; plain wa.me href stays as no-JS fallback.
(() => {
  const WA = 'https://wa.me/19342012490', MAIL = 'team@unbanz.com';
  const services = [['unban', 'Unban my account'], ['ban', 'Ban an account'], ['username', 'Username claim'], ['ad', 'Ad account'], ['other', 'Other']];
  const platforms = ['Instagram', 'Facebook', 'Snapchat'];
  const p = new URLSearchParams(location.search);
  const campaign = ['utm_source', 'utm_campaign'].map(k => p.get(k)?.replace(/[\r\n]/g, ' ').slice(0, 100)).filter(Boolean).join(' / ');
  let modal, lastFocus, state = { service: 'unban', platform: 'Instagram' };
  const pills = (name, items) => items.map(([v, l], i) => `<button type="button" class="cm-pill" data-group="${name}" data-value="${v}" aria-pressed="${i === 0}">${l}</button>`).join('');
  const sentence = () => {
    const pl = state.platform, s = state.service;
    const base = s === 'unban' ? `I want to unban my ${pl} account`
      : s === 'ban' ? `I want to get a ${pl} account taken down`
      : s === 'username' ? `I want to claim a ${pl} username`
      : s === 'ad' ? (pl === 'Instagram' || pl === 'Facebook' ? `I need help with my Meta ad account (${pl})` : `I need help with an ad account on ${pl}`)
      : `I need help with my ${pl} account`;
    const reason = modal.querySelector('#cm-reason').value.replace(/\s+/g, ' ').trim();
    return `Hey Unbanz, ${base}.` + (reason ? ` Reason: ${reason}` : '') + (campaign ? `\nCampaign: ${campaign}` : '');
  };
  const build = () => {
    modal = document.createElement('div');
    modal.className = 'cm-backdrop';
    modal.hidden = true;
    modal.innerHTML = `<div class="cm-dialog" role="dialog" aria-modal="true" aria-labelledby="cm-title" tabindex="-1">
      <button type="button" class="cm-close" aria-label="Close">×</button>
      <p class="eyebrow cm-eyebrow">LET'S GET IT DONE</p>
      <h2 id="cm-title">What do you need?</h2>
      <fieldset class="cm-group"><legend>Service</legend><div class="cm-pills">${pills('service', services)}</div></fieldset>
      <fieldset class="cm-group"><legend>Platform</legend><div class="cm-pills">${pills('platform', platforms.map(x => [x, x]))}</div></fieldset>
      <label class="cm-label" for="cm-reason">Short reason <span>(optional)</span></label>
      <textarea id="cm-reason" maxlength="200" rows="3" placeholder="e.g. disabled after a login from a new phone"></textarea>
      <p class="cm-count" aria-live="polite"><span>0</span>/200</p>
      <div class="cm-actions"><a class="button button-blue cm-wa" href="${WA}" target="_blank" rel="noopener">Continue on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="button button-light cm-mail" href="mailto:${MAIL}">Email us instead</a></div>
      <p class="cm-note">Never send passwords or login codes.</p></div>`;
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
    modal.querySelector('.cm-mail').href = `mailto:${MAIL}?subject=${encodeURIComponent('Account help')}&body=${encodeURIComponent(text)}`;
  };
  const open = () => {
    if (!modal) build();
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
    open();
  });
  window.unbanzContact = { open, close };
})();
