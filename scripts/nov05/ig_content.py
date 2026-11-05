def ul(*x): return '<ul>'+''.join('<li>%s</li>'%i for i in x)+'</ul>'
def ol(*x): return '<ol>'+''.join('<li>%s</li>'%i for i in x)+'</ol>'
def p(x): return '<p>%s</p>'%x
WHICH=('which','Which do you need?',ul('<strong>Handle on a dead or empty account:</strong> see <a href="/can-i-claim-an-inactive-instagram-username/">can I claim an inactive Instagram username</a>.','<strong>Handle that matches your brand:</strong> see <a href="/someone-has-my-brand-name-on-instagram/">someone has my brand name on Instagram</a>.','<strong>Account pretending to be you:</strong> see <a href="/instagram-impersonator-using-my-username/">impersonator using my username</a>.','<strong>Lost your own handle:</strong> see <a href="/get-instagram-username-back-after-ban/">after a ban</a>, <a href="/instagram-username-taken-after-hack-and-sold/">after a hack</a> or <a href="/get-instagram-username-back-after-deleting-account/">after deleting</a>.'))
EU=('eu','If you are in the EU',p('Under the EU Digital Services Act, Instagram has to explain moderation decisions and offer an internal complaint route. If Instagram removes or restricts an account in a username dispute, you can also use a certified out-of-court body such as <a href="/appeals-centre-europe-instagram-facebook-suspension/">Appeals Centre Europe</a>. This does not create a right to someone else’s username.'))
def BEFORE(*x): return ('before','Before you start',ul(*x))
B0=BEFORE('Write down the exact handle, with any dots or underscores.','Screenshot the account holding it, with the date.','Have your own profile link ready.','If you rely on a trademark, have the registration number and office.','Never share your password or login codes with anyone.')
OFF=('official','Official route','')
# ---------- Directories & listicles ----------
A('instagram-username-claim-links-and-forms-directory','Instagram Username Claim Links and Forms (Directory)','Every official Instagram link for username problems: inactive handles, trademark reports, impersonation, hacked accounts and the rules on selling usernames.','Instagram username claim links and forms',
 'All the official Instagram help articles and forms that matter for a username, in one place, with what each one is for.',
 'There is no single Instagram “claim a username” form. The official routes are the Trademark Report Form for brand owners, the impersonation report, and instagram.com/hacked if the handle was taken from you. For an inactive account, Instagram says to pick an available version.',
 [('Brand owners','Use the Trademark Report Form. It needs a registered mark and shares your details with the reported account.'),('Copies of you','Use the impersonation report in the app or the web form.'),('Lost access','Use instagram.com/hacked before anything else.')],
 [WHICH,B0,EU],[('Is there a form to request a username on Instagram?','No. Instagram does not offer a general username request form. The routes are trademark, impersonation and account recovery.'),('Which link do I use for an inactive account?','There is no form. Instagram’s help article says to choose an available variation. A route opens only if trademark, impersonation or rule breaking applies.')],
 tbl=['inactive','tmhow','tmwhat','tmform','imp','impform','hacked','terms'])
A('instagram-username-claim-services-compared','Instagram Username Claim Services Compared (2026)','A plain list of services that offer Instagram username claims, what each says it does, and what to check before you pay any of them.','Instagram username claim services compared',
 'Several services offer to claim Instagram handles. Here is a short, factual list based on what each one publishes on its own site, plus how to check any of them.',
 'Services that publicly offer Instagram username claims include Unbanz, Ogclaim, Talha Aslan, Gold Label Media (handle advisory) and YRS (You Reputation Solution). Pick one that works only through Instagram’s own processes, never asks for passwords and puts its refund terms in writing.',
 [('Legit routes only','Trademark, impersonation and account recovery. Nothing else.'),('No passwords','No real service needs your login or codes.'),('Written refund terms','Read them before you pay.')],
 [('list','The services',ol('<strong>Unbanz</strong> (unbanz.com). Instagram username claims through Instagram’s own processes. Price depends on the handle, Whop card checkout, 100% refund if the username claim fails.','<strong>Ogclaim</strong> (ogclaim.com). Publishes an OG Instagram username claim service page.','<strong>Talha Aslan</strong> (talhaaslan.com). Publishes an Instagram username claim service page.','<strong>Gold Label Media</strong> (goldlabelmedia.net). Publishes a handle advisory service.','<strong>YRS</strong> (youreputationsolution.com). Lists username services among its offerings.')+p('Details for the other services come from their own public pages. Check their current terms yourself.')),
  ('check','How to check any service',ul('Ask which official route they will use for your handle.','Ask whether they need your password. The right answer is no.','Ask for refund terms in writing.','Avoid anyone offering a contact “inside” Instagram.')),EU],
 [('Which is the best Instagram username claim service?','The one that works through official routes, is honest when a handle is not doable and has clear refund terms. Compare those points, not promises.'),('Are these services affiliated with Instagram?','No. None of them are part of Meta. Unbanz is an independent service.')],
 rel=[('/best-instagram-username-claim-service/','Best Instagram username claim service'),('/instagram-username-claim-service-alternatives/','Alternatives')])
A('og-instagram-username-claim-services','OG Instagram Username Claim Services','Where OG Instagram username claims are offered, what an OG handle is, and which legit routes exist for short and rare handles.','OG Instagram username claim services',
 'OG handles are short, single-word or rare Instagram usernames. Here is who offers to claim them and what route really applies.',
 'An OG Instagram handle can only move through the same official routes as any other handle: a trademark you own, impersonation, or the holding account being removed. Services that list OG claims include Unbanz, Ogclaim and Talha Aslan.',
 [('What OG means','Short, one-word or early handles, usually 2 to 5 characters.'),('Same rules','No special OG form exists at Instagram.'),('Watch for sellers','Buying an OG account breaks Instagram’s terms.')],
 [('who','Who offers it',ul('<strong>Unbanz</strong>: OG and short handles via official routes. See <a href="/og-username/">OG usernames</a>.','<strong>Ogclaim</strong>: publishes an OG Instagram username claim page.','<strong>Talha Aslan</strong>: publishes an Instagram username claim page.')),
  ('route','Which route fits an OG handle',p('Most OG handles are dictionary words or initials. A trademark route needs a registered mark for that exact word in your field. Where no route exists, an honest service says so.')),WHICH],
 [('Can I get a 3 letter OG Instagram handle?','Only if a legit route applies, usually a matching registered trademark. See <a href="/are-3-letter-instagram-usernames-available/">3 letter usernames</a>.'),('Why are OG handles sold online?','Because people trade accounts, which breaks Instagram’s terms. Those accounts can be recovered by the original owner or removed.')],tbl=['tmhow','tmform','terms'])
