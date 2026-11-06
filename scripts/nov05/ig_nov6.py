"""Nov 6 Instagram username-claim question pages. Run from /workspace/site:
python3 scripts/nov05/ig_nov6.py
"""
import sys
sys.path.insert(0,'scripts/nov05')
from uclaims import page

HUB=('/username-claim-questions/','All username claim questions')
REL=[('/instagram-username-claim/','Instagram username claims'),('/inactive-instagram-username/','Inactive usernames'),('/trademark-username-claim/','Trademark claims'),('/instagram-username-claim-links-and-forms-directory/','Official links'),HUB]
def X(u,t=None): return '<a href="%s" rel="noopener" target="_blank">%s</a>'%(u,t or u.replace('https://',''))
L={
 'inactive':('Inactive username help article',X('https://help.instagram.com/513717858639392'),'Instagram’s own answer for a handle on an account that seems inactive: pick an available version. There is no request form.'),
 'tmhow':('Report a username for trademark',X('https://help.instagram.com/2039132876317734'),'How Instagram handles usernames that may infringe a trademark. Usernames are first-come, first-served.'),
 'tmwhat':('What is a trademark violation',X('https://help.instagram.com/101826856646059'),'What counts and what does not. Use of a mark unrelated to its goods or services is not a violation.'),
 'tmform':('Trademark Report Form',X('https://help.instagram.com/contact/230197320740525'),'The form rights owners file. Your name, email and the nature of the report are shared with the reported account.'),
 'imp':('Report impersonation',X('https://help.instagram.com/1291391774792379'),'In-app report for accounts pretending to be you, someone you represent or a business.'),
 'impform':('Impersonation form',X('https://help.instagram.com/contact/636276399721841'),'Web form when you cannot report from the app.'),
 'hacked':('Hacked account',X('https://www.instagram.com/hacked/'),'Start here if a hacker took the account or changed your username.'),
 'terms':('Instagram Terms of Use',X('https://help.instagram.com/581066165581870'),'Bans buying, selling or transferring accounts and usernames.'),
 'euipo':('EUIPO',X('https://www.euipo.europa.eu/'),'EU trade mark, one registration for all EU countries.'),
 'memorial':('Memorialized accounts',X('https://help.instagram.com/231764660354890'),'How Instagram memorializes an account after someone has passed away.'),
}
def table(*keys,title='Official links'):
  return ('links',title,'<div class="table-wrap"><table><thead><tr><th>Link</th><th>What it is for</th></tr></thead><tbody>'+''.join('<tr><td><strong>%s</strong><br>%s</td><td>%s</td></tr>'%L[k] for k in keys)+'</tbody></table></div>')
def ul(*x): return '<ul>'+''.join('<li>%s</li>'%i for i in x)+'</ul>'
def ol(*x): return '<ol>'+''.join('<li>%s</li>'%i for i in x)+'</ol>'
def p(x): return '<p>%s</p>'%x
WHICH=('which','Which do you need?',ul(
 '<strong>Handle on a dead or empty account:</strong> see <a href="/can-i-claim-an-inactive-instagram-username/">can I claim an inactive Instagram username</a>.',
 '<strong>Handle that matches your brand:</strong> see <a href="/someone-has-my-brand-name-on-instagram/">someone has my brand name on Instagram</a>.',
 '<strong>Account pretending to be you:</strong> see <a href="/instagram-impersonator-using-my-username/">impersonator using my username</a>.',
 '<strong>Lost your own handle:</strong> see <a href="/get-instagram-username-back-after-ban/">after a ban</a> or <a href="/get-instagram-username-back-after-deleting-account/">after deleting</a>.'))
EU=('eu','If you are in the EU',p('Under the EU Digital Services Act, Instagram has to explain moderation decisions and offer an internal complaint route. If Instagram removes or restricts an account in a username dispute, you can also use a certified out-of-court body such as <a href="/appeals-centre-europe-instagram-facebook-suspension/">Appeals Centre Europe</a>. This does not create a right to someone else’s username.'))
B0=('before','Before you start',ul(
 'Write down the exact handle, with any dots or underscores.',
 'Screenshot the account holding it, with the date.',
 'Have your own profile link ready.',
 'If you rely on a trademark, have the registration number and office.',
 'Never share your password or login codes with anyone.'))

