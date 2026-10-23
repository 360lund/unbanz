#!/usr/bin/env python3
"""One-shot: homepage-style hero + tidy layout for main service pages. Run once from repo root (idempotent: skips pages already converted)."""
import re, json, hashlib, os, html, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
css = open('scripts/svc-hero.css').read()
h = hashlib.md5(css.encode()).hexdigest()[:10]
CSSF = f'assets/svc-hero.{h}.css'
if not os.path.exists(CSSF): open(CSSF, 'w').write(css)
CSSLINK = f'<link rel="stylesheet" href="/{CSSF}">'
TS = re.search(r'testimonials\.(\w+)\.css', open('reviews/index.html').read()).group(1)
TVID = json.load(open('scripts/testimonials.json'))[0]
e = lambda s: html.escape(s, quote=True)
ORN_FB = '<div class="ornament ornament-facebook"><img src="/assets/hero-facebook.c3ca6b00d0.webp" width="360" height="360" alt="" fetchpriority="high" decoding="async"></div>'
ORN_IG = '<div class="ornament ornament-instagram"><img src="/assets/hero-instagram.fef5a3021b.webp" width="360" height="360" alt="" decoding="async"></div>'
UNB = "We appeal through Meta’s official process and keep you posted until you’re back in."
REP = "Scam, impersonator or harassment account? We help you report it the right way."
PAGES = {
 'username': ("Get the Instagram", "username you want.", "Inactive or taken handle? Send us the name and we’ll go get it for you.", 'ig'),
 'unban': ("Banned on Instagram", "or Facebook?", "Disabled, suspended or banned? " + UNB, 'both'),
 'ban': ("Instagram &amp; Facebook", "account removals.", REP, 'both'),
 'services': ("Unbans, removals", "&amp; usernames.", "Instagram, Facebook and Snapchat. Tell us what happened and we’ll take it from there.", 'both'),
 'instagram-unban-service': ("Instagram", "unban service.", "Banned, disabled or suspended? " + UNB, 'ig'),
 'facebook-unban-service': ("Facebook", "unban service.", "Profile, Page or Marketplace disabled? " + UNB, 'fb'),
 'snapchat-unban-service': ("Snapchat", "unban service.", "Locked or banned on Snapchat? We appeal through Snapchat’s official support process.", 'both'),
 'instagram-account-ban-service': ("Instagram account", "removal help.", REP, 'ig'),
 'facebook-account-ban-service': ("Facebook account", "removal help.", REP, 'fb'),
 'snapchat-account-ban-service': ("Snapchat account", "removal help.", REP, 'both'),
 'impersonation-account-removal': ("Someone pretending", "to be you?", "We help you report impersonator accounts on Instagram, Facebook and Snapchat the right way.", 'both'),
 'fake-account-takedown': ("Fake account", "takedown.", "Fake, scam or impersonator account? We help you report it the right way.", 'both'),
 'ad-account-recovery': ("Meta ad account", "restricted?", "We appeal restricted and disabled ad accounts through Meta’s official process.", 'fb'),
 'instagram-account-recovery': ("Get your Instagram", "account back.", "Hacked, disabled or locked out? We work through Instagram’s official recovery and appeal routes.", 'ig'),
 'facebook-account-recovery': ("Get your Facebook", "account back.", "Hacked, disabled or locked out? We work through Facebook’s official recovery and appeal routes.", 'fb'),
}
MORE = {'username': 'More about username claims'}
def sections(m):
    out, i = [], 0
    for x in re.finditer(r'<section\b[^>]*>.*?</section>', m, re.S): out.append(x.group())
    return out
