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
