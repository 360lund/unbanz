import re,sys,os
R='/workspace/site'
en=[l.strip() for l in open('/tmp/agency_en_slugs.txt')]
n=0
for s in en+['white-label-agency']:
    p=os.path.join(R,s,'index.html'); h=open(p).read()
    h2=re.sub(r'(<meta (?:property="og:image:alt"|name="twitter:image:alt") content="Unbanz) — ',r'\1: ',h)
    if h2!=h: open(p,'w').write(h2); n+=1
print('fixed',n)