P=[]
def A(slug,title,desc,h1,lead,answer,cards,secs,faqs,tbl=None,rel=None):
  secs=list(secs)+[WHICH,B0,EU]
  if tbl: secs=secs+[table(*tbl)]
  P.append(page(slug,title,desc,h1,lead,answer,secs,faqs,'Instagram',(rel or [])+REL,cards=cards))

A('does-instagram-notify-the-holder-of-a-username-claim',
 'Does Instagram Notify the Holder of a Username Claim?','Does Instagram tell the person who holds a username when you file a trademark or impersonation report? What the reported account sees.','Does Instagram notify the holder of a username claim?',
 'Short answer, then what that means for your plan.',
 'Yes for trademark reports: Instagram’s Trademark Report Form says your name, email and the nature of the report are shared with the reported account. Impersonation reports are different; Instagram does not publish the same notice rule. Plan for the holder to learn that a rights report was filed.',
 [('Trademark form','They see your name and email.'),('Impersonation','Different path; less public detail.'),('Plan ahead','Do not expect a silent claim.')],
 [('what','What the holder sees on a trademark report',p('Instagram’s own trademark help says the reported account is told your name, email and the nature of the report. They are not given your full evidence package the same way, but they know a rights owner contacted Instagram about the username.')),
  ('prep','How to prepare',ul('Use a business email you are fine having shared.','Keep screenshots dated before you file.','Have your registered mark details ready.','See also <a href="/can-the-other-account-see-my-instagram-trademark-report/">can the other account see my trademark report</a>.'))],
 [('Will they get my phone number?','Instagram’s trademark form language covers name, email and the nature of the report. Read the current form text before you submit.'),
  ('Can I file anonymously?','Not through the Trademark Report Form. Rights owners identify themselves.'),
  ('Does Unbanz file in your name?','We prepare and file through Instagram’s own tools. The price depends on the handle; you get the quote in chat before anything starts.')],
 tbl=['tmhow','tmform','imp','impform'])

A('can-i-claim-an-instagram-username-with-an-euipo-trademark',
 'Can I Claim an Instagram Username With an EUIPO Trademark?','Can an EU trade mark (EUIPO) support an Instagram username claim? What the Trademark Report Form asks and how EUIPO fits.','Can I claim an Instagram username with an EUIPO trademark?',
 'EU brands often ask whether one EUIPO mark is enough.',
 'Yes, an EUIPO (EU trade mark) registration can be used as the registered mark on Instagram’s Trademark Report Form. The form asks for registration details and country of registration. Strength still depends on whether the account uses your mark for related goods or services in a confusing way. Instagram decides.',
 [('EUIPO works','One EU registration covers all EU countries.'),('Related use','The account must use it in your field.'),('Form details','Registration number and owner name.')],
 [('how','How EUIPO fits the form',ol('Have the EU trade mark number and the owner name exactly as registered.','Confirm the goods or services cover how the Instagram account is used.','File Instagram’s Trademark Report Form with the EUIPO details.','Keep proof of the registration certificate ready if Instagram asks.')),
  ('limits','Limits to know',ul('An unused handle is not automatically a violation.','A pending EUIPO application is weaker than a registration.','A real other business with the same name in another field may not be a violation.')+p('More offices: <a href="/instagram-username-trademark-offices-directory/">trademark offices directory</a>. Related: <a href="/can-an-international-trademark-be-used-for-an-instagram-username/">international trademarks</a> and <a href="/instagram-username-trademark-claim-eu/">Instagram username trademark claim in the EU</a>.'))],
 [('Do I need a trademark in every EU country?','An EUIPO registration already covers all EU member states as one mark.'),
  ('Is UKIPO the same after Brexit?','No. The UK uses UKIPO. See <a href="/instagram-username-claim-uk/">Instagram username claim in the UK</a>.'),
  ('How much does Unbanz charge?','It depends on the handle. You get your quote in the chat before anything starts. 100% refund if the username claim fails.')],
 tbl=['euipo','tmform','tmwhat','tmhow'])

