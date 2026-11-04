import sys,os;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
ns={};exec(open('scripts/nov04m/fanout2.py').read().split('P={')[0],ns);g=ns;A=g['A'];qa=g['qa']
UI=('Can I claim a username from an inactive account?','Instagram has no public form to request an inactive username. A name usually frees up only when the holding account is removed or deleted. A registered trademark adds an official route: Instagram’s trademark report form, which covers accounts that infringe the mark, not just accounts that share the name.')
UT=('How long until a released username is free?','Instagram does not publish a date. After you change your own username, Instagram usually lets you switch back for 14 days, so a name you just gave up can stay reserved for a while.')
UTM=('Does a trademark help with a username?','It can. Instagram’s trademark form is for accounts using a registered mark in a way that confuses people. Have the registration number, the owner name and the country of registration ready, and use the same name on the request.')
US=('Is a username claim safe for my account?','A claim should never need your password or login codes. Buying or selling usernames or accounts goes against Instagram’s Terms of Use and can get both accounts removed, so avoid marketplaces.')
UFB=('How do Facebook usernames work?','A Facebook Page or profile username is the name in its web address. It must be unique and not already in use, and a Page may need some activity before it can set one. Facebook does not publish a request form for names that are taken.')
P={
'taken-instagram-username':[UI,UT,UTM,US],'og-username':[UI,UT,US],'facebook-username-claim':[UFB,UTM,US],
'trademark-username-claim':[UTM,UI,US],'business-username-claim':[UTM,UI,US],'one-letter-username':[UI,UT,US],
'can-you-claim-a-username-from-an-inactive-instagram-account':[UTM,US],'how-long-does-it-take-to-claim-an-instagram-username':[UT,UI],
'someone-took-my-old-instagram-username':[UT,UTM,US],'instagram-username-not-available-but-no-account':[UT,UI],
'can-you-buy-an-instagram-username':[US,UI],'how-long-until-instagram-username-is-available':[UI,UTM],
'can-someone-take-my-inactive-instagram-username':[UT,US],'instagram-username-claim-routes':[UTM,US],
}
urls=[]
for p,it in P.items():
    if not os.path.exists(p+'/index.html'): print('skip',p);continue
    s=open(p+'/index.html').read();it=[x for x in it if x[0] not in s]
    if it and add_section(p,qa('Username questions people also ask (2026)',it,''),anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b22.txt','w').write('\n'.join(urls))
