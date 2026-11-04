import re,glob,os
os.chdir('/workspace/site')
NT=['australia','austria','belgium','denmark','finland','germany','hong-kong','india','ireland','israel','italy','kuwait','luxembourg','new-zealand','norway','pakistan','qatar','saudi-arabia','singapore','south-korea','spain','sweden','switzerland','uae','gulf','japan','taiwan','brazil','poland','portugal','malta','cyprus','oman','bahrain','monaco','iceland','estonia','slovenia','czech-republic','liechtenstein']
T=['usa','us','uk','canada','netherlands','france','eu']
sm=open('sitemap.xml').read(); done=[]
for d in sorted(glob.glob('*/')):
    s='-'+d.strip('/')+'-'
    if d.startswith(('fr/','nl/','es/','pt-br/')): continue
    if not any('-'+c+'-' in s for c in NT): continue
    if any('-'+c+'-' in s for c in T): continue
    f=d+'index.html'
    if not os.path.exists(f): continue
    h=open(f).read()
    h2=h.replace('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex,follow">',1)
    if h2!=h: open(f,'w').write(h2); done.append(d)
    sm=re.sub(r'<url><loc>https://unbanz.com/%s</loc>.*?</url>\n?'%re.escape(d),'',sm)
open('sitemap.xml','w').write(sm)
open('/tmp/noindexed.txt','w').write('\n'.join(done))
print(len(done),'noindexed; sitemap',sm.count('<loc>'))
