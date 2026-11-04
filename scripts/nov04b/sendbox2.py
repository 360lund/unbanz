import re,urllib.parse,sys
P0={
'guides/facebook-account-disabled-appeal':('Facebook','my Facebook account is disabled or suspended'),
'guides/instagram-account-suspended-appeal':('Instagram','my Instagram account is suspended'),
'guides/instagram-disabled-no-appeal-button':('Instagram','my Instagram is disabled and there is no appeal button'),
'guides/facebook-lost-access-to-email-or-phone':('Facebook','I lost access to the email and phone on my Facebook'),
'guides/meta-ad-account-restricted':('Meta ad account','my Meta ad account is restricted'),
'guides/instagram-id-verification-request':('Instagram','Instagram asked me for ID'),
'guides/instagram-appeal-sent-no-response':('Instagram','I sent my Instagram appeal and heard nothing'),
'guides/instagram-account-disabled':('Instagram','my Instagram account is disabled'),
'facebook-account-recovery':('Facebook','I need help getting my Facebook account back'),
'ban':(None,'I want to report an account that is impersonating or harassing me'),
}
P={
'reviews':('Instagram, Facebook or Meta ad','I found you on your reviews page and need help with an account'),
'is-unbanz-legit':('Instagram, Facebook or Meta ad','I need help with an account'),
'instagram-unban-service':('Instagram','my Instagram account is suspended or disabled'),
'facebook-unban-service':('Facebook','my Facebook account is suspended or disabled'),
'ad-account-recovery':('Meta ad account','my Meta ad account is disabled or restricted'),
'guides/facebook-disabled-appeal-rejected':('Facebook','my Facebook appeal was rejected'),
'guides/facebook-page-restricted':('Facebook Page','my Facebook Page is restricted'),
}
for path,(plat,situ) in P.items():
    f=path+'/index.html'; h=open(f).read()
    if 'data-nov04b="send"' in h: continue
    msg=f"Hi Unbanz, {situ}. Username or link: . Country: . I can send a screenshot of the notice."
    wa="https://wa.me/19342012490?text="+urllib.parse.quote(msg)
    if plat:
        who=f"<strong>Who we can help:</strong> the owner of the {plat} account who can show the notice on their screen. We do not help anyone get into an account that is not theirs."
        send="<li>A screenshot of the full notice, with any date or policy shown</li><li>The username or profile link</li><li>Your country, and what you have already tried</li>"
    else:
        who="<strong>Who we can help:</strong> people being impersonated, harassed or scammed by a specific account, with links and screenshots to show it."
        send="<li>The link to the account you are reporting</li><li>Screenshots of what it posted or sent</li><li>Your own account link and country</li>"
    box=f'''<section class="container" data-nov04b="send"><div class="guide-note" style="border-left:3px solid #2f6fdb;background:#f3f7fd;padding:14px 18px;margin:18px 0;border-radius:6px"><p><strong>Want us to look at yours?</strong> Send it on WhatsApp. {who}</p><p><strong>What to send:</strong></p><ul>{send}</ul><p>Never send your password or login codes. In the US, UK or EU? Say so: you may have extra routes, such as the <a href="/dsa-appeal-right-instagram-facebook/">EU DSA appeal right</a> or <a href="/your-rights-when-meta-disables-your-account/">your rights after a ban</a>. We tell you honestly whether we can help, and terms are agreed with you before any work starts.</p><p><a class="button button-blue" href="{wa}">Send us the notice on WhatsApp <span aria-hidden="true">↗︎</span></a></p></div></section>'''
    i=max(h.find('class="service-hero"'),h.find('<main')); j=h.find('</section>',i)+len('</section>')
    h=h[:j]+box+h[j:]
    h=h.replace('https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20need%20help%20with%20an%20account',wa)
    open(f,'w').write(h); print('ok',path)
