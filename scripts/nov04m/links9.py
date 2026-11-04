import sys;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
D='<a href="/meta-appeal-links-and-forms-directory/">Meta appeal links and forms directory</a>'
def blk(kind,vs):
    best={'ig':('/best-instagram-recovery-service/','how Instagram recovery services compare'),
          'fb':('/best-service-to-recover-disabled-facebook-account/','how Facebook recovery services compare'),
          'ad':('/best-facebook-ad-account-recovery-service/','how ad account recovery services compare')}[kind]
    v={'unbanx':'Unbanz vs Unbanx','unbanpro':'Unbanz vs UnbanPro','rescuno':'Unbanz vs Rescuno'}[vs]
    return ('<h2 id="compare-2026">Official links and comparisons (2026)</h2>'
      f'<p>Every official Meta form mentioned here is listed in one place in the {D}, so you can go straight to the right page. '
      f'Comparing options before asking for help? See <a href="{best[0]}">{best[1]}</a>'
      + (', the <a href="/best-meta-ad-account-recovery-service-usa/">US</a> and <a href="/best-meta-ad-account-recovery-service-uk/">UK</a> ad account guides' if kind=='ad' else '')
      + f', or <a href="/unbanz-vs-{vs}/">{v}</a>.</p>')
P={'guides/instagram-account-suspended-appeal':('ig','unbanx'),'guides/facebook-account-disabled-appeal':('fb','unbanx'),
'guides/facebook-lost-access-to-email-or-phone':('fb','rescuno'),'guides/instagram-disabled-no-appeal-button':('ig','unbanpro'),
'guides/meta-ad-account-restricted':('ad','unbanx'),'guides/instagram-id-verification-request':('ig','rescuno'),
'instagram-account-recovery':('ig','unbanpro'),'guides/hacked-instagram-account-recovery':('ig','unbanx'),
'facebook-account-recovery':('fb','unbanpro'),'facebook-unban-service':('fb','unbanx'),'guides/meta-ad-payment-declined-fix':('ad','unbanpro'),
'guides/facebook-disabled-appeal-rejected':('fb','rescuno'),'guides/instagram-account-disabled':('ig','unbanx'),
'facebook-account-disabled-usa-what-to-do':('fb','unbanx'),'guides/instagram-account-integrity':('ig','rescuno')}
urls=[]
for p,(k,v) in P.items():
    s=open(p+'/index.html').read()
    if '/meta-appeal-links-and-forms-directory/' in s and f'/unbanz-vs-{v}/' in s: continue
    if add_section(p,blk(k,v),anchor='compare-2026'): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b30.txt','w').write('\n'.join(urls))
