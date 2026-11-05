import sys; sys.path.insert(0,'scripts/nov05')
from uclaims import page
P=[]
HUB=('/username-claim-questions/','Username claim questions')
R={'Instagram':[('/instagram-username-claim/','Instagram username claims'),('/inactive-instagram-username/','Inactive usernames'),('/trademark-username-claim/','Trademark claims'),HUB,('/username/','Username claims')],
   'TikTok':[('/tiktok-username-claim/','TikTok username claims'),('/tiktok-inactive-username/','Inactive TikTok usernames'),('/tiktok-username-trademark-claim/','TikTok trademark claims'),HUB,('/username/','Username claims')],
   'Snapchat':[('/snapchat-username-claim/','Snapchat username claims'),('/snapchat-inactive-username/','Inactive Snapchat usernames'),('/snapchat-username-trademark-claim/','Snapchat trademark claims'),HUB,('/username/','Username claims')]}
def A(*a,**k): P.append(page(*a,**k))
PL={'TikTok':{'chg':'TikTok lets you change your username once every 30 days.','del':'A deleted TikTok account is deactivated for 30 days before it is permanently deleted.','ip':'TikTok’s intellectual property report form','imp':'TikTok’s impersonation report'},
    'Snapchat':{'chg':'Snapchat lets you change your username about once a year.','del':'A deleted Snapchat account is deactivated for 30 days before it is permanently deleted.','ip':'Snapchat’s intellectual property report on its Support site','imp':'Snapchat’s impersonation report'}}
