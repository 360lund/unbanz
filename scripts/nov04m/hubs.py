import sys,re;sys.path.insert(0,'scripts/nov04l');from lib import add_section,table,bump_lastmod
s=open('guides/index.html').read()
cards=[('/unbanz-vs-respect-network/','Unbanz vs Respect Network','How the two services differ on scope, payment and what each says publicly, checked in 2026.'),
('/unbanz-vs-hacked-com/','Unbanz vs Hacked.com','A side-by-side look at services, listed prices and contact routes, from each site’s own pages.'),
('/unbanz-vs-rescuno/','Unbanz vs Rescuno','Who runs each service, what they list and how to contact them, checked in 2026.')]
if 'href="/unbanz-vs-rescuno/"' not in s:
    i=s.find('<section class="guide-cards container">');j=s.find('</section>',i)
    s=s[:j]+''.join(f'<article><h2><a href="{u}">{t}</a></h2><p>{d}</p><a href="{u}">Read the comparison ↗︎</a></article>' for u,t,d in cards)+s[j:]
    open('guides/index.html','w').write(s)
blk='<h2 id="compared-2026">Ways people try to get a username in 2026</h2><p>There are a handful of routes. Here is a plain comparison, so you can pick the one that fits.</p>'+table(['Route','Who it suits','Cost','Things to know'],[
['Instagram’s own trademark report','Owners of a registered trademark that exactly matches the name','Free','Instagram decides. A trademark helps but does not give an automatic right to the name.'],
['A trademark lawyer','Brands with a registered mark and a clear confusion issue','Hourly or agreed fee','Useful when the current holder is using the name in a confusing way.'],
['Contacting the holder','Names held by a person who is still reachable','Varies','Never hand over money before you control the name. Buying and selling usernames is against Instagram’s terms.'],
['Username marketplaces and forums','Not recommended','Varies','Against Instagram’s terms, and a common source of scams and later reclaims.'],
['Unbanz','People and brands who want it handled for them through official routes','Quoted per request','Your password stays with you. Terms are agreed with you before any work starts.']])+'<p>Comparing account recovery services as well? See <a href="/compare/">the comparison hub</a>.</p>'
add_section('best-instagram-username-claim-service',blk,anchor='compared-2026')
print(bump_lastmod(['https://unbanz.com/guides/','https://unbanz.com/best-instagram-username-claim-service/']))