A('where-to-get-an-inactive-instagram-handle','Where to Get an Inactive Instagram Handle','Where you can and cannot get an inactive Instagram handle, what Instagram says, and the legit routes that exist.','Where to get an inactive Instagram handle',
 'You found the perfect handle, but the account has not posted in years. Here is where people actually get handles like that, legitimately.',
 'Instagram does not hand out inactive handles on request. The legit places are: the Trademark Report Form if you own the mark, the impersonation report if the account copies you, waiting for the owner to delete it, or a service that works those routes for you.',
 [('Not from sellers','Marketplaces selling accounts break Instagram’s terms.'),('Not from support','Instagram support does not reassign handles.'),('Yes via official routes','Trademark, impersonation, removal.')],
 [('where','Places that work',ol('Instagram’s Trademark Report Form, for registered marks.','The impersonation report, if the account pretends to be you.','The account owner, if they choose to change their own handle. No payment for login details.','A service like Unbanz that handles official routes for you.')),
  ('not','Places that do not',ul('Account marketplaces and “handle shops”.','Anyone claiming a contact at Meta.','Tools promising to “release” a handle.')),B0],
 [('Can I buy an inactive Instagram account?','Buying or selling accounts is against Instagram’s Terms of Use. See <a href="/is-selling-instagram-usernames-allowed/">is selling usernames allowed</a>.'),('Will Instagram ever free an inactive handle?','Instagram does not publish an inactivity rule. Handles free up when accounts are deleted or removed.')],tbl=['inactive','tmform','terms'])
A('instagram-username-claim-service-alternatives','Instagram Username Claim Service Alternatives','Alternatives to paying for an Instagram username claim: doing it yourself, choosing a variation, or using another service.','Alternatives to an Instagram username claim service',
 'You do not always need a service. Here are the honest alternatives, including doing the official steps yourself.',
 'You can file Instagram’s Trademark Report Form or impersonation report yourself for free. You can also choose an available variation, as Instagram suggests. A service helps when you want someone to pick the right route and prepare it.',
 [('Do it yourself','The official forms are free to use.'),('Use a variation','Add a word like official, hq or your city.'),('Use a service','Unbanz, Ogclaim, Talha Aslan and others.')],
 [('diy','Doing it yourself',ol('Check whether the account actually violates trademark or impersonation rules.','Use the matching official form.','Keep screenshots and your trademark details.','Wait for Instagram’s reply by email.')),
  ('var','Good variations',ul('yourbrand.official','yourbrandhq','getyourbrand','yourbrand_city')),EU],
 [('Is doing it myself cheaper?','Yes. The forms are free. You pay a service only for doing the work.'),('Do services have access I do not?','No legit service has special access. Be careful of anyone claiming otherwise.')],
 rel=[('/instagram-username-claim-services-compared/','Services compared')],tbl=['inactive','tmform','impform'])
def VS(slug,name,site,what):
  A(slug,'Unbanz vs %s for Instagram Username Claims'%name,'Unbanz vs %s: what each says it offers for Instagram username claims, and the questions to ask before choosing.'%name,'Unbanz vs %s'%name,
   'A plain comparison of Unbanz and %s for Instagram usernames, using only what each publishes.'%name,
   'Both Unbanz and %s (%s) publicly offer help with Instagram handles. Unbanz works only through Instagram’s own processes, prices by the handle, takes card payment through Whop checkout and gives a 100%% refund if the username claim fails. Check %s’s current terms on its own site.'%(name,site,name),
   [('Unbanz','Instagram username claims, price depends on the handle.'),(name,what),('Your choice','Compare routes, refund terms and how they handle passwords.')],
   [('table','Side by side','<div class="table-wrap"><table><thead><tr><th>Point</th><th>Unbanz</th><th>%s</th></tr></thead><tbody><tr><td>Published offer</td><td>Instagram username claims</td><td>%s</td></tr><tr><td>Price</td><td>Depends on the handle</td><td>See their site</td></tr><tr><td>Refund</td><td>100%% refund if a username claim fails</td><td>See their site</td></tr><tr><td>Passwords</td><td>Never asked</td><td>Ask them</td></tr></tbody></table></div>'%(name,what)),
    ('ask','Questions to ask either one',ul('Which official route fits my handle?','Do you need my login? (It should be no.)','What happens if it does not work?'))],
   [('Is %s affiliated with Unbanz?'%name,'No. They are separate businesses.'),('Is either affiliated with Instagram?','No. Neither is part of Meta.')],
   rel=[('/instagram-username-claim-services-compared/','Services compared')])
