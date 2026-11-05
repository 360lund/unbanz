import re,sys,html
sys.path.insert(0,'scripts/nov05');import pages8
P={p['slug']:p for p in pages8.PAGES}
def add(f,key,sec):
    h=open(f).read()
    if key in h: return
    for a in ['<h2 id="related"','<section class="faq-section"','<nav class="related-services','<footer']:
        if a in h: h=h.replace(a,sec+a,1);break
    open(f,'w').write(h);print('linked',f)
def ul(sl): return '<ul>'+''.join(f'<li><a href="/{s}/">{html.escape(P[s]["crumb"])}</a></li>' for s in sl)+'</ul>'
allS=list(P)
ag=[s for s in allS if s.startswith('agency-client')]+['client-fired-agency-removed-access','former-employee-still-admin']
dirs=['youtube-channel-terminated-appeal-links-directory','x-suspended-account-appeal-links-directory','meta-appeal-links-saudi-arabia','meta-appeal-links-qatar','meta-appeal-links-kuwait']
W=lambda t,sl:f'<section class="service-editorial container"><article><h2>{t}</h2>{ul(sl)}</article></section>'
add('site-map/index.html','agency-client-account-banned-usa',W('New November 2026',allS))
add('guides/index.html','agency-client-account-banned-usa',W('New November 2026',allS))
add('for-agencies-banned-client-accounts/index.html','agency-client-account-banned-usa',W('By country, and access disputes',ag))
add('questions-agencies-ask-about-banned-client-accounts/index.html','former-employee-still-admin',W('More agency questions',ag))
add('meta-appeal-links-and-forms-directory/index.html','meta-appeal-links-qatar',W('More directories',dirs))
add('meta-appeal-links-uae/index.html','meta-appeal-links-qatar',W('Nearby countries',dirs[2:]))
for c in ['usa','uk','canada','australia','uae']: add(f'white-label-agency-{c}/index.html',f'agency-client-account-banned-{c}',W('For agencies here',[f'agency-client-account-banned-{c}']))
s=open('sitemap.xml').read();L1=open('llms.txt').read();L2=open('llms-full.txt').read()
for k,p in P.items():
    u=f'https://unbanz.com/{k}/'
    if u not in s: s=s.replace('</urlset>',f'<url><loc>{u}</loc><lastmod>2026-11-05</lastmod></url>\n</urlset>')
    line=f'- [{p["crumb"]}]({u}): {p["desc"]}\n'
    if u not in L1: L1+=line
    if u not in L2: L2+=line
note='\n## Freshness, 5 November 2026\nThe top 40 pages by visits from AI assistants got an "Updated November 2026" section with current appeal-flow notes, a new FAQ and a what-to-send checklist.\n'
if 'Freshness, 5 November 2026' not in L1: L1+=note;L2+=note
for f,v in [('sitemap.xml',s),('llms.txt',L1),('llms-full.txt',L2)]: open(f,'w').write(v)
