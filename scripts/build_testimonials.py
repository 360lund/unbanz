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
RV_CSS = ('<style>.rv-top{padding:36px 0 8px}.rv-top h1{font-size:44px;letter-spacing:-.045em;line-height:1.05;margin:0}.rv-top p{margin:10px 0 0;font-size:17px;opacity:.75}'
  '.rv .vt-page{padding:22px 0 0}.rv .vt-page .vt-track{max-width:860px;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}'
  '.rv .vt-play b{font-size:17px}.rv .vt-play i{width:58px;height:58px}'
  '.rv-cta{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;padding:34px 0 10px}.rv-cta .button{font-size:17px;padding-inline:28px}.rv-cta .rv-mail{font-weight:600;text-decoration:underline;text-underline-offset:3px}'
  '.rv-faq{padding:46px 0 70px}.rv-faq h2{font-size:22px;letter-spacing:-.02em;margin:0 0 10px}'
  '@media (max-width:760px){.rv .vt-page .vt-track{max-width:none}.rv-top{padding:22px 0 4px}.rv-top h1{font-size:34px}.rv-top p{font-size:15px}'
  '.rv .vt-page .vt-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;margin-inline:-20px;padding:2px 20px 8px;gap:14px;scrollbar-width:none}'
  '.rv .vt-page .vt-card{flex:0 0 78vw;max-width:340px;scroll-snap-align:center}.rv-cta{padding-top:22px}.rv-cta .button{width:100%;justify-content:center}.rv-cta .rv-mail{width:100%;text-align:center}}</style>')
FAQ = [("Is Unbanz legit?", "Yes. Unbanz is a real, independent service at unbanz.com. The clients above share their experience on camera."),
       ("Do I need to share my password?", "No. Your password stays with you."),
       ("How do I get a price?", "Message us on WhatsApp or email with what happened. You get a clear price before any work starts."),
       ("What can Unbanz help with?", "Instagram and Facebook unbans, restricted ad accounts, removing fake or impersonation accounts, and username claims.")]
main = ('<main id="content" class="rv"><section class="rv-top container"><h1>Unbanz reviews</h1><p>Real clients, on camera. Tap a video to play.</p></section>'
        '<section class="vt vt-page container" aria-label="Video reviews"><ul class="vt-track">' + ''.join(card(v) for v in V) + '</ul></section>'
        '<section class="rv-cta container" aria-label="Contact"><a class="button button-light" href="https://wa.me/447723162824?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20an%20account">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="rv-mail" href="mailto:team@unbanz.com?subject=Account%20help">Or email team@unbanz.com</a></section>'
        '<section class="rv-faq container" aria-labelledby="rvq"><h2 id="rvq">Questions</h2><div class="simple-faq">' + ''.join(f'<details><summary>{e(q)}<span aria-hidden="true">+</span></summary><p>{e(a)}</p></details>' for q, a in FAQ) + '</div></section></main>')
t = t.replace('</head>', RV_CSS + '</head>', 1)
t = re.sub(r'<main id="content">.*?</main>', lambda m: main, t, count=1, flags=re.S)
t = re.sub(r'<div class="lightbox" id="lightbox".*?</div></div>', '', t, count=1, flags=re.S)
t = t.replace('<a href="/reviews/">Reviews</a>', '<a href="/reviews/" aria-current="page">Reviews</a>')
t = re.sub(r"<script>\(function\(\)\{var lb=document\.getElementById\('lightbox'\).*?</script>", '', t, flags=re.S)
os.makedirs('reviews', exist_ok=True); open('reviews/index.html', 'w').write(t)
print('built', len(V), 'videos; assets', h)
