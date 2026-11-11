import re,json,html,os
os.chdir('/workspace/site')
T=open('facebook-notice-types/index.html').read()
slug='meta-appeal-links-and-forms-directory'
URL=f'https://unbanz.com/{slug}/'
title='Meta Appeal Links and Forms Directory (2026)'
desc='Every official Instagram, Facebook and Meta ad account appeal, recovery and support link in one place, checked November 2026. What each one is for and which old forms no longer work.'
h1='Meta appeal links and forms, in one place.'
lede='The official Instagram, Facebook and Meta ad account links, what each one is for, and which old forms now redirect. Checked 4 November 2026.'
answer=('<strong>There is no single Meta appeal form.</strong> A suspended or disabled Instagram or Facebook account is appealed from the notice you see when you log in, or from Accounts Center. A hacked account starts at instagram.com/hacked or facebook.com/hacked. A restricted or disabled ad account is reviewed from Business Support Home (Account Quality), by an admin. Meta has no general public phone number. Many old help/contact form links now redirect to Account Status or the Meta AI support assistant. Meta makes the final decision.')
WA='https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account'
sections=[
('instagram','Instagram',[
 ('Account Status','https://help.instagram.com/338481628002750','Where Instagram shows removed content, features you cannot use and the Request a review option. Settings, then Account Status.'),
 ('About disabled Instagram accounts','https://help.instagram.com/366993040048856','Meta’s page on disabled accounts. If you are disabled, you see a message when you log in and appeal from there.'),
 ('Hacked account','https://www.instagram.com/hacked/','Start here if you cannot log in and see no disabled or suspended message. Someone may have changed your email or phone.'),
 ('Accounts Center','https://accountscenter.instagram.com/','Passwords, two-factor, logged-in devices and linked Facebook accounts. Some appeals now open from here.'),
 ('Old “my account was deactivated” form (606967319425038)','https://help.instagram.com/contact/606967319425038','Still shared on forums and in videos. When we checked it on 4 November 2026 it opened the Account Status help page and the Meta AI support assistant, not a form.'),
]),
('facebook','Facebook',[
 ('My personal Facebook account is suspended or disabled','https://www.facebook.com/help/103873106370583','Meta says you can appeal a suspension within 180 days, and that the period varies by region. After that, or after a failed appeal, the account is permanently disabled.'),
 ('Hacked account','https://www.facebook.com/hacked','For a takeover: email, phone, name or password changed without you.'),
 ('Find your account','https://www.facebook.com/login/identify','Password reset and lost email or phone. Use it before anything else if there is no disabled message.'),
 ('Phone support','https://www.facebook.com/help/1088016719924954','Meta says it has no general public phone number for customer service. A number claiming to be Meta support is likely a scam.'),
]),
('meta','Meta-wide support',[
 ('Account Recovery Hub','https://www.meta.com/account-recovery-support/','Meta’s own starting page for Facebook, Instagram and Threads login and recovery problems.'),
 ('Meta AI support assistant and Meta One','https://www.meta.com/help/subscriptions/2290591971482409/','In the app: Settings, More info and support, then Help or Meta AI support assistant. Meta One plans include a set number of human support requests a month.'),
 ('How Meta disables accounts','https://transparency.meta.com/enforcement/taking-action/disabling-accounts/','Meta’s explanation of when and why it disables accounts.'),
 ('Community Standards','https://transparency.meta.com/policies/community-standards/','The rules most notices refer to. Read the section your notice names before you appeal.'),
]),
('ads','Meta ad accounts and Business Portfolios',[
 ('Troubleshoot a disabled or restricted account','https://www.facebook.com/business/help/422289316306981','On a computer: Business Support Home, Account Overview, the restricted account, then What you can do.'),
 ('Request a review if you are restricted from advertising','https://www.facebook.com/business/help/530209463124901','Only an admin can request it. Meta says reviews are limited, and once a review is completed the decision is final.'),
 ('Business Support Home (Account Quality)','https://business.facebook.com/accountquality','Where ad account, Page and Business Portfolio restrictions show up and where Request review appears.'),
 ('Advertising Standards','https://transparency.meta.com/policies/ad-standards/','The ad rules. Fix the cause named in the notice before you request a review.'),
]),
('eu','EU and UK options after an appeal',[
 ('Appeals Centre Europe','https://www.appealscentre.eu/','An independent out-of-court dispute body for people in the EU, under the Digital Services Act. Used after Meta’s own appeal.'),
 ('Oversight Board','https://www.oversightboard.com/','Takes a small number of content decisions after Meta’s appeal is finished.'),
]),
]
ext=lambda u:f'<a href="{u}" rel="noopener" target="_blank">{u.replace("https://","")}</a>'
body=[]
body.append('<h2 id="which-link">Which link do you need?</h2><ul>'
 '<li>You see “We suspended your account” or “Your account has been disabled”: appeal from that screen. See <a href="/instagram-account-disabled-vs-suspended-vs-restricted/">disabled vs suspended vs restricted</a>.</li>'
 '<li>You cannot log in and see no message: use the hacked or find-your-account link.</li>'
 '<li>Your ads stopped and the ad account says restricted or disabled: Business Support Home.</li>'
 '<li>You want a username held by an inactive account: see <a href="/instagram-username-claim/">username claims</a>.</li></ul>')
