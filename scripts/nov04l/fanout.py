import sys;sys.path.insert(0,'scripts/nov04l')
from lib import *
def qa(items): return ''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in items)
C={
'usa':dict(n='the US',
  report=f'If the account was hacked or someone used it to scam people, report it to the FTC at {ext("https://reportfraud.ftc.gov/")} and to the FBI’s Internet Crime Complaint Center at {ext("https://www.ic3.gov/")}. Neither restores accounts, but a report number helps if money moved.',
  reg='The US has no regulator that reviews a single Instagram or Facebook account decision. There is no US equivalent of the EU’s out-of-court dispute bodies. Your route is Meta’s own appeal.',
  id='Meta usually accepts a US passport, driver’s license or state ID card. Use the same name that is on the account.',
  biz=f'Meta may ask for your legal business name, address and an official document. In the US that is often your IRS EIN letter, articles of incorporation or a state business license.',
  tm=f'A registered US trademark from the USPTO ({ext("https://www.uspto.gov/")}) is the strongest proof for a trademark-based username request.',
  phone='Use the +1 number on the account. If you changed carriers, port the number rather than getting a new one, so login codes keep reaching you.'),
'uk':dict(n='the UK',
  report=f'Report a hacked account or a scam to Report Fraud at {ext("https://www.reportfraud.police.uk/")} or 0300 123 2040. It replaced Action Fraud on 4 December 2025 for England, Wales and Northern Ireland. In Scotland, call Police Scotland on 101. The NCSC has a guide at {ext("https://www.ncsc.gov.uk/guidance/recovering-a-hacked-account")}.',
  reg='Ofcom enforces the Online Safety Act, but it does not decide individual account appeals. Since Brexit, UK users cannot use the EU’s Appeals Centre Europe under the DSA. You can ask Meta for your data with a UK GDPR subject access request; see <a href="/uk-gdpr-subject-access-request-meta-disabled-account/">the SAR guide</a>.',
  id='Meta usually accepts a UK passport, a photocard driving licence or a national identity card. Use the same name that is on the account.',
  biz='Meta may ask for your legal business name, address and an official document. In the UK that is often your Companies House registration, a VAT certificate or a recent utility bill in the business name.',
  tm=f'A registered UK trademark from the UK Intellectual Property Office ({ext("https://www.gov.uk/government/organisations/intellectual-property-office")}) is the strongest proof for a trademark-based username request.',
  phone='Use the +44 number on the account. Drop the first 0 when you type it, so 07700 900123 becomes +44 7700 900123.'),
'canada':dict(n='Canada',
  report=f'Report a hacked account or a scam to the Canadian Anti-Fraud Centre at {ext("https://antifraudcentre-centreantifraude.ca/")} and to your local police. Neither restores accounts.',
  reg=f'Canada has no body that reviews a single Instagram or Facebook account decision. The Office of the Privacy Commissioner ({ext("https://www.priv.gc.ca/")}) handles privacy complaints, not account appeals. Your route is Meta’s own appeal.',
  id='Meta usually accepts a Canadian passport, a provincial driver’s licence or a provincial photo ID card. Use the same name that is on the account.',
  biz='Meta may ask for your legal business name, address and an official document. In Canada that is often your CRA Business Number confirmation, articles of incorporation or a provincial business registration.',
  tm=f'A registered Canadian trademark from the Canadian Intellectual Property Office ({ext("https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en")}) is the strongest proof for a trademark-based username request.',
  phone='Use the +1 number on the account. If you moved provinces or carriers, keep the old number active until you are back in.'),
'netherlands':dict(n='the Netherlands',
  report=f'Report fraud with a hacked account to the police (politie.nl) and get advice from the Fraudehelpdesk ({ext("https://www.fraudehelpdesk.nl/")}). Neither restores accounts.',
  reg=f'Under the EU Digital Services Act, after Meta’s internal appeal you can take a suspension to a certified out-of-court body. Appeals Centre Europe ({ext("https://www.appealscentre.eu/")}) has reviewed Facebook and Instagram account suspensions since 2025, free for users. Its decisions are not binding, but platforms must engage in good faith. The ACM is the Dutch Digital Services Coordinator; it takes reports when a platform breaks its DSA duties, not individual appeals ({ext("https://www.acm.nl/nl/digitale-economie/rechten-van-ondernemers-bij-online-diensten/account-geblokkeerd-content-verwijderd")}).',
  id='Meta usually accepts a Dutch passport, ID card (identiteitskaart) or driving licence (rijbewijs). You may cover your BSN on the image.',
  biz='Meta may ask for your legal business name, address and an official document. In the Netherlands that is often a KvK extract (uittreksel) or a BTW-number letter from the Belastingdienst.',
  tm=f'A registered Benelux trademark from BOIP ({ext("https://www.boip.int/")}) or an EU trademark from the EUIPO is the strongest proof for a trademark-based username request.',
  phone='Use the +31 number on the account. Drop the first 0, so 06 12345678 becomes +31 6 12345678.'),
'france':dict(n='France',
  report=f'For a hacked account, run the free 17Cyber diagnostic at {ext("https://17cyber.gouv.fr/")}, run by the police, gendarmerie and Cybermalveillance.gouv.fr. If someone demands money or scams your contacts, you can file a complaint online on the Thésée platform.',
  reg=f'Under the EU Digital Services Act, after Meta’s internal appeal you can take a suspension to a certified out-of-court body such as Appeals Centre Europe ({ext("https://www.appealscentre.eu/")}), free for users. Arcom is the French Digital Services Coordinator; it does not judge individual decisions. Out-of-court bodies propose a solution within 90 days, which the platform does not have to follow ({ext("https://www.arcom.fr/nous-connaitre-nos-missions/superviser-les-plateformes-en-ligne-et-les-reseaux-sociaux/contester-les-decisions-prises-par-une-plateforme-en-ligne-lencontre-des-utilisateurs","arcom.fr")}).',
  id='Meta usually accepts a French passport, carte nationale d’identité or permis de conduire. Use the same name that is on the account.',
  biz='Meta may ask for your legal business name, address and an official document. In France that is often a Kbis extract, an INSEE SIRENE notice with your SIREN/SIRET, or a TVA number document.',
  tm=f'A registered French trademark from INPI ({ext("https://www.inpi.fr/")}) or an EU trademark from the EUIPO is the strongest proof for a trademark-based username request.',
  phone='Use the +33 number on the account. Drop the first 0, so 06 12 34 56 78 becomes +33 6 12 34 56 78.'),
}
EU={'netherlands','france'}
def disabled(c,plat):
    d=C[c];fb=plat=='Facebook'
    items=[(f'Where do I appeal a disabled {plat} account in {d["n"]}?',f'From the notice you see when you log in, or from Meta Accounts Center. There is no separate form for {d["n"]}. Old contact-form links mostly redirect now; see the <a href="/meta-appeal-links-and-forms-directory/">official links directory</a>.'),
     (f'How long do I have to appeal?','Facebook says you can appeal a suspension within 180 days, and that the period varies by region. After that, or after a failed appeal, the account is permanently disabled.' if fb else 'Instagram shows the deadline on the notice. Meta generally gives up to 180 days for a suspension. Do not wait for the last day.'),
     (f'Is there a Meta phone number in {d["n"]}?','No. Meta says it has no general public phone number for customer service. A number claiming to be Meta support is likely a scam.'),
     (f'What ID does Meta accept from {d["n"]}?',d['id']),
     ('What about my phone number?',d['phone']),
     (f'Does Meta Verified help a disabled account?','Meta Verified gives access to support for accounts you can still log in to. It does not reopen an account that is already disabled.'),
     (f'Is there an official body above Meta in {d["n"]}?',d['reg']),
     ('Who do I report a hack or scam to?',d['report']),
     (f'Can someone in {d["n"]} get my account back for me?','Nobody can override Meta, and nobody legit needs your password. A service can help you prepare and follow up the appeal. Meta makes the final decision.')]
    return f'<h2 id="quick-answers-2026">{plat} disabled in {d["n"]}: quick answers (2026)</h2>'+qa(items)