VS('unbanz-vs-ogclaim','Ogclaim','ogclaim.com','Publishes an OG Instagram username claim page')
VS('unbanz-vs-talha-aslan','Talha Aslan','talhaaslan.com','Publishes an Instagram username claim service page')
VS('unbanz-vs-gold-label-media','Gold Label Media','goldlabelmedia.net','Publishes a handle advisory service')
VS('unbanz-vs-yrs-username','YRS','youreputationsolution.com','Lists username services among its offerings')
A('instagram-username-trademark-offices-directory','Trademark Offices for Instagram Username Claims (Directory)','Which trademark office to use for an Instagram username claim: USPTO, UKIPO, CIPO, EUIPO, INPI, BOIP and WIPO Madrid.','Trademark offices for Instagram username claims',
 'Instagram’s trademark route needs a registered mark. Here is where marks are registered in the countries we cover.',
 'Instagram’s Trademark Report Form asks for a registered trademark and the country of registration. The main offices are USPTO (US), UKIPO (UK), CIPO (Canada), EUIPO (EU-wide), INPI (France), BOIP (Netherlands and Benelux) and WIPO’s Madrid System for international marks.',
 [('Registered beats pending','A filed application is weaker than a registration.'),('Match the word','The mark should match the handle.'),('Match the field','The account should use it for related goods or services.')],
 [('which','Which office fits you',ul('Selling in the US: USPTO.','UK: UKIPO.','Canada: CIPO.','Several EU countries: EUIPO.','France only: INPI.','Netherlands, Belgium, Luxembourg: BOIP.','Many countries at once: WIPO Madrid.')),EU],
 [('Does Instagram accept any country’s trademark?','The form asks where the mark is registered. A national registration is accepted as evidence; how it applies depends on the account.'),('Is a logo mark enough?','A word mark is clearer for a username. See <a href="/word-or-logo-trademark-for-instagram-username/">word or logo trademark</a>.')],
 tbl=['uspto','ukipo','cipo','euipo','inpi','boip','wipo','tmform'])
A('instagram-username-help-articles-explained','Instagram Username Help Articles Explained','What each Instagram help article about usernames actually says, in plain words.','Instagram username help articles explained',
 'Instagram’s help pages about usernames are short and scattered. Here is what each one says.',
 'In short, Instagram says: usernames are first-come, first-served and cannot be reserved; there is no form for inactive handles; brand owners can report trademark use; impersonation can be reported; and buying or selling usernames is against the terms.',
 [('First-come','Nobody can reserve a username.'),('Inactive','Choose a variation.'),('Trademark','Report with a registered mark.')],
 [('each','What each one says',ul('<strong>Inactive account article:</strong> if a username is claimed but seems inactive, choose an available variation.','<strong>Trademark violation article:</strong> using a mark in a way unrelated to its goods or services is not a violation.','<strong>Trademark username article:</strong> how to report a username that infringes your mark.','<strong>Impersonation article:</strong> how to report accounts pretending to be you.','<strong>Terms of Use:</strong> no buying, selling or transferring accounts or usernames.'))],
 [('Do help articles change?','Yes. Always open the current version from the links below.'),('Is there a hidden username request article?','No. There is no public general username request route.')],tbl=['inactive','tmwhat','tmhow','imp','terms'])
A('instagram-username-seller-red-flags','Instagram Username Seller Red Flags (List)','Red flags that an Instagram username seller or claim service is a scam: passwords, inside contacts, crypto only and more.','Red flags for Instagram username sellers',
 'Handle scams are common. These are the signs to walk away.',
 'Walk away if anyone asks for your password or login code, claims a contact inside Meta, sells an account rather than claiming through official routes, wants payment only in crypto or gift cards, or promises a handle by a date.',
 [('Passwords','No legit service needs them.'),('Inside contacts','Nobody legit has one.'),('Account sales','Against Instagram’s terms.')],
 [('list','The red flags',ol('Asks for your password, codes or to log in through their link.','Claims an “admin” or “plug” at Instagram.','Sells an existing account with the handle.','Wants gift cards or crypto only.','Promises a result by a set date.','Has no written refund terms.')),('safe','What safe looks like',p('A named route, no login needed, card payment with a clear checkout and written refund terms. See <a href="/instagram-username-claim-scams/">username claim scams</a>.'))],
 [('I already paid a scammer. What now?','Stop paying, change your password, turn on two-factor authentication and contact your card provider.'),('Can a scammer take my account?','If you shared login details, yes. Secure it at instagram.com/hacked if you lost access.')],tbl=['hacked','terms'])
A('documents-needed-for-instagram-username-claim','Documents Needed for an Instagram Username Claim','The documents and details you need for an Instagram username claim: trademark registration, ID, screenshots and links.','Documents needed for an Instagram username claim',
 'What to gather before any Instagram username claim, by route.',
 'For a trademark route you need the registration number, office, owner name and the goods or services covered. For impersonation you need proof of identity and the account link. For every route: the exact handle, screenshots and your own profile link.',
 [('Trademark','Registration number, office, owner.'),('Impersonation','ID and the account link.'),('Always','Handle, screenshots, your profile.')],
 [('tm','Trademark route',ul('Registration number and certificate.','Office and country.','Owner name exactly as registered.','Goods or services covered.','If you are an agent, authorisation from the owner.')),('imp','Impersonation route',ul('A government ID of the person impersonated, or business proof.','The impersonating account link.')),('never','Never needed',p('Your password or login codes.'))],
 [('Do I need a lawyer?','No. The forms are made for rights owners. Some people use a lawyer for complex marks.'),('Will Instagram share my documents?','The trademark form shares your name, email and the nature of the report with the reported account.')],tbl=['tmform','impform'])
# ---------- Question pages ----------
def Q(slug,title,desc,h1,lead,answer,cards,secs,faqs,tbl=None,rel=None):
  A(slug,title,desc,h1,lead,answer,cards,secs+[WHICH],faqs,rel=rel,tbl=tbl)
Q('can-i-claim-an-inactive-instagram-username','Can I Claim an Inactive Instagram Username?','Can you claim an inactive Instagram username? What Instagram says, the routes that exist and what to do next.','Can I claim an inactive Instagram username?',
 'Short answer, then the detail.',
 'Not just because it is inactive. Instagram’s help says to choose an available variation when a username seems inactive. An inactive handle can move only through another route: your registered trademark, impersonation, or the account being removed or deleted.',
 [('Inactivity alone','Not a route.'),('Trademark','Often the main route.'),('Removal','If the account breaks rules.')],
 [('routes','Routes that can work',ul('You own a registered trademark that matches and the account uses it for related things.','The account pretends to be you.','The owner deletes the account.')),B0],
 [('How long until Instagram frees it?','Instagram publishes no inactivity timeline.'),('Can I report it as inactive?','There is no inactive report form.')],tbl=['inactive','tmform'])
