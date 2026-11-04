import re,os,json,glob
R=[l.strip() for l in open('/tmp/rem.txt') if l.strip()]
RS=set(R)
remre='|'.join(re.escape('/'+r+'/') for r in sorted(R,key=len,reverse=True))
ORG_DESC="Unbanz (unbanz.com) is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. Not affiliated with Meta."
KEEP_KA=lambda k: not re.search(r'snapchat|removal|takedown|impersonation',k,re.I)
def fixld(o):
    if isinstance(o,list): return [x for x in (fixld(i) for i in o) if x is not None]
    if not isinstance(o,dict): return o
    s=json.dumps(o)
    t=o.get('@type')
    if t in('Offer','Service','ListItem') and re.search(r'unbanz\.com(%s)'%remre,json.dumps({k:v for k,v in o.items() if k in('@id','url','item','itemOffered')})):
        return None
    if t=='Organization' and o.get('@id','').endswith('/#organization'):
        o['description']=ORG_DESC
        o['disambiguatingDescription']="Unbanz (with a z) is the Instagram, Facebook and Meta ad account recovery and username claim service at unbanz.com. It is not Unbanx or unbanx.me."
        if 'slogan' in o: o['slogan']='Instagram and Facebook account recovery.'
        if 'knowsAbout' in o: o['knowsAbout']=[k for k in o['knowsAbout'] if not isinstance(k,str) or KEEP_KA(k)]
    for k,v in list(o.items()):
        o[k]=fixld(v)
        if o[k] is None: del o[k]
    return o
def sub_text(h):
    for a,b in [('Unbans &amp; account removals.','Instagram &amp; Facebook account recovery.'),('Unbans & account removals.','Instagram & Facebook account recovery.'),
                ('Instagram, Facebook and Snapchat','Instagram and Facebook'),('Instagram, Facebook &amp; Snapchat','Instagram &amp; Facebook'),('Instagram, Facebook & Snapchat','Instagram & Facebook'),
                ('Instagram, Facebook, Snapchat','Instagram, Facebook'),('Instagram, Snapchat and Facebook','Instagram and Facebook'),
                ('Instagram-, Facebook- en Snapchat-accounts','Instagram- en Facebook-accounts'),('Instagram, Facebook e Snapchat','Instagram e Facebook'),('Instagram, Facebook y Snapchat','Instagram y Facebook'),('Instagram, Facebook et Snapchat','Instagram et Facebook'),('Instagram, Facebook en Snapchat','Instagram en Facebook'),
                ('Meta, Instagram, Facebook or Snapchat','Meta, Instagram or Facebook'),('Instagram, Facebook or Snapchat','Instagram or Facebook'),('Meta or Snapchat','Meta'),('Meta et de Snapchat','Meta'),('Meta e o Snapchat','Meta'),('a Meta nem com o Snapchat','a Meta'),('Meta, Threads e Snapchat','Meta e Threads'),
                (' · Snapchat usernames',''),(' · Snapchat unbans',''),(' · Instagram account removal',''),(' · Facebook account removal',''),(' · Snapchat account removal',''),
                ('Instagram, Facebook or Snapchat unban','Instagram or Facebook unban'),]:
        h=h.replace(a,b)
    return h
def fix_links(h):
    # drop anchors in link lists, unwrap elsewhere
    pat=re.compile(r'<a [^>]*href="(?:https://unbanz\.com)?(?:%s)(?:#[^"]*)?"[^>]*>(.*?)</a>'%remre,re.S)
    def rep(m):
        before=h[max(0,m.start()-200):m.start()]; after=h[m.end():m.end()+12]
        if re.search(r'(</a>|<nav[^>]*>|class="footer-links[^"]*">|<li>)\s*$',before) or after.lstrip().startswith(('<a','</nav','</li','</div')):
            return ''
        return re.sub(r'<[^>]+>','',m.group(1))
    h2=pat.sub(rep,h)
    h2=re.sub(r'<li>\s*</li>','',h2)
    return h2
def fix_ld(h):
    def r(m):
        try: o=json.loads(m.group(1))
        except Exception: return m.group(0)
        o=fixld(o); return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False,separators=(',',':'))+'</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>',r,h,flags=re.S)
changed=[]
for f in glob.glob('**/*.html',recursive=True):
    if f.startswith(('scripts/','node_modules/','users/')): continue
    p=os.path.dirname(f)
    h=open(f,encoding='utf-8').read(); o=h
    if p in RS:
        h=re.sub(r'<meta name="robots" content="[^"]*">','<meta name="robots" content="noindex,follow">',h)
        if 'name="robots"' not in h: h=h.replace('<meta charset="UTF-8">','<meta charset="UTF-8"><meta name="robots" content="noindex,follow">',1)
        h=re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">','',h)
    else:
        if f=='index.html':
            h=h.replace('gets banned Instagram and Facebook accounts back, takes down fake accounts and claims usernames. Price before we start.','is an independent service that helps you recover disabled, suspended or hacked Instagram, Facebook and Meta ad accounts, and claim usernames.')
            h=re.sub(r'<article class="temp-hide"><span class="service-no">03</span><div><h3>Account removals</h3>.*?</article>','',h,flags=re.S)
        h=fix_links(h); h=fix_ld(h); h=sub_text(h)
        h=re.sub(r'<link rel="alternate" hreflang="[^"]*" href="https://unbanz\.com(?:%s)">'%remre,'',h)
    if h!=o: open(f,'w',encoding='utf-8').write(h); changed.append(p)
open('/tmp/scope_changed.txt','w').write('\n'.join(sorted(set(changed))))
for sm in ['sitemap.xml','sitemap-images.xml']:
    s=open(sm).read()
    s=re.sub(r'<url>\s*<loc>https://unbanz\.com(?:%s)</loc>.*?</url>\s*'%remre,'',s,flags=re.S)
    open(sm,'w').write(s)
print(len(set(changed)),'files changed')