for p,k in (('TikTok','tiktok'),('Snapchat','snapchat')):
  d=PL[p]; r=R[p]
  if p=='TikTok':
    A('tiktok-username-claim','TikTok Username Claim: Inactive, Taken and OG Handles','TikTok username claim help for inactive, taken, short and brand handles. Legit routes only, $1,200, 100% refund if the claim fails.','TikTok username claim',
      'Want a TikTok handle that an inactive account, a squatter or an impersonator is sitting on? We look at whether there is a legit route and handle it through TikTok’s own processes.',
      'A TikTok username claim works when there is a real route: a trademark or brand report, an impersonation report, or a dead account TikTok removes. Inactivity alone does not free a handle.',
      [('routes','Routes that can work','<ul><li><strong>Trademark or brand name.</strong> If you own the brand, %s is the main route.</li><li><strong>Impersonation.</strong> If the account pretends to be you or your business, %s applies.</li><li><strong>Squatting.</strong> TikTok’s rules do not allow holding usernames just to sell them.</li></ul>'%(d['ip'],d['imp'])),
       ('not','What we do not do','<p>No hacking, no buying stolen handles, no false reports. If a handle has no honest route, we tell you.</p>')],
      [('Can I claim any TikTok username I want?','No. It depends on who holds it and why. Send the handle and we tell you whether there is a route.')],p,r)
  A('%s-inactive-username'%k,'Can You Claim an Inactive %s Username?'%p,'Can you get a %s username from an inactive account? What %s says, which routes exist and what a claim costs.'%(p,p),'Can you claim an inactive %s username?'%p,
    'An account that has not posted in years can still hold the username you want. Here is what you can actually do.',
    '%s does not publish a rule that frees usernames after a set time of inactivity. A claim needs another route: trademark, impersonation, squatting or the account being removed.'%p,
    [('rule','What %s says'%p,'<p>There is no public form to request an inactive %s username. Inactive accounts usually keep their handle unless they are deleted or removed.</p>'%p),
     ('routes','When an inactive handle can move','<ul><li>The handle matches your registered trademark or brand.</li><li>The account impersonates you or your business.</li><li>The account breaks the rules and %s removes it.</li><li>The owner deletes it. %s</li></ul>'%(p,d['del']))],
    [('Does %s delete inactive accounts?'%p,'%s does not publish a timeline for removing inactive accounts.'%p),('Can I just message the owner?','You can. Never pay a stranger for login details; that breaks %s’s terms and the account can be pulled back.'%p)],p,r)
  A('%s-username-taken'%k,'%s Username Taken? What You Can Do'%p,'Your %s username is taken by someone else. When a claim is possible, which routes work and what it costs.'%p,'%s username taken: what can you do?'%p,
    'Someone has the %s handle you want. Sometimes there is a route, sometimes there isn’t.'%p,
    'If the account holding your name is inactive, impersonating you, squatting or using your trademark, there may be a route through %s’s own reports. If it is a real, active person using their own name, there usually is not.'%p,
    [('check','First check who holds it','<p>Look at the profile. Is it empty, dead, a fan page, a copy of you, or a real person with that name? The answer decides the route.</p>'),
     ('alt','If there is no route','<p>Pick a close version for now and keep your brand consistent across platforms. We will tell you straight when a handle is not claimable.</p>')],
    [('Is a taken %s username ever released?'%p,'Yes, when the account is deleted or removed. %s'%d['del'])],p,r)
  A('%s-og-short-username'%k,'How to Get an OG or Short %s Username'%p,'OG, rare, one-word and short %s usernames: how they move, which claims are legit and what to avoid.'%p,'How to get an OG or short %s username'%p,
    'Short, one-word and rare %s handles are the most wanted and the most scammed.'%p,
    'An OG %s handle is only claimable through a real route, usually a trademark or brand match or a dead account that %s removes. Buying one from a seller breaks %s’s terms.'%(p,p,p),
    [('who','Who can realistically claim one','<p>Brands and people whose registered name matches the handle have the strongest route. A short word with no link to you is much harder.</p>'),
     ('sellers','About OG handle sellers','<p>Handles sold on forums are often stolen. %s can take them back and the seller disappears.</p>'%p)],
    [('Can I buy an OG %s username?'%p,'Selling usernames breaks %s’s terms. We don’t buy or sell handles.'%p)],p,r)
  A('%s-username-trademark-claim'%k,'%s Username Trademark Claim for Your Brand'%p,'Use your trademark or brand name to claim a %s username. How the IP route works, what to prepare and what it costs.'%p,'%s username trademark claim'%p,
    'If an account is using your brand name as its %s handle, your trademark is the strongest route.'%p,
    'A registered trademark that matches the handle lets you report the account through %s. %s decides whether to act.'%(d['ip'],p),
    [('need','What helps','<ul><li>Registration number and office (USPTO, UKIPO, EUIPO, CIPO and others).</li><li>Proof the account uses your mark in a confusing way.</li><li>Your own active %s profile to receive the handle.</li></ul>'%p),
     ('no-tm','No registered trademark?','<p>An unregistered brand is weaker but not always hopeless, for example when the account impersonates your business. Ask us.</p>')],
    [('Does my trademark need to be in the same country?','It helps when it covers where the account operates. Send the details and we tell you if it fits.')],p,r)
  A('%s-impersonator-using-my-name'%k,'Impersonator Has My Name on %s: Getting the Username'%p,'Someone is pretending to be you or your business on %s and holds your name. How to report it and claim the username.'%p,'An impersonator is using my name on %s'%p,
    'A fake account using your name or brand is both a safety problem and a username problem.',
    'Report it through %s. If the account is removed, the handle can then be claimed onto your own profile, but %s makes the final call.'%(d['imp'],p),
    [('steps','What to do now','<ol><li>Screenshot the fake profile and its messages.</li><li>Warn followers from your real account.</li><li>Report it as impersonation, not just spam.</li></ol>')],
    [('Does removing the fake account give me the handle?','Not on its own. A freed handle can go back into the open pool. That is why a claim is filed with the removal.')],p,r)
  A('%s-username-back-after-ban'%k,'Get Your %s Username Back After a Ban'%p,'Lost your %s username when your account was banned? When you can get it back and what the routes are.'%p,'Get your %s username back after a ban'%p,
    'A banned %s account usually keeps its username, so nobody else can take it, including you on a new account.'%p,
    'The best route is usually getting the banned account back through %s’s appeal. If the account is gone for good, a claim may work when the handle matches your name or brand.'%p,
    [('appeal','Try the appeal first','<p>See <a href="/%s/">our %s help</a>. If the account returns, the handle comes back with it.</p>'%('tiktok-account-banned-appeal' if p=='TikTok' else 'snapchat-permanently-banned-appeal',p))],
    [('Can I use my old username on a new account?','Not while the banned account still holds it.')],p,r)
  A('%s-username-back-after-hack'%k,'Hacker Changed My %s Username: Get It Back'%p,'A hacker took your %s account or changed your username. Recover the account first, then the handle.'%p,'Hacker changed my %s username'%p,
    'Hackers often rename the account and grab or sell the original handle.',
    'Recover the account through %s’s hacked account process first. If someone else now holds your old handle, a claim may work when it matches your name or brand.'%p,
    [('first','First steps','<ol><li>Use %s’s hacked account recovery.</li><li>Change your password and turn on two-factor.</li><li>Check where your old handle is now.</li></ol>'%p)],
    [('Will %s give me my old username back automatically?'%p,'Not always. If it is still free you can switch back. %s'%d['chg'])],p,r)
  A('%s-username-back-after-deleting-account'%k,'Get Your %s Username Back After Deleting Your Account'%p,'Deleted your %s account and want the username back? How long you have and what to do if someone took it.'%p,'Get your %s username back after deleting your account'%p,
    'Deleting an account can free the handle for anyone.',
    '%s If you log back in during that window you can usually keep your username. After that it may be taken.'%d['del'],
    [('taken','If someone grabbed it','<p>A claim may work when the handle matches your registered brand or the new account impersonates you.</p>')],
    [('Can deleted usernames be reused?','After permanent deletion, the handle can become available to others.')],p,r)
  A('%s-username-not-available-notice'%k,'“This Username Isn’t Available” on %s: What It Means'%p,'What the %s “username isn’t available” or “already taken” notice means and whether the handle can be claimed.'%p,'“This username isn’t available” on %s'%p,
    'You type a handle and %s says it isn’t available, even when no profile shows up.'%p,
    'The notice means the name is held by an active, deactivated, banned or reserved account, or it breaks %s’s naming rules. It does not mean the handle can never move.'%p,
    [('why','Common reasons','<ul><li>An account holds it, even a private or banned one.</li><li>A deactivated account is still inside its 30-day window.</li><li>The name is reserved or blocked by %s.</li><li>It uses characters or words %s does not allow.</li></ul>'%(p,p))],
    [('No profile shows up. Why is it still unavailable?','Banned, deactivated and reserved accounts often don’t show in search.')],p,r)
  A('%s-username-claim-cost'%k,'How Much Does a %s Username Claim Cost?'%p,'A %s username claim with Unbanz costs $1,200, paid by card through Whop. 100%% refund if the claim fails.'%p,'How much does a %s username claim cost?'%p,
    'One price, said upfront, and a refund policy if it doesn’t work.',
    'A %s username claim with Unbanz costs $1,200. You pay by card through Whop checkout. If the claim fails, our refund policy gives a 100%% refund.'%p,
    [('includes','What you pay for','<p>Checking the route, preparing evidence and reports, filing through %s’s own processes and following up.</p>'%p)],
    [('Is there a deposit?','No separate deposit. Asking is free.')],p,r)
  A('how-long-does-a-%s-username-claim-take'%k,'How Long Does a %s Username Claim Take?'%p,'How long a %s username claim can take, what affects it and why nobody can promise a date.'%p,'How long does a %s username claim take?'%p,
    'Timing depends on %s, not on us.'%p,
    'There is no set time. %s decides when it acts on a report. We give you an estimate in writing before you pay, but we can’t promise timing.'%p,
    [('affects','What affects it','<ul><li>The route: trademark, impersonation or a removed account.</li><li>How clear the evidence is.</li><li>How quickly %s responds.</li></ul>'%p)],
    [],p,r)
  A('is-a-%s-username-claim-safe'%k,'Is a %s Username Claim Safe and Legit?'%p,'How to tell a safe %s username claim from a scam: no passwords, no stolen handles, official routes, a refund policy.'%p,'Is a %s username claim safe?'%p,
    'A legit claim uses %s’s own processes and leaves your account in your hands.'%p,
    'A safe claim never needs your password or codes, never moves a stolen account to you, uses %s’s own reports and comes with a written price and refund policy.'%p,
    [('check','What to check','<ul><li>Real website and email.</li><li>Price and refund policy in writing.</li><li>Card payment, not gift cards.</li></ul>')],
    [],p,r)
  A('%s-username-claim-scams'%k,'%s Username Claim Scams to Avoid'%p,'Common %s username scams: fake “plugs”, stolen OG handles, login links and gift card payments. How to spot them.'%p,'%s username claim scams to avoid'%p,
    'Username scams target people who want a handle badly.',
    'Walk away from anyone who asks for your password or codes, claims inside access at %s, sells accounts, or wants gift cards or crypto only.'%p,
    [('signs','Red flags','<ul><li>“I have a plug at %s.”</li><li>A login link to “verify” your account.</li><li>Selling a ready-made account with the handle.</li><li>Pressure to pay now.</li></ul>'%p)],
    [],p,r)
  A('%s-username-for-business'%k,'%s Username for Your Business or Brand'%p,'Your business name is taken on %s. Routes for brands: trademark, impersonation and squatted handles.'%p,'%s username for your business'%p,
    'A matching handle makes your business easier to find and harder to copy.',
    'Businesses have the best routes: a registered trademark, an account impersonating the business, or a squatter holding the name. Each goes through %s’s own reports.'%p,
    [('prep','What to have ready','<ul><li>Trademark details, if you have them.</li><li>Your website and business profile.</li><li>Links to the account holding the name.</li></ul>')],
    [],p,r)
  A('%s-username-for-creators'%k,'%s Username for Creators'%p,'Creators: getting your name as your %s username when someone else holds it.'%p,'%s username for creators'%p,
    'For creators, your handle is your name. Here is when you can get it.',
    'Creators can claim a handle when an account impersonates them, squats on their known name, or uses their trademark. Fame alone is not a route.'%(),
    [('tips','Help your claim','<ul><li>Keep your real account active and consistent.</li><li>Link your other platforms.</li><li>Save evidence of anyone copying you.</li></ul>')],
    [],p,r)
  for c,cn in (('usa','the USA'),('uk','the UK')):
    tm='USPTO' if c=='usa' else 'UKIPO'
    A('%s-username-claim-%s'%(k,c),'%s Username Claim in %s'%(p,cn.replace('the ','')),'%s username claims for people and brands in %s. %s trademark route, $1,200, 100%% refund if the claim fails.'%(p,cn,tm),'%s username claim in %s'%(p,cn),
      'For people and businesses in %s who want an inactive, taken or brand %s handle.'%(cn,p),
      'In %s, a %s registration is the strongest base for a brand handle claim. Without one, impersonation or squatting routes may still fit.'%(cn,tm),
      [('local','What applies in %s'%cn,'<p>%s applies the same rules everywhere. Locally, what helps is a %s trademark and a business registered in %s.</p>'%(p,tm,cn))],
      [],p,r)
