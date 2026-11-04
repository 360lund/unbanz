# Top-10 lead guides (US/UK/CA/NL/FR + ChatGPT, 22 Oct-4 Nov): answer-first block, top CTA, page FAQs into FAQPage, cluster links.
import re,json,html
T="Terms are agreed with you before any work starts."
WA="https://wa.me/19342012490?text="
e=lambda s:html.escape(s,quote=False)
G={
'instagram-account-suspended-appeal':('Instagram','my Instagram account is suspended',
 ['Appeal once from the notice, before the countdown ends.','Do the video selfie or ID check if Instagram asks. Use the same face and name as the profile.','Then wait. A second appeal or a new account can make things worse.'],
 [('How many days do I have to appeal an Instagram suspension?','Usually 180 days, shown on the notice. Appeal early, while the account and its content still exist.'),
  ('What if the appeal button is missing?','Update the app, try instagram.com in a browser, and check the Account Status page. Some notices only show the option there.'),
  ('Can Unbanz help after I already appealed?','Yes, we can look at where it stands and what route is left. Meta makes the final decision. '+T)],
 ['/guides/instagram-disabled-no-appeal-button/','/guides/instagram-id-verification-request/','/guides/instagram-appeal-sent-no-response/','/instagram-account-recovery/']),
'facebook-account-disabled-appeal':('Facebook','my Facebook account is disabled',
 ['Appeal once from the disabled notice, logged in on your usual device.','Upload a clear government ID if asked. The name must match the profile.','Keep the screenshots. If the appeal is rejected, they show what was sent.'],
 [('How long do I have to appeal a disabled Facebook account?','Usually 180 days from the notice. After that the account can be permanently disabled.'),
  ('Can I call Facebook about a disabled account?','No. Facebook does not run phone support for disabled accounts, and numbers that claim to be Facebook are often scams.'),
  ('Can Unbanz help with a disabled Facebook account?','Yes. We help prepare and handle the appeal through Meta’s official process. Meta makes the final decision. '+T)],
 ['/guides/facebook-disabled-appeal-rejected/','/guides/facebook-lost-access-to-email-or-phone/','/best-service-to-recover-disabled-facebook-account/','/facebook-account-recovery/']),
'instagram-disabled-no-appeal-button':('Instagram','my Instagram is disabled and there is no appeal button',
 ['Update the app and try instagram.com in a browser. The option often shows on one and not the other.','Check Settings, then Account Status, if you can still log in.','If the notice says the decision is final, the in-app route is usually closed. Other official routes may still exist.'],
 [('Why is there no appeal button on my disabled Instagram?','The appeal window may have closed, the decision may be marked final, or the app version may hide it. Try a browser first.'),
  ('Does a new account help?','No. Making a new account to get around a ban can get that one removed too.'),
  ('Can Unbanz help when there is no appeal option?','We tell you honestly whether an official route is left. '+T)],
 ['/guides/instagram-account-suspended-appeal/','/guides/instagram-account-disabled/','/guides/instagram-appeal-sent-no-response/','/instagram-account-recovery/']),
'instagram-id-verification-request':('Instagram','Instagram asked me to verify my identity',
 ['Do the video selfie or upload the ID from your usual phone, in good light.','The name and face must match what is on the profile.','Submit once. Repeated uploads can reset the queue.'],
 [('Why does Instagram keep rejecting my ID or selfie?','Common reasons are a blurry photo, a name that does not match the profile, or no clear photos of your face on the account.'),
  ('How long does Instagram take after an ID check?','It varies. Some get a reply in days, others wait weeks. Meta does not publish a timeline.'),
  ('Can Unbanz help with a stuck verification?','Yes. We look at what is going wrong and help you prepare it again properly. '+T)],
 ['/guides/instagram-account-suspended-appeal/','/guides/instagram-appeal-sent-no-response/','/guides/instagram-account-disabled/','/instagram-account-recovery/']),
'instagram-account-disabled':('Instagram','my Instagram account is disabled',
 ['Read the notice: it names the reason and any deadline.','Appeal once from the notice and do any selfie or ID check.','If you were hacked first, say so in one line.'],
 [('Can a disabled Instagram account come back?','Sometimes, when the appeal is clear and accurate. Meta makes the final decision.'),
  ('Will my followers see that I am disabled?','Your profile is hidden while it is disabled. It shows again if it is restored.'),
  ('Can Unbanz help with a disabled Instagram account?','Yes. We help you appeal through Meta’s official process. '+T)],
 ['/guides/instagram-account-suspended-appeal/','/guides/instagram-disabled-no-appeal-button/','/guides/instagram-id-verification-request/','/instagram-account-recovery/']),
'facebook-lost-access-to-email-or-phone':('Facebook','I lost access to the email or phone on my Facebook',
 ['Go to facebook.com/login/identify and search by name, email or phone.','Choose the option that you no longer have access to those contacts.','Use a device and network you have used before, and upload ID if asked.'],
 [('Can I recover Facebook without my old email or phone?','Often, through the identity check on facebook.com/login/identify or facebook.com/hacked. It works best from a device Facebook already knows.'),
  ('What if Facebook sends the code to an old number?','Choose No longer have access and follow the ID steps. Do not keep requesting codes.'),
  ('Can Unbanz help?','Yes. We work out which official route fits and prepare what to send. '+T)],
 ['/facebook-hacked-usa-what-to-do/','/facebook-hacked-uk-what-to-do/','/guides/facebook-account-disabled-appeal/','/facebook-account-recovery/']),
'instagram-appeal-sent-no-response':('Instagram','I appealed my Instagram and heard nothing back',
 ['Check the email on the account, including spam, and the Support Requests page in the app.','Do not send the same appeal again and again.','If the countdown is still running, the account is still under review.'],
 [('How long does an Instagram appeal take?','Meta does not publish a timeline. Some replies come in days, others take weeks.'),
  ('Should I appeal again?','One complete appeal is better than many. Duplicates can slow things down.'),
  ('Can Unbanz help when there is no reply?','We check where it stands and whether another official route fits. '+T)],
 ['/guides/instagram-account-suspended-appeal/','/guides/instagram-id-verification-request/','/guides/instagram-disabled-no-appeal-button/','/instagram-account-recovery/']),
'meta-ad-account-restricted':('Meta ad account','my Meta ad account is restricted',
 ['Open Account Quality and screenshot the notice before changing anything.','Fix the likely cause: payment, identity or the ad that was flagged.','Request one review, with a short note on what the business does.'],
 [('How long does a Meta ad account review take?','It varies. Meta does not publish a timeline for ad account reviews.'),
  ('Should I open a new ad account?','No. New ad accounts to get around a restriction can get the whole business portfolio restricted.'),
  ('Can Unbanz help with a restricted ad account?','Yes. We help you read the notice, fix the cause and prepare the review through Meta’s process. '+T)],
 ['/best-meta-ad-account-recovery-service-usa/','/best-meta-ad-account-recovery-service-uk/','/best-facebook-ad-account-recovery-service/','/ad-account-recovery/']),
'facebook-disabled-appeal-rejected':('Facebook','my Facebook appeal was rejected',
 ['Screenshot the rejection message and the date.','In the EU, ask for the statement of reasons and look at Appeals Centre Europe.','Do not make a new profile. It can be removed too.'],
 [('Is a rejected Facebook appeal final?','Often, for the in-app route. In the EU and UK there can be other official routes.'),
  ('Can I appeal a Facebook rejection again?','Usually not from the same notice. Other routes depend on where you live.'),
  ('Can Unbanz help after a rejection?','We tell you honestly whether a route is left. '+T)],
 ['/guides/facebook-account-disabled-appeal/','/appeals-centre-europe-instagram-facebook-suspension/','/best-service-to-recover-disabled-facebook-account/','/facebook-account-recovery/']),
'hacked-instagram-account-recovery':('Instagram','my Instagram account was hacked',
 ['Open the "your account was changed" email and use the secure link, if it is there.','Use Forgot password, then Need more help, and do the video selfie.','Once back in, turn on two-factor authentication and remove unknown devices.'],
 [('Can I recover a hacked Instagram if the email and phone were changed?','Often, with Need more help on the login screen and the video selfie.'),
  ('Should I pay someone in my DMs to recover it?','No. Those offers are scams. Nobody needs your password or codes.'),
  ('Can Unbanz help with a hacked Instagram?','Yes. We map the recovery routes and prepare what to send. '+T)],
 ['/instagram-hacked-usa-what-to-do/','/instagram-hacked-uk-what-to-do/','/hacker-changed-my-instagram-email-and-password/','/instagram-account-recovery/']),
}
def title(u):
    s=open(u.strip('/')+'/index.html').read(); return html.unescape(re.search(r'<title>([^<|:]*)',s).group(1).strip())
