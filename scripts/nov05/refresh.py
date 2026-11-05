import re,json,sys,html as H
TODAY='2026-11-05'
A=lambda s,t:f'<a href="/{s}/">{t}</a>'
SEND='<h3>What to send us</h3><ul><li>The username or profile link.</li><li>A screenshot of the exact notice, with the date visible.</li><li>Whether you already appealed, and what Meta replied.</li><li>Whether you still have the email and phone number on the account.</li><li>Never your password or login codes.</li></ul><p>Send it on <a href="https://wa.me/19342012490">WhatsApp</a> or to <a href="mailto:team@unbanz.com">team@unbanz.com</a>.</p>'
EMAILQ=('I emailed my appeal letter to Meta. Did it arrive?','Meta does not process account appeals by email. Paste a short version of your letter into the appeal field shown in the app, Account Status or Business Support Home.')
C={
'fbdis':('<p>The Facebook appeal still starts from the notice you see when you log in: choose the option to disagree or request a review, and complete any check Meta asks for, such as a video selfie or an ID upload. Meta states that you generally have 180 days to appeal a suspension. If the screen offers no appeal, see '+A('instagram-disabled-no-appeal-button-what-to-do','what to do with no appeal button')+' and the '+A('facebook-appeal-links-and-forms-directory','Facebook appeal links directory')+'.</p>',EMAILQ),
'igdis':('<p>For Instagram, the appeal starts from the notice at login or from Account Status in the app. Meta may ask for a video selfie before it looks at the appeal. A countdown on the notice shows how long the account can still be appealed. If both Instagram and Facebook went down together, see '+A('facebook-and-instagram-disabled-together-linked-accounts','linked accounts disabled together')+'. All official links: '+A('instagram-appeal-links-and-forms-directory','Instagram appeal links directory')+'.</p>',EMAILQ),
'ads':('<p>Ad account, Page and Business Portfolio restrictions are reviewed in Business Support Home (formerly Account Quality) on a computer, by an admin. Open the restricted asset, read the reason, then request a review once. If an admin’s personal profile is restricted, that comes first. For agencies, see '+A('for-agencies-banned-client-accounts','the agency hub')+' and '+A('meta-business-portfolio-appeal-links-directory','Business Portfolio appeal links')+'.</p>',('Should the agency or the client request the ad account review?','Either can if they are an admin. The person who knows the account history best should write it.')),
'hack':('<p>For a takeover, start at instagram.com/hacked or facebook.com/hacked from a device you used before. If the hacker changed the email, Meta’s flow lets you choose that you no longer have access and verify another way. After you are back, check Accounts Center for unknown logins and connected accounts, and turn on two-factor authentication. See '+A('facebook-hacked-email-changed','Facebook hacked and email changed')+'.</p>',('The hacker changed my email and phone. Can I still recover it?','Often yes, through the hacked page and identity checks such as a video selfie. Use a device and network you used before.')),
'verify':('<p>Meta uses video selfies and ID uploads to confirm a real person owns the account. Use good light, no glasses or filters, and follow the head movements slowly. If the check loops or fails, wait before retrying rather than repeating it many times. See '+A('instagram-selfie-verification-keeps-looping','selfie verification keeps looping')+'.</p>',('The video selfie keeps failing. What should I do?','Try once more in good light on the device you normally use, then wait. Repeating it many times in a row does not help.')),
'snap':('<p>Snapchat locks and bans are handled through Snapchat Support forms. A temporary lock usually ends on its own; permanent bans and device bans need the support form. All official links: '+A('snapchat-support-links-and-forms-directory','Snapchat support links directory')+'.</p>',('Can I unlock Snapchat by making a new account?','Not while the device is banned. New accounts on the same device can be locked too.')),
'dir':('<p>New this month: country and platform versions of this directory. See '+A('meta-appeal-links-usa','USA')+', '+A('meta-appeal-links-uk','UK')+', '+A('meta-appeal-links-canada','Canada')+', '+A('meta-appeal-links-australia','Australia')+', '+A('meta-appeal-links-uae','UAE')+', '+A('fr/liens-officiels-appel-meta-instagram-facebook','France')+', '+A('nl/officiele-bezwaarlinks-meta-instagram-facebook','Nederland')+', plus '+A('tiktok-appeal-links-and-forms-directory','TikTok')+', '+A('whatsapp-banned-number-appeal-links-directory','WhatsApp')+' and '+A('threads-appeal-links-directory','Threads')+'. Meta does not take appeals by email or phone.</p>',EMAILQ),
'wl':('<p>New for agencies this month: question-led pages for the situations agency owners describe most, from a client’s Instagram disabled to a whole Business Portfolio down. Start at '+A('for-agencies-banned-client-accounts','the agency hub')+' or '+A('questions-agencies-ask-about-banned-client-accounts','questions agencies ask')+'.</p>',('Can we refer client accounts under our own brand?','Yes. In a white-label setup you speak to the client and we work behind your brand.')),
}
def cat(p):
    s=p.lower()
    if 'white-label' in s: return 'wl'
    if 'snap' in s: return 'snap'
    if 'directory' in s or 'contact-meta' in s or 'meta-verified' in s: return 'dir'
    if 'ad-' in s or 'ad-account' in s or 'conta-de-anuncios' in s or 'payment' in s: return 'ads'
    if 'selfie' in s or 'id-' in s or 'verification' in s: return 'verify'
    if 'hack' in s or 'email-or-phone' in s: return 'hack'
    if 'instagram' in s: return 'igdis'
    return 'fbdis'
