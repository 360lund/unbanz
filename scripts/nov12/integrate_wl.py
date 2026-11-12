import re,json,glob,html,os
os.chdir('/workspace/site')
NEW=['white-label-recovery-services-by-platform','white-label-bulk-recovery-cases-for-agencies','white-label-private-label-case-reports','white-label-tiktok-account-recovery','white-label-youtube-channel-recovery','white-label-whatsapp-number-unban','white-label-recovery-for-account-recovery-resellers','white-label-recovery-for-creator-networks-and-mcns','white-label-recovery-for-it-and-cybersecurity-providers']
MK=['white-label-agency-australia','white-label-agency-uae','white-label-agency-taiwan','white-label-agency-hong-kong','zh-tw/white-label-agency','zh-hk/white-label-agency']
def title(s): return html.unescape(re.search(r'<title>(.*?)</title>',open(s+'/index.html').read()).group(1)).split(' | ')[0]
def li(ss): return '<ul>'+''.join(f'<li><a href="/{s}/">{html.escape(title(s))}</a></li>' for s in ss)+'</ul>'
def touch(t):
    t=re.sub(r'"dateModified": ?"[0-9-]+"','"dateModified": "2026-11-12"',t)
    return re.sub(r'<meta property="article:modified_time" content="[^"]*">','<meta property="article:modified_time" content="2026-11-12">',t)
changed=set()
def save(f,t,o):
    if t!=o: open(f,'w').write(touch(t)); changed.add(f)
# 1 hub
f='white-label-agency/index.html'; t=o=open(f).read()
if 'id="nov12-partners"' not in t:
    blk=('<h2 id="nov12-partners">Partner program: volume, reports and more platforms</h2><p>Partners who send cases regularly or in batches get volume pricing, agreed in writing before the work starts, a dedicated contact at <a href="mailto:team@unbanz.com">team@unbanz.com</a>, and private-label updates with no Unbanz name on them.</p>'
         +li(NEW)+'<h2 id="nov12-markets">By market</h2>'+li(MK))
    t=t.replace('<h2 id="about-unbanz">',blk+'<h2 id="about-unbanz">',1)
save(f,t,o)
# 2 fixed-fees page: volume pricing wording
f='white-label-recovery-fixed-fees-for-agencies/index.html'; t=o=open(f).read()
for x,y in [('Any partner terms are agreed in writing before the first case; we do not publish partner discounts.','Partners who send cases regularly or in batches get volume pricing, agreed in writing before the first case; we do not publish those numbers.'),
            ('No invented discounts.','Volume pricing for regular partners.'),('No invented discounts','Volume pricing for regular partners'),
            ('We do not advertise discounts; ask, and the answer will be in writing.','Volume pricing for partners who send cases regularly or in batches, in writing.'),
            ('Do agencies get a discount?','Do agencies get volume pricing?'),
            ('We do not publish partner discounts. Any partner terms are agreed in writing before work starts.','Yes. Partners who send cases regularly or in batches get volume pricing, agreed in writing before work starts. We do not publish the numbers.')]:
    t=t.replace(x,y)
if 'id="nov12-partners"' not in t: t=t.replace('<h2 id="about-unbanz">','<h2 id="nov12-partners">More for partners</h2>'+li(NEW[:3])+'<h2 id="about-unbanz">',1)
save(f,t,o)
assert 'discount' not in open(f).read().lower(), 'discount left'
# 3 existing WL platform/audience pages: partner links
REL='<nav class="related-services container" aria-label="White label partner program" data-nov12="wl">'+''.join(f'<a href="/{s}/">{html.escape(l)}</a>' for s,l in [('white-label-recovery-services-by-platform','All white label services'),('white-label-bulk-recovery-cases-for-agencies','Sending cases in bulk'),('white-label-private-label-case-reports','Private-label reports'),('white-label-tiktok-account-recovery','White label TikTok'),('white-label-youtube-channel-recovery','White label YouTube'),('white-label-whatsapp-number-unban','White label WhatsApp')])+'</nav>'
targets=[d.rstrip('/') for d in glob.glob('white-label-*/')]+['become-a-white-label-recovery-partner','how-white-label-account-recovery-works','what-your-client-sees-white-label-recovery','agency-pricing-models-reselling-recovery','how-to-price-account-recovery-for-agencies','agency-intake-form-checklist-account-recovery','how-to-choose-a-white-label-recovery-partner','for-agencies-banned-client-accounts','agency-ad-account-recovery']
for s in targets:
    f=s+'/index.html'
    if not os.path.exists(f): continue
    t=o=open(f).read()
    if 'data-nov12="wl"' in t or '<meta name="robots" content="noindex' in t: continue
    t=t.replace('</main>',REL+'</main>',1); save(f,t,o)