Q('someone-has-my-brand-name-on-instagram','Someone Has My Brand Name on Instagram. What Can I Do?','Someone took your brand name as an Instagram username. What you can do through trademark and impersonation routes.','Someone has my brand name on Instagram',
 'Your brand name is taken on Instagram. Here is what usually works.',
 'If you have a registered trademark for the name and the account uses it for related goods or services, or to confuse people, file Instagram’s Trademark Report Form. If the account poses as your business, use the impersonation report. Without a mark, options are limited.',
 [('Registered mark','The strongest position.'),('Copycat','Report impersonation.'),('Real other business','Often not a violation.')],
 [('check','Check how they use it',p('Instagram says using a mark in a way unrelated to its goods or services is not a violation. A bakery called your name is different from a copy of your shop.')),B0],
 [('Can I report without a trademark?','Not under trademark. You may still report impersonation.'),('Will they know I reported?','Yes, the form shares your name and email with them.')],tbl=['tmwhat','tmform','imp'])
Q('is-selling-instagram-usernames-allowed','Is Selling Instagram Usernames Allowed?','Is it allowed to sell or buy Instagram usernames? What Instagram’s Terms of Use say and the risks.','Is selling Instagram usernames allowed?',
 'People sell handles every day. That does not make it allowed.',
 'No. Instagram’s Terms of Use say you cannot buy, sell or transfer any aspect of your account, including your username. A bought handle can be reclaimed by the original owner or removed by Instagram.',
 [('Terms','No buying, selling or transferring.'),('Risk','The handle can be pulled back.'),('Legit way','Official routes only.')],
 [('why','Why it matters',p('If you pay a seller and log into their account, you have no rights under the terms. Recovery by the seller is common.'))],
 [('Is paying a claim service the same as buying a username?','No. A claim service works through official routes onto your own profile. It does not sell accounts.'),('Can I sell my own handle?','Instagram’s terms do not allow it.')],tbl=['terms'])
Q('how-much-does-an-og-instagram-handle-cost','How Much Does an OG Instagram Handle Cost?','How much an OG Instagram handle costs to claim, and why handle sales are risky.','How much does an OG Instagram handle cost?',
 'There is no list price for OG handles.',
 'With Unbanz, the price depends on the handle. You get your quote in the chat before anything starts, pay by card through Whop checkout, and get a 100% refund if the username claim fails. Prices you see on account markets are for sales that break Instagram’s terms.',
 [('Depends on the handle','Length, route and who holds it matter.'),('Quote first','Before anything starts.'),('Refund','100% if the claim fails.')],
 [('drivers','What changes the price',ul('Whether there is a legit route.','How short or common the word is.','What the holding account is doing.'))],
 [('Is a 2 letter handle more expensive?','Usually harder, so it depends on the handle.'),('Can I pay later?','Payment is by card through Whop checkout once you agree to the quote.')],tbl=['terms'])
Q('can-instagram-give-you-a-taken-username','Can Instagram Give You a Taken Username?','Can Instagram give you a username someone else has? When Instagram moves a taken handle and when it will not.','Can Instagram give you a taken username?',
 'Instagram support does not hand over taken handles on request.',
 'Instagram can remove or change a username after a valid trademark report, and can act on impersonation. It does not give a taken username to you just because you ask, want it more or are verified.',
 [('Trademark','Instagram may act on a valid report.'),('Impersonation','The account may be removed.'),('Requests','Not a route.')],
 [('after','What happens after a valid report',p('Instagram may remove or change the handle. It is then first-come, first-served, so be ready to set it on your profile.'))],
 [('Does Meta Verified help?','Meta Verified does not include username requests. See <a href="/can-meta-verified-get-me-an-instagram-username/">Meta Verified and usernames</a>.'),('Can I email Instagram?','There is no username request email.')],tbl=['tmhow','imp'])
Q('what-counts-as-trademark-infringement-in-an-instagram-username','What Counts as a Trademark Violation in an Instagram Username?','When an Instagram username violates a trademark, and when it does not, by Instagram’s own help.','What counts as a trademark violation in an Instagram username?',
 'Not every use of your brand word is a violation.',
 'A username can violate a trademark when it uses your registered mark for related goods or services in a way likely to confuse people. Instagram says using the mark in a way unrelated to its goods or services is generally not a violation.',
 [('Related use','Same goods or services.'),('Confusion','People think it is you.'),('Unrelated use','Usually fine.')],
 [('examples','Examples',ul('Your shoe brand name used by a shop selling shoes: likely.','Same word used by a person as their own name: usually not.','Same word used by a fan page that does not sell anything: depends.'))],
 [('Is an unused account a violation?','Holding a handle without use is not automatically a violation.'),('Do I need a registered mark?','Yes, the trademark form asks for registration details.')],tbl=['tmwhat','tmform'])
Q('why-isnt-this-instagram-username-available-if-no-one-uses-it','Why Isn’t This Instagram Username Available if No One Uses It?','Why Instagram says a username is not available when no account shows. Deleted, disabled, private and reserved handles explained.','Why isn’t this Instagram username available if no one uses it?',
 'You search the handle, nothing appears, but Instagram still says it is taken.',
 'Usually the handle is held by a disabled, deactivated, recently deleted or recently changed account, or Instagram is blocking it. These accounts do not show in search, but the name stays held.',
 [('Deactivated','Hidden but held.'),('Disabled','Held while Instagram decides.'),('Recently changed','Held for the old owner for a while.')],
 [('next','What to do',ol('Try the handle again later.','Check if it matches your trademark.','Ask us if there is a route.')+p('More on the notice: <a href="/instagram-this-username-isnt-available-notice/">“This username isn’t available”</a>.'))],
 [('Will it free up?','Sometimes. Instagram does not publish when.'),('Can a service free it?','Only through official routes.')],tbl=['inactive'])
