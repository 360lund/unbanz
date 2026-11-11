import sys,re,html; sys.path.insert(0,'/workspace/site/scripts/nov11')
import gen2,b13 as b12
from gen import ul,a
SITE='/workspace/site'
for p in b12.PAGES: gen2.build(dict(p))
S=[p['slug'] for p in b12.PAGES]
def t_of(s): return html.unescape(re.search(r'<title>(.*?)</title>',open(f'{SITE}/{s}/index.html').read()).group(1)).split(' | ')[0]
def li(ss): return ul([a('/'+s+'/',html.escape(t_of(s))) for s in ss])
BMS=[s for s in S if 'portfolio' in s or 'business' in s or 'pixel' in s or 'partner' in s]
HUBS={'business-and-creator-account-help':('More business guides (new)',S),'guides':('More business and agency guides (new)',S),
 'white-label-agency':('Client communication',['what-to-tell-a-client-when-their-meta-account-is-restricted']),
 'facebook-page-recovery':('Hacked Page running ads',['facebook-page-hacked-running-scam-ads']),
 'meta-business-portfolio-restricted-help':('Gulf business verification',['meta-business-verification-uae-trade-licence','meta-business-verification-saudi-commercial-registration'])}
n=0
for h,(title,ss) in HUBS.items():
    f=f'{SITE}/{h}/index.html'; t=open(f).read()
    t=re.sub(r'<section class="service-editorial container" data-nov11="r5b">.*?</section>','',t,flags=re.S)
    sec=f'<section class="service-editorial container" data-nov11="r5b"><article><h2>{title}</h2>{li(ss)}</article></section>'
    if '<h2 id="about-unbanz">' in t and h!='guides':
        t=t.replace('<h2 id="about-unbanz">',f'<h2 id="r5b-guides">{title}</h2>{li(ss)}<h2 id="about-unbanz">',1) if 'id="r5b-guides"' not in t else t
    else:
        i=t.find('<section class="service-editorial container" data-nov11="r2">')
        if i<0: i=t.find('</main>')
        t=t[:i]+sec+t[i:]
    open(f,'w').write(t); n+=1
open('/workspace/aeo_nov11/built13.txt','w').write('\n'.join(S)+'\n'); print('built',len(S),'hubs',n)
