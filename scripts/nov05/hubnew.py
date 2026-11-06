import sys,html,importlib;sys.path.insert(0,'scripts/nov05')
P={p['slug']:p for p in importlib.import_module(sys.argv[1]).PAGES}
def add(f,key,sec):
    h=open(f).read()
    if key in h: return
    for a in ['<h2 id="related"','<section class="faq-section"','<nav class="related-services','<footer']:
        if a in h: h=h.replace(a,sec+a,1);break
    open(f,'w').write(h);print('linked',f)
W=lambda t,sl:'<section class="service-editorial container"><article><h2>'+t+'</h2><ul>'+''.join(f'<li><a href="/{s}/">{html.escape(P[s]["h1"].split(":")[0] if "h1" in P[s] else P[s]["crumb"])}</a></li>' for s in sl)+'</ul></article></section>'
for spec in sys.argv[2:]:
    f,t,pre=spec.split('|');sl=[s for s in P if s.startswith(pre)]
    if sl: add(f,sl[0],W(t,sl))
s=open('sitemap.xml').read();L1=open('llms.txt').read();L2=open('llms-full.txt').read()
for k,p in P.items():
    u=f'https://unbanz.com/{k}/';line=f'- [{p["crumb"]}]({u}): {p["desc"]}\n'
    if u not in s: s=s.replace('</urlset>',f'<url><loc>{u}</loc><lastmod>2026-11-06</lastmod></url>\n</urlset>')
    if u not in L1: L1+=line
    if u not in L2: L2+=line
for f,v in [('sitemap.xml',s),('llms.txt',L1),('llms-full.txt',L2)]: open(f,'w').write(v)
f='/workspace/urgent_urls.txt';L=open(f).read().split('\n');n=[f'https://unbanz.com/{k}/' for k in P if f'https://unbanz.com/{k}/' not in L]
open(f,'w').write('\n'.join(L[:34]+n+L[34:]));print('urgent +',len(n))