A('what-happens-to-an-instagram-username-during-a-180-day-disable',
 'What Happens to an Instagram Username During a 180-Day Disable?','When Instagram or Facebook shows a long disable or suspension window, what happens to the Instagram username and whether someone else can take it.','What happens to an Instagram username during a 180-day disable?',
 'A long disable window makes people worry the handle will slip away.',
 'While an Instagram account is disabled or suspended, it usually still holds its username. Other people generally cannot take that handle during the window. If the account is permanently removed later, the username can become available on a first-come, first-served basis. Restoring your own account is still the cleanest way to keep the handle.',
 [('Held while disabled','The name usually stays with the account.'),('Appeal first','Getting the account back keeps the handle.'),('After removal','The name can free up later.')],
 [('own','If it is your account',ul('Appeal from the disabled notice. See <a href="/guides/instagram-account-suspended-appeal/">Instagram suspended appeal</a>.','Do not create a second account just to grab the same handle.','If the appeal ends and the account is gone, a separate username claim may fit when the handle matches your brand or someone else took it unfairly.')+p('Also: <a href="/get-instagram-username-back-after-ban/">get your username back after a ban</a> and <a href="/instagram-username-held-by-a-banned-account/">username held by a banned account</a>.')),
  ('other','If someone else’s account is in a long disable',p('You still need a legit route: trademark, impersonation, or waiting until Instagram removes the account. Inactivity or a long disable alone is not a public request form.'))],
 [('Can I reserve the handle while I wait?','No. Instagram does not let anyone reserve usernames.'),
  ('Does a 180-day Facebook notice free an Instagram handle?','Not by itself. Linked accounts can be affected, but the Instagram username stays with its account until that account changes or is removed.'),
  ('Can Unbanz help during the window?','If the goal is recovering your disabled account, that is an unban route. If the goal is a handle on someone else’s disabled account, we only proceed when a legit Instagram route exists. Price depends on the handle.')],
 tbl=['inactive','hacked','terms','tmform'])

A('how-to-prepare-screenshots-for-an-instagram-username-claim',
 'How to Prepare Screenshots for an Instagram Username Claim','Which screenshots to take before an Instagram username claim: the holding profile, dates, trademark proof and your own @.','How to prepare screenshots for an Instagram username claim?',
 'Clear evidence speeds up the right route. Bad crops slow everything down.',
 'Before any Instagram username claim, screenshot the holding profile (username, name, bio, highlights and recent posts), the date on your device, your own profile link, and your trademark registration if you use that route. Do not edit or annotate over the important text. Never include passwords or login codes.',
 [('Full profile','Username, bio and posts.'),('Date visible','Device date or in-app timestamp.'),('Your @ ready','The profile that will receive the handle.')],
 [('list','Screenshot checklist',ol('The profile page showing the exact @username.','The name field and bio.','A grid or post that shows how they use your brand, if relevant.','Any impersonation messages or story replies, if relevant.','Your trademark certificate or EUIPO/USPTO record, for a trademark route.','Your own Instagram profile link and a screenshot of Edit profile.')),
  ('do-not','What not to do',ul('Do not crop out the username.','Do not send password screens or 2FA codes.','Do not submit edited memes or fake stamps.','Do not mass-report while you gather evidence.')+p('Related: <a href="/documents-needed-for-instagram-username-claim/">documents needed</a> and <a href="/what-to-send-for-an-instagram-username-claim/">what to send for a claim</a>.'))],
 [('Do screenshots expire?','Take fresh ones close to filing. Old screenshots can still help as history.'),
  ('Should I send videos too?','A short screen recording can help for stories that disappear, but still keep still screenshots.'),
  ('Where do I send them?','WhatsApp <a href="https://wa.me/19342012490">+1 934 201 2490</a> or team@unbanz.com. Asking is free; the price depends on the handle.')],
 tbl=['tmform','impform','inactive','terms'])

print('wrote',len(P),'ig pages:',P)
