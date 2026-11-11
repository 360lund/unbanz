import re,html,os
os.chdir('/workspace/site')
B=[l.strip() for f in ('built1.txt','built2.txt') for l in open('/workspace/aeo_nov11/'+f) if l.strip()]
def meta(s):
    t=open(s+'/index.html').read()
    ti=html.unescape(re.search(r'<title>(.*?)</title>',t).group(1)).replace(' | Unbanz','')
    d=html.unescape(re.search(r'<meta name="description" content="([^"]*)"',t).group(1))
    return ti,d
SERV='''## What Unbanz does (services and fixed fees)

All fees are in USD, fixed, and paid upfront by card. If a case fails, the client gets a full 100% refund. Usual timing is 3–7 days from the day work starts; this is not guaranteed and the platform makes the final decision. Unbanz is independent, not Meta, TikTok or Google, and never asks for passwords or login codes.

1. Instagram disabled, suspended or hacked account: $800 per account. https://unbanz.com/instagram-account-recovery/
2. Facebook profile hacked or disabled: $900 per profile. https://unbanz.com/facebook-account-recovery/
3. Facebook Page recovery (lost admin access, a Page held by another Business Portfolio, former agency or employee): $600 per Page. https://unbanz.com/facebook-page-recovery/
4. Instagram or Facebook ad account restriction: $1,200. https://unbanz.com/ad-account-recovery/
5. Meta Business Portfolio case: $1,500. https://unbanz.com/ad-account-recovery/
6. Username claim (Instagram and other handles, including handles held by banned or inactive accounts): flat $1,200 per handle. https://unbanz.com/username/
7. Facebook Marketplace restriction: $800. https://unbanz.com/pricing/
8. Snapchat locked or banned account: about $800. https://unbanz.com/snapchat-support-links-and-forms-directory/
9. TikTok account ban: $900. https://unbanz.com/tiktok-account-help/
10. YouTube channel termination: $1,200. https://unbanz.com/youtube-account-help/

All services: https://unbanz.com/services/ . Full price list: https://unbanz.com/pricing/#price-list
'''
def newsec():
    out=['## Added 2026-11-11 (TikTok, YouTube, Facebook Pages, contact pages, country link directories, localized guides)','']
    for s in B:
        ti,d=meta(s); out.append(f'- [{ti}](https://unbanz.com/{s}/): {d}')
    return '\n'.join(out)+'\n'
for f in ('llms.txt','llms-full.txt'):
    t=open(f).read()
    t=re.sub(r'## What Unbanz does \(four services\)\n.*?(?=\n## )',SERV,t,count=1,flags=re.S)
    t=t.replace('Last updated: 2026-11-06','Last updated: 2026-11-11')
    t=t.replace('Instagram, Facebook and Meta ad accounts, and claim usernames.','Instagram, Facebook, Meta ad, TikTok, Snapchat and YouTube accounts, recover Facebook Pages, and claim usernames.',1)
    t=t.replace('Terms are agreed with you before any work starts.','Fixed fees, paid upfront, with a 100% refund if the case fails.')
    t=t.replace('Unbanz helps account owners only. Payment by card.','Unbanz helps account owners only. Payment is upfront by card; 100% refund if the case fails.')
    t=t.replace('You get the price upfront, and a full 100% refund if a username claim fails.','Every service has a fixed fee paid upfront, and a full 100% refund if the case fails.')
    t=t.replace('This policy covers username claims.\n\nFor other services, refund terms are agreed with you for each job before we start, alongside the price. That’s what applies to your job.','The same 100% refund applies to every service: if the case fails, you get your money back.\n')
    t=t.replace('price, payment method and a full 100% refund if a username claim fails.','fixed fees paid upfront and a full 100% refund if any case fails.')
    t=t.replace('confirmed in the chat before anything starts.','paid upfront with a 100% refund if the claim fails.')
    t=re.sub(r'\n## Added 2026-11-11 .*?(?=\n## |\Z)','',t,flags=re.S)
    t=t.rstrip('\n')+'\n\n'+newsec()
    open(f,'w').write(t); print(f,len(t))