def ads(c):
    d=C[c]
    items=[(f'Where do I request a review for a disabled ad account in {d["n"]}?',f'On a computer, open Business Support Home (Account Quality), pick the restricted ad account, then What you can do. Only an admin can request it. Meta’s steps: {ext("https://www.facebook.com/business/help/422289316306981")}.'),
     ('How many reviews do I get?',f'Meta says reviews are limited, and once a review is completed the decision is final ({ext("https://www.facebook.com/business/help/530209463124901")}). Fix the cause in the notice before you click.'),
     (f'What business documents work in {d["n"]}?',d['biz']),
     (f'What ID does Meta accept for the admin in {d["n"]}?',d['id']),
     ('Does my card or billing country matter?','It can. A payment method in a different country from the business, a failed charge or a sudden spend jump can all trigger a restriction. Keep billing details matching your registered business.'),
     ('Is there a Meta Business Support phone line?','No general public one. Support is through Business Support Home, Meta’s chat for eligible advertisers, and Meta Verified for business.'),
     (f'Is there an official body above Meta in {d["n"]}?',d['reg'] if c in EU else d['reg'].replace('Instagram or Facebook account decision','ad account decision')),
     ('Will a new ad account fix it?','Usually not. Meta can link new accounts to the restricted person or portfolio and restrict them too, which makes things worse.')]
    return f'<h2 id="quick-answers-2026">Meta ad account disabled in {d["n"]}: quick answers (2026)</h2>'+qa(items)
