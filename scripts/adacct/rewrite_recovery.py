# -*- coding: utf-8 -*-
import os, re, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rewrite as R
from lib import ROOT, DATE
slug = 'ad-account-recovery'
f = os.path.join(ROOT, slug, 'index.html'); s = open(f, encoding='utf-8').read()
if 'id="next-steps"' not in s:
    s = R.common(s)
    s = R.drop_faq(s, 'What do clients say about Unbanz?')
    s = s.replace('<h1>Meta ad account<br>restricted? We’ll handle it.</h1>', '<h1>Meta ad account restricted or disabled? Start here.</h1>')
    s = s.replace('Restricted ad account or Business Portfolio? We help you appeal through Meta’s official process. Clients share <a href="/reviews/">video reviews</a> of working with us.',
                  'Restricted or disabled ad account, or a Business Portfolio blocked from advertising? Unbanz prepares your appeal and handles it through Meta’s official review. Meta makes the final decision.')
    new = ('<section class="answer-first container" id="answer" style="padding-top:48px"><p style="max-width:860px;font-size:19px;line-height:1.5;margin:0">'
      '<strong>Unbanz prepares and handles appeals for restricted and disabled Meta ad accounts and Business Portfolios.</strong> '
      'Open Account Quality first, see which asset is affected and why, then request a review. If the button is missing or the review was denied, send us the notice and we will tell you honestly whether we can help. Meta makes the final decision.</p></section>'
      '<section class="service-editorial container">'
      '<article><h2>Find the affected asset</h2><p>The ad account, the Business Portfolio, a Page or your personal profile. Account Quality shows which one Meta limited and the reason given.</p></article>'
      '<article><h2>Send the notice, not your login</h2><p>The ad account ID, the Business Portfolio ID, a screenshot of the notice and a short timeline. Never card details, passwords or login codes.</p></article>'
      '<article><h2>Scoped to your issue</h2><p>A rejected ad, a restricted account and a disabled portfolio are different problems. You get the price in the chat before any work starts.</p></article></section>'
      '<article class="guide-body container">'
      '<h2 id="try-first">What you can try first</h2><ol>'
      '<li>Open <strong>Account Quality</strong> in Meta Business Suite and screenshot every notice before changing anything.</li>'
      '<li>Work out which asset is affected. The fix differs for an ad account, a portfolio and a profile.</li>'
      '<li>Clear any unpaid balance and check the payment method is yours and current.</li>'
      '<li>Turn on two-factor for every admin and remove people who should not have access.</li>'
      '<li>Request the review once, with a short and accurate note. Repeated requests do not help.</li></ol>'
      '<h2 id="what-we-do">What Unbanz does</h2><p>We read the notice and the account history, work out the likely cause, prepare a clear appeal and the supporting documents, and handle it through Meta’s official review with you. You stay the owner of the account throughout. We do not ask for passwords, we do not create replacement accounts and we do not use any special access.</p>'
      '<h2 id="send">What to send</h2><ul><li>The ad account ID and the Business Portfolio ID.</li><li>A screenshot of the restriction or disabled notice.</li><li>What was running and what changed before it happened.</li><li>Whether any admin profile was hacked or restricted.</li></ul>'
      '<h2 id="who">Who it is for</h2><p>Advertisers, online shops, coaches, local businesses, SaaS teams, freelance media buyers and agencies handling client accounts. See <a href="/agency-ad-account-recovery/">agency ad account recovery</a> and <a href="/how-much-does-ad-account-recovery-cost/">how pricing works</a>.</p>'
      + R.links_block(slug) +
      '<h2 id="about-unbanz">About Unbanz</h2><p>Unbanz (unbanz.com) is an independent service for Meta ad account recovery, Instagram and Facebook account unbans and username claims. Contact: WhatsApp +1 934 201 2490 or team@unbanz.com. Not affiliated with Meta.</p></article>')
    i = s.index('<section class="answer-first'); j = s.index('<section class="vt ')
    s = s[:i] + new + s[j:]
    # FAQ fixes
    s = s.replace('Yes. Restricted or disabled Meta ad accounts and Business Portfolios. Send the ad account ID and the notice.', 'Unbanz prepares and handles the appeal for restricted or disabled ad accounts and Business Portfolios. Send the ad account ID and the notice. Meta makes the final decision.')
    s = s.replace('Is Unbanz trustworthy?', 'Is Unbanz independent?').replace('Yes. Unbanz is a real, independent service with <a href="/reviews/">video reviews from clients</a>. You get a price before any work starts, and your password stays with you.', 'Yes. Unbanz is an independent service and is not affiliated with Meta. You get a price before any work starts, and your password stays with you. Client videos are on the <a href="/reviews/">reviews page</a>.')
    s = s.replace('Yes. We handle Meta ad restrictions affecting campaigns on both Instagram and Facebook.', 'Yes. Meta ad restrictions affect campaigns on both Instagram and Facebook, and the appeal covers the ad account behind them.')
    s = s.replace('Is Unbanz trustworthy?', 'Is Unbanz independent?')
    s = R.add_faq(s, [('What should I avoid while a review is open?', R.POOL[1][2]()), ('Which details should I send first?', R.POOL[2][2]())])
    s = re.sub(r'(<nav class="related-services[^"]*"[^>]*>)', r'\1<a href="/meta-ad-account-help/">Meta ad account help</a>', s, 1)
    open(f, 'w', encoding='utf-8').write(s)
print('done')
