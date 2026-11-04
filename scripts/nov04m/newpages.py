import sys,re;sys.path.insert(0,'scripts/nov04l');from lib import make,add_to_sitemap,ext
P=[]
P.append(dict(slug='how-long-does-a-facebook-appeal-take',
title='How long does a Facebook appeal take? (2026) | Unbanz',
desc='Facebook does not publish a review time for disabled or suspended account appeals. What affects the wait, where to check status, and what to do meanwhile.',
h1='How long does a Facebook appeal take?',
lede='There is no published review time. Here is what affects the wait and what you can do while it runs.',
answer='Facebook (Meta) does not publish how long an appeal for a disabled or suspended account takes, and waits vary widely. What you can rely on is the appeal window: a disable notice usually gives about 180 days to disagree. Check progress in Accounts Center under Account status, and do not send repeated appeals or open new accounts while you wait.',
body='''<h2 id="window">The window and the wait are different things</h2><p>The about-180-day figure on a disable notice is how long you have to disagree, not how long Meta takes to answer. Note the date on your notice. After the window closes, the account can be permanently removed.</p>
<h2 id="slower">What can add to the wait</h2><ul><li>An identity check, such as a video selfie or an ID upload.</li><li>A linked hack, where Meta needs to work out who controls the account.</li><li>A Page, ad account or business portfolio tied to the profile.</li><li>Several appeals sent for the same decision.</li></ul>
<h2 id="status">Where to check status</h2><p>Open Settings, then Accounts Center, then Account status. If you cannot log in, the notice on the login screen shows the current state. Also check the email linked to the account, including spam, for messages from facebookmail.com.</p>
<h2 id="meanwhile">What to do meanwhile</h2><ul><li>Screenshot the notice and the date.</li><li>Secure the linked email and phone.</li><li>Do not create a new profile to get around the decision.</li><li>If you were hacked, use facebook.com/hacked as well.</li></ul>
<h2 id="after">If the answer is no</h2><p>In the EU, Appeals Centre Europe has reviewed Facebook suspensions since 2025, once Meta’s own appeal is finished. It is free and non-binding. Outside the EU there is no equivalent body. See <a href="/guides/facebook-account-disabled-appeal/">the Facebook appeal guide</a> and the <a href="/how-long-does-an-instagram-appeal-take/">Instagram version of this page</a>.</p>
<h2 id="country">By country</h2><p>Local steps: <a href="/facebook-account-disabled-usa-what-to-do/">US</a>, <a href="/facebook-account-disabled-uk-what-to-do/">UK</a>, <a href="/facebook-account-disabled-canada-what-to-do/">Canada</a>, <a href="/facebook-account-disabled-netherlands-what-to-do/">Netherlands</a>, <a href="/facebook-account-disabled-france-what-to-do/">France</a>.</p>''',
faqs=[('Does Facebook tell you how long an appeal takes?','No. Meta does not publish a review time for account appeals.'),('Is 180 days the review time?','No. It is usually the window you have to disagree with the decision, shown on the notice.'),('Will sending more appeals speed it up?','No. Repeated appeals do not help and can make the history harder to follow.')]))
P.append(dict(slug='how-to-appeal-in-accounts-center',
title='How to appeal a disabled account in Meta Accounts Center (2026) | Unbanz',
desc='Step by step: find Account status in Meta Accounts Center, open the decision on your Instagram or Facebook account, and request a review.',
h1='How to appeal in Meta Accounts Center',
lede='Where the Account status screen is, and what each option means for Instagram and Facebook accounts.',
answer='To appeal in Meta Accounts Center, open Settings in Instagram or Facebook, tap Accounts Center, then Account status, choose the account, open the decision and tap the option to disagree or request a review. If you cannot log in, the notice on the login screen has the same button. Menu names change between app versions, so follow the wording on your screen.',
body='''<h2 id="steps">Steps</h2><ol><li>Open Instagram or Facebook and go to Settings.</li><li>Tap Accounts Center. On Facebook it may sit under See more in Accounts Center.</li><li>Choose Account status, or Account quality for business assets.</li><li>Pick the profile, then the decision you want to appeal.</li><li>Tap Disagree with decision or Request review, and follow the prompts, which may include a video selfie.</li></ol>
<h2 id="cannot-login">If you cannot log in</h2><p>A disabled account usually shows its notice right after you enter the password. The review button sits on that screen. If the account was hacked, start at instagram.com/hacked or facebook.com/hacked instead.</p>
<h2 id="ads">Ad accounts and business portfolios</h2><p>For ad accounts, use Account Quality in Meta Business Suite (business.facebook.com/accountquality). Select the asset and use Request review if shown. See <a href="/guides/meta-ad-account-restricted/">the ad account guide</a>.</p>
<h2 id="no-button">No button at all?</h2><p>Sometimes there is no review option, often when a decision is marked final or the window has closed. Screenshot the screen with the date. In the EU, Appeals Centre Europe may be an option once Meta’s own process is finished. See <a href="/instagram-no-appeal-button-usa-canada/">no appeal button (US and Canada)</a> and <a href="/instagram-no-appeal-button-eu-uk-routes/">EU and UK routes</a>.</p>''',
faqs=[('Where is Account status in Accounts Center?','Settings, then Accounts Center, then Account status. The exact names can differ by app version.'),('Can I appeal a Facebook and an Instagram account in the same place?','Yes, if both are linked in the same Accounts Center. Each decision is appealed separately.'),('Does the appeal need a password from anyone else?','No. You do it from your own login. Nobody legit needs your password.')]))
P.append(dict(slug='facebook-video-selfie-verification-stuck',
title='Facebook video selfie verification stuck or rejected (2026) | Unbanz',
desc='Facebook asked for a video selfie and nothing happened, or it was rejected. What the screens mean and what to do next, using Meta’s official routes.',
h1='Facebook video selfie verification stuck?',
lede='What “we’re reviewing your info” means after a video selfie, and what to do if it is rejected.',
answer='If Facebook is stuck after a video selfie, it usually means Meta received the selfie and is checking it. Do not record another one unless asked. If it was rejected, try once more in good light with your full face visible, no glasses, hat or filters, and make sure the profile has clear photos of you. Meta does not publish how long the check takes.',
body='''<h2 id="screens">What the screens mean</h2><ul><li><strong>We’re reviewing your info</strong>: the selfie was received. Wait, and do not resubmit.</li><li><strong>We couldn’t confirm it’s you</strong>: the check failed. You may get another try or a choice to upload ID.</li><li><strong>No option shown</strong>: screenshot it with the date and check the linked email.</li></ul>
<h2 id="tips">Before another try</h2><ul><li>Good, even light, facing the camera.</li><li>Follow the head movements on screen slowly.</li><li>The profile should have at least one clear photo of your face.</li><li>Use the same device and network you usually log in from.</li></ul>
<h2 id="id">If an ID is asked for instead</h2><p>Use an official photo ID with the same name as the profile. See <a href="/facebook-disabled-id-upload-rejected-again/">ID upload rejected again</a>, and local guides for the <a href="/facebook-id-verification-usa/">US</a> and <a href="/facebook-id-verification-uk/">UK</a>.</p>
<h2 id="instagram">On Instagram?</h2><p>See <a href="/instagram-verification-stuck-on-reviewing/">Instagram verification stuck on reviewing</a> and <a href="/instagram-video-selfie-rejected-again/">video selfie rejected again</a>.</p>''',
faqs=[('How long does a Facebook video selfie check take?','Meta does not publish a time. Waits vary.'),('Should I record the selfie again?','Only if Facebook asks. Repeated selfies do not speed things up.'),('Is the video selfie shared publicly?','Meta says video selfies are used for the check and not shown on your profile.')]))
urls=[make(**p) for p in P]
print(add_to_sitemap(urls))
L=open('llms.txt').read()
add=''.join(f'- [{p["h1"]}]({u}): {p["answer"].split(". ")[0]}.\n' for p,u in zip(P,urls) if u not in L)
i=L.find('\n',L.find('unbanz-vs-rescuno'))+1;open('llms.txt','w').write(L[:i]+add+L[i:])
S=open('site-map/index.html').read()
if urls[0] not in S and '/'+P[0]['slug']+'/' not in S:
    k=S.find('<li><a href="/unbanz-vs-rescuno/">')
    S=S[:k]+''.join(f'<li><a href="/{p["slug"]}/">{p["h1"]}</a></li>' for p in P)+S[k:];open('site-map/index.html','w').write(S)
open('/tmp/b9.txt','w').write('\n'.join(urls+['https://unbanz.com/site-map/']))
print(urls)
