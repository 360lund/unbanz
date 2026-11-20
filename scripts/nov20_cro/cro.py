"""Nov 20 2026 CRO pass (homepage + /contact/). Idempotent: markers cro-*."""
import re, pathlib
R = pathlib.Path(__file__).resolve().parents[2]
MAIL = 'mailto:team@unbanz.com?subject=Account%20help&amp;body=Hi%20Unbanz%2C%0A%0APlatform%3A%20%0AUsername%20or%20profile%20link%3A%20%0AWhat%20happened%3A%20%0ACountry%3A%20%0A%0AThanks'
CK = '<svg aria-hidden="true" viewBox="0 0 16 16"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
TRUST = ['No password needed', 'Usually 7–14 days', 'Full refund if not reinstated in 14 days', 'Signed agreement before you pay']
def chips(cls): return f'<ul class="{cls}" aria-label="What you get">' + ''.join(f'<li>{CK}{t}</li>' for t in TRUST) + '</ul>'
CSS = '''<style id="cro-css">
.cro-trust{list-style:none;margin:22px auto 0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:8px 10px;max-width:900px}
.cro-trust li{display:inline-flex;align-items:center;gap:6px;font-size:14px;line-height:1.2;padding:8px 13px;border-radius:999px;background:rgba(255,255,255,.16);color:#fff;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.28)}
.cro-trust svg,.cro-trust-l svg{width:14px;height:14px;flex:none}
.hero-cta .hero-button{font-weight:600}
.cro-how{padding:56px 0 8px}
.cro-how .eyebrow{margin:0 0 10px}
.cro-how h2{margin:0 0 26px;font-size:clamp(28px,3.4vw,44px);font-weight:400;letter-spacing:-.04em;line-height:1.08;color:#10243a}
.cro-steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;counter-reset:s}
.cro-steps li{background:#fff;border-radius:22px;padding:22px 22px 24px;box-shadow:0 18px 40px -32px rgba(16,52,76,.45);counter-increment:s}
.cro-steps li:before{content:"0" counter(s);display:block;font-size:13px;letter-spacing:.1em;color:#2d6f99;margin-bottom:10px;font-weight:600}
.cro-steps h3{margin:0 0 6px;font-size:19px;font-weight:600;letter-spacing:-.02em;color:#10243a}
.cro-steps p{margin:0;font-size:15px;line-height:1.55;color:#4b6378}
.cro-row{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;margin-top:22px}
.cro-row .button{min-height:48px}
.cro-trust-l{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px 16px;font-size:14px;color:#2b4a63}
.cro-trust-l li{display:inline-flex;align-items:center;gap:6px}
.cro-trust-l svg{color:#1f9d55}
.cro-fine{margin:12px 0 0;font-size:13px;color:#6a8195}
.contact-trust{margin:14px 0 4px}
@media (max-width:760px){.cro-trust{gap:6px;margin-top:16px}.cro-trust li{font-size:12.5px;padding:7px 11px}.cro-steps{grid-template-columns:1fr;gap:10px}.cro-steps li{padding:18px 18px 20px}.cro-how{padding:40px 0 0}.cro-row .button{width:100%;justify-content:center}}
</style>'''
HOW = f'''<section class="cro-how container" id="how" aria-labelledby="cro-how-t"><p class="eyebrow">HOW IT WORKS</p><h2 id="cro-how-t">Three steps. You stay in control.</h2><ol class="cro-steps"><li><h3>Tell us what happened</h3><p>Pick your issue and send your username plus a screenshot of the notice. Takes about two minutes. Asking is free.</p></li><li><h3>Get an honest answer</h3><p>We tell you straight if it’s doable. If you go ahead, you sign an agreement, then pay by bank transfer. From $1,000.</p></li><li><h3>We handle the appeal</h3><p>Through Meta’s official support and appeal process, usually 7–14 days. Not reinstated within 14 days? Full refund, paid the same business day.</p></li></ol><div class="cro-row"><a class="button button-blue cro-cta" href="{MAIL}">Get a free case review <span aria-hidden="true">↗︎</span></a>{chips("cro-trust-l")}</div><p class="cro-fine">Unbanz is independent and not affiliated with Meta, Instagram or Facebook. The platform makes the final decision.</p></section>'''
FAQ = [
 ("Is Unbanz part of Meta?", "No. Unbanz is an independent service, not affiliated with Meta, Instagram or Facebook. We work through Meta’s official support and appeal process, and Meta makes the final decision."),
 ("How do I pay?", "By bank transfer only, after you’ve signed our service agreement. The account details are on the agreement. We don’t take card payments and we never ask for your password."),
 ("What if my account isn’t reinstated?", "If the account isn’t reinstated within 14 calendar days of the day we start, you get a full refund, paid the same business day."),
 ("Can we talk on a call?", "Cases are handled in writing over email (and WhatsApp in some countries), with a signed agreement, so every step and promise is on record. There is no phone line."),
]
def esc(t): return t.replace('&', '&amp;')
def home():
    p = R / 'index.html'; s = p.read_text()
    if 'id="cro-css"' not in s: s = s.replace('</head>', CSS + '\n</head>', 1)
    s = s.replace('<p class="hero-description">Banned or disabled Instagram or Facebook account? We help you get it back through Meta’s official support and appeal process.</p>',
                  '<p class="hero-description">Banned, disabled or hacked Instagram or Facebook account? An independent team helps you get it back through Meta’s official support and appeal process.</p>')
    s = re.sub(r'(<div class="hero-cta"><a class="button button-light hero-button" href="[^"]*">)Email us( <span aria-hidden="true">↗︎</span></a></div>)', r'\1Get a free case review\2', s, 1)
    if 'class="cro-trust"' not in s: s = re.sub(r'(<div class="hero-cta"><a class="button button-light hero-button"[^>]*>.*?</a></div>)', lambda m: m.group(1) + chips('cro-trust'), s, 1, flags=re.S)
    if 'id="how"' not in s: s = s.replace('<section class="recovery-intro container"', HOW + '<section class="recovery-intro container"', 1)
    s = s.replace('<p class="days">3–14<span>days</span></p><p class="timing-note">From the day we start.', '<p class="days">7–14<span>days</span></p><p class="timing-note">Usually, from the day we start.')
    if 'Is Unbanz part of Meta?' not in s:
        html = ''.join(f'<details><summary>{esc(q)}<span aria-hidden="true">+</span></summary><p>{esc(a)}</p></details>' for q, a in FAQ)
        s = s.replace('<div class="simple-faq">', '<div class="simple-faq">' + html, 1)
        ld = ''.join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}},' % (q, a) for q, a in FAQ)
        k = '"@id":"https://unbanz.com/#faq","url":"https://unbanz.com/","mainEntity":['
        assert k in s; s = s.replace(k, k + ld, 1)
    p.write_text(s)
def contact():
    p = R / 'contact' / 'index.html'; s = p.read_text()
    if 'id="cro-css"' not in s: s = s.replace('</head>', CSS + '\n</head>', 1)
    if 'cro-trust-l contact-trust"' not in s:
        i = s.find('<h1'); j = s.find('</h1>', i) + 5
        s = s[:j] + chips('cro-trust-l contact-trust') + s[j:]
    p.write_text(s)
home(); contact(); print('ok')
