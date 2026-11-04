# Ad account cluster upgrade (4 Nov): answer-first block, prefilled WhatsApp CTA, country notes, FAQ schema, cluster links.
import re,json,html,urllib.parse as U
T="Terms are agreed with you before any work starts."
e=lambda s:html.escape(s,quote=False)
CL=[('/ad-account-recovery/','Ad account recovery service'),('/facebook-ad-account-disabled/','Ad account disabled'),
('/facebook-profile-restricted-ad-account-affected/','Restricted from advertising'),('/business-manager-disabled/','Business Manager disabled'),
('/meta-business-portfolio-restricted-help/','Business Portfolio restricted'),('/ad-account-restricted-payment-issue/','Payment flag'),
('/ad-account-policy-violation-appeal/','Policy violation'),('/agency-ad-account-recovery/','Agency accounts'),
('/client-ad-account-disabled-agency-help/','Client account disabled')]
CO=('<h3>Where you are changes the paperwork</h3><ul>'
'<li><strong>United States:</strong> business verification usually wants the legal name and address as on IRS or state records, for example an EIN letter or articles of organization.</li>'
'<li><strong>United Kingdom:</strong> the name should match Companies House, or your sole trader details and a utility bill.</li>'
'<li><strong>Canada:</strong> a provincial or federal registration or a Business Number document, with the same address the portfolio shows.</li>'
'<li><strong>Netherlands:</strong> a KvK extract. As an EU business you can also ask Meta for a statement of reasons under the Digital Services Act.</li>'
'<li><strong>France:</strong> a Kbis or SIRENE extract, and the same DSA statement-of-reasons right.</li></ul>')
P={
'ad-account-recovery':('my Meta ad account is disabled or restricted','Meta ad account disabled or restricted: the short answer',
 'Open Meta Business Support Home, screenshot the exact notice, fix the cause it points to, then request one review as an admin. Most failed appeals argue the decision was wrong instead of showing what changed. Unbanz prepares the appeal and handles it through Meta’s official review. Meta makes the final decision.',
 [('What is the difference between a disabled and a restricted ad account?','Restricted usually means a limit you can request review on. Disabled means ads stopped at account level. The notice in Business Support Home says which one applies.'),
  ('How long does Meta take to review an ad account?','Meta says many reviews finish in about 48 hours, but some take much longer. With Unbanz the usual estimate is 3–14 days from the day work starts.'),
  ('What does Unbanz need to look at my ad account?','The ad account ID, the Business Portfolio ID, a screenshot of the notice, your country and whether business verification is done. Never a password or login code.'),
  ('Can I just open a new ad account?','Creating new accounts to get around a restriction can be treated as circumventing systems and make things worse. Deal with the original account first.')]),
'facebook-ad-account-disabled':('my Facebook ad account is disabled','Disabled ad account: the short answer',
 'A disabled ad account means Meta stopped all ads at account level. Screenshot the notice, check for a payment or policy reason, fix it, then request one review from Business Support Home. Unbanz helps prepare that review through Meta’s official process.',
 [('Can a disabled Meta ad account be reinstated?','Sometimes, when the cause is fixed and the review is clear. If it stays ineligible for six months, Meta says it cannot be reinstated, so act early.'),
  ('Will I lose my prepaid ad balance?','Meta says unused prepaid funds may be forfeited where the law allows if the account stays disabled for policy reasons. Ask about a refund separately.'),
  ('Can Unbanz help with a disabled ad account?','Yes. We read the notice, tell you honestly what route is left and prepare the review. '+T)]),
'facebook-profile-restricted-ad-account-affected':('my profile is restricted from advertising','Restricted from advertising: the short answer',
 'When the person, not the ad account, is restricted from advertising, every ad account they admin stops. Check the profile in Business Support Home, confirm identity if asked, then request review on the profile itself. Unbanz helps prepare it through Meta’s official process.',
 [('Why is my personal profile restricted from advertising?','Common triggers are unusual logins, a hack, links to a restricted portfolio, or repeated ad rejections. The notice names the area.'),
  ('Can another admin keep running ads?','Often yes, if their own profile is in good standing. Adding a new admin only to dodge the restriction can backfire.'),
  ('Can Unbanz help with an advertising restriction?','Yes. We help with the profile review through Meta’s official process. '+T)]),
'business-manager-disabled':('my Business Manager is disabled','Business Manager disabled: the short answer',
 'A disabled Business Manager, now called a Business Portfolio, takes every ad account, Page and pixel inside it offline. Screenshot the notice, check business verification and admin history, then request one review as an admin. Unbanz helps prepare the review through Meta’s official process.',
 [('Do I lose my Pages if my Business Portfolio is disabled?','Pages usually still exist but can’t be managed or advertised through that portfolio. Personal admins of the Page may still reach it.'),
  ('Is a Business Manager the same as a Business Portfolio?','Yes. Meta renamed Business Manager to Business Portfolio. Help pages use both names.'),
  ('Can Unbanz help with a disabled portfolio?','Yes. We map the structure, find the likely trigger and prepare the review. '+T)]),
'meta-business-portfolio-restricted-help':('my Business Portfolio is restricted','Business Portfolio restricted: the short answer',
 'A restricted portfolio often limits advertising while the assets stay visible. Open Business Support Home, read “What you can do”, complete any verification and request review. Shared admins or assets linked to a restricted account are frequent causes. Unbanz helps prepare the review through Meta’s official process.',
 [('What causes a Business Portfolio restriction?','Usually a verification gap, an admin with a restricted profile, a shared payment method or an asset linked to another restricted portfolio.'),
  ('Should I remove admins before appealing?','Remove people you do not recognise and secure the rest first. Do not reshuffle the whole structure, which can look like evasion.'),
  ('Can Unbanz help with a restricted portfolio?','Yes, through Meta’s official review only. '+T)]),
'ad-account-restricted-payment-issue':('my ad account is restricted for a payment issue','Payment flag: the short answer',
 'Payment restrictions usually follow a failed charge, a chargeback, a new card in another name or a billing country change. Settle any balance, use a card in the business or admin name, then request review. Unbanz helps prepare it through Meta’s official process.',
 [('Can I fix a payment restriction just by paying the balance?','Sometimes the account unlocks once the balance clears. If it stays restricted, request review with the payment proof.'),
  ('Does a chargeback get an ad account disabled?','It can. Disputing a Meta charge with your bank often triggers a payment-related restriction.'),
  ('Can Unbanz help with a payment restriction?','Yes. We help put the payment record in order and prepare the review. '+T)]),
'ad-account-policy-violation-appeal':('my ad account was flagged for a policy violation','Policy flag: the short answer',
 'Find the policy named in the notice, then fix the ads and landing pages behind it before you appeal. A review that shows what changed has a better chance than one that only disagrees. Unbanz helps prepare that review through Meta’s official process.',
 [('Which policies most often disable ad accounts?','Circumventing systems, unacceptable business practices, misleading claims, personal attributes and restricted goods such as supplements or finance.'),
  ('Should I delete the rejected ads before appealing?','Pause or edit them and keep screenshots. Deleting everything can remove the evidence you need to explain the change.'),
  ('Can Unbanz help with a policy appeal?','Yes. We help prepare an appeal that maps the notice to the fixes. '+T)]),
'agency-ad-account-recovery':('a client ad account we manage is restricted','Agency accounts: the short answer',
 'When a client account goes down, act as the agency partner, not the owner: the client portfolio admin must request review. Gather the notice, IDs and recent ads, check whether a shared admin or payment links several clients, then file one review. Unbanz works with agencies through Meta’s official process.',
 [('Can an agency request review for a client account?','Only an admin on the account can request review. Often the client must click it, with the agency preparing the content.'),
  ('Can one flagged client affect our other clients?','Yes, through shared admins, payment methods or assets. Separate them once the review is underway.'),
  ('Does Unbanz work white-label for agencies?','Yes. We can work behind your agency and keep you as the client contact. '+T)]),
'client-ad-account-disabled-agency-help':('a client ad account is disabled','Client account disabled: the short answer',
 'Ask the client to screenshot the notice in Business Support Home, then check the agency’s access, payment and recent creative. Prepare one review the client admin submits. Do not move the client into a fresh account. Unbanz helps agencies prepare these reviews through Meta’s official process.',
 [('Who should submit the review for a client account?','An admin of the client’s portfolio. The agency can draft it and gather evidence.'),
  ('Should we move the client to our own Business Portfolio?','Not while it is under review. Moving assets can look like evasion and spread the restriction.'),
  ('Can Unbanz help our agency?','Yes, including white-label work. '+T)]),
}
BAN=re.compile(r'\bcases?\b|we review|fixed price|fast turnaround|guarantee|gets it done|price in the chat|crypto',re.I)
out=[]
for slug,(situ,h2,ans,faqs) in P.items():
    f=slug+'/index.html'; h=open(f).read()
    h=re.sub(r'<section class="container" data-nov04i="ads">.*?</section>','',h,flags=re.S)
    msg='https://wa.me/19342012490?text='+U.quote('Hi Unbanz, %s. Ad account ID: . Business Portfolio ID: . Country: . I can send a screenshot of the notice.'%situ)
    b='<section class="container" data-nov04i="ads"><h2>%s</h2><p class="answer">%s</p>'%(e(h2),e(ans))
    b+='<p><a class="button button-blue" href="%s">Send the ad account ID on WhatsApp</a> or email <a href="mailto:team@unbanz.com?subject=Ad%%20account%%20help">team@unbanz.com</a>. Your password stays with you. The usual estimate is 3–14 days from the day work starts. %s</p>'%(msg,T)
    b+=('<h3>What to send</h3><ul><li>A screenshot of the full notice from Business Support Home</li><li>The ad account ID and Business Portfolio ID</li>'
        '<li>The landing page and ads running when it happened</li><li>Whether business verification is complete, and your country</li></ul>'
        '<h3>What we never do</h3><ul><li>Ask for a password, login code or backup code</li><li>Rent, sell or supply ad accounts, or help anyone get around an enforcement decision</li>'
        '<li>Claim contacts inside Meta. Meta’s review team makes the decision</li></ul>')
    b+=CO+'<h3>Quick answers</h3>'+''.join('<h4>%s</h4><p>%s</p>'%(e(q),e(a)) for q,a in faqs)
    b+='<nav aria-label="Ad account help"><strong>Ad account help:</strong> '+' · '.join('<a href="%s">%s</a>'%(u,e(t)) for u,t in CL if u!='/%s/'%slug)+'</nav></section>'
    assert not BAN.search(b),slug
    m=re.search(r'<section class="container" data-nov04b="send">.*?</section>',h,re.S)
    i=m.end() if m else h.find('</section>',h.find('class="service-hero"'))+10
    h=h[:i]+b+h[i:]
    def r(mm):
        if 'FAQPage' not in mm.group(1) and '"dateModified"' not in mm.group(1): return mm.group(0)
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
    assert h.count('FAQPage')>=1,slug
    open(f,'w').write(h); out.append('https://unbanz.com/%s/'%slug); print('ok',slug)
open('/tmp/ads.txt','w').write('\n'.join(out))
