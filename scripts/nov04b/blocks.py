import re,glob,os,json
R=set(l.strip() for l in open('/tmp/rem.txt') if l.strip())
BAD=re.compile(r'snapchat|account removals?|takedowns?|taken down|fake account removal|removed instead|pretending to be you|report a fake|impersonation (?:account|report)|scam account|harass',re.I)
def blk(tag,h):
    def r(m):
        t=m.group(0)
        if '<'+tag in t[1:] or len(re.sub(r'<[^>]+>','',t))>700: return t
        return '' if BAD.search(re.sub(r'<[^>]+>',' ',t)) or re.search(r'>Read the guide ↗︎</'+tag,t) or re.search(r'>See details ↗︎</div',t) and 'href' not in t.split('service-row-actions')[-1][:200] else t
    return re.sub(r'<%s(?:\s[^>]*)?>.*?</%s>'%(tag,tag),r,h,flags=re.S)
def ldq(o):
    if isinstance(o,list): return [x for x in (ldq(i) for i in o) if x is not None]
    if isinstance(o,dict):
        if o.get('@type')=='Question' and BAD.search(json.dumps(o,ensure_ascii=False)): return None
        return {k:ldq(v) for k,v in o.items()}
    return o
def fixld(h):
    def r(m):
        try:o=json.loads(m.group(1))
        except Exception:return m.group(0)
        return '<script type="application/ld+json">'+json.dumps(ldq(o),ensure_ascii=False,separators=(',',':'))+'</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>',r,h,flags=re.S)
ch=[]
for f in glob.glob('**/index.html',recursive=True):
    p=os.path.dirname(f) or '.'
    if p in R or f.startswith(('scripts','users')): continue
    if re.search(r'sextortion|memorialized',p): continue
    h=open(f).read();o=h
    for t in ['article','details','li']: h=blk(t,h)
    h=fixld(h)
    if h!=o: open(f,'w').write(h); ch.append(p)
print(len(ch)); open('/tmp/blocks_changed.txt','w').write('\n'.join(ch))