ANS={
'guides/meta-ad-account-restricted':'<strong>A restricted Meta ad account is reviewed in Business Support Home.</strong> Open it on a computer as an admin, select the restricted ad account, Page or person, read the reason, and request a review once. Check payments and recent rejected ads first. If an admin’s profile is restricted, appeal that first. Meta makes the final decision.',
'guides/instagram-disabled-no-appeal-button':'<strong>No appeal button usually means the appeal was already used, the time to appeal passed, or the notice says the decision is final.</strong> Check Account Status if you can log in, use instagram.com/hacked if someone changed your details, and in the EU consider an out-of-court dispute body. Meta makes the final decision.',
'guides/instagram-account-disabled':'<strong>A disabled Instagram account is appealed from the notice you see when you log in.</strong> Screenshot the notice, request a review, complete any video selfie Meta asks for, and appeal once with a short factual message. Do not create new accounts while waiting. If you cannot log in at all, start at instagram.com/hacked. Meta makes the final decision.',
'guides/hacked-facebook-account-recovery':'<strong>Start at facebook.com/hacked from a phone or computer you used before.</strong> If the hacker changed the email or phone, choose that you no longer have access and follow the identity checks. Once back in, remove unknown logins, change the password and turn on two-factor authentication. Meta makes the final decision.',
'guides/instagram-video-selfie-verification':'<strong>Instagram uses a video selfie to confirm a real person owns the account.</strong> Use the device you normally use, good light, no filters or glasses, and turn your head slowly as asked. If it fails, wait before trying again rather than repeating it many times. Meta makes the final decision.',
}
def refresh(p):
    f=p+'/index.html';h=open(f,encoding='utf-8').read()
    if 'id="updated-nov-2026"' in h: return False
    k=cat(p);body,(q,a)=C[k]
    sec=f'<article class="guide-body container"><h2 id="updated-nov-2026">Updated November 2026</h2>{body}<h3>{q}</h3><p>{a}</p>{SEND}</article>'
    for anc in ['<section class="faq-section"','<section class="service-proof','<footer']:
        if anc in h: h=h.replace(anc,sec+anc,1);break
    if p in ANS and 'answer-first' not in h and 'quick-answer' not in h:
        i=h.find('</section>',h.find('<section class="service-hero"'))+10
        h=h[:i]+f'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">{ANS[p]}</p></section>'+h[i:]
    # FAQ schema
    m=re.search(r'"@type"\s*:\s*"FAQPage"\s*,\s*"mainEntity"\s*:\s*\[',h)
    if m:
        qj=json.dumps({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}},ensure_ascii=False)
        h=h[:m.end()]+qj+','+h[m.end():]
    h=re.sub(r'("dateModified"\s*:\s*")[^"]*"',r'\g<1>'+TODAY+'"',h)
    h=re.sub(r'(article:modified_time" content=")[^"]*"',r'\g<1>'+TODAY+'"',h)
    h=re.sub(r'(<p class="guide-meta">Updated <time datetime=")[^"]*">>?[^<]*</time>',r'\g<1>'+TODAY+'">5 November 2026</time>',h)
    h=re.sub(r'((?i:last updated):?\s*)(?:<time[^>]*>)?\d{1,2} [A-Z][a-z]+ 2026(</time>)?',lambda m:m.group(1)+'5 November 2026',h)
    open(f,'w',encoding='utf-8').write(h);return True
if __name__=='__main__':
    L=[x for x in open(sys.argv[1]).read().split() if x]
    done=[p for p in L if refresh(p)]
    s=open('sitemap.xml').read()
    for p in done:
        s=re.sub(r'(<loc>https://unbanz.com/'+re.escape(p)+r'/</loc>\s*<lastmod>)[^<]*',r'\g<1>'+TODAY,s)
    open('sitemap.xml','w').write(s)
    open('/workspace/refreshed.txt','a').write('\n'.join(done)+'\n');print(len(done))