BAN=re.compile(r'\bcases?\b|we review|fixed price|fast turnaround|guarantee',re.I)
for slug,(plat,situ,short,faqs,rel) in G.items():
    f='guides/%s/index.html'%slug; h=open(f).read()
    h=re.sub(r'<section class="container" data-nov04g="top">.*?</section>','',h,flags=re.S)
    msg=WA+("Hi Unbanz, "+situ+". Username or link: . Country: .").replace(' ','%20').replace(',','%2C')
    b='<section class="container" data-nov04g="top"><h2>In short</h2><ol>'+''.join('<li>%s</li>'%e(x) for x in short)+'</ol>'
    b+='<p>Unbanz is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. Your password stays with you. The usual estimate is 3–14 days from the day work starts. %s</p>'%T
    b+='<p><a class="button button-blue" href="%s">Message Unbanz on WhatsApp</a> or email <a href="mailto:team@unbanz.com">team@unbanz.com</a>.</p>'%msg
    b+='<h2>Quick answers</h2>'+''.join('<h3>%s</h3><p>%s</p>'%(e(q),e(a)) for q,a in faqs)
    b+='<p><strong>Related:</strong> '+' · '.join('<a href="%s">%s</a>'%(u,e(title(u))) for u in rel)+'</p></section>'
    assert not BAN.search(b),slug
    m=re.search(r'<section class="container" data-nov04b="send">.*?</section>',h,re.S)
    i=m.end() if m else h.find('</section>',h.find('class="service-hero"'))+10
    h=h[:i]+b+h[i:]
    def r(mm):
        o=json.loads(mm.group(1))
        def walk(x):
            if isinstance(x,dict):
                if x.get('@type')=='FAQPage':
                    ex={q.get('name') for q in x.get('mainEntity',[])}
                    for q,a in faqs:
                        if q not in ex: x.setdefault('mainEntity',[]).append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}})
                if 'dateModified' in x: x['dateModified']='2026-11-04'
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(o); return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False,separators=(',',':'))+'</script>'
    h=re.sub(r'<script type="application/ld\+json">(.*?)</script>',r,h,flags=re.S)
    open(f,'w').write(h); print('ok',slug)