# Instagram extras
r=R['Instagram']
A('instagram-this-username-isnt-available-notice','“This Username Isn’t Available” on Instagram','What Instagram’s “This username isn’t available” notice means and whether the handle can be claimed.','“This username isn’t available” on Instagram',
  'You type a handle and Instagram says it isn’t available.',
  'The notice means another account holds the name, including a deactivated, banned or reserved one, or the name breaks Instagram’s rules. It does not mean the handle can never move.',
  [('why','Common reasons','<ul><li>A private, banned or deactivated account holds it.</li><li>Someone renamed and has 14 days to switch back.</li><li>Instagram reserves or blocks the name.</li></ul><p>See also <a href="/instagram-username-not-available-but-no-account/">not available but no account</a>.</p>')],
  [],'Instagram',r)
A('get-instagram-username-back-after-ban','Get Your Instagram Username Back After a Ban','Lost your Instagram username in a ban? When you can get it back and which routes work.','Get your Instagram username back after a ban',
  'A disabled Instagram account usually keeps its username.',
  'The best route is usually the appeal: if the account returns, so does the handle. If it is gone for good and the handle matches your name or brand, a claim may work.',
  [('appeal','Start with the appeal','<p>See <a href="/instagram-unban-service/">Instagram unbans</a>.</p>')],[],'Instagram',r)