changed = []
for slug, (l1, l2, sub, orn) in PAGES.items():
    f = f'{slug}/index.html'; s = open(f).read()
    if 'hero-svc' in s: continue
    hdr = re.search(r'<header class="service-header container">.*?</header>', s, re.S).group()
    mnav = re.search(r'<nav class="mobile-nav".*?</nav>', s, re.S).group()
    s = s.replace(hdr, '', 1).replace(mnav, '', 1)
    a, b = s.index('<main id="content">') + len('<main id="content">'), s.index('</main>')
    secs = sections(s[a:b])
    old = secs[0]; assert 'service-hero' in old
    wa = re.search(r'<a class="button button-light" (href="https://wa\.me/[^"]*"(?: data-service="[^"]*")?)', old).group(1)
    mail = re.search(r'<a class="hero-email" (href="mailto:[^"]*")', old).group(1)
    orns = (ORN_FB if orn in ('fb', 'both') else '') + (ORN_IG if orn in ('ig', 'both') else '')
    if orn == 'fb': orns += ORN_IG.replace('ornament-instagram"', 'ornament-instagram" style="opacity:.0"') if False else ''
    hero = ('<section class="hero hero-svc" aria-labelledby="hero-title"><div class="hero-sky" aria-hidden="true"></div>'
            + hdr.replace('class="service-header container"', 'class="site-header container"') + mnav
            + f'<div class="hero-ornaments" aria-hidden="true">{orns}</div><div class="hero-content container">'
            f'<h1 id="hero-title"><span class="title-line"><span>{l1}</span></span><span class="title-line"><span>{l2}</span></span></h1>'
            f'<p class="hero-description">{sub}</p><div class="hero-cta"><a class="button button-light hero-button" {wa}>Get a quote on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="hero-email" {mail}>Prefer email? ↗︎</a></div></div></section>')
    rest = secs[1:]
    steps_sec = next((x for x in rest if 'service-editorial' in x and re.search(r'<h2>1\.', x)), None)
    hub = [x for x in rest if 'hub-services' in x]
    faq = [x for x in rest if 'faq-section' in x]
    proof = [x for x in rest if 'service-proof' in x]
    links = [x for x in rest if 'guide-links' in x]
    more = [x for x in rest if x not in hub + faq + proof + links and x is not steps_sec]
    top = []
    if steps_sec:
        items = re.findall(r'<h2>\d\.\s*(.*?)</h2><p>(.*?)</p>', steps_sec, re.S)
        top.append('<section class="svc-steps container" aria-labelledby="steps-h"><h2 id="steps-h">How it works</h2><ol>'
                   + ''.join(f'<li><b>{i+1}</b><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(items)) + '</ol></section>')
    if slug == 'username':
        v = TVID
        top.append(f'<section class="vt svc-video container" aria-labelledby="vid-h"><h2 id="vid-h">From a client</h2><ul class="vt-track"><li class="vt-card" data-src="{e(v["src"])}"><div class="vt-media"><img src="/assets/testimonials/{v["id"]}.jpg" width="540" height="960" alt="{e(v["name"])}" loading="lazy" decoding="async"><button class="vt-play" type="button" aria-label="Play video: {e(v["name"])}"><b>{e(v["label"])}</b><i><svg width="16" height="18" viewBox="0 0 18 20" aria-hidden="true"><path d="M17 10 1 19V1z" fill="currentColor"/></svg></i></button></div><details class="vt-tr"><summary>Transcript</summary><div class="vt-body"><p>{e(v["transcript"])}</p></div></details></li></ul></section>')
    morehtml = ''
    if more:
        morehtml = (f'<details class="svc-more container"><summary>{MORE.get(slug, "More details")}</summary>'
                    + ''.join(x.replace(' container"', '"', 1) for x in more) + '</details>')
    def trim(x):
        d = re.findall(r'<details>.*?</details>', x, re.S)
        if len(d) <= 6: return x
        x = x.replace(''.join(d), ''.join(d[:6]) + '<details class="svc-faq-more"><summary>More questions +</summary>' + ''.join(d[6:]) + '</details>', 1)
        assert 'svc-faq-more' in x
        return x
    faq = [trim(x) for x in faq]
    main = hero + ''.join(top + hub + faq + proof) + morehtml + ''.join(links)
    s = s[:a] + main + s[b:]
    s = s.replace('<body class="service-page">', '<body class="service-page has-hero-svc">', 1)
    head_add = CSSLINK
    if slug == 'username':
        head_add += f'<link rel="preconnect" href="https://cdn.dbimg.app"><link rel="stylesheet" href="/assets/testimonials.{TS}.css"><script src="/assets/testimonials.{TS}.js" defer></script>'
        vo = {"@context": "https://schema.org", "@type": "VideoObject", "@id": "https://unbanz.com/username/#video-" + TVID['id'], "name": TVID["name"], "description": TVID["description"],
              "thumbnailUrl": [f"https://unbanz.com/assets/testimonials/{TVID['id']}.jpg"], "uploadDate": TVID["uploadDate"], "duration": TVID["duration"], "contentUrl": TVID["src"],
              "transcript": TVID["transcript"], "inLanguage": "en", "publisher": {"@id": "https://unbanz.com/#organization"}}
        head_add += '<script type="application/ld+json">' + json.dumps(vo, ensure_ascii=False, separators=(",", ":")) + '</script>'
    s = s.replace('</head>', head_add + '</head>', 1)
    open(f, 'w').write(s); changed.append(slug)
print('changed', changed)
