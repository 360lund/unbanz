import sys,os;sys.path.insert(0,'scripts/nov04l');sys.path.insert(0,'scripts/nov04m')
from lib import add_section,bump_lastmod
import importlib.util
spec=importlib.util.spec_from_file_location('c1','scripts/nov04m/country.py')
src=open('scripts/nov04m/country.py').read().split('T={}')[0];ns={};exec(src,ns);C=ns['C'];A=ns['A']
NM={'usa':'US','uk':'UK','canada':'Canada','netherlands':'Netherlands','france':'France'}
def rep(cs,app):
    return [(f'Where do I report a hack or scam in the {NM[c]}?' if c in('usa','uk','netherlands') else f'Where do I report a hack or scam in {NM[c]}?',C[c]['rep'][0].upper()+C[c]['rep'][1:]+'.') for c in cs]
def outside(cs): return [(f'Is there an outside appeal in {C[c]["n"]}?',C[c]['out']) for c in cs]
def ids(cs,app): return [(f'Which ID works for {app} in {C[c]["n"]}?',f'Usually {C[c]["id"]}, with the same name as the profile. {app} often asks for a video selfie instead.') for c in cs]
def tm(cs): return [(f'Which trademark office counts in {C[c]["n"]}?',f'A registration from the {C[c]["tm"]} can support Instagram’s trademark report if it matches the username exactly. Instagram decides, and a trademark does not give an automatic right to the name.') for c in cs]
NOANS=('No reply after the appeal: what now?','Meta does not commit to a timeline. Check Accounts Center, then Account status, and the linked email including spam. Do not send repeated appeals or open new accounts while waiting.')
ACC=('Where is the appeal in Accounts Center?','Settings, then Accounts Center, then Account status. If you cannot log in, use the button on the notice shown at login.')
LOST=('Lost the email and phone on the account?','Use the “try another way” or “I no longer have access” option on the login screen, which may lead to a video selfie or ID check. Secure any new email before you use it for recovery.')
T={
'facebook-appeal-rejected-usa-canada':outside(['usa','canada'])+rep(['usa','canada'],'Facebook'),
'facebook-appeal-rejected-uk-australia':outside(['uk'])+rep(['uk'],'Facebook'),
'instagram-appeal-no-response-usa-canada':[NOANS,ACC]+outside(['usa','canada']),
'instagram-appeal-no-response-uk-eu':[NOANS,ACC]+outside(['uk','netherlands']),
'instagram-id-verification-usa-canada':ids(['usa','canada'],'Instagram')+[NOANS],
'instagram-id-verification-uk-eu':ids(['uk','netherlands','france'],'Instagram'),
'instagram-id-verification-france-germany':ids(['france'],'Instagram')+outside(['france']),
'facebook-id-verification-canada-australia':ids(['canada'],'Facebook')+outside(['canada']),
'facebook-id-verification-france-germany':ids(['france'],'Facebook')+outside(['france']),
'facebook-lost-access-to-email-or-phone-usa':[LOST]+ids(['usa'],'Facebook')+rep(['usa'],'Facebook'),
'facebook-lost-access-to-email-or-phone-uk-eu':[LOST]+ids(['uk','netherlands'],'Facebook'),
'facebook-lost-access-to-email-or-phone-canada-australia':[LOST]+ids(['canada'],'Facebook'),
'facebook-lost-access-to-email-or-phone-france-germany':[LOST]+ids(['france'],'Facebook'),
'instagram-no-appeal-button-usa-canada':[ACC]+outside(['usa','canada']),
'instagram-no-appeal-button-eu-uk-routes':[ACC]+outside(['uk','netherlands','france']),
'inactive-instagram-username-usa':tm(['usa']),'inactive-instagram-username-uk':tm(['uk']),'inactive-instagram-username-canada':tm(['canada']),
'instagram-username-claim-with-us-trademark':tm(['canada'])+[('Does a pending US application count?','Instagram’s form asks for a registration. A pending application may carry less weight, so check the form’s current wording.')],
'instagram-username-claim-with-uk-or-eu-trademark':tm(['netherlands','france']),
'canada-australia-hacked-or-banned-account-where-to-report':rep(['canada'],'Instagram')+outside(['canada']),
}
urls=[]
for p,it in T.items():
    if not os.path.exists(p+'/index.html'): print('skip',p);continue
    b=f'<h2 id="{A}">Local questions, answered (2026)</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in it)
    if add_section(p,b,anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b11.txt','w').write('\n'.join(urls))
