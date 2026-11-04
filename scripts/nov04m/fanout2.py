import sys;sys.path.insert(0,'scripts/nov04l');from lib import add_section,table,bump_lastmod
A='sub-questions-2026'
def qa(t,items,tail=''): return f'<h2 id="{A}">{t}</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in items)+tail
CTRY=table(['Country','Report a hack or scam','Regulator note'],[
['United States','FTC (reportfraud.ftc.gov) and FBI IC3 (ic3.gov)','No outside appeal body for Meta account decisions'],
['United Kingdom','Report Fraud (replaced Action Fraud on 4 December 2025), 0300 123 2040; Police Scotland on 101','Ofcom does not decide individual appeals'],
['Canada','Canadian Anti-Fraud Centre, 1-888-495-8501','The Privacy Commissioner handles privacy complaints, not appeals'],
['Netherlands','Fraudehelpdesk and a police report (aangifte)','EU users can go to Appeals Centre Europe after Meta’s own appeal'],
['France','17Cyber (17cyber.gouv.fr) and THESEE for online complaints','EU users can go to Appeals Centre Europe after Meta’s own appeal']])
AC=('Where is the appeal in Accounts Center?','If you can still log in, open Settings, then Accounts Center, then Account status, and pick the account. If you cannot log in, the login screen usually shows the notice with a button to disagree or request a review. Menu names change between app versions, so match the wording on your screen.')
NOID=('Disabled and no option to send ID?','Meta often asks for a video selfie instead of a document, or shows no upload at all. Record the selfie once, in good light, with no filters or glasses. If no option appears, screenshot the screen with the date. Sending repeated requests does not help.')
HACK=('Hacked and then disabled: which comes first?','Start with the hacked route (instagram.com/hacked or facebook.com/hacked), not the normal appeal, so the record shows the account was taken. Secure the linked email and phone first, then appeal the disable if a button appears. Report the scam where you live (table below).')
TIME=('How long does an appeal take?','Meta does not commit to a timeline. Waits vary widely, and identity checks can add to them. The appeal window shown on a disable notice is usually about 180 days, so note the date on yours.')
VER=('Stuck on “we’re reviewing your info” after verification?','That screen means the selfie or document was received. Do not resubmit unless asked, and do not create new accounts while waiting, which can be treated as getting around the decision. If nothing changes for weeks, an EU user can look at Appeals Centre Europe once Meta’s own appeal is done.')
ACE=('Is there anywhere to go after a final no?','In the EU, Appeals Centre Europe can review Facebook and Instagram account decisions. It is free and non-binding, and Meta’s internal appeal must be finished first. Outside the EU there is no equivalent body for account decisions.')
ADR=('What are the usual reasons for an ad account restriction?','The common ones are a declined or disputed payment, a billing country or currency change, a sudden spend increase, repeated rejected ads, a login from a new device or country, unverified business details, or an admin whose personal profile is itself restricted. Account Quality usually names the policy.')
ADV=('Business verification or ID check pending: what helps?','Use documents that match the business portfolio name and address exactly, such as an EIN letter (US), Companies House record (UK), CRA business number (Canada), KvK extract (Netherlands) or Kbis/SIREN (France). A name mismatch is one of the most common reasons verification fails.')
ADT=('How long does an ad account review take?','Meta does not state one. While you wait, do not open new ad accounts or move spend to a fresh profile, which can be read as circumventing systems. Check Account Quality for status rather than resubmitting.')
ADAC=('Where do I request the review?','Go to Account Quality in Meta Business Suite (business.facebook.com/accountquality), select the ad account, and use Request review if it is shown. For a personal ad account, open Accounts Center, then Account status.')
ACC='Fanout answers, checked November 2026'
P={
'instagram-unban-service':[AC,NOID,HACK,TIME,ACE],
'facebook-unban-service':[AC,NOID,HACK,TIME,ACE],
'instagram-account-recovery':[AC,NOID,HACK,VER],
'facebook-account-recovery':[AC,NOID,HACK,VER],
'guides/instagram-account-disabled':[AC,NOID,HACK,VER,ACE],
'guides/facebook-account-disabled-appeal':[AC,NOID,HACK,VER,ACE],
'guides/hacked-instagram-account-recovery':[HACK,NOID,VER,TIME],
'ad-account-recovery':[ADR,ADAC,ADV,ADT],
'guides/meta-ad-account-restricted':[ADAC,ADV,ADT],
'meta-ad-account-help':[ADR,ADAC,ADV,ADT],
}
urls=[]
for p,it in P.items():
    ad=p in('ad-account-recovery','guides/meta-ad-account-restricted','meta-ad-account-help')
    t='Ad account questions people also ask (2026)' if ad else 'Questions people also ask (2026)'
    tail='' if ad else '<p>Where to report a hack or scam, by country:</p>'+CTRY
    if add_section(p,qa(t,it,tail),anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b7.txt','w').write('\n'.join(urls))
