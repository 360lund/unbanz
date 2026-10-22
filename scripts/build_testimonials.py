#!/usr/bin/env python3
"""Single source for video testimonials. Edit scripts/testimonials.json (+ add poster at
assets/testimonials/<id>.jpg), then run: python3 scripts/build_testimonials.py
Rebuilds the homepage section (first 3) and /reviews/ (all), with VideoObject schema."""
import json, re, hashlib, os, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(R)
V = json.load(open('scripts/testimonials.json'))
css, js = open('scripts/testimonials.css').read(), open('scripts/testimonials.js').read()
h = hashlib.md5((css + js).encode()).hexdigest()[:10]
for ext, src in (('css', css), ('js', js)):
    p = f'assets/testimonials.{h}.{ext}'
    if not os.path.exists(p): open(p, 'w').write(src)
ASSETS = '<link rel="preconnect" href="https://cdn.dbimg.app">' + f'<link rel="stylesheet" href="/assets/testimonials.{h}.css"><script src="/assets/testimonials.{h}.js" defer></script>'
PLAY = '<svg width="16" height="18" viewBox="0 0 18 20" aria-hidden="true"><path d="M17 10 1 19V1z" fill="currentColor"/></svg>'
e = lambda s: html.escape(s, quote=True)
def card(v, open_tr=False):
    p = f"/assets/testimonials/{v['id']}.jpg"
    return (f'<li class="vt-card" data-src="{e(v["src"])}"><div class="vt-media"><img src="{p}" width="540" height="960" alt="{e(v["name"])}" loading="lazy" decoding="async">'
            f'<button class="vt-play" type="button" aria-label="Play video: {e(v["name"])}"><b>{e(v["label"])}</b><i>{PLAY}</i></button></div>'
            + (f'<div class="vt-q"><b>{e(v["label"])}</b><blockquote><p>“{e(v["transcript"])}”</p></blockquote></div></li>' if open_tr else
               f'<details class="vt-tr"><summary>Transcript</summary><div class="vt-body"><p>{e(v["transcript"])}</p></div></details></li>'))
def vo(v, page):
    return {"@type": "VideoObject", "@id": f"{page}#video-{v['id']}", "name": v["name"], "description": v["description"],
            "thumbnailUrl": [f"https://unbanz.com/assets/testimonials/{v['id']}.jpg"], "uploadDate": v["uploadDate"], "duration": v["duration"],
            "contentUrl": v["src"], "transcript": v["transcript"], "inLanguage": "en", "publisher": {"@id": "https://unbanz.com/#organization"}}
LD = lambda g: '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":")) + '</script>'
# homepage
s = open('index.html').read()
sec = ('<section class="vt container" id="testimonials" aria-labelledby="vt-title"><div class="vt-head"><div><p class="eyebrow">CLIENTS</p><h2 id="vt-title">In their words.</h2></div>'
       '</div><ul class="vt-track">' + ''.join(card(v) for v in V[:3]) + '</ul></section>')
s = re.sub(r'<section class="vt container".*?</ul></section>', lambda m: sec, s, count=1, flags=re.S)
s = re.sub(r'(?:<link rel="preconnect" href="https://cdn.dbimg.app">)?<link rel="stylesheet" href="/assets/testimonials\.\w+\.css"><script src="/assets/testimonials\.\w+\.js" defer></script><script type="application/ld\+json">[^<]*VideoObject[^<]*</script>',
           lambda m: ASSETS + LD([vo(v, "https://unbanz.com/") for v in V[:3]]), s, count=1)
