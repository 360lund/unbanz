import re,glob,os
os.chdir('/workspace/site')
M={'guides/ad-account-circumventing-systems':'ad-account-disabled-circumventing-systems-help',
'guides/ad-account-unacceptable-business-practices':'ad-account-disabled-unacceptable-business-practices-help',
'guides/instagram-account-disabled-for-no-reason':'instagram-disabled-no-reason-given',
'white-label-vs-in-house-account-recovery':'white-label-vs-referral-vs-in-house-recovery'}
sm=open('sitemap.xml').read()
for s,p in M.items():
    f=s+'/index.html'; h=open(f).read()
    h=h.replace(f'<link rel="canonical" href="https://unbanz.com/{s}/">',f'<link rel="canonical" href="https://unbanz.com/{p}/">')
    h=re.sub(r'<link rel="alternate" hreflang="[^"]+" href="https://unbanz.com/%s/">'%re.escape(s),'',h)
    open(f,'w').write(h)
    sm=re.sub(r'<url><loc>https://unbanz.com/%s/</loc>.*?</url>\n?'%re.escape(s),'',sm)
open('sitemap.xml','w').write(sm)
n=0
for f in glob.glob('**/index.html',recursive=True):
    if f.startswith('scripts/'):continue
    h=open(f).read();o=h
    for s,p in M.items():
        if f==p+'/index.html': continue
        h=h.replace(f'href="/{s}/"',f'href="/{p}/"')
    if h!=o: open(f,'w').write(h); n+=1
print('relinked',n)