for sid,name,items in sections:
    body.append(f'<h2 id="{sid}">{name}</h2><div class="table-wrap"><table><thead><tr><th>Link</th><th>What it is for</th></tr></thead><tbody>')
    for t,u,w in items:
        body.append(f'<tr><td><strong>{html.escape(t)}</strong><br>{ext(u)}</td><td>{html.escape(w)}</td></tr>')
    body.append('</tbody></table></div>')
body.append('<h2 id="old-forms">Old forms that no longer work the way they used to</h2><p>Many help/contact links passed around in forums and videos were built years ago. Some now open a help article or the Meta AI support assistant instead of a form. If a link drops you on a help page, go back to the notice in the app or to Accounts Center. There is no “private” appeal link.</p>')
body.append('<h2 id="before-you-appeal">Before you use any of them</h2><ol><li>Screenshot the full notice with the date.</li><li>Use the phone or computer you normally use.</li><li>Appeal once, clearly. Do not open a new account while you wait.</li><li>Keep every email from Meta, including any reference number.</li></ol>')
body.append('<h2 id="by-country">If you are in the US, UK, Canada, the Netherlands or France</h2><p>The in-app routes are the same. EU users, including in the Netherlands and France, can also use Digital Services Act routes after the internal appeal. See <a href="/dsa-appeal-right-instagram-facebook/">DSA appeal rights</a>, <a href="/instagram-suspended-appeal-usa/">Instagram suspended in the US</a>, <a href="/instagram-suspended-appeal-uk/">in the UK</a>, <a href="/instagram-suspended-appeal-canada/">in Canada</a>, <a href="/facebook-account-disabled-netherlands-what-to-do/">Facebook disabled in the Netherlands</a> and <a href="/facebook-account-disabled-france-what-to-do/">in France</a>.</p>')
body.append('<h2 id="want-it-done">Want it done for you?</h2><p>Want it done for you? Get a quote for account recovery. Your password stays with you. Terms are agreed with you before any work starts.</p>')
body.append('<h2 id="related">Related</h2><p>See <a href="/instagram-notice-types/">Instagram notice types</a>, <a href="/facebook-notice-types/">Facebook notice types</a>, <a href="/meta-ad-account-notice-types/">Meta ad account notice types</a>, <a href="/instagram-appeal-form-not-working/">Instagram appeal form not working</a>, <a href="/ad-account-appeal-form-keeps-erroring/">ad account appeal form erroring</a>.</p>')
body.append('<h2 id="about-unbanz">About Unbanz</h2><p>Unbanz (unbanz.com) is an independent service that helps people recover disabled, suspended and hacked Instagram, Facebook and Meta ad accounts, and claim usernames. Contact: WhatsApp +1 934 201 2490 or team@unbanz.com. Not affiliated with Meta.</p>')
faqs=[('Is there one official Meta appeal form?','No. Instagram and Facebook appeals start from the notice in the app or Accounts Center. Ad accounts are reviewed from Business Support Home.'),
('Does Meta have a phone number for account recovery?','Meta says it has no general public phone number for customer service. Numbers claiming to be Meta support are likely scams.'),
('Why does the old Instagram appeal form open a help page?','When we checked on 4 November 2026, it opened the Account Status help page and the Meta AI support assistant. Use the notice in the app instead.'),
('Do I need to share my password?','No. Your password and login codes stay with you.')]
faq_html=''.join(f'<details><summary>{html.escape(q)}<span aria-hidden="true">+</span></summary><p>{html.escape(a)}</p></details>' for q,a in faqs)
# head
head_end=T.find('</head>')
head=T[:head_end]
old_t=re.search(r'<title>(.*?)</title>',head).group(1)
olddesc=re.search(r'name="description" content="([^"]*)"',head).group(1)
head=head.replace(old_t,html.escape(title)).replace(olddesc,html.escape(desc)).replace('https://unbanz.com/facebook-notice-types/',URL)
# schema
m=re.search(r'<script type="application/ld\+json">(.*?)</script>',head,re.S)
g=json.loads(m.group(1))
org,site=g['@graph'][0],g['@graph'][1]
graph=[org,site,
 {"@type":"WebPage","@id":URL+"#webpage","url":URL,"name":title,"description":desc,"isPartOf":{"@id":"https://unbanz.com/#website"},"publisher":{"@id":"https://unbanz.com/#organization"},"inLanguage":"en","datePublished":"2026-11-04","dateModified":"2026-11-04","breadcrumb":{"@id":URL+"#breadcrumb"},
  "mainEntity":{"@type":"ItemList","name":"Official Meta appeal, recovery and support links","itemListElement":[{"@type":"ListItem","position":i+1,"name":t,"url":u} for i,(t,u,w) in enumerate([x for s in sections for x in s[2]])]}},
 {"@type":"BreadcrumbList","@id":URL+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://unbanz.com/"},{"@type":"ListItem","position":2,"name":"Guides","item":"https://unbanz.com/guides/"},{"@type":"ListItem","position":3,"name":"Meta appeal links and forms directory","item":URL}]},
 {"@type":"FAQPage","@id":URL+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]
head=head[:m.start(1)]+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+head[m.end(1):]
# body
b0=T[head_end:]
i=b0.find('<main id="content">'); main_close=b0.find('<section class="vt vt-page')
pre=b0[:i]
post=b0[main_close:]
hero=(f'<main id="content"><section class="service-hero"><div class="container"><a class="crumb" href="/guides/">Home / Guides</a><h1>{h1}</h1><p>{lede}</p><p class="guide-meta">Updated <time datetime="2026-11-04">4 November 2026</time></p>'
 f'<div class="hero-cta"><a class="button button-light" href="{WA}" data-service="unban">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Account%20help">Prefer email? ↗︎</a></div></div></section>'
 f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{answer}</p></section>'
 '<section class="service-editorial container"><article><h2>Official links only</h2><p>Every link here goes to Meta or an official dispute body.</p></article><article><h2>Checked</h2><p>Checked 4 November 2026.</p></article><article><h2>Keep proof</h2><p>Screenshot every notice with the date.</p></article></section>'
 '<article class="guide-body container">'+''.join(body)+'</article>')
# replace faq inside post
post=re.sub(r'<div class="simple-faq">.*?</div></div></section>','<div class="simple-faq">'+faq_html+'</div></div></section>',post,count=1,flags=re.S)
post=post.replace('Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20Facebook%20account','Hey%20Unbanz%2C%20I%20need%20help%20with%20my%20account').replace('subject=Facebook%20account','subject=Account%20help')
os.makedirs(slug,exist_ok=True)
open(slug+'/index.html','w').write(head+pre+hero+post)
print('ok',len(head+pre+hero+post))
