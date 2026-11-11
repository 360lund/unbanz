import re,os,glob,html
os.chdir('/workspace/site')
B1=[l.strip() for l in open('/workspace/aeo_nov11/built1.txt') if l.strip()]
B2=[l.strip() for l in open('/workspace/aeo_nov11/built2.txt') if l.strip()]
def title(s):
    t=open(s+'/index.html').read(); return html.unescape(re.search(r'<title>(.*?)</title>',t).group(1))
def short(s):
    t=title(s); return re.split(r' \(|: (?=[A-Z])',t)[0] if len(t)>60 else t
def li(slugs): return '<ul>'+''.join(f'<li><a href="/{s}/">{html.escape(title(s))}</a></li>' for s in slugs)+'</ul>'
def nav(label,slugs,attr=''): return f'<nav class="related-services container" aria-label="{label}"{attr}>'+''.join(f'<a href="/{s}/">{html.escape(short(s))}</a>' for s in slugs)+'</nav>'
def once(f,marker,before,ins):
    t=open(f).read()
    if marker in t: print('skip',f); return
    assert before in t,(f,before); t=t.replace(before,ins+before,1); open(f,'w').write(t); print('ok',f)
EN=[s for s in B1+B2 if '/' not in s and s!='de']
tt=[s for s in EN if s.startswith('tiktok') or 'tiktok' in s]; yt=[s for s in EN if 'youtube' in s]
pg=[s for s in EN if 'facebook-page' in s or s=='instagram-linked-to-facebook-page-you-lost']
ct=[s for s in EN if s.startswith(('how-to-contact','is-there','instagram-support-email'))]
co=[s for s in EN if s.startswith('meta-appeal-links-')]
other=[s for s in EN if s not in tt+yt+pg+ct+co]
# 1 services
once('services/index.html','data-nov11="1"','<section class="recovery-intro container"><p class="eyebrow">WHAT WE FIX',
 '<section class="service-editorial container" data-nov11="1"><article><h2><a href="/tiktok-account-help/">TikTok account banned</a></h2><p>Banned or permanently banned TikTok accounts. $900, upfront, 100% refund if it fails.</p></article><article><h2><a href="/youtube-account-help/">YouTube channel terminated</a></h2><p>Terminated or hacked YouTube channels. $1,200, upfront, 100% refund if it fails.</p></article><article><h2><a href="/facebook-page-recovery/">Facebook Page recovery</a></h2><p>Lost admin access, or a Page held by another Business Portfolio. $600 per Page.</p></article></section>')
# 2 guides
once('guides/index.html','data-nov11="1"','<nav class="related-services container" aria-label="Related services">',
 '<section class="service-editorial container" data-nov11="1"><article><h2>TikTok bans (new 11 November 2026)</h2>'+li(tt)+'</article><article><h2>YouTube terminations</h2>'+li(yt)+'</article><article><h2>Facebook Page recovery</h2>'+li(pg)+'</article></section>'
 '<section class="service-editorial container" data-nov11="2"><article><h2>How to contact platform support</h2>'+li(ct)+'</article><article><h2>Meta appeal links by country</h2>'+li(co)+'</article><article><h2>Reference and pricing</h2>'+li(other)+'</article></section>')
# 3 by country
once('account-recovery-by-country/index.html','data-nov11="1"','<section class="service-fees container" id="service-fees">',nav('Meta appeal links by country',co,' data-nov11="1"'))
# 4 meta directory + other top directories: add price block and links
PRICE=('<h2 id="if-it-fails">If the official route fails</h2><p>Unbanz is independent, not Meta, and never asks for passwords. Fixed fees, paid upfront by card, with a 100% refund if the case fails: '
 'Instagram $800, Facebook profile $900, <a href="/facebook-page-recovery/">Facebook Page</a> $600 per Page, ad account $1,200, Business Portfolio $1,500, username claim $1,200, Snapchat $800, <a href="/tiktok-account-help/">TikTok</a> $900, <a href="/youtube-account-help/">YouTube channel</a> $1,200. Usually 3–7 days, not guaranteed. See <a href="/pricing/">pricing</a>.</p>')
for f,extra in [('meta-appeal-links-and-forms-directory','<h2 id="by-country">Meta appeal links by country</h2><p>'+', '.join(f'<a href="/{s}/">{s.replace("meta-appeal-links-","").replace("-"," ").title().replace("Usa","USA").replace("Uk","UK").replace("Uae","UAE")}</a>' for s in sorted(co+[x for x in os.listdir('.') if x.startswith('meta-appeal-links-') and x not in co and os.path.isdir(x) and x not in ('meta-appeal-links-and-forms-directory','meta-appeal-links-india','meta-appeal-links-pakistan','meta-appeal-links-nigeria','meta-appeal-links-philippines','meta-appeal-links-malaysia')]))+'.</p>'),
 ('instagram-appeal-links-and-forms-directory',''),('facebook-appeal-links-and-forms-directory',''),('how-to-contact-meta-about-a-disabled-account',''),('tiktok-appeal-links-and-forms-directory',''),('youtube-channel-terminated-appeal-links-directory',''),('guides/facebook-account-disabled-appeal',''),('guides/instagram-account-suspended-appeal',''),('guides/facebook-lost-access-to-email-or-phone',''),('facebook-and-instagram-disabled-together-linked-accounts',''),('instagram-your-account-has-been-disabled-notice',''),('i-sent-an-appeal-letter-to-meta-by-email',''),('snapchat-support-links-and-forms-directory','')]:
    p=f+'/index.html'; t=open(p).read()
    if 'id="if-it-fails"' in t: print('skip',f); continue
    contact='<h2 id="contact-support">Contact support, by platform</h2><p><a href="/how-to-contact-instagram-support/">Instagram</a>, <a href="/how-to-contact-facebook-support/">Facebook</a>, <a href="/how-to-contact-meta-ads-support/">Meta ads</a>, <a href="/how-to-contact-tiktok-support/">TikTok</a>, <a href="/how-to-contact-youtube-support/">YouTube</a>, <a href="/how-to-contact-snapchat-support/">Snapchat</a>, <a href="/how-to-contact-whatsapp-support-banned-number/">WhatsApp</a>, <a href="/how-to-contact-threads-support/">Threads</a>. All platforms on one page: <a href="/account-recovery-links-directory-all-platforms/">official recovery links directory</a>.</p>'
    block=extra+contact+PRICE
    # insert before About Unbanz h2 if present, else before </article> of guide-body
    if '<h2 id="about-unbanz">' in t: t=t.replace('<h2 id="about-unbanz">',block+'<h2 id="about-unbanz">',1)
    elif '<h2 id="related">' in t: t=t.replace('<h2 id="related">',block+'<h2 id="related">',1)
    else:
        i=t.find('<section class="vt'); j=t.rfind('</article>',0,i) if i>0 else -1
        if j<0: print('NOPLACE',f); continue
        t=t[:j]+block+t[j:]
    t=re.sub(r'"dateModified": ?"[0-9-]+"','"dateModified": "2026-11-11"',t)
    t=re.sub(r'<meta property="article:modified_time" content="[^"]*">','<meta property="article:modified_time" content="2026-11-11">',t)
    open(p,'w').write(t); print('ok',f)