A('get-instagram-username-back-after-deleting-account','Get Your Instagram Username Back After Deleting','Deleted your Instagram account and want the username back? What happens to the handle and what to do.','Get your Instagram username back after deleting your account',
  'Deleting can free the handle for anyone.',
  'Instagram gives you 30 days to cancel a deletion by logging in. After that the username can be taken. If someone took it, a claim may work when it matches your brand or they impersonate you.',
  [],[],'Instagram',r)
A('instagram-impersonator-using-my-username','Instagram Impersonator Using My Name as Username','Someone impersonates you on Instagram and holds your name. Report it and claim the handle.','An impersonator is using my name on Instagram',
  'A fake account with your name is a safety and username problem.',
  'Report it through Instagram’s impersonation form. If it is removed, the handle can be claimed onto your own profile, but Instagram makes the final call.',
  [('more','Related','<p>See <a href="/someone-is-pretending-to-be-me-on-instagram/">someone is pretending to be me</a>.</p>')],[],'Instagram',r)
A('instagram-username-claim-scams','Instagram Username Claim Scams to Avoid','Common Instagram username scams: fake Meta plugs, stolen OG handles, login links. How to spot them.','Instagram username claim scams to avoid',
  'Scammers target people who want a handle badly.',
  'Walk away from anyone who asks for your password or codes, claims inside access at Meta, sells accounts, or wants gift cards.',
  [('signs','Red flags','<ul><li>“Meta plug” or portal access.</li><li>Login links.</li><li>Selling accounts.</li></ul>')],[],'Instagram',r)
