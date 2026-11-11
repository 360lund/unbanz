# Nov 11 page generator. Builds static pages from the current live templates
# (keeps nav, CTAs, contact-policy assets, testimonials, footer).
import re, json, html, os
SITE='/workspace/site'
D='2026-11-11'
DH={'en':'11 November 2026','fr':'11 novembre 2026','es':'11 de noviembre de 2026','pt-br':'11 de novembro de 2026','nl':'11 november 2026','de':'11. November 2026'}
UPD={'en':'Updated','fr':'Mis à jour le','es':'Actualizado el','pt-br':'Atualizado em','nl':'Bijgewerkt op','de':'Aktualisiert am'}
TPL={'en':'tiktok-appeal-links-and-forms-directory','fr':'fr/liens-officiels-appel-tiktok','nl':'nl/officiele-bezwaarlinks-tiktok',
     'es':'es/contactar-con-instagram-o-meta-desde-espana','pt-br':'pt-br/falar-com-o-instagram-ou-a-meta-no-brasil','de':'tiktok-appeal-links-and-forms-directory'}
LOC={'en':'en_US','fr':'fr_FR','nl':'nl_NL','es':'es_ES','pt-br':'pt_BR','de':'de_DE'}
HL={'en':'en','fr':'fr','nl':'nl','es':'es','pt-br':'pt-BR','de':'de'}
CTA={'en':('Message us on WhatsApp','Prefer email? ↗︎'),'fr':('Parlons-en sur WhatsApp','Plutôt par e-mail ? ↗︎'),'es':('Escríbenos por WhatsApp','¿Prefieres email? ↗︎'),
     'pt-br':('Fale com a gente no WhatsApp','Prefere e-mail? ↗︎'),'nl':('Stuur ons een WhatsApp','Liever e-mail? ↗︎'),'de':('Schreib uns auf WhatsApp','Lieber per E-Mail? ↗︎')}
ABOUT={'en':('About Unbanz','Unbanz (unbanz.com) is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook, TikTok, YouTube, Snapchat and Meta ad accounts, recover Facebook Pages and claim usernames. Fees are fixed and paid upfront, with a 100% refund if the case fails. Contact: team@unbanz.com. Not affiliated with Meta, TikTok, Snap or Google.'),
 'fr':('À propos d’Unbanz','Unbanz (unbanz.com) est un service indépendant qui aide à récupérer des comptes Instagram, Facebook, TikTok, YouTube, Snapchat et publicitaires Meta désactivés, suspendus ou piratés, des Pages Facebook, et à obtenir des noms d’utilisateur. Tarifs fixes payés d’avance, remboursés à 100 % si le dossier échoue. Contact : team@unbanz.com. Sans lien avec Meta, TikTok, Snap ou Google.'),
 'es':('Sobre Unbanz','Unbanz (unbanz.com) es un servicio independiente que ayuda a recuperar cuentas de Instagram, Facebook, TikTok, YouTube, Snapchat y publicitarias de Meta desactivadas, suspendidas o hackeadas, páginas de Facebook y nombres de usuario. Precios fijos pagados por adelantado, con reembolso del 100 % si el caso falla. Contacto: team@unbanz.com. Sin relación con Meta, TikTok, Snap ni Google.'),
 'pt-br':('Sobre a Unbanz','A Unbanz (unbanz.com) é um serviço independente que ajuda a recuperar contas do Instagram, Facebook, TikTok, YouTube, Snapchat e de anúncios da Meta desativadas, suspensas ou hackeadas, Páginas do Facebook e nomes de usuário. Preços fixos pagos antecipadamente, com reembolso de 100% se o caso falhar. Contato: team@unbanz.com. Sem vínculo com Meta, TikTok, Snap ou Google.'),
 'nl':('Over Unbanz','Unbanz (unbanz.com) is een onafhankelijke dienst die helpt bij het terugkrijgen van uitgeschakelde, opgeschorte en gehackte Instagram-, Facebook-, TikTok-, YouTube-, Snapchat- en Meta-advertentieaccounts, Facebook-pagina’s en gebruikersnamen. Vaste prijzen, vooraf betaald, 100% terugbetaling als de zaak mislukt. Contact: team@unbanz.com. Niet verbonden aan Meta, TikTok, Snap of Google.'),
 'de':('Über Unbanz','Unbanz (unbanz.com) ist ein unabhängiger Dienst, der hilft, deaktivierte, gesperrte und gehackte Instagram-, Facebook-, TikTok-, YouTube-, Snapchat- und Meta-Werbekonten, Facebook-Seiten und Nutzernamen zurückzuholen. Feste Preise, im Voraus bezahlt, 100 % Rückerstattung, wenn der Fall scheitert. Kontakt: team@unbanz.com. Nicht mit Meta, TikTok, Snap oder Google verbunden.')}
