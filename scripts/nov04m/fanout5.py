import sys,os;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod,table
ns={};exec(open('scripts/nov04m/fanout2.py').read().split('P={')[0],ns);g=ns
A=g['A'];qa=g['qa'];CTRY=g['CTRY']
LINKS='<p>Country guides: '+', '.join(f'<a href="/{s}/">{n}</a>' for s,n in [('instagram-disabled-usa-what-to-do','US'),('instagram-disabled-uk-what-to-do','UK'),('instagram-disabled-canada-what-to-do','Canada'),('instagram-account-suspended-netherlands-what-to-do','Netherlands'),('instagram-disabled-france-what-to-do','France')])+'.</p>'
ADL='<p>Country guides: '+', '.join(f'<a href="/{s}/">{n}</a>' for s,n in [('facebook-ad-account-restricted-us-business','US'),('facebook-ad-account-disabled-uk','UK'),('facebook-ad-account-disabled-canada','Canada'),('meta-ad-account-disabled-netherlands','Netherlands'),('meta-ad-account-disabled-france','France')])+'.</p>'
P={
'facebook-ad-account-disabled':([g['ADR'],g['ADAC'],g['ADV'],g['ADT']],False),
'facebook-ad-account-restricted-help':([g['ADR'],g['ADAC'],g['ADT']],False),
'meta-ad-account-restricted':([g['ADR'],g['ADAC'],g['ADV']],False),
'instagram-ads-account-restricted':([g['ADR'],g['ADAC'],g['ADT']],False),
'guides/meta-ad-account-disabled-payment':([g['ADAC'],g['ADT']],False),
'ad-account-restricted-payment-issue':([g['ADAC'],g['ADT']],False),
'ad-account-unusual-activity':([g['ADR'],g['ADAC'],g['ADV']],False),
'ad-account-policy-violation-appeal':([g['ADR'],g['ADAC'],g['ADT']],False),
'ad-account-request-review-not-showing':([g['ADR'],g['ADT']],False),
'can-i-make-a-new-ad-account-after-ban':([g['ADAC'],g['ADT']],False),
'who-can-recover-a-disabled-facebook-ad-account':([g['ADR'],g['ADAC'],g['ADV']],False),
'meta-business-verification-rejected':([g['ADT'],g['ADAC']],False),
'meta-ad-account-appeal-what-to-write':([g['ADR'],g['ADV'],g['ADT']],False),
'ad-account-disabled-circumventing-systems-help':([g['ADAC'],g['ADV']],False),
'facebook-account-disabled-appeal-help':([g['AC'],g['NOID'],g['HACK'],g['TIME'],g['ACE']],True),
'guides/hacked-facebook-account-recovery':([g['HACK'],g['NOID'],g['AC']],True),
'guides/instagram-video-selfie-verification':([g['VER'],g['TIME'],g['AC']],True),
'guides/instagram-id-verification-request':([g['VER'],g['NOID'],g['TIME']],True),
'instagram-account-suspended-180-days':([g['AC'],g['TIME'],g['ACE']],True),
'facebook-account-suspended-180-days':([g['AC'],g['TIME'],g['ACE']],True),
'instagram-business-account-disabled-recovery':([g['AC'],g['NOID'],g['HACK'],g['TIME']],True),
'guides/facebook-disabled-appeal-rejected':([g['ACE'],g['NOID']],True),
'guides/facebook-account-disabled-for-no-reason':([g['AC'],g['HACK'],g['TIME']],True),
'guides/facebook-disabled-no-appeal-option':([g['AC'],g['NOID'],g['ACE']],True),
'instagram-appeal-form-not-working':([g['AC'],g['VER'],g['TIME']],True),
'who-can-help-get-my-instagram-account-back':([g['AC'],g['HACK'],g['TIME'],g['ACE']],True),
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
print(bump_lastmod(urls),len(urls));open('/tmp/b23.txt','w').write('\n'.join(urls))
