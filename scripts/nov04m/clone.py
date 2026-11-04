import re,json,html,os
B='https://unbanz.com'
def make(lang,tpl,slug,en,title,desc,nav,h1,answer,secs,help_html,faq,related,twins=None,crumb='Guides'):
    s=open(f'{lang}/{tpl}/index.html').read();u=f'{B}/{lang}/{slug}/';tu=f'{B}/{lang}/{tpl}/'
    E=lambda t:html.escape(t,quote=True)
    s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{E(desc)}">',s)
    s=re.sub(r'(<meta (?:property|name)="(?:og|twitter):description" content=")[^"]*',lambda m:m.group(1)+E(desc),s)
    s=re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*',lambda m:m.group(1)+E(title),s)
    s=re.sub(r'<title>[^<]*</title>',f'<title>{E(title)}</title>',s)
    loc={'fr':['fr','fr-FR'],'nl':['nl','nl-NL'],'es':['es','es-ES'],'pt-br':['pt-BR']}
    alts=[('en',B+'/'+en+'/'),('en-US',B+'/'+en+'/')]
    for l in loc[lang]: alts.append((l,u))
    for tl,tu2 in (twins or {}).items():
        for l in loc[tl]: alts.append((l,tu2))
    alts.append(('x-default',B+'/'+en+'/'))
    hl=''.join(f'<link rel="alternate" hreflang="{a}" href="{b}">' for a,b in alts)
    s=re.sub(r'<link rel="canonical"[^>]*>(<link rel="alternate"[^>]*>)+',f'<link rel="canonical" href="{u}">'+hl,s)
    s=s.replace(f'content="{tu}"',f'content="{u}"')
    # jsonld
    m=re.search(r'<script type="application/ld\+json">(.*?)</script>',s,re.S);g=json.loads(m.group(1))
    for n in g['@graph']:
        t=n.get('@type')
        if t=='WebPage': n.update({'@id':u+'#webpage','url':u,'name':title,'description':desc,'dateModified':'2026-11-04','breadcrumb':{'@id':u+'#breadcrumb'}})
        if t=='BreadcrumbList': n['@id']=u+'#breadcrumb';n['itemListElement'][-1].update({'name':nav,'item':u})
        if t=='FAQPage': n.update({'@id':u+'#faq','url':u,'mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faq]})
    s=s[:m.start(1)]+json.dumps(g,ensure_ascii=False,separators=(',',':'))+s[m.end(1):]
    s=re.sub(r'<h1>.*?</h1>',f'<h1>{h1}</h1>',s,1,re.S)
    s=re.sub(r'(</time></p><p>).*?(</p><div class="hero-cta">)',lambda m:m.group(1)+answer+m.group(2),s,1,re.S)
    a=s.find('<article class="guide-body container">')+len('<article class="guide-body container">');h=s.find('<h2 id="',s.find('id="aide"' if lang=='fr' else 'id="help"')+5)
    ai=s.find('<h2 id="aide">' if lang=='fr' else '<h2 id="help">')
    body=''.join(f'<h2 id="{i}">{t}</h2>{c}' for i,t,c in secs)
    nxt=s.find('<h2 id=',ai+5)
    s=s[:a]+body+s[ai:ai+len(s[ai:nxt].split('</h2>')[0])+5]+help_html+s[nxt:]
    q=s.find('<h2 id="questions-2026">')
    if q>0: s=s[:q]+s[s.find('<h2 id=',q+5):]
    f0=s.find('<div class="simple-faq">');f1=s.find('</div>',f0)
    s=s[:f0]+'<div class="simple-faq">'+''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in faq)+s[f1:]
    s=re.sub(r'(<nav class="related-services container" aria-label="[^"]*">).*?(</nav></main>)',lambda m:m.group(1)+''.join(f'<a href="{h}">{l}</a>' for h,l in related)+m.group(2),s,1,re.S)
    assert tpl not in s.replace(f'href="/{lang}/{tpl}/"',''),[x.start() for x in re.finditer(tpl,s)][:5]
    os.makedirs(f'{lang}/{slug}',exist_ok=True);open(f'{lang}/{slug}/index.html','w').write(s)
    # reciprocal hreflang on en + twins
    for p in [en]+[t.replace(B+'/','').strip('/') for t in (twins or {}).values()]:
        fp=p+'/index.html';x=open(fp).read()
        if u in x: continue
        tag=''.join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l in loc[lang])
        x=re.sub(r'<link rel="alternate" hreflang="x-default"',tag+'<link rel="alternate" hreflang="x-default"',x,1);open(fp,'w').write(x)
    sm=open('sitemap.xml').read()
    if u not in sm: open('sitemap.xml','w').write(sm.replace('</urlset>',f'<url><loc>{u}</loc><lastmod>2026-11-04</lastmod></url>\n</urlset>'))
    for fn in ('llms.txt','llms-full.txt'):
        t=open(fn).read()
        if u not in t: open(fn,'w').write(t.rstrip('\n')+f'\n- [{title.replace(" | Unbanz","")}]({u}): {desc}\n')
    return u
