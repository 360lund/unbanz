import sys,os;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod,table
ns={};exec(open('scripts/nov04m/fanout2.py').read().split('P={')[0],ns);g=ns
A=g['A'];qa=g['qa'];CTRY=g['CTRY']
LINKS='<p>Country guides: '+', '.join(f'<a href="/{s}/">{n}</a>' for s,n in [('instagram-disabled-usa-what-to-do','US'),('instagram-disabled-uk-what-to-do','UK'),('instagram-disabled-canada-what-to-do','Canada'),('instagram-account-suspended-netherlands-what-to-do','Netherlands'),('instagram-disabled-france-what-to-do','France')])+'.</p>'
ADL='<p>Country guides: '+', '.join(f'<a href="/{s}/">{n}</a>' for s,n in [('facebook-ad-account-restricted-us-business','US'),('facebook-ad-account-disabled-uk','UK'),('facebook-ad-account-disabled-canada','Canada'),('meta-ad-account-disabled-netherlands','Netherlands'),('meta-ad-account-disabled-france','France')])+'.</p>'
P={
'unban':([g['AC'],g['NOID'],g['HACK'],g['TIME'],g['ACE']],True),
'instagram-account-disabled-appeal':([g['AC'],g['NOID'],g['VER'],g['ACE']],True),
'instagram-appeal-denied':([g['ACE'],g['NOID']],True),
'instagram-account-disabled-after-hack-appeal':([g['HACK'],g['VER']],True),
'how-long-does-an-instagram-appeal-take':([g['VER'],g['AC']],True),
'instagram-account-help':([g['AC'],g['NOID'],g['HACK'],g['TIME']],True),
'facebook-account-help':([g['AC'],g['NOID'],g['HACK'],g['TIME']],True),
'ad-account-disabled-after-hack':([g['ADAC'],g['ADV'],g['ADT']],False),
'why-was-my-facebook-ad-account-disabled-without-warning':([g['ADAC'],g['ADV'],g['ADT']],False),
'ad-account-identity-verification-loop':([g['ADV'],g['ADT']],False),
'business-manager-disabled':([g['ADR'],g['ADAC'],g['ADV']],False),
'how-long-does-meta-ad-account-review-take':([g['ADR'],g['ADV']],False),
'meta-ad-account-appeal-rejected-what-next':([g['ADR'],g['ADV'],g['ADT']],False),
'agency-ad-account-recovery':([g['ADR'],g['ADAC'],g['ADV']],False),
}
urls=[]
for p,(it,acct) in P.items():
    if not os.path.exists(p+'/index.html'): print('skip',p);continue
    s=open(p+'/index.html').read()
    it=[x for x in it if x[0] not in s]
    if not it: continue
    t='Questions people also ask (2026)' if acct else 'Ad account questions people also ask (2026)'
    tail=('<p>Where to report a hack or scam, by country:</p>'+CTRY+LINKS) if acct else ADL
    if add_section(p,qa(t,it,tail),anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b13.txt','w').write('\n'.join(urls))