Q('can-i-report-an-instagram-account-to-get-its-username','Can I Report an Instagram Account to Get Its Username?','Can you report an Instagram account to get its username? Which reports are legit and why false reports backfire.','Can I report an Instagram account to get its username?',
 'Reporting is a tool for real violations, not a way to take names.',
 'Only if the account really breaks a rule that affects you, such as trademark infringement or impersonation. False reports break Instagram’s rules and can harm your own account.',
 [('Real violation','Report it.'),('No violation','Do not report.'),('Mass reports','Not a route.')],
 [('not','What not to do',ul('Mass reporting.','Paying “report services”.','Filing a trademark report without a mark.'))],
 [('Does reporting give me the handle?','No. Even if the account is removed, the handle is first-come, first-served.'),('Can I report for an inactive account?','There is no inactive report.')],tbl=['tmform','imp'])
Q('does-instagram-release-inactive-usernames','Does Instagram Release Inactive Usernames?','Does Instagram release inactive usernames? What it says and what actually frees a handle.','Does Instagram release inactive usernames?',
 'A common belief is that Instagram cleans out old accounts. Here is the reality.',
 'Instagram does not publish a policy of releasing usernames after inactivity. Handles free up when the owner changes or deletes them, or when Instagram removes the account.',
 [('No public rule','No inactivity timer.'),('Deletion','Frees the name eventually.'),('Removal','Frees the name when the account goes.')],
 [('why','Why some do free up',p('Accounts get removed for breaking rules, or owners delete them. That can look like a release.'))],
 [('Should I keep checking?','You can. Also check if a legit route applies.'),('Does a username tool help?','Tools only check availability.')],tbl=['inactive'])
Q('how-long-does-instagram-hold-a-username-after-deletion','How Long Does Instagram Hold a Username After Deletion?','How long a deleted Instagram account keeps its username, and when it may become available.','How long does Instagram hold a username after deletion?',
 'What happens to a username when an account is deleted.',
 'When someone asks to delete an Instagram account, it is held for 30 days, during which they can cancel. After that, deletion is processed. Instagram does not promise when the username becomes available again.',
 [('30 days','The deletion window.'),('After that','Deletion goes through.'),('No promise','On when the name frees.')],
 [('own','If it was your account',p('See <a href="/get-instagram-username-back-after-deleting-account/">get your username back after deleting</a>.'))],
 [('Can I reserve it?','No. Usernames cannot be reserved.'),('Can someone else take it first?','Yes, it is first-come, first-served.')])
Q('can-i-get-my-instagram-username-back-after-changing-it','Can I Get My Instagram Username Back After Changing It?','Changed your Instagram username and someone took the old one? What you can do.','Can I get my Instagram username back after changing it?',
 'You changed your handle and the old one is gone.',
 'Instagram lets you switch back within 14 days in many accounts if the old name is still free. If someone else already took it, there is no automatic way back; a route applies only if they impersonate you or infringe your mark.',
 [('Within 14 days','Try switching back.'),('Taken already','Check impersonation or trademark.'),('No form','For changed usernames.')],
 [('steps','Steps',ol('Try your old name in Edit profile.','If taken, screenshot the new holder.','Check if they copy you.'))],
 [('Why did it go so fast?','People watch for good names.'),('Can Unbanz help?','If a legit route exists, yes.')],tbl=['imp'])
Q('my-instagram-username-was-changed-without-permission','My Instagram Username Was Changed Without Permission','Your Instagram username changed without your permission. Secure the account and get the handle back.','My Instagram username was changed without permission',
 'A changed handle you did not make usually means someone else got in.',
 'Treat it as a hacked account. Go to instagram.com/hacked, secure your login and email, and change the username back if it is still free. If the hacker moved your old handle to another account, that is a separate step.',
 [('Secure first','instagram.com/hacked.'),('Change back','If still free.'),('Moved?','See after a hack.')],
 [('also','Also check',ul('Your email and phone on the account.','Two-factor authentication.','Logged-in devices.')+p('More: <a href="/instagram-username-taken-after-hack-and-sold/">username taken after a hack</a>.'))],
 [('Can a friend change it?','Only with your login. Change your password.'),('Do you need my login?','No. We never ask for passwords or codes.')],tbl=['hacked'])
Q('is-it-legal-to-claim-an-instagram-username','Is It Legal to Claim an Instagram Username?','Is claiming an Instagram username legal? The difference between official claims and buying or hacking.','Is it legal to claim an Instagram username?',
 'Claiming and stealing are not the same thing.',
 'Using Instagram’s own processes, like the Trademark Report Form or impersonation reports, is legitimate. Hacking accounts, buying stolen handles or filing false reports is not.',
 [('Official routes','Legit.'),('Buying accounts','Against terms.'),('Hacking','Illegal.')],
 [('ours','How we do it',p('Unbanz works only through official routes, onto your own profile.'))],
 [('Is this legal advice?','No. For a dispute over a trademark, talk to a lawyer.'),('Can I get in trouble for asking?','No. Asking is fine.')],tbl=['tmform','terms'])
Q('do-i-need-a-trademark-to-claim-an-instagram-username','Do I Need a Trademark to Claim an Instagram Username?','Do you need a trademark for an Instagram username claim? When it helps and what works without one.','Do I need a trademark to claim an Instagram username?',
 'A trademark is the most common route, but not the only one.',
 'For the trademark route, yes: Instagram’s form asks for a registered mark. Without one, routes are limited to impersonation, your own lost account, or the holding account being removed.',
 [('With a mark','Trademark route.'),('Without','Impersonation or recovery.'),('Pending','Weaker.')],
 [('get','Getting a mark',p('See the <a href="/instagram-username-trademark-offices-directory/">trademark offices directory</a>.'))],
 [('Will a pending application work?','See <a href="/does-a-pending-trademark-count-for-an-instagram-username/">pending trademarks</a>.'),('Do I need it in every country?','One registration is enough as evidence; strength depends on the account.')],tbl=['tmform'])
