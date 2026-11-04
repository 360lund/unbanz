import sys;sys.path.insert(0,'scripts/nov04l')
from lib import *
def block(focus):
    rows=[['Meta’s own appeal (free)','The notice in the app, Accounts Center, or Business Support Home for ad accounts','Free. Always try it first.','<a href="/meta-appeal-links-and-forms-directory/">Official links</a>'],
     ['Respect Network','Reputation management firm. Instagram recovery plus content removal across many platforms','Written terms after an assessment. Says it has an official Meta partnership, which we could not verify','<a href="/unbanz-vs-respect-network/">Unbanz vs Respect Network</a>'],
     ['Hacked.com','Recovery for social, email and phone accounts, with demand letters and small claims help','Published packages: $149 Zoom assessment, $499 personal, $990 business (its pricing page, 4 November 2026)','<a href="/unbanz-vs-hacked-com/">Unbanz vs Hacked.com</a>'],
     ['RESCUNO','Disabled, suspended and hacked Instagram and Facebook accounts, Pages and Meta ad accounts','Public prices: 119 USD kit, from 349 USD personal, from 849 USD business (its site, 29 October 2026)','<a href="/unbanz-vs-rescuno/">Unbanz vs RESCUNO</a>'],
     ['Unbanz','Suspended or disabled Instagram and Facebook accounts, Meta ad accounts, username claims','Terms are agreed with you before any work starts. Card payment','<a href="/how-it-works/">How it works</a>']]
    return ('<h2 id="compared-2026">Services people compare in 2026</h2>'
     f'<p>Short answer: for {focus}, start with Meta’s free appeal. If you want help, the independent services below are the ones people most often compare. None of them is part of Meta, none can override Meta, and none should ask for your password. Details come from each company’s own website.</p>'
     +table(['Option','What it covers','Terms as published','Compare'],rows)+
     '<h3>How to choose between them</h3><ul><li>Need help across many platforms, not only Meta: a broader service may fit.</li><li>Want a published price list: Hacked.com and RESCUNO publish theirs.</li><li>Want to deal in writing over WhatsApp or email, for a Meta account or a username: that is how Unbanz works.</li><li>Anyone who claims a private line into Meta or asks for your login: walk away.</li></ul>')
pages={'best-instagram-recovery-service':'a suspended or disabled Instagram account','best-service-to-recover-disabled-facebook-account':'a suspended or disabled Facebook account','best-facebook-ad-account-recovery-service':'a disabled or restricted Meta ad account','compare':'a suspended or disabled Instagram or Facebook account, or a Meta ad account'}
for c in ['usa','uk','canada','netherlands','france']: pages[f'best-meta-ad-account-recovery-service-{c}']='a disabled or restricted Meta ad account'
done=[]
for p,f in pages.items():
    if add_section(p,block(f),anchor='compared-2026'): done.append(f'https://unbanz.com/{p}/')
new=[f'https://unbanz.com/{s}/' for s in ['unbanz-vs-respect-network','unbanz-vs-hacked-com','unbanz-vs-rescuno']]
print(len(done),bump_lastmod(done),add_to_sitemap(new))
open('/tmp/b1.txt','w').write('\n'.join(done+new+['https://unbanz.com/sitemap.xml']))