def uname(c):
    d=C[c]
    items=[(f'Can I get an inactive Instagram username in {d["n"]}?','Sometimes. Instagram has no public form to request a username held by an inactive account. Inactive handles are not released on a schedule.'),
     ('Is there an official route?','Yes, if you own a registered trademark for the name: Instagram’s trademark report, in the Help Center under intellectual property. Without a trademark there is no official request form.'),
     (f'What trademark counts in {d["n"]}?',d['tm']),
     ('Should I buy a username from a seller?','No. Instagram’s terms do not allow buying or selling usernames, and sellers often scam or hand over an account that gets taken back.'),
     ('Do I need to give my password?','No. Your password stays with you. The username is moved to an account you control.'),
     ('Is it legal?','Using Instagram’s own processes is. Hacking, buying or pressuring the holder is not something we do.')]
    return f'<h2 id="quick-answers-2026">Instagram username claims in {d["n"]}: quick answers (2026)</h2>'+qa(items)
plan=[]
igp={'usa':'instagram-disabled-usa-what-to-do','uk':'instagram-disabled-uk-what-to-do','canada':'instagram-disabled-canada-what-to-do','france':'instagram-disabled-france-what-to-do','netherlands':'instagram-account-suspended-netherlands-what-to-do'}
adp={'usa':'facebook-ad-account-restricted-us-business','uk':'facebook-ad-account-disabled-uk','canada':'facebook-ad-account-disabled-canada','netherlands':'meta-ad-account-disabled-netherlands','france':'meta-ad-account-disabled-france'}
for c in C:
    plan+= [(igp[c],disabled(c,'Instagram')),(f'facebook-account-disabled-{c}-what-to-do',disabled(c,'Facebook')),(adp[c],ads(c)),(f'instagram-username-claim-{c}',uname(c))]
done=[]
for p,b in plan:
    if not os.path.isdir(p): print('missing',p);continue
    if add_section(p,b,anchor='quick-answers-2026' if 'quick-answers-2026' in b else 'username-quick-answers'): done.append(f'https://unbanz.com/{p}/')
print(len(done),bump_lastmod(done))
open('/tmp/b2.txt','w').write('\n'.join(done+['https://unbanz.com/sitemap.xml']))
