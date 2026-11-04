import sys,os;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
ns={};exec(open('scripts/nov04m/fanout2.py').read().split('P={')[0],ns);g=ns;A=g['A'];qa=g['qa']
L1=('What if I no longer have the email or phone on the account?','Start from facebook.com/login/identify or the Instagram “Forgot password” screen on a phone or computer you have logged in from before. Meta may offer other options there, such as a code to a different contact, a video selfie or an ID photo. Which options appear depends on the account.')
L2=('Does a recognised device help?','Often, yes. Meta may trust a phone, browser or network you have used to log in before, so try recovery from that device and connection rather than a new one.')
L3=('What if a hacker changed the email and phone?','Check the old inbox for a security email from Meta about the change. It can include a link to undo it. On Instagram, use “My login details were changed” in the login help, or instagram.com/hacked.')
P={'guides/facebook-lost-access-to-email-or-phone':[L1,L2,L3,g['NOID'],g['HACK']],
'how-to-appeal-in-accounts-center':[g['NOID'],g['TIME'],g['ACE']],
'guides/instagram-account-integrity':[g['AC'],g['TIME'],g['ACE']],
'facebook-disabled-suspicious-activity-appeal':[g['AC'],g['HACK'],g['VER']],
'guides/facebook-account-locked':[L1,L2,g['VER']],
'instagram-account-ban-service':[g['AC'],g['NOID'],g['TIME']],
'guides/meta-ad-payment-declined-fix':[g['ADAC'],g['ADT']],
'guides/hacked-instagram-account-recovery':[L3,L2],
'guides/instagram-account-suspended-appeal':[L1,L2],
'guides/facebook-account-disabled-appeal':[L1,L2],
}
urls=[]
for p,it in P.items():
    if not os.path.exists(p+'/index.html'): print('skip',p);continue
    s=open(p+'/index.html').read();it=[x for x in it if x[0] not in s]
    if not it: continue
    t='Ad account questions people also ask (2026)' if 'ad-' in p else ('Login and recovery questions (2026)' if p.count('/')>0 and any(x in (L1,L2,L3) for x in it) else 'Questions people also ask (2026)')
    an=A if not any(x in (L1,L2,L3) for x in it) else 'login-questions-2026'
    h=qa(t,it,'').replace(f'id="{A}"',f'id="{an}"',1)
    if add_section(p,h,anchor=an): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b25.txt','w').write('\n'.join(urls))