Q('can-i-claim-my-own-name-on-instagram','Can I Claim My Own Name on Instagram?','Someone has your personal name as an Instagram username. When you can claim it and when you cannot.','Can I claim my own name on Instagram?',
 'Your name is your name, but on Instagram handles are first-come, first-served.',
 'Only if the account impersonates you, or your name is a registered trademark used by the account for related things. Another person with the same name has the same right to it.',
 [('Impersonation','Report it.'),('Same name','Usually no route.'),('Trademark','If registered.')],
 [('tips','Good options',ul('yourname.official','yourname + your field')+p('For creators: <a href="/instagram-creator-name-taken/">creator name taken</a>.'))],
 [('Does fame matter?','Not by itself.'),('Does verification help?','Not for taking a handle.')],tbl=['imp','impform'])
Q('can-i-claim-my-business-name-on-instagram','Can I Claim My Business Name on Instagram?','Can you claim your business name on Instagram? Trademark, impersonation and the documents to have ready.','Can I claim my business name on Instagram?',
 'A business name is strongest when it is a registered mark.',
 'Yes, if your business name is a registered trademark and the account uses it for related goods or services or to pose as your business. A registered company name alone, without a trademark, is weaker.',
 [('Trademark','Main route.'),('Company register','Weaker.'),('Impersonation','If they pose as you.')],
 [('more','More',p('See <a href="/business-username-claim/">business username claims</a>.'))],
 [('Is a company registration enough?','It is not a trademark.'),('Can an agency file?','With authorisation from the owner.')],tbl=['tmform','impform'])
Q('what-happens-to-followers-when-you-claim-an-instagram-username','What Happens to Followers When You Claim an Instagram Username?','When you claim an Instagram username, do you get the followers? What moves and what does not.','What happens to followers when you claim an Instagram username?',
 'A claim moves a name, not an audience.',
 'You get the handle on your own profile. You do not get the old account’s followers, posts or messages. Your own followers stay with you.',
 [('Handle','Moves to you.'),('Old followers','Do not.'),('Your followers','Stay.')],
 [('plan','Plan the switch',ul('Tell your followers.','Update links in bio elsewhere.'))],
 [('Will my links break?','Links with the old handle stop working.'),('Will my posts stay?','Yes.')])
Q('can-meta-verified-get-me-an-instagram-username','Can Meta Verified Get Me an Instagram Username?','Does Meta Verified help get a taken Instagram username? What it includes and what it does not.','Can Meta Verified get me an Instagram username?',
 'Meta Verified offers a badge, support and protection. Not usernames.',
 'Meta Verified does not include requesting or reclaiming someone else’s username. It can help you contact support about your own account and impersonation.',
 [('Badge','Yes.'),('Support','For your account.'),('Username transfer','No.')],[],
 [('Is it worth it for a claim?','Not for the claim itself.'),('Does it help with impersonation?','It includes impersonation protection.')],tbl=['imp'])
Q('can-instagram-support-change-my-username','Can Instagram Support Change My Username?','Can Instagram support give you a username or change yours? What support does and does not do.','Can Instagram support change my username?',
 'You can change your own handle anytime the new one is free.',
 'You change your own username in Edit profile. Support does not assign taken usernames to you. It can act on trademark and impersonation reports.',
 [('Your change','Edit profile.'),('Taken name','Not via support.'),('Reports','Trademark, impersonation.')],[],
 [('Is there a support email for usernames?','No.'),('What about a support chat?','It will not reassign handles.')],tbl=['tmform','imp'])
Q('word-or-logo-trademark-for-instagram-username','Word or Logo Trademark for an Instagram Username?','Word mark vs logo mark for an Instagram username claim. Which is stronger.','Word or logo trademark for an Instagram username?',
 'Not all marks are equal for a username.',
 'A word mark protects the name itself and is the clearest match for a username. A logo mark protects the design; if the word is part of it, it can still help but is weaker.',
 [('Word mark','Clearest.'),('Logo mark','Weaker.'),('Both','Best.')],
 [('match','Match the handle',p('The handle should match the word closely.'))],
 [('Does spelling matter?','Yes.'),('Can I file a word mark now?','Yes, at your office.')],tbl=['uspto','euipo','ukipo'])
Q('can-an-international-trademark-be-used-for-an-instagram-username','Can an International Trademark Be Used for an Instagram Username?','Using a WIPO Madrid or foreign trademark for an Instagram username claim.','Can an international trademark be used for an Instagram username?',
 'Madrid registrations work through national offices.',
 'Yes. Instagram’s form asks for the registration and country. A WIPO Madrid registration designates countries; use the registration that covers where the mark is protected.',
 [('Madrid','Valid for designated countries.'),('National','Also valid.'),('EU','EUIPO for all EU.')],[],
 [('Do I need a US mark for a US account?','Not necessarily, but local coverage helps.'),('Where do I find my number?','In WIPO’s Madrid Monitor.')],tbl=['wipo','tmform'])
Q('does-a-pending-trademark-count-for-an-instagram-username','Does a Pending Trademark Count for an Instagram Username?','Does a trademark application count for an Instagram username claim?','Does a pending trademark count for an Instagram username?',
 'Filed is not registered.',
 'Instagram’s trademark form asks for a registered mark. A pending application is generally not enough on its own. Wait for registration where you can.',
 [('Registered','Strong.'),('Pending','Weak.'),('Meanwhile','Use a variation.')],[],
 [('How long does registration take?','It depends on the office.'),('Can I report impersonation meanwhile?','Yes, if it applies.')],tbl=['tmform'])
Q('what-happens-if-you-buy-an-instagram-account-for-the-username','What Happens If You Buy an Instagram Account for the Username?','The risks of buying an Instagram account just for its username.','What happens if you buy an Instagram account for the username?',
 'Buying looks quick. Here is what often follows.',
 'It breaks Instagram’s Terms of Use. The seller or original owner can recover the account, Instagram can disable it, and you have no recourse.',
 [('Terms','Broken.'),('Recovery','Seller can pull it back.'),('Money','Usually gone.')],[],
 [('Is it ever safe?','No.'),('What is the legit way?','Official routes.')],tbl=['terms'])
