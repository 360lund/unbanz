import re,json,html,os,sys
os.chdir('/workspace/site')
D='2026-11-05'
ext=lambda u:f'<a href="{u}" rel="noopener" target="_blank">{u.replace("https://","")}</a>'
CFG={'en':dict(tpl='facebook-notice-types/index.html',old='https://unbanz.com/facebook-notice-types/',home='/guides/',crumb='Home / Guides',upd='Updated',dh='5 November 2026',wa='Message us on WhatsApp',em='Prefer email?',th=('Link','What it is for'),lang='en',
  hn='Home',gn='Guides',gu='https://unbanz.com/guides/',want='Want it done for you?',wantp='If you would rather hand it over, get a quote for account recovery. Your password stays with you, and terms are agreed with you before any work starts. Unbanz is independent and cannot see inside Meta’s systems; the platform makes the final decision.',rel='Related',about='About Unbanz',aboutp='Unbanz (unbanz.com) is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook, Snapchat and Meta ad accounts, and claim usernames. Contact: WhatsApp +1 934 201 2490 or team@unbanz.com. Not affiliated with Meta.'),
 'fr':dict(tpl='fr/compte-facebook-desactive-faire-appel/index.html',old='https://unbanz.com/fr/compte-facebook-desactive-faire-appel/',home='/fr/',crumb='Accueil / Guides',upd='Mis à jour le',dh='5 novembre 2026',wa='Parlons-en sur WhatsApp',em='Plutôt par e-mail ?',th=('Lien','À quoi il sert'),lang='fr',
  hn='Accueil',gn='Guides',gu='https://unbanz.com/fr/',want='Vous préférez déléguer ?',wantp='Demandez un devis pour la récupération de votre compte. Votre mot de passe reste chez vous, et les conditions sont convenues avec vous avant tout travail. Unbanz est indépendant et n’a pas accès aux systèmes de Meta ; la plateforme prend la décision finale.',rel='À lire aussi',about='À propos d’Unbanz',aboutp='Unbanz (unbanz.com) est un service indépendant qui aide à récupérer des comptes Instagram, Facebook, Snapchat et publicitaires Meta désactivés, suspendus ou piratés, et à obtenir des noms d’utilisateur. Contact : WhatsApp +1 934 201 2490 ou team@unbanz.com. Non affilié à Meta.'),
 'nl':dict(tpl='nl/facebook-account-uitgeschakeld-bezwaar/index.html',old='https://unbanz.com/nl/facebook-account-uitgeschakeld-bezwaar/',home='/nl/',crumb='Home / Gidsen',upd='Bijgewerkt op',dh='5 november 2026',wa='Stuur ons een WhatsApp',em='Liever per e-mail?',th=('Link','Waarvoor'),lang='nl',
  hn='Home',gn='Gidsen',gu='https://unbanz.com/nl/',want='Liever uitbesteden?',wantp='Vraag een offerte aan voor accountherstel. Je wachtwoord blijft bij jou, en de voorwaarden spreken we met je af voordat er iets gebeurt. Unbanz is onafhankelijk en kan niet in de systemen van Meta kijken; het platform neemt het eindbesluit.',rel='Lees ook',about='Over Unbanz',aboutp='Unbanz (unbanz.com) is een onafhankelijke dienst die helpt bij het terugkrijgen van uitgeschakelde, opgeschorte en gehackte Instagram-, Facebook-, Snapchat- en Meta-advertentieaccounts, en bij het claimen van gebruikersnamen. Contact: WhatsApp +1 934 201 2490 of team@unbanz.com. Niet gelieerd aan Meta.')}