WA='https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account'
def ext(u,label=None): return f'<a href="{u}" rel="noopener" target="_blank">{label or html.escape(u.replace("https://",""))}</a>'
def table(rows,heads=('Link','What it is for')):
    return '<div class="table-wrap"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
def linkrows(items): return table([(f'<strong>{html.escape(t)}</strong><br>{ext(u)}',html.escape(w)) for t,u,w in items])
def ul(items): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
def ol(items): return '<ol>'+''.join(f'<li>{i}</li>' for i in items)+'</ol>'
def a(href,text): return f'<a href="{href}">{text}</a>'
def strip(s): return html.unescape(re.sub(r'<[^>]+>','',s))
BUILT=[]
def build(p):
    lang=p.get('lang','en'); slug=p['slug'].strip('/'); URL=f'https://unbanz.com/{slug}/'
    T=open(f"{SITE}/{TPL[lang]}/index.html").read()
    turl='https://unbanz.com/'+TPL[lang]+'/'
    he=T.find('</head>'); head=T[:he]; body=T[he:]
    ot=re.search(r'<title>(.*?)</title>',head).group(1); od=re.search(r'name="description" content="([^"]*)"',head).group(1)
    head=head.replace(f'<title>{ot}</title>',f'<title>{html.escape(p["title"])}</title>')
    head=head.replace(f'content="{od}"',f'content="{html.escape(p["desc"],quote=True)}"')
    head=head.replace(f'content="{ot}"',f'content="{html.escape(p["title"],quote=True)}"')
    head=re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*','',head)
    head=re.sub(r'<meta property="og:locale:alternate"[^>]*>\s*','',head)
    head=head.replace(turl,URL)
    head=re.sub(r'<html lang="[^"]*"',f'<html lang="{HL[lang]}"',head)
    head=re.sub(r'<meta property="og:locale" content="[^"]*">',f'<meta property="og:locale" content="{LOC[lang]}">',head)
    head=re.sub(r'<meta property="article:modified_time" content="[^"]*">',f'<meta property="article:modified_time" content="{D}">',head)
    alts=p.get('alts') or {}
    if alts:
        tags=''.join(f'<link rel="alternate" hreflang="{HL[l]}" href="https://unbanz.com/{u.strip("/")}/">' for l,u in alts.items())
        x=alts.get('en'); tags+=f'<link rel="alternate" hreflang="x-default" href="https://unbanz.com/{x.strip("/")}/">' if x else ''
        head=head.replace('<link rel="canonical"',tags+'<link rel="canonical"',1)
    m=re.search(r'<script type="application/ld\+json">(.*?)</script>',head,re.S); g=json.loads(m.group(1))
    org=[x for x in g['@graph'] if x.get('@type') in ('Organization','WebSite')]
    crumb_name,crumb_href=p.get('crumb',('Guides','/guides/'))
    faqs=p.get('faqs',[])
    wp={"@type":"WebPage","@id":URL+"#webpage","url":URL,"name":p['title'],"description":p['desc'],"isPartOf":{"@id":"https://unbanz.com/#website"},"publisher":{"@id":"https://unbanz.com/#organization"},"inLanguage":HL[lang],"datePublished":p.get('published',D),"dateModified":D,"breadcrumb":{"@id":URL+"#breadcrumb"}}
    if p.get('itemlist'): wp['mainEntity']={"@type":"ItemList","name":p['h1t'] if p.get('h1t') else strip(p['h1']),"itemListElement":[{"@type":"ListItem","position":i+1,"name":t,"url":u} for i,(t,u) in enumerate(p['itemlist'])]}
    graph=org+[wp,{"@type":"BreadcrumbList","@id":URL+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://unbanz.com/" if lang=='en' else f"https://unbanz.com/{lang}/"},{"@type":"ListItem","position":2,"name":crumb_name,"item":"https://unbanz.com"+crumb_href},{"@type":"ListItem","position":3,"name":p.get('short',strip(p['h1'])[:70]),"item":URL}]}]
    if faqs: graph.append({"@type":"FAQPage","@id":URL+"#faq","mainEntity":[{"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(an)}} for q,an in faqs]})
    if p.get('service'):
        nm,price,area=p['service']
        graph.append({"@type":"Service","@id":URL+"#service","name":nm,"serviceType":"Account recovery","provider":{"@id":"https://unbanz.com/#organization"},"url":URL,"areaServed":["US","GB","CA","AU","IE","NZ","AE","SA","QA","KW","DE","FR","NL","BE","CH","ES","PT","IT","SE","NO","DK"],
          "offers":{"@type":"Offer","price":price,"priceCurrency":"USD","url":URL,"description":"Paid upfront by card. 100% refund if the case fails. Usually 3–7 days, not guaranteed."}})
    if p.get('howto'):
        graph.append({"@type":"HowTo","@id":URL+"#howto","name":p['howto'][0],"step":[{"@type":"HowToStep","position":i+1,"name":s[:80],"text":s} for i,s in enumerate(p['howto'][1])]})
    head=head[:m.start(1)]+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+head[m.end(1):]
    i=body.find('<main id="content">')
    ends=[x for x in (body.find('<section class="vt vt-page',i),body.find('<section class="faq-section"',i)) if x>0]; j=min(ends)
    pre=body[:i]; post=body[j:]
    sv=p.get('sv','unban'); wa,em=CTA[lang]
    cards=''.join(f'<article><h2>{x}</h2><p>{y}</p></article>' for x,y in p.get('cards',[]))
    secs=''.join(f'<h2 id="{sid}">{h}</h2>{c}' for sid,h,c in p['sections'])
    ab=ABOUT[lang]
    rel=p.get('related',[])
    relhtml=('<h2 id="related">'+{'en':'Related','fr':'À lire aussi','es':'Relacionado','pt-br':'Relacionados','nl':'Gerelateerd','de':'Verwandte Seiten'}[lang]+'</h2><p>'+', '.join(a(h,t) for h,t in rel)+'.</p>') if rel else ''
    hero=(f'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="{crumb_href}">{html.escape(p.get("crumbtxt","Home / "+crumb_name))}</a><h1>{p["h1"]}</h1><p>{p["lede"]}</p><p class="guide-meta">{UPD[lang]} <time datetime="{D}">{DH[lang]}</time></p>'
      f'<div class="hero-cta"><a class="button button-light" href="{WA}" data-service="{sv}">{wa} <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Account%20help">{em}</a></div></div></section>'
      f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{p["answer"]}</p></section>'
      +(f'<section class="service-editorial container">{cards}</section>' if cards else '')+
      f'<article class="guide-body container">{secs}{relhtml}<h2 id="about-unbanz">{ab[0]}</h2><p>{ab[1]}</p></article>')
    if faqs:
        fh=''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{an}</p></details>' for q,an in faqs)
        post=re.sub(r'<div class="simple-faq">.*?</div></div></section>','<div class="simple-faq">'+fh+'</div></div></section>',post,count=1,flags=re.S)
    else:
        post=re.sub(r'<section class="faq-section".*?</div></div></section>','',post,count=1,flags=re.S)
    post=post.replace('Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Facebook%20account','Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account')
    if p.get('navrel'):
        post=re.sub(r'(<nav class="related-services container" aria-label="[^"]*">).*?(</nav>)',lambda mm:mm.group(1)+''.join(a(h,t) for h,t in p['navrel'])+mm.group(2),post,count=1,flags=re.S)
    post=re.sub(r'<nav class="related-services container"[^>]*data-dd29[^>]*>.*?</nav>','',post,flags=re.S)
    if lang=='de':
        post=post.replace('QUICK ANSWERS','KURZE ANTWORTEN').replace('<h2>Good to know.</h2>','<h2>Gut zu wissen.</h2>').replace('<h2>Tell us what you need.</h2>','<h2>Sag uns, was passiert ist.</h2>').replace('>Email us<','>E-Mail schreiben<').replace('Message us on WhatsApp','Schreib uns auf WhatsApp').replace('What clients say','Was Kunden sagen')
        pre=pre.replace('Skip to content','Zum Inhalt springen')
    out=head+pre+hero+post
    assert out.count('<main id="content">')==1 and '</html>' in out
    os.makedirs(f'{SITE}/{slug}',exist_ok=True); open(f'{SITE}/{slug}/index.html','w').write(out)
    BUILT.append((slug,lang,p.get('alts')))
    return URL