Q('how-do-people-get-og-instagram-usernames','How Do People Get OG Instagram Usernames?','How people really get OG Instagram usernames: early sign-up, trademarks, and unsafe trades.','How do people get OG Instagram usernames?',
 'Some got there first. Others used legit routes.',
 'Mostly by signing up early, catching a handle when it frees, or using a trademark route. Many traded handles come from account sales or hacks, which are not legit.',
 [('Early','Got there first.'),('Trademark','Legit route.'),('Trades','Not legit.')],[],
 [('Can I watch for a handle to free?','Yes, by checking it.'),('Are OG handles safe to buy?','No.')],tbl=['tmform','terms'])
def SHORT(n,word):
  Q('are-%s-letter-instagram-usernames-available'%n,'Are %s Letter Instagram Usernames Available?'%word,'Can you get a %s letter Instagram username? Availability and legit routes.'%n,'Are %s letter Instagram usernames available?'%word.lower(),
   '%s letter handles are among the rarest.'%word,
   'Almost all %s letter Instagram usernames are taken. One can move only through a legit route, usually a registered trademark for that exact string.'%n,
   [('Taken','Nearly all.'),('Trademark','The usual route.'),('Sellers','Avoid.')],[],
   [('Can I claim one with initials?','Only with a matching mark.'),('How much?','It depends on the handle.')],tbl=['tmform'],rel=[('/og-username/','OG usernames')])
SHORT('2','Two'); SHORT('3','Three'); SHORT('4','Four'); SHORT('5','Five')
Q('instagram-username-held-by-a-banned-account','Instagram Username Held by a Banned Account','The handle you want belongs to a banned or disabled Instagram account. What happens to the username.','Instagram username held by a banned account',
 'Disabled accounts can keep their handle.',
 'A disabled account can hold the username while Instagram decides, and while the owner appeals. It may free up after the account is permanently removed. There is no request form.',
 [('Held','During review.'),('Removed','May free up.'),('No form','To request it.')],[],
 [('How long?','Instagram does not say.'),('Can I check?','Try the handle later.')],tbl=['inactive'])
Q('instagram-username-held-by-a-private-account-with-no-posts','Instagram Username Held by a Private Account With No Posts','A private, empty account has your Instagram username. What you can do.','Instagram username held by a private account with no posts',
 'Empty private accounts are common squatters.',
 'An empty private account is not a violation by itself. A route applies if it uses your registered mark or poses as you.',
 [('Empty','Not a violation alone.'),('Your mark','Trademark route.'),('Your identity','Impersonation.')],[],
 [('Can I message them?','You can, but do not pay for login details.'),('Can I report it as fake?','Only if it impersonates.')],tbl=['tmform','imp'])
Q('someone-made-an-instagram-with-my-name-before-me','Someone Made an Instagram With My Name Before Me','Someone registered your name on Instagram before you did. When you can claim it.','Someone made an Instagram with my name before me',
 'Who was first matters on Instagram.',
 'Instagram is first-come, first-served. If the account pretends to be you, report impersonation. If it is a brand you registered, use the trademark form.',
 [('First-come','Rule.'),('Pretending','Impersonation.'),('Brand','Trademark.')],[],
 [('What if it is a fan page?','See <a href="/instagram-username-taken-by-fan-page/">fan pages</a>.'),('Can I get it back?','Only via a route.')],tbl=['imp','tmform'])
def NICHE(slug,who,line):
  Q(slug,'Instagram Username for %s'%who,'Getting the right Instagram username for %s: legit routes and what to prepare.'%who.lower(),'Instagram username for %s'%who.lower(),
   'Practical notes for %s.'%who.lower(),line,
   [('Trademark','If registered.'),('Impersonation','If copied.'),('Variation','Meanwhile.')],[B0],
   [('Does size matter?','No; the route matters.'),('Price?','It depends on the handle.')],tbl=['tmform','imp'])
NICHE('instagram-username-for-a-new-brand-launch','a New Brand Launch','Before launch, register your trademark and check the handle. If it is taken by an account using your mark for related goods, the trademark route applies once registered.')
NICHE('instagram-username-for-a-podcast','a Podcast','A podcast name is easier to claim when it is a registered word mark for entertainment services and the account holding it uses it for similar content.')
NICHE('instagram-username-for-athletes','Athletes','Athletes are often impersonated. If an account poses as you, the impersonation report is the route. Your name as a registered mark helps further.')
NICHE('instagram-username-for-a-nonprofit','a Nonprofit','A nonprofit name works like a brand name. A registered mark and proof that the account confuses supporters are the key points.')
NICHE('instagram-username-for-an-app-or-saas','an App or SaaS','An app name usually has a word mark for software. If the handle holder uses it for software or tech, the trademark route fits.')
Q('instagram-creator-name-taken','Instagram Creator Name Taken','Your creator name is taken on Instagram. What creators can do.','Instagram creator name taken',
 'For creators the name is the brand.',
 'If the account copies you, report impersonation. If your creator name is a registered mark, use the trademark route. If it is someone with the same name, choose a variation.',
 [('Copy','Impersonation.'),('Mark','Trademark.'),('Same name','Variation.')],[],
 [('Do follower counts matter?','No.'),('Can my manager file?','With authorisation.')],tbl=['imp','tmform'])
Q('instagram-username-taken-after-hack-and-sold','Instagram Username Taken After a Hack and Sold','A hacker took your Instagram handle and sold it. How to get it back through official routes.','Instagram username taken after a hack and sold',
 'Stolen handles often end up on another account.',
 'First recover your own account at instagram.com/hacked. Then report the account now holding your handle for impersonation if it copies you, or trademark if you hold a mark. Keep proof the handle was yours.',
 [('Recover','instagram.com/hacked.'),('Proof','Old screenshots.'),('Report','Matching route.')],[],
 [('Can I contact the buyer?','You can, but do not pay.'),('Can Unbanz help?','Yes, through official routes.')],tbl=['hacked','imp','tmform'])