A('how-does-an-instagram-username-claim-work','How Does an Instagram Username Claim Work?','Step by step: how an Instagram username claim works through Instagram’s own processes, cost and refund policy.','How does an Instagram username claim work?',
  'Plain steps, no secret methods.',
  'You send the handle, we find whether there is a legit route (trademark, impersonation, squatting or an inactive account Instagram removes), you pay $1,200 by card through Whop, and we file and follow up through Instagram’s own processes.',
  [],[],'Instagram',r)
# Cross-platform
A('how-to-pay-for-a-username-claim','How to Pay for a Username Claim','Paying Unbanz for a username claim: $1,200 by card through Whop checkout, 100% refund if the claim fails.','How do I pay for a username claim?',
  'Card only, through Whop checkout.',
  'Username claims for Instagram, TikTok and Snapchat cost $1,200, paid by card through Whop checkout. Our refund policy gives a 100% refund if the claim fails.',
  [('not','What we never ask for','<p>Gift cards, passwords, login codes or payment to a personal account.</p>')],[],'Instagram',r)
# Hub
def li(items): return '<ul>'+''.join('<li><a href="/%s/">%s</a></li>'%(s,h) for s,h,_ in items)+'</ul>'
grp=lambda f:[x for x in P if f(x[0])]
tk=grp(lambda s:'tiktok' in s); sc=grp(lambda s:'snapchat' in s); ig=grp(lambda s:'instagram' in s); ot=grp(lambda s:'tiktok' not in s and 'snapchat' not in s and 'instagram' not in s)
old='<ul><li><a href="/instagram-username-claim/">Instagram username claims</a></li><li><a href="/inactive-instagram-username/">Inactive Instagram usernames</a></li><li><a href="/taken-instagram-username/">Taken Instagram usernames</a></li><li><a href="/og-username/">OG usernames</a></li><li><a href="/trademark-username-claim/">Trademark username claims</a></li><li><a href="/snapchat-username-claim/">Snapchat username claims</a></li><li><a href="/business-username-claim/">Business username claims</a></li><li><a href="/username-claim-pricing/">Username claim pricing</a></li><li><a href="/is-a-username-claim-safe/">Is a username claim safe?</a></li></ul>'
page('username-claim-questions','Username Claim Questions: Instagram, TikTok, Snapchat','Answers on claiming inactive, taken, OG and brand usernames on Instagram, TikTok and Snapchat: how it works, cost, timing, safety and scams.','Username claim questions',
 'Every Unbanz answer on Instagram, TikTok and Snapchat username claims in one place.',
 'Unbanz claims inactive, taken, OG and brand handles on Instagram, TikTok and Snapchat through the platforms’ own processes. A claim costs $1,200, paid by card through Whop. Our refund policy gives a 100% refund if the claim fails.',
 [('instagram','Instagram',li(ig)+old),('tiktok','TikTok',li(tk)),('snapchat','Snapchat',li(sc)),('payment','Paying',li(ot))],[],'Instagram',[('/username/','Username claims'),('/refund-policy/','Refund policy'),('/contact/','Contact')])
P.append(('username-claim-questions','Username claim questions','Answers on claiming inactive, taken, OG and brand usernames on Instagram, TikTok and Snapchat.'))
import json; json.dump(P,open('/tmp/uclaims.json','w'),ensure_ascii=False)
print(len(P))
