import re,json,html,os
os.chdir('/workspace/site')
T=open('facebook-notice-types/index.html').read()
WA='https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account'
BANNED=re.compile(r'\b(cases?|we review|fixed price|fast turnaround|guarantee[ds]?|snapchat)\b',re.I)
def ext(u,label=None): return f'<a href="{u}" rel="noopener" target="_blank">{label or u.replace("https://","").replace("www.","")}</a>'
ABOUT='<h2 id="about-unbanz">About Unbanz</h2><p>Unbanz (unbanz.com) is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. Contact: WhatsApp +1 934 201 2490 or team@unbanz.com. Not affiliated with Meta.</p>'
CTA='<h2 id="want-it-done">Want it done for you?</h2><p>Want it done for you? Get a quote. Your password stays with you. Terms are agreed with you before any work starts.</p>'
def make(slug,title,desc,h1,lede,answer,body,faqs,crumb=('Guides','/guides/'),cards=None,extra_graph=None,date='2026-11-04'):
    URL=f'https://unbanz.com/{slug}/'
    txt=' '.join([title,desc,h1,lede,answer,body]+[q+' '+a for q,a in faqs])
    bad=BANNED.findall(re.sub(r'<[^>]+>|https?://\S+','',txt))
    assert not bad,(slug,bad)
    he=T.find('</head>');head=T[:he]
    ot=re.search(r'<title>(.*?)</title>',head).group(1);od=re.search(r'name="description" content="([^"]*)"',head).group(1)
    head=head.replace(ot,html.escape(title)).replace(od,html.escape(desc)).replace('https://unbanz.com/facebook-notice-types/',URL)
    m=re.search(r'<script type="application/ld\+json">(.*?)</script>',head,re.S);g=json.loads(m.group(1))
    wp={"@type":"WebPage","@id":URL+"#webpage","url":URL,"name":title,"description":desc,"isPartOf":{"@id":"https://unbanz.com/#website"},"publisher":{"@id":"https://unbanz.com/#organization"},"about":{"@id":"https://unbanz.com/#organization"},"inLanguage":"en","datePublished":date,"dateModified":date,"breadcrumb":{"@id":URL+"#breadcrumb"}}
    graph=[g['@graph'][0],g['@graph'][1],wp,
     {"@type":"BreadcrumbList","@id":URL+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://unbanz.com/"},{"@type":"ListItem","position":2,"name":crumb[0],"item":"https://unbanz.com"+crumb[1]},{"@type":"ListItem","position":3,"name":h1.rstrip('.'),"item":URL}]},
     {"@type":"FAQPage","@id":URL+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]+(extra_graph or [])
    head=head[:m.start(1)]+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+head[m.end(1):]
    b0=T[he:];i=b0.find('<main id="content">');mc=b0.find('<section class="vt vt-page')
    pre,post=b0[:i],b0[mc:]
    cards=cards or [('Official routes first','Every route here starts with Meta’s own tools.'),('Updated','Checked '+date_h(date)+'.'),('Your password stays with you','Nobody legit needs it.')]
    hero=(f'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="{crumb[1]}">Home / {crumb[0]}</a><h1>{h1}</h1><p>{lede}</p><p class="guide-meta">Updated <time datetime="{date}">{date_h(date)}</time></p>'
     f'<div class="hero-cta"><a class="button button-light" href="{WA}" data-service="unban">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Account%20help">Prefer email? ↗︎</a></div></div></section>'
     f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{answer}</p></section>'
     '<section class="service-editorial container">'+''.join(f'<article><h2>{a}</h2><p>{b}</p></article>' for a,b in cards)+'</section>'
     '<article class="guide-body container">'+body+CTA+ABOUT+'</article>')
    fh=''.join(f'<details><summary>{html.escape(q)}<span aria-hidden="true">+</span></summary><p>{html.escape(a)}</p></details>' for q,a in faqs)
    post=re.sub(r'<div class="simple-faq">.*?</div></div></section>','<div class="simple-faq">'+fh+'</div></div></section>',post,count=1,flags=re.S)
    post=post.replace('Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Facebook%20account','Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account').replace('subject=Facebook%20account','subject=Account%20help')
    os.makedirs(slug,exist_ok=True);open(slug+'/index.html','w').write(head+pre+hero+post)
    return URL
def date_h(d):
    y,m,dd=d.split('-');return f"{int(dd)} {['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {y}"
def table(head,rows):
    return '<div class="table-wrap"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'

def add_section(rel,block,date='2026-11-04',anchor=None):
    """Append a new section into a page's main article (no existing copy changed), bump visible Updated + dateModified."""
    p=rel.strip('/')+'/index.html';s=open(p).read()
    t=re.sub(r'<[^>]+>|https?://\S+','',block);bad=BANNED.findall(t);assert not bad,(rel,bad)
    if anchor and f'id="{anchor}"' in s: return False
    end=s.find('<section class="vt');end=end if end>0 else s.find('<footer')
    m=s.rfind('<main',0,end); 
    a=s.rfind('</article>',0,end)
    if a<m: a=s.rfind('</main>',0,end)
    ab=s.rfind('<h2 id="about-unbanz">',m,a)
    at=ab if ab>0 else a
    sec=s.rfind('<section',m,at)
    if sec>0 and 'service-editorial' in s[sec:sec+80] and s.find('</section>',sec)<at:
        se=s.find('</section>',at)+10
        s=s[:se]+'<article class="guide-body container">'+block+'</article>'+s[se:]
    else:
        s=s[:at]+block+s[at:]
    s=re.sub(r'"dateModified":"[^"]*"',f'"dateModified":"{date}"',s)
    if '"dateModified"' not in s:
        s=s.replace('"@type":"WebPage",',f'"@type":"WebPage","dateModified":"{date}",',1)
    if re.search(r'<p class="guide-meta">',s):
        s=re.sub(r'(<p class="guide-meta">[^<]*?)Updated <time datetime="[^"]*">[^<]*</time>',lambda mm:mm.group(1)+f'Updated <time datetime="{date}">{date_h(date)}</time>',s,count=1)
        if f'datetime="{date}"' not in s:
            s=s.replace('<p class="guide-meta">',f'<p class="guide-meta">Updated <time datetime="{date}">{date_h(date)}</time> · ',1)
    else:
        h=s.find('</h1>',m)
        if h>0:
            s=s[:h+5]+f'<p class="guide-meta">Updated <time datetime="{date}">{date_h(date)}</time></p>'+s[h+5:]
    open(p,'w').write(s);return True

def bump_lastmod(urls,date='2026-11-04'):
    sm=open('sitemap.xml').read();n=0
    for u in urls:
        r=re.compile(r'(<loc>'+re.escape(u)+r'</loc>\s*<lastmod>)[^<]*(</lastmod>)')
        sm,k=r.subn(r'\g<1>'+date+r'\g<2>',sm);n+=k
    open('sitemap.xml','w').write(sm);return n

def add_to_sitemap(urls,date='2026-11-04'):
    sm=open('sitemap.xml').read();n=0
    for u in urls:
        if f'<loc>{u}</loc>' in sm: continue
        sm=sm.replace('</urlset>',f'<url><loc>{u}</loc><lastmod>{date}</lastmod></url>\n</urlset>');n+=1
    open('sitemap.xml','w').write(sm);return n