# 4 single-client platform pages: plain agency link (no pricing talk)
for s,u,l in [('tiktok-account-help','white-label-tiktok-account-recovery','white label TikTok recovery'),('youtube-account-help','white-label-youtube-channel-recovery','white label YouTube channel recovery'),('whatsapp-banned-number','white-label-whatsapp-number-unban','white label WhatsApp help')]:
    f=s+'/index.html'; t=o=open(f).read()
    if 'data-nov12="wl"' not in t:
        t=t.replace('</main>',f'<nav class="related-services container" aria-label="For agencies" data-nov12="wl"><a href="/{u}/">Agency? See {l}</a><a href="/white-label-recovery-services-by-platform/">All white label services</a></nav></main>',1)
    save(f,t,o)
# 5 services page
f='services/index.html'; t=o=open(f).read()
if 'data-nov12="wl"' not in t:
    t=t.replace('<section class="recovery-intro container"><p class="eyebrow">WHAT WE FIX','<section class="service-editorial container" data-nov12="wl"><article><h2><a href="/white-label-agency/">White label for agencies</a></h2><p>Resell every service above under your own brand. Your client only deals with you. <a href="/white-label-recovery-services-by-platform/">All white label services</a>.</p></article></section><section class="recovery-intro container"><p class="eyebrow">WHAT WE FIX',1)
save(f,t,o)
# 6 sitewide EN footer link
ADD='<a href="/white-label-agency/">White label for agencies</a>'
n=0
for f in glob.glob('**/index.html',recursive=True):
    if f.startswith(('fr/','es/','pt-br/','nl/','de/','ar/','it/','tr/','zh-tw/','zh-hk/','users/','node_modules','scripts/')): continue
    t=open(f).read()
    m=re.search(r'<div class="footer-links">(.*?)</div>',t,re.S)
    if not m or 'href="/white-label-agency/">White label' in m.group(0): continue
    anchor='<a href="/meta-ad-account-help/">Ad account help</a>'
    for anc in [anchor,'<a href="/guides/">Guides</a>','<a href="/contact/">Contact</a>']:
        if anc in m.group(0):
            seg=m.group(0).replace(anc,anc+ADD,1); t=t.replace(m.group(0),seg,1); open(f,'w').write(t); n+=1; break
print('footer',n)
# 7 site-map page
f='site-map/index.html'; t=o=open(f).read()
if 'data-nov12="wl"' not in t:
    i=t.find('<h2>New 6 November 2026</h2>')
    sec='<h2 data-nov12="wl">White label partner pages (12 November 2026)</h2>'+li(NEW+MK)
    t=t[:i]+sec+t[i:] if i>0 else t.replace('</main>',sec+'</main>',1)
save(f,t,o)
# 8 redirects
v=json.load(open('vercel.json'))
have={r['source'] for r in v['redirects']}
for s in ['/white-label','/white-label/','/partners','/partners/','/partner-program','/partner-program/']:
    if s not in have: v['redirects'].append({'source':s,'destination':'/white-label-agency/','permanent':True})
json.dump(v,open('vercel.json','w'),indent=2,ensure_ascii=False); open('vercel.json','a').write('\n')
print('changed',len(changed))
