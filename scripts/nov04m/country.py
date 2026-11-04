import sys;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
A='local-questions-2026'
C={
'usa':dict(n='the US',rep='the FTC at reportfraud.ftc.gov and the FBI’s IC3 at ic3.gov',sext='NCMEC’s Take It Down (for under-18s) and IC3',doc='an EIN confirmation letter (CP 575 or 147C), articles of incorporation or a utility bill in the business name',id='a US driver’s license, state ID or passport',out='There is no outside appeal body for Meta account decisions in the US, so Meta’s own review is the only formal route.',tm='USPTO'),
'uk':dict(n='the UK',rep='Report Fraud (which replaced Action Fraud on 4 December 2025) on 0300 123 2040, or Police Scotland on 101',sext='Report Remove (under-18s) and the Revenge Porn Helpline',doc='a Companies House record, a VAT certificate or a utility bill in the business name',id='a UK passport, photocard driving licence or biometric residence permit',out='Ofcom regulates platforms under the Online Safety Act but does not decide individual appeals. Appeals Centre Europe is set up under EU law and is aimed at users in the EU.',tm='UKIPO'),
'canada':dict(n='Canada',rep='the Canadian Anti-Fraud Centre (1-888-495-8501) and local police',sext='Cybertip.ca and NeedHelpNow.ca',doc='CRA business number documents, articles of incorporation or a provincial registration',id='a Canadian passport, driver’s licence or provincial photo ID',out='The Office of the Privacy Commissioner handles privacy complaints, not account appeals. There is no outside appeal body for Meta account decisions.',tm='CIPO'),
'netherlands':dict(n='the Netherlands',rep='the Fraudehelpdesk (fraudehelpdesk.nl) and a police report (aangifte), online or at a station',sext='Helpwanted.nl and Offlimits',doc='a recent KvK extract or BTW (VAT) documents',id='a Dutch passport, ID card or driving licence',out='Once Meta’s own appeal is done, EU users can go to Appeals Centre Europe, which has reviewed suspensions since 2025. It is free and non-binding. The ACM is the Dutch Digital Services Coordinator but does not decide individual appeals.',tm='BOIP or EUIPO'),
'france':dict(n='France',rep='17Cyber (17cyber.gouv.fr) for guidance and THESEE for an online complaint',sext='Pharos and the 3018 helpline',doc='a recent Kbis extract or a SIREN/INSEE notice',id='a French passport, carte d’identité or titre de séjour',out='Once Meta’s own appeal is done, EU users can go to Appeals Centre Europe, which has reviewed suspensions since 2025. It is free and non-binding. Arcom is the French Digital Services Coordinator but does not decide individual appeals.',tm='INPI or EUIPO'),
}
def acct(c,app):
    f=C[c];h='instagram.com/hacked' if app=='Instagram' else 'facebook.com/hacked'
    return [
    (f'Which ID does {app} accept in {f["n"]}?',f'Meta’s list changes, but {f["id"]} is the usual choice. Make sure the name matches the profile. Often {app} asks for a video selfie instead of a document.'),
    (f'Disabled and {app} shows no ID option?','Do the video selfie if offered, once, in good light. If nothing is offered, screenshot the screen with the date and avoid opening new accounts while you wait.'),
    (f'Hacked and disabled in {f["n"]}: who do I tell?',f'Use {h} first, then appeal the disable. Report the hack or scam to {f["rep"]}.'),
    (f'Where do I check status in Accounts Center?','Settings, then Accounts Center, then Account status. If you cannot log in, the notice on the login screen has the review button.'),
    (f'Is there an outside appeal in {f["n"]}?',f['out'])]
def hacked(c,app):
    f=C[c];h='instagram.com/hacked' if app=='Instagram' else 'facebook.com/hacked'
    return [
    ('Hacked and now disabled too: what order?',f'Start at {h}, so the record shows the account was taken, then appeal the disable if a button appears. Secure the email and phone first.'),
    (f'Who do I report it to in {f["n"]}?',f'{f["rep"][0].upper()+f["rep"][1:]}. If the hacker is threatening to share private images, also use {f["sext"]}.'),
    ('Does a police or fraud report help the appeal?','Meta does not ask for one, but a reference number is useful if money was taken or if you later need to show the account was compromised.'),
    (f'Is there an outside appeal in {f["n"]}?',f['out'])]
def verify(c,app):
    f=C[c];return [
    ('Stuck on “we’re reviewing your info”?','The selfie or document was received. Do not resubmit unless asked. Waits vary and Meta does not commit to one.'),
    (f'Which document works best in {f["n"]}?',f'Usually {f["id"]}, with the name matching the profile. For business verification, use {f["doc"]}.'),
    (f'Is there an outside appeal in {f["n"]}?',f['out'])]
def ads(c):
    f=C[c];return [
    (f'Why do ad accounts in {f["n"]} get restricted?','The usual triggers are a declined or disputed card, a billing country or currency change, a spend spike, repeated rejected ads, a login from a new country, or an admin whose own profile is restricted.'),
    (f'What documents pass business verification in {f["n"]}?',f'Use {f["doc"]}, with the legal name and address matching the business portfolio exactly.'),
    ('Where do I request the review?','Account Quality in Meta Business Suite (business.facebook.com/accountquality). Select the ad account and use Request review if shown. Meta does not state a review time.'),
    (f'Is there an outside appeal in {f["n"]}?',f['out'])]
T={}
for c in C:
    T[f'instagram-account-recovery-{c}']=acct(c,'Instagram');T[f'facebook-account-recovery-{c}']=acct(c,'Facebook')
    T[f'instagram-hacked-{c}-what-to-do']=hacked(c,'Instagram')
    if c!='france': T[f'facebook-hacked-{c}-what-to-do']=hacked(c,'Facebook')
    T[f'best-meta-ad-account-recovery-service-{c}']=ads(c)
for c in ['usa','uk','canada']: T[f'instagram-suspended-appeal-{c}']=acct(c,'Instagram')
T['facebook-id-verification-usa']=verify('usa','Facebook');T['facebook-id-verification-uk']=verify('uk','Facebook')
T['instagram-suspended-appeal-usa']=acct('usa','Instagram')
T['meta-ad-account-disabled-uk-business-first-steps']=ads('uk');T['meta-ad-account-disabled-us-small-business-first-steps']=ads('usa')
T['instagram-account-suspended-france-what-to-do']=acct('france','Instagram')
urls=[]
import os
for p,it in T.items():
    if not os.path.exists(p+'/index.html'): print('skip',p);continue
    b=f'<h2 id="{A}">Local questions, answered (2026)</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in it)
    if add_section(p,b,anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b8.txt','w').write('\n'.join(urls))