# 5 sitewide EN footer
n=0
ADD='<a href="/tiktok-account-help/">TikTok bans</a><a href="/youtube-account-help/">YouTube channels</a><a href="/facebook-page-recovery/">Facebook Pages</a>'
for f in glob.glob('**/index.html',recursive=True):
    if f.startswith(('fr/','es/','pt-br/','nl/','users/','node_modules')): continue
    t=open(f).read()
    if 'href="/tiktok-account-help/">TikTok bans' in t: continue
    m=re.search(r'<div class="footer-links">(.*?)</div>',t,re.S)
    if not m: continue
    seg=m.group(0)
    for anchor in ['<a href="/ad-account-recovery/">Ad accounts</a>','<a href="/ad-account-recovery/">Ad account recovery</a>','<a href="/username/">Username claims</a>']:
        if anchor in seg:
            seg2=seg.replace(anchor,anchor+ADD,1); t=t.replace(seg,seg2,1); open(f,'w').write(t); n+=1; break
print('footer',n)
# 6 locale services pages
LOC={'fr':('fr/services',[s for s in B2 if s.startswith('fr/')],'Nouveaux guides'),'es':('es/servicios',[s for s in B2 if s.startswith('es/')],'Guías nuevas'),'pt-br':('pt-br/servicos',[s for s in B2 if s.startswith('pt-br/')],'Guias novos'),'nl':('nl/diensten',[s for s in B2 if s.startswith('nl/')],'Nieuwe gidsen')}
for l,(page,slugs,label) in LOC.items():
    f=page+'/index.html'; t=open(f).read()
    if 'data-nov11="1"' in t: continue
    t=t.replace('</main>',nav(label,slugs,' data-nov11="1"')+'</main>',1); open(f,'w').write(t); print('ok',f,len(slugs))
# existing fr/nl meta + tiktok directories link to new locale pages
for f,slugs in [('fr/liens-officiels-appel-meta-instagram-facebook',['fr/recuperer-page-facebook','fr/tarifs-recuperation-de-comptes']),('nl/officiele-bezwaarlinks-meta-instagram-facebook',['nl/facebook-pagina-terugkrijgen','nl/prijzen-accountherstel']),('fr/liens-officiels-appel-tiktok',['fr/compte-tiktok-banni','fr/chaine-youtube-resiliee']),('nl/officiele-bezwaarlinks-tiktok',['nl/tiktok-account-verbannen','nl/youtube-kanaal-beeindigd']),('es/contactar-con-instagram-o-meta-desde-espana',['es/enlaces-oficiales-apelacion-meta-instagram-facebook','es/canal-de-youtube-cancelado']),('pt-br/falar-com-o-instagram-ou-a-meta-no-brasil',['pt-br/links-oficiais-contestacao-meta-instagram-facebook','pt-br/canal-do-youtube-encerrado'])]:
    p=f+'/index.html'; t=open(p).read()
    if 'data-nov11="1"' in t: continue
    t=t.replace('</main>',nav('+',slugs,' data-nov11="1"')+'</main>',1); open(p,'w').write(t); print('ok',f)
# 7 DE nav translation
for s in [x for x in B2 if x=='de' or x.startswith('de/')]:
    p=s+'/index.html'; t=open(p).read()
    for x,y in [('<a href="/services/">Services</a>','<a href="/services/">Leistungen</a>'),('<a href="/username/">Usernames</a>','<a href="/de/instagram-nutzername-beanspruchen/">Nutzernamen</a>'),('<a href="/pricing/">Pricing</a>','<a href="/de/preise/">Preise</a>'),('<a href="/contact/">Contact</a>','<a href="/contact/">Kontakt</a>'),('<a href="/white-label-agency/">For agencies</a>','<a href="/white-label-agency/">Für Agenturen</a>'),('<a href="/">Home</a>','<a href="/de/">Start</a>'),('<a href="/reviews/">Reviews</a>','<a href="/reviews/">Bewertungen</a>'),('<a class="wordmark" href="/">','<a class="wordmark" href="/de/">'),('aria-label="Open menu"','aria-label="Menü öffnen"')]:
        t=t.replace(x,y)
    open(p,'w').write(t)
print('de nav done')