Q('instagram-username-not-available-after-account-deleted','Instagram Username Not Available After Account Deleted','You deleted an account and the username still is not available.','Instagram username not available after account deleted',
 'Deletion takes time to clear.',
 'Instagram holds deleted accounts for 30 days and then processes deletion. The name may stay unavailable for a while after that.',
 [('30 days','Window.'),('Then','Processing.'),('Then','Maybe free.')],[],
 [('Can I speed it up?','No.'),('Can someone else grab it?','Yes, first-come.')])
Q('how-to-check-if-an-instagram-username-is-claimable','How to Check If an Instagram Username Is Claimable','A quick checklist to see whether a taken Instagram username has a legit route.','How to check if an Instagram username is claimable',
 'Five questions decide it.',
 'A taken handle is claimable when at least one route applies: your registered mark used by the account for related things, the account impersonates you, it was your account, or the account is being removed.',
 [('Mark','Do you own one?'),('Copy','Does it pose as you?'),('Yours','Was it yours?')],
 [('check','The checklist',ol('Do you hold a registered mark for the word?','Does the account use it for related goods or services?','Does it pretend to be you?','Was it your handle before?','Is the account disabled or deleted?'))],
 [('None apply?','Pick a variation.'),('Unsure?','Send us the handle.')],tbl=['tmwhat','imp'])
Q('what-to-send-for-an-instagram-username-claim','What to Send for an Instagram Username Claim','What to send Unbanz to check an Instagram username claim.','What to send for an Instagram username claim',
 'We only need a few things.',
 'Send the handle you want, your Instagram profile link, and any trademark details. We never ask for passwords or codes.',
 [('Handle','Exact.'),('Profile','Link.'),('Mark','If any.')],[],
 [('Do I pay to ask?','No.'),('Where do I send it?','WhatsApp or team@unbanz.com.')])
Q('what-does-unbanz-do-in-an-instagram-username-claim','What Does Unbanz Do in an Instagram Username Claim?','What Unbanz does in an Instagram username claim, step by step.','What does Unbanz do in an Instagram username claim?',
 'Plain steps, no secrets.',
 'Unbanz checks the handle, tells you if a legit route exists, prepares and files it through Instagram’s own processes, and helps set the handle on your own profile.',
 [('Check','Route or not.'),('Prepare','Documents.'),('File','Official forms.')],[],
 [('Do you hack?','No.'),('Do you sell accounts?','No.')])
Q('instagram-trademark-report-rejected-username','Instagram Trademark Report Rejected for a Username','Your Instagram trademark report about a username was rejected. Why and what to do.','Instagram trademark report rejected for a username',
 'Rejections usually have a clear reason.',
 'Common reasons: the mark is not registered, does not match, or the account uses the word in an unrelated way. Fix the issue or check another route.',
 [('Not registered','Wait.'),('Mismatch','Check spelling.'),('Unrelated use','Not a violation.')],[],
 [('Can I file again?','With new information.'),('Can you help?','Send us the reply.')],tbl=['tmwhat','tmform'])
Q('can-the-other-account-see-my-instagram-trademark-report','Can the Other Account See My Instagram Trademark Report?','Will the account you report see your name in an Instagram trademark report?','Can the other account see my Instagram trademark report?',
 'Yes, and that matters.',
 'Instagram says it may share your name, email and the nature of the report with the reported account. Use a business email.',
 [('Name','Shared.'),('Email','Shared.'),('Use','A business email.')],[],
 [('Can I stay anonymous?','Not on this form.'),('Can an agent file?','Yes, with authorisation.')],tbl=['tmform'])
# ---------- Countries ----------
def C(slug,title,h1,lead,answer,tb):
  A(slug,title,'%s. Legit routes, trademark offices and what to prepare.'%title,h1,lead,answer,
   [('Trademark','Local or EU mark.'),('Impersonation','Same everywhere.'),('Price','Depends on the handle.')],[B0,EU] if 'eu' in slug or 'france' in slug or 'netherlands' in slug else [B0],
   [('Does the country change Instagram’s rules?','No. The routes are the same; the trademark office differs.'),('Can I use an EU mark?','Yes, where it covers you.')],tbl=tb)
C('instagram-username-trademark-claim-canada','Instagram Username Trademark Claim in Canada','Instagram username trademark claim in Canada','For Canadian brands.','Canadian brands use a CIPO registration with Instagram’s Trademark Report Form.',['cipo','tmform'])
C('instagram-username-trademark-claim-france','Instagram Username Trademark Claim in France','Instagram username trademark claim in France','For French brands.','French brands use an INPI or EUIPO registration with Instagram’s Trademark Report Form.',['inpi','euipo','tmform'])
C('instagram-username-trademark-claim-netherlands','Instagram Username Trademark Claim in the Netherlands','Instagram username trademark claim in the Netherlands','For Dutch brands.','Dutch brands use a BOIP (Benelux) or EUIPO registration with Instagram’s Trademark Report Form.',['boip','euipo','tmform'])
C('instagram-username-trademark-claim-eu','Instagram Username Trademark Claim in the EU','Instagram username trademark claim in the EU','For EU brands.','An EUIPO trade mark covers all EU countries and works with Instagram’s Trademark Report Form.',['euipo','tmform'])
C('inactive-instagram-username-france','Inactive Instagram Username in France','Inactive Instagram username in France','For users in France.','Instagram’s rules on inactive handles are the same in France: choose a variation unless a trademark or impersonation route applies.',['inactive','inpi'])
C('inactive-instagram-username-netherlands','Inactive Instagram Username in the Netherlands','Inactive Instagram username in the Netherlands','For users in the Netherlands.','Same rules: no inactivity form. A BOIP or EUIPO mark opens the trademark route.',['inactive','boip'])
C('inactive-instagram-username-eu','Inactive Instagram Username in the EU','Inactive Instagram username in the EU','For EU users.','No EU rule frees inactive handles. The DSA gives complaint rights on moderation, not a right to a username.',['inactive','euipo'])
C('instagram-username-claim-eu','Instagram Username Claim in the EU','Instagram username claim in the EU','For EU brands and creators.','EU users have the same Instagram routes plus DSA complaint rights. An EUIPO mark is the strongest base.',['euipo','tmform','imp'])
