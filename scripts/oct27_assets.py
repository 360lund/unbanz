#!/usr/bin/env python3
"""Create NEW hashed site JS/CSS (old files are kept: cached pages and session replays still request them).
JS:  (1) prepend the mobile WhatsApp-direct injector, (2) utm_source=outreach -> source 'Outreach' (group Other),
     (3) popup interceptor skips data-direct links, (4) tracker logs data-direct clicks as k:'whatsapp'.
CSS: .wa-direct styles (mobile only, <=650px, the same breakpoint as the sticky bar).
The sticky .mobile-contact bar code is not touched. Prints the new file names."""
import hashlib, os, sys
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')
OLD_JS, OLD_CSSES = 'site.d4eb65f0bc51.js', ['site.0c72990a1a48.css', 'site.5861d0cd0caa.css']

INJECT = r"""// Mobile primary CTA: a direct WhatsApp link with a prefilled message about the page. The popup link stays as the secondary option.
(() => {
  try {
    if (!/^en\b/i.test(document.documentElement.lang || '')) return;
    if (/^\/(users|contact|apply|terms|privacy|reviews)(\/|$)/.test(location.pathname)) return;
    const wrap = document.querySelector('.service-hero > .container');
    if (!wrap) return;
    const orig = wrap.querySelector('.hero-cta a[href^="https://wa.me/"], .guide-cta-top a[href^="https://wa.me/"]');
    if (!orig || wrap.querySelector('.wa-direct')) return;
    const u = new URL(orig.href);
    let text = (u.searchParams.get('text') || '').trim();
    if (!text || /^Hey Unbanz, I need help with an account\.?$/i.test(text)) {
      const h = wrap.querySelector('h1');
      let t = '';
      if (h) { const c = h.cloneNode(true); c.querySelectorAll('br').forEach(b => b.replaceWith(' ')); t = c.textContent.replace(/\s+/g, ' ').trim().replace(/[.!?]+$/, ''); }
      if (t.length > 90) t = t.slice(0, 90).replace(/\s+\S*$/, '');
      text = t ? 'Hey Unbanz, I’m on your page “' + t + '” and need help with my account. Can you help?' : 'Hey Unbanz, I need help with my account. Can you help?';
    }
    const direct = document.createElement('a');
    direct.className = orig.className.replace(/\bservice-chat\b/g, '').trim() + ' wa-direct';
    if (!/\bbutton\b/.test(direct.className) && !orig.closest('.guide-cta-top')) direct.className += ' button button-light';
    direct.href = 'https://wa.me/19342012490?text=' + encodeURIComponent(text);
    direct.target = '_blank'; direct.rel = 'noopener';
    direct.setAttribute('data-direct', '');
    ['service', 'platform'].forEach(k => { if (orig.dataset[k]) direct.dataset[k] = orig.dataset[k]; });
    direct.innerHTML = 'Message us on WhatsApp <span aria-hidden="true">↗︎</span>';
    const note = document.createElement('span');
    note.className = 'wa-direct-note';
    note.textContent = 'Your message is already written. Just press send.';
    const alt = document.createElement('span'); alt.className = 'wa-lbl-m'; alt.innerHTML = 'Choose your topic first <span aria-hidden="true">↗︎</span>';
    const old = document.createElement('span'); old.className = 'wa-lbl-d';
    while (orig.firstChild) old.appendChild(orig.firstChild);
    orig.append(old, alt);
    orig.classList.add('wa-alt');
    orig.parentNode.insertBefore(direct, orig);
    orig.parentNode.insertBefore(note, orig);
    wrap.classList.add('wa-on');
  } catch (e) {}
})();
"""

CSS = """
/* Mobile primary WhatsApp CTA (prefilled, direct) with the popup link as secondary. Same breakpoint as the sticky bar. */
.wa-direct, .wa-direct-note { display: none; }
.guide-cta-top a.wa-direct { display: none; }
.wa-lbl-d { display: contents; }
.wa-lbl-m { display: none; }
@media (max-width: 650px) {
  .wa-on .wa-direct { display: inline-flex; width: 100%; }
  .wa-on .guide-cta-top a.wa-direct { display: inline-flex; justify-content: center; }
  .wa-on .wa-direct-note { display: block; margin: 8px 0 0; font-size: 13px; line-height: 1.45; color: #e0f0fc; }
  .wa-on .hero-cta { width: 100%; }
  .wa-on .hero-cta .button { width: 100%; }
  .wa-on .wa-alt { margin-top: 12px; background: transparent !important; color: white !important; box-shadow: inset 0 0 0 1.5px #ffffffb8; transform: none !important; }
  .wa-on .guide-cta-top .wa-alt { display: inline-flex; width: 100%; }
  .wa-on .wa-alt .wa-lbl-d { display: none; }
  .wa-on .wa-alt .wa-lbl-m { display: contents; }
}
"""

def edit(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)

js = open(os.path.join(A, OLD_JS), encoding='utf-8').read()
# (2) outreach source, first in the chain so it wins over medium=email / referrers
js = edit(js, "    if (p.has('gclid') || p.has('gbraid')", "    if (us === 'outreach') { s = 'Outreach'; g = 'Other'; m = 'outreach'; }\n    else if (p.has('gclid') || p.has('gbraid')")
# (3) popup interceptor ignores direct links
js = edit(js, "if (!a || a.closest('.cm-dialog') || e.metaKey || e.ctrlKey || e.shiftKey) return;\n    e.preventDefault();\n    open(",
          "if (!a || a.closest('.cm-dialog') || a.hasAttribute('data-direct') || e.metaKey || e.ctrlKey || e.shiftKey) return;\n    e.preventDefault();\n    open(")
# (4) tracker: direct links are real WhatsApp clicks
js = edit(js, "const k = wa ? (dlg || e.metaKey", "const k = wa ? (dlg || a.hasAttribute('data-direct') || e.metaKey")
js = INJECT + js

def put(prefix, ext, body):
    h = hashlib.sha256(body.encode()).hexdigest()[:12]
    n = f'{prefix}.{h}.{ext}'
    open(os.path.join(A, n), 'w', encoding='utf-8').write(body)
    return n
newjs = put('site', 'js', js)
print('JS', OLD_JS, '->', newjs)
for oc in OLD_CSSES:
    css = open(os.path.join(A, oc), encoding='utf-8').read().rstrip('\n') + '\n' + CSS
    print('CSS', oc, '->', put('site', 'css', css))
