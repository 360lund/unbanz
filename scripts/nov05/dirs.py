import re,json,html,os
os.chdir('/workspace/site')
T=open('facebook-notice-types/index.html').read()
D='2026-11-05'; DH='5 November 2026'
WA='https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account'
ext=lambda u:f'<a href="{u}" rel="noopener" target="_blank">{u.replace("https://","")}</a>'
def build(p):
    slug=p['slug'];URL=f'https://unbanz.com/{slug}/'
    body=[p['pre']]
    for sid,name,items in p['sections']:
        body.append(f'<h2 id="{sid}">{name}</h2><div class="table-wrap"><table><thead><tr><th>Link</th><th>What it is for</th></tr></thead><tbody>')
        for t,u,w in items: body.append(f'<tr><td><strong>{html.escape(t)}</strong><br>{ext(u)}</td><td>{html.escape(w)}</td></tr>')
        body.append('</tbody></table></div>')
    body+=p['post']
    body.append('<h2 id="want-it-done">Want it done for you?</h2><p>If you would rather hand it over, get a quote for account recovery. Your password stays with you, and terms are agreed with you before any work starts. Unbanz is not Meta or Snap and cannot see inside their systems; the platform makes the final decision.</p>')
    body.append('<h2 id="related">Related</h2><p>'+p['related']+'</p>')
    body.append('<h2 id="about-unbanz">About Unbanz</h2><p>Unbanz (unbanz.com) is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook, Snapchat and Meta ad accounts, and claim usernames. Contact: WhatsApp +1 934 201 2490 or team@unbanz.com. Not affiliated with Meta.</p>')
    faqs=p['faqs']
    faq_html=''.join(f'<details><summary>{html.escape(q)}<span aria-hidden="true">+</span></summary><p>{html.escape(a)}</p></details>' for q,a in faqs)
    he=T.find('</head>');head=T[:he]
    ot=re.search(r'<title>(.*?)</title>',head).group(1);od=re.search(r'name="description" content="([^"]*)"',head).group(1)
    head=head.replace(ot,html.escape(p['title'])).replace(od,html.escape(p['desc'])).replace('https://unbanz.com/facebook-notice-types/',URL)
    m=re.search(r'<script type="application/ld\+json">(.*?)</script>',head,re.S);g=json.loads(m.group(1))
    links=[x for s in p['sections'] for x in s[2]]
    graph=[g['@graph'][0],g['@graph'][1],
     {"@type":"WebPage","@id":URL+"#webpage","url":URL,"name":p['title'],"description":p['desc'],"isPartOf":{"@id":"https://unbanz.com/#website"},"publisher":{"@id":"https://unbanz.com/#organization"},"inLanguage":"en","datePublished":D,"dateModified":D,"breadcrumb":{"@id":URL+"#breadcrumb"},
      "mainEntity":{"@type":"ItemList","name":p['listname'],"itemListElement":[{"@type":"ListItem","position":i+1,"name":t,"url":u} for i,(t,u,w) in enumerate(links)]}},
     {"@type":"BreadcrumbList","@id":URL+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://unbanz.com/"},{"@type":"ListItem","position":2,"name":"Guides","item":"https://unbanz.com/guides/"},{"@type":"ListItem","position":3,"name":p['crumb'],"item":URL}]},
     {"@type":"FAQPage","@id":URL+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]
    head=head[:m.start(1)]+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+head[m.end(1):]
    b0=T[he:];i=b0.find('<main id="content">');mc=b0.find('<section class="vt vt-page')
    pre=b0[:i];post=b0[mc:]
    hero=(f'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="/guides/">Home / Guides</a><h1>{p["h1"]}</h1><p>{p["lede"]}</p><p class="guide-meta">Updated <time datetime="{D}">{DH}</time></p>'
     f'<div class="hero-cta"><a class="button button-light" href="{WA}" data-service="unban">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Account%20help">Prefer email? ↗︎</a></div></div></section>'
     f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{p["answer"]}</p></section>'
     '<section class="service-editorial container">'+''.join(f'<article><h2>{a}</h2><p>{b}</p></article>' for a,b in p['cards'])+'</section>'
     '<article class="guide-body container">'+''.join(body)+'</article>')
    post=re.sub(r'<div class="simple-faq">.*?</div></div></section>','<div class="simple-faq">'+faq_html+'</div></div></section>',post,count=1,flags=re.S)
    post=post.replace('Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Facebook%20account','Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account').replace('subject=Facebook%20account','subject=Account%20help')
    os.makedirs(slug,exist_ok=True);open(slug+'/index.html','w').write(head+pre+hero+post);print('ok',slug)
from pages import PAGES
for p in PAGES: build(p)