def build(p):
    c=CFG[p.get('lang','en')];slug=p['slug'];URL=f'https://unbanz.com/{slug}/'
    T=open(c['tpl']).read()
    body=[p['pre']]
    for sid,name,items in p['sections']:
        body.append(f'<h2 id="{sid}">{name}</h2><div class="table-wrap"><table><thead><tr><th>{c["th"][0]}</th><th>{c["th"][1]}</th></tr></thead><tbody>')
        for t,u,w in items: body.append(f'<tr><td><strong>{html.escape(t)}</strong><br>{ext(u)}</td><td>{html.escape(w)}</td></tr>')
        body.append('</tbody></table></div>')
    body+=p['post']
    body.append(f'<h2 id="want-it-done">{c["want"]}</h2><p>{c["wantp"]}</p><h2 id="related">{c["rel"]}</h2><p>{p["related"]}</p><h2 id="about-unbanz">{c["about"]}</h2><p>{c["aboutp"]}</p>')
    faqs=p['faqs'];faq_html=''.join(f'<details><summary>{html.escape(q)}<span aria-hidden="true">+</span></summary><p>{html.escape(a)}</p></details>' for q,a in faqs)
    he=T.find('</head>');head=T[:he]
    ot=re.search(r'<title>(.*?)</title>',head).group(1);od=re.search(r'name="description" content="([^"]*)"',head).group(1)
    head=head.replace(ot,html.escape(p['title'])).replace(od,html.escape(p['desc']))
    head=re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>','',head)
    head=head.replace(c['old'],URL)
    hl=p.get('hreflang')
    if hl: head=head.replace('</title>','</title>'+''.join(f'<link rel="alternate" hreflang="{k}" href="{v}">' for k,v in hl),1)
    og=re.search(r'property="og:title" content="([^"]*)"',head)
    if og: head=head.replace(og.group(0),f'property="og:title" content="{html.escape(p["title"])}"')
    m=re.search(r'<script type="application/ld\+json">(.*?)</script>',head,re.S);g=json.loads(m.group(1))
    keep=[x for x in g.get('@graph',[]) if x.get('@type') in ('Organization','WebSite','ProfessionalService','LocalBusiness')][:2]
    links=[x for s in p['sections'] for x in s[2]]
    graph=keep+[{"@type":"WebPage","@id":URL+"#webpage","url":URL,"name":p['title'],"description":p['desc'],"isPartOf":{"@id":"https://unbanz.com/#website"},"publisher":{"@id":"https://unbanz.com/#organization"},"inLanguage":c['lang'],"datePublished":D,"dateModified":D,"breadcrumb":{"@id":URL+"#breadcrumb"},
      "mainEntity":{"@type":"ItemList","name":p['title'],"itemListElement":[{"@type":"ListItem","position":i+1,"name":t,"url":u} for i,(t,u,w) in enumerate(links)]}},
     {"@type":"BreadcrumbList","@id":URL+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":c['hn'],"item":"https://unbanz.com/"},{"@type":"ListItem","position":2,"name":c['gn'],"item":c['gu']},{"@type":"ListItem","position":3,"name":p['crumb'],"item":URL}]},
     {"@type":"FAQPage","@id":URL+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]
    head=head[:m.start(1)]+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+head[m.end(1):]
    b0=T[he:];i=b0.find('<main id="content">')
    mc=b0.find('<section class="vt vt-page')
    if mc<0: mc=b0.find('</article>',i)+len('</article>')
    pre=b0[:i];post=b0[mc:]
    WA=re.search(r'https://wa\.me/19342012490\?text=[^"]*',b0).group(0)
    hero=(f'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="{c["home"]}">{c["crumb"]}</a><h1>{p["h1"]}</h1><p>{p["lede"]}</p><p class="guide-meta">{c["upd"]} <time datetime="{D}">{c["dh"]}</time></p>'
     f'<div class="hero-cta"><a class="button button-light" href="{WA}" data-service="unban">{c["wa"]} <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Account%20help">{c["em"]} ↗︎</a></div></div></section>'
     f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{p["answer"]}</p></section>'
     +('<section class="service-editorial container">'+''.join(f'<article><h2>{a}</h2><p>{b}</p></article>' for a,b in p['cards'])+'</section>' if p.get('cards') else '')+
     '<article class="guide-body container">'+''.join(body)+'</article>')
    post=re.sub(r'<div class="simple-faq">.*?</div></div></section>','<div class="simple-faq">'+faq_html+'</div></div></section>',post,count=1,flags=re.S)
    post=post.replace('Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Facebook%20account','Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account').replace('subject=Facebook%20account','subject=Account%20help')
    os.makedirs(slug,exist_ok=True);open(slug+'/index.html','w').write(head+pre+hero+post);print('ok',slug)
if __name__=='__main__':
    sys.path.insert(0,'scripts/nov05')
    for p in __import__(sys.argv[1]).PAGES: build(p)
