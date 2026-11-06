import json,re,html,pathlib,sys
T=open('can-someone-take-my-inactive-instagram-username/index.html').read()
HEAD_END=T.index('<script type="application/ld+json">')
LD_END=T.index('</script>',HEAD_END)+9
MAIN_START=T.index('<main id="content">')+len('<main id="content">')
MAIN_END=T.index('</main>')
g=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',T,re.S).group(1))
BASE=[n for n in g['@graph'] if n['@type'] in('Organization','WebSite')]
OLD='https://unbanz.com/can-someone-take-my-inactive-instagram-username/'
OT='Can Someone Get My Instagram Username If I’m Inactive?'
OD='Can someone take your Instagram username if your account is inactive? What Instagram actually says, when a handle can move, and how to protect yours.'
WA='https://wa.me/19342012490?text=Hey%20Unbanz%2C%20I%20want%20to%20claim%20this%20username%3A%20%40'
DATE='2026-11-06'
def e(x): return html.escape(x,quote=True)
def strip(x): return re.sub('<[^>]+>','',x)
COST={'Instagram':'','TikTok':'','Snapchat':''}
def shared_faq(p):
    return [
     ('How much does a %s username claim cost?'%p,'It depends on the handle. You get your quote in the chat before anything starts. You pay by card through Whop checkout. Nothing is charged for asking whether a handle is doable.'),
     ('What if the claim fails?','Our refund policy gives a 100% refund if a username claim fails, meaning the handle is not claimed onto your profile. See <a href="/refund-policy/">refund policy</a>.'),
     ('Do you need my password or login codes?','No. We never ask for passwords or codes. We work from the handle you want and your profile link.'),
    ]
def how(p):
    return ('how','How it works with Unbanz','<ol><li>Send the handle you want and your %s profile link on <a href="https://wa.me/19342012490">WhatsApp</a> or to <a href="mailto:team@unbanz.com">team@unbanz.com</a>.</li><li>We tell you straight whether there is a legit route: an inactive account, a trademark or brand report, an impersonation report or %s’s own processes.</li><li>If there is, you get your quote in the chat. It depends on the handle. You pay by card through Whop checkout.</li><li>We prepare and file everything through %s’s own tools and keep you posted. %s makes the final call, so we can’t promise timing or an outcome. If the claim fails, our refund policy gives you 100%% back.</li></ol>'%(p,p,p,p))
SAFE=('safe','Staying safe','<p>We never ask for passwords or codes. We don’t hack accounts, buy stolen handles or file false reports. If someone offers a “plug” at the platform, asks you to log in through their link or wants to sell you an account, walk away.</p>')
ABOUT=('about-unbanz','About Unbanz','<p>Unbanz (unbanz.com) is an independent service that claims Instagram usernames onto clients’ own profiles through Instagram’s own processes. The price depends on the handle; card payment through Whop checkout; 100% refund if a username claim fails. We never ask for passwords or codes. Contact: <a href="https://wa.me/19342012490">WhatsApp +1 934 201 2490</a> or <a href="mailto:team@unbanz.com">team@unbanz.com</a>. Not affiliated with Meta.</p>')
def page(slug,title,desc,h1,lead,answer,secs,faqs,plat,related,crumb=('/username/','Home / Usernames'),noshared=False,cards=None):
    url='https://unbanz.com/%s/'%slug
    head=T[:HEAD_END].replace(OLD,url).replace(e(OT),e(title)).replace(OT,e(title)).replace(OD,e(desc))
    allf=faqs+([] if noshared else shared_faq(plat))
    if not noshared: secs=secs+[how(plat),SAFE,ABOUT]
    graph=BASE+[{"@type":"WebPage","@id":url+"#webpage","url":url,"name":title,"description":desc,"isPartOf":{"@id":"https://unbanz.com/#website"},"about":{"@id":"https://unbanz.com/#organization"},"inLanguage":"en-US","dateModified":DATE,"breadcrumb":{"@id":url+"#breadcrumb"}},
      {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://unbanz.com/"},{"@type":"ListItem","position":2,"name":"Username claims","item":"https://unbanz.com/username/"},{"@type":"ListItem","position":3,"name":h1,"item":url}]},
      {"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in allf]}]
    ld='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)+'</script>'
    body=T[LD_END:MAIN_START]
    m=('<section class="service-hero"><div class="container"><a class="crumb" href="%s">%s</a><h1>%s</h1><p class="guide-meta">Updated <time datetime="%s">6 November 2026</time></p><p>%s</p><div class="hero-cta"><a class="button button-light" href="%s" data-service="username" data-platform="%s">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="hero-email" href="mailto:team@unbanz.com?subject=Username%%20claim">Prefer email? ↗︎</a></div></div></section>'%(crumb[0],crumb[1],e(h1),DATE,lead,WA,plat)
      +'<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0"><strong>%s</strong></p></section>'%answer+('<section class="service-editorial container">'+''.join('<article><h2>%s</h2><p>%s</p></article>'%c for c in cards)+'</section>' if cards else '')+'<article class="guide-body container">'
      +''.join('<h2 id="%s">%s</h2>%s'%(i,h,b) for i,h,b in secs)
      +'<p class="inline-wa"><strong>Got a handle in mind?</strong> <a href="%s" data-service="username">Send it to us on WhatsApp ↗︎</a> and you hear first if it’s doable.</p></article>'%WA
      +'<section class="faq-section" id="faq"><div class="container faq-layout"><div class="faq-intro"><p class="eyebrow">QUICK ANSWERS</p><h2>Good to know.</h2></div><div class="simple-faq">'
      +''.join('<details><summary>%s<span aria-hidden="true">+</span></summary><p>%s</p></details>'%(e(q),a) for q,a in allf)
      +'</div></div></section><section class="service-proof container"><h2>Tell us the handle you want.</h2><div class="cta-pair"><a class="button button-blue" href="%s">Message us on WhatsApp <span aria-hidden="true">↗︎</span></a><a class="button button-light" href="mailto:team@unbanz.com?subject=Username%%20claim">Email us</a></div></section>'%WA
      +'<nav class="related-services container" aria-label="Related pages">'+''.join('<a href="%s">%s</a>'%(u,t) for u,t in related)+'</nav>')
    out=head+ld+body+m+T[MAIN_END:]
    p=pathlib.Path(slug); p.mkdir(exist_ok=True); (p/'index.html').write_text(out)
    return slug,h1,desc
