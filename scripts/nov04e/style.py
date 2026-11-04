import re,json,html
T="Terms are agreed with you before any work starts."
WA="https://wa.me/19342012490?text="
def esc(s): return html.escape(s,quote=False)
P={
'instagram-account-recovery':dict(plat='Instagram',situ='my Instagram account is disabled or hacked',
 lead='Unbanz is an independent service that helps you recover a disabled, suspended or hacked Instagram account through Meta\u2019s official processes. Your password stays with you.',
 tiles=[('Disabled','The account is shut and the appeal you sent went nowhere, or there is no appeal button.'),('Suspended','A suspension notice with a deadline, or a loop of confirm-it\u2019s-you screens.'),('Hacked','Someone changed the email, phone or password. We still never need your password.'),('Creator and business','Shops, creators and brand accounts, large or small.')]),
'facebook-account-recovery':dict(plat='Facebook',situ='my Facebook account is disabled or I lost access',
 lead='Unbanz is an independent service that helps you recover a disabled, suspended or hacked Facebook profile or restricted Page through Meta\u2019s official processes. Your password stays with you.',
 tiles=[('Disabled profile','Facebook disabled the profile and the appeal was rejected or never answered.'),('Lost email or phone','You can\u2019t get the code because the email or number is old or was changed.'),('Hacked','Someone took over the profile or a Page you run.'),('Pages and business','Restricted Pages and profiles that run a business.')]),
'instagram-unban-service':dict(plat='Instagram',situ='my Instagram account was banned',
 lead='Banned, disabled or suspended on Instagram? Unbanz prepares and handles the appeal through Meta\u2019s official channels, even when there is no appeal button left.',
 tiles=[('Banned for no clear reason','The notice is vague. We help you work out which rule Meta named and answer it.'),('Appeal rejected','A \u201cwe can\u2019t reverse this decision\u201d message is not always the end.'),('No appeal button','The button is gone or the deadline passed.'),('ID check stuck','A selfie video or ID request that keeps failing.')]),
'facebook-unban-service':dict(plat='Facebook',situ='my Facebook account was banned',
 lead='Facebook account banned or disabled? Unbanz prepares and handles the appeal through Meta\u2019s official channels and keeps following up. Meta makes the final decision.',
 tiles=[('Disabled','The profile is disabled and the first appeal did nothing.'),('Rejected appeal','Facebook says the decision is final.'),('Identity check','Facebook asked for ID and nothing happened after you sent it.'),('Page or business','A Page or business profile tied to the account.')]),
'ad-account-recovery':dict(plat='Meta ad account',situ='my Meta ad account is restricted',
 lead='Unbanz is an independent service that helps advertisers and agencies get disabled or restricted Meta ad accounts and Business Portfolios reviewed again through Meta\u2019s official processes.',
 tiles=[('Ad account disabled','Ads stopped and the account shows as disabled.'),('Restricted from advertising','The profile or Business Portfolio can\u2019t run ads.'),('Review denied','The in-app request review was rejected.'),('Agencies','Client accounts you manage.')]),
'username':dict(plat='username',situ='I want to claim a username',
 lead='Unbanz helps you claim inactive or taken Instagram and Facebook handles onto your own profile, through the platform\u2019s own processes. No accounts are bought or sold.',
 tiles=[('Inactive handle','The name sits on an account nobody uses.'),('Taken by a squatter','Someone holds the name with no real use for it.'),('Your brand name','A registered trademark held by someone else.'),('Your old handle','A name you lost and want back.')]),
}
STEPS=[('Send the username','A screenshot of the notice and your country. Leave the password out.'),('Get a straight answer','We read the notice and tell you honestly what can be done. '+T),('We handle it','We prepare it and file it through Meta\u2019s own channels, then keep following up. The usual estimate is 3\u201314 days from the day work starts.'),('Meta decides','Meta makes the final decision. We keep you posted on WhatsApp or email.')]
WHY=['Independent service. Not affiliated with Meta, and we never pretend to be.','Your password and login codes stay with you. Anyone using our name who asks for them is not us.',T,'Meta\u2019s official channels only. No hacks, no bought accounts, no false reports.','Only contacts: WhatsApp +1 934 201 2490 and team@unbanz.com.']
def faqs(plat):
    return [('Is Unbanz legit?','Unbanz is an independent service at unbanz.com that helps people recover Instagram, Facebook and Meta ad accounts and claim usernames. It is not affiliated with Meta and never asks for your password.'),
            ('How long does it take?','The usual estimate is 3\u201314 days from the day work starts. Meta sets its own pace, so nobody can promise a date.'),
            ('Do you need my password?','No. Not the password, not a login code, not a backup code. We work from the username and a screenshot of the notice.'),
            ('What does it cost?','It depends on the account and the issue. '+T)]
def block(slug,d):
    msg=WA+re.sub(' ','%20',"Hi Unbanz, "+d['situ']+". Username or link: . Country: .").replace(',','%2C')
    s='<section class="container" data-nov04e="style"><p class="eyebrow">HOW IT GOES</p><h2>Four steps. No password.</h2><p>'+esc(d['lead'])+'</p><ol>'
    s+=''.join('<li><strong>%s.</strong> %s</li>'%(esc(a),esc(b)) for a,b in STEPS)+'</ol>'
    s+='<h2>What we help with</h2><ul>'+''.join('<li><strong>%s.</strong> %s</li>'%(esc(a),esc(b)) for a,b in d['tiles'])+'</ul>'
    s+='<h2>Why people message Unbanz</h2><ul>'+''.join('<li>%s</li>'%esc(w) for w in WHY)+'</ul>'
    s+='<h2>Before you message us</h2>'+''.join('<h3>%s</h3><p>%s</p>'%(esc(q),esc(a)) for q,a in faqs(d['plat']))
    s+='<p><a class="button" href="%s">Send the username on WhatsApp</a> or email <a href="mailto:team@unbanz.com">team@unbanz.com</a>.</p></section>'%msg
    return s
BAN=re.compile(r'\bcases?\b|we review|fixed price|fast turnaround|guarantee',re.I)
for slug,d in P.items():
    f=slug+'/index.html'; h=open(f).read()
    h=re.sub(r'<section class="container" data-nov04e="style">.*?</section>','',h,flags=re.S)
    b=block(slug,d); assert not BAN.search(b),slug
    m=re.search(r'<section class="container" data-nov04b="send">.*?</section>',h,re.S)
    if m: i=m.end()
    else:
        j=h.find('class="service-hero"'); i=h.find('</section>',j)+10
    h=h[:i]+b+h[i:]
    # add to FAQPage
    def r(mm):
        o=json.loads(mm.group(1))
        def walk(x):
            if isinstance(x,dict):
                if x.get('@type')=='FAQPage':
                    ex={q.get('name') for q in x.get('mainEntity',[])}
                    for q,a in faqs(d['plat']):
                        if q not in ex: x.setdefault('mainEntity',[]).append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}})
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(o); return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False,separators=(',',':'))+'</script>'
    h=re.sub(r'<script type="application/ld\+json">(.*?)</script>',r,h,flags=re.S)
    open(f,'w').write(h); print('ok',slug)