open('index.html', 'w').write(s)
# /reviews/ built from the /work/ page shell (same header, menu, footer)
t = open('work/index.html').read()
U = "https://unbanz.com/reviews/"
TITLE = "Unbanz Reviews: Video Reviews from Clients | Unbanz"
DESC = "Unbanz reviews from real clients: short videos about Instagram and Facebook unbans, ad accounts, account removals and username claims, with full transcripts."
t = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', t, count=1)
t = re.sub(r'(<meta (?:name|property)="(?:og:|twitter:)?title" content=")[^"]*', lambda m: m.group(1) + TITLE.replace('&', '&amp;'), t)
t = re.sub(r'(<meta (?:name|property)="(?:og:|twitter:)?description" content=")[^"]*', lambda m: m.group(1) + DESC, t)
t = t.replace('https://unbanz.com/work/"', U + '"')
t = re.sub(r'<script type="application/ld\+json">.*?</script>', '', t, flags=re.S)
org = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', open('work/index.html').read(), re.S).group(1))["@graph"][0]
org = dict(org, subjectOf=[{"@id": U + "#video-" + v["id"]} for v in V] + [{"@id": U + "#webpage"}])
ilist = {"@type": "ItemList", "@id": U + "#videos", "name": "Unbanz client video testimonials", "numberOfItems": len(V),
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@id": U + "#video-" + v["id"]}} for i, v in enumerate(V)]}
graph = [org, {"@type": "WebPage", "@id": U + "#webpage", "url": U, "name": TITLE, "description": DESC, "isPartOf": {"@id": "https://unbanz.com/#website"}, "about": {"@id": "https://unbanz.com/#organization"}, "mainEntity": {"@id": U + "#videos"}, "breadcrumb": {"@id": U + "#breadcrumb"}, "inLanguage": "en"},
         {"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://unbanz.com/"}, {"@type": "ListItem", "position": 2, "name": "Unbanz reviews", "item": U}]}] + [ilist] + [vo(v, U) for v in V]
t = t.replace('</head>', LD(graph) + ASSETS + '</head>', 1)
main = ('<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="/">Home / Reviews</a><h1>Unbanz reviews</h1><p>On-camera videos from Unbanz clients: a client who got an Instagram username from a dead profile in about 5 days, an agency owner who has used Unbanz for 3 months for unbans, account removals and username claims, and an advertiser whose restricted Facebook ad account was restored within a week. Full transcripts sit below each video.</p>'
        '<div class="hero-cta"><a class="button button-light" href="https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20an%20account">Get a quote on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Account%20help">Prefer email? ↗︎</a></div></div></section>'
        '<section class="guide-body container" aria-labelledby="wcs"><h2 id="wcs">What clients say</h2><blockquote><p>“I needed an Instagram username but it was a dead profile. Unbanz really helped me with it. It took like 5 days.”</p><p>Client, Instagram username claim</p></blockquote><blockquote><p>“I’ve been working with Unbanz for the last 3 months now. They’re handling all the bans and unbans, username claims for my clients, taking down accounts.”</p><p>Management agency owner</p></blockquote><blockquote><p>“My Facebook ad account was restricted and I was unable to run ads. ChatGPT recommended me Unbanz and they got it back within a week.”</p><p>Advertiser, restricted Facebook ad account</p></blockquote><h2>Is Unbanz trustworthy?</h2><p>Yes. Unbanz is a real, independent service at unbanz.com. Clients share their experience in the videos below, each with a full transcript. You get a price before any work starts, and your password stays with you.</p></section>'
        '<section class="vt vt-page container" aria-label="Video testimonials"><ul class="vt-track">' + ''.join(card(v, True) for v in V) + '</ul></section></main>')
t = re.sub(r'<main id="content">.*?</main>', lambda m: main, t, count=1, flags=re.S)
t = re.sub(r'<div class="lightbox" id="lightbox".*?</div></div>', '', t, count=1, flags=re.S)
t = t.replace('<a href="/reviews/">Reviews</a>', '<a href="/reviews/" aria-current="page">Reviews</a>')
t = re.sub(r"<script>\(function\(\)\{var lb=document\.getElementById\('lightbox'\).*?</script>", '', t, flags=re.S)
os.makedirs('reviews', exist_ok=True); open('reviews/index.html', 'w').write(t)
print('built', len(V), 'videos; assets', h)
