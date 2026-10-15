'use strict';

// Set the business number with country code and digits only when it is supplied.
const SITE_CONFIG = { name: 'Unbanz', whatsappNumber: '19342012490' };
const $ = (selector, scope = document) => scope.querySelector(selector);
const $$ = (selector, scope = document) => [...scope.querySelectorAll(selector)];

// Text stays visible and still. Subtle logo and background motion is CSS-only,
// so scrolling and pointer events cannot repeatedly restart animations.

$('#year').textContent = new Date().getFullYear();

const menuButton = $('.menu-button');
const mobileNav = $('#mobile-nav');
function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Open menu');
  mobileNav.hidden = true;
}
menuButton.addEventListener('click', () => {
  const opening = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(opening));
  menuButton.setAttribute('aria-label', opening ? 'Close menu' : 'Open menu');
  mobileNav.hidden = !opening;
});
$$('a', mobileNav).forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });

// Each service opens independently, keeping the clicked heading in place.
const offerings = $$('[data-offering]');
offerings.forEach(offering => {
  $('.offering-toggle', offering).addEventListener('click', () => {
    const expanded = !offering.classList.contains('is-open');
    offering.classList.toggle('is-open', expanded);
    $('.offering-toggle', offering).setAttribute('aria-expanded', String(expanded));
    const panel = $('.offering-panel', offering);
    panel.setAttribute('aria-hidden', String(!expanded));
    panel.inert = !expanded;
  });
});

let lastFocusedElement = null;
const infoDialog = $('#info-dialog');
function openDialog(dialog) {
  lastFocusedElement = document.activeElement;
  dialog.showModal(); document.body.classList.add('modal-open');
}
$$('[data-open-request]').forEach(button => {
  button.addEventListener('click', () => {
    const service = button.dataset.service;
    window.location.assign('/apply/' + (service ? '?service=' + encodeURIComponent(service) : ''));
  });
});
$('.info-close').addEventListener('click', () => infoDialog.close());
infoDialog.addEventListener('click', event => {
  if (event.target !== infoDialog) return;
  const b = infoDialog.getBoundingClientRect();
  if (event.clientX < b.left || event.clientX > b.right || event.clientY < b.top || event.clientY > b.bottom) infoDialog.close();
});
infoDialog.addEventListener('close', () => {
  document.body.classList.remove('modal-open');
  if (lastFocusedElement?.isConnected) lastFocusedElement.focus();
});

const information = {
  privacy: {
    title: 'Your details, respected.',
    paragraphs: [
      'The application form collects your selected service, account link, reply email and optional note. When direct sending is available, pressing Send application transmits these details to our email provider for delivery to team@unbanz.com. We do not store applications in a website customer database.',
      'The contact email link opens your email app. The application form submits on this website when the backend is connected. Use WhatsApp prepares a WhatsApp draft. These providers handle your information under their own privacy terms. Direct email applications use Resend for delivery and may be retained in provider delivery logs and our inbox.',
      'Only include information needed to explain the issue. Do not include passwords, login codes, recovery codes, identity documents or payment details.',
      'This page does not use advertising trackers or analytics cookies.'
    ]
  },
  terms: {
    title: 'The fine print.',
    paragraphs: [
      'Unbanz is an independent account support service. All platform names and logos belong to their respective owners.',
      'Services are subject to case review. We work with account owners and authorised representatives, and only support reports concerning genuine violations. Account outcomes depend on the case and the platform’s decision.',
      'The estimated turnaround is 3–14 days after a case is accepted and the required information is received. Actual timing depends on the issue and the platform. Final decisions are made by the platform.',
      'Pricing, scope, payment terms and any applicable refund terms must be agreed separately before work starts. Creating or sharing an enquiry does not constitute acceptance of a case.'
    ]
  }
};
$$('[data-open-info]').forEach(button => {
  button.addEventListener('click', () => {
    const info = information[button.dataset.openInfo];
    $('#info-title').textContent = info.title;
    const content = $('#info-content');
    content.replaceChildren(...info.paragraphs.map(text => {
      const paragraph = document.createElement('p');
      paragraph.textContent = text;
      return paragraph;
    }));
    openDialog(infoDialog);
  });
});

// Accessible FAQ panels; each opens without collapsing content above it.
$$('.faq-toggle').forEach(button => {
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    const panel = document.getElementById(button.getAttribute('aria-controls'));
    panel.setAttribute('aria-hidden', String(!open));
    panel.inert = !open;
    button.closest('.faq-item').classList.toggle('is-open', open);
  });
});
window.matchMedia('(min-width: 651px)').addEventListener('change', event => {
  if (event.matches) closeMenu();
});

// Reveal once, only when motion is welcome; no repeating scroll or pointer animation.
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('in-view'); observer.unobserve(entry.target); } });
  }, {threshold: 0.08});
  document.querySelectorAll('[data-reveal], .approach, .faq-intro, .service-copy, .service-proof').forEach(element => {
    if (element.getBoundingClientRect().top > innerHeight) { element.classList.add('will-reveal'); observer.observe(element); }
  });
}

