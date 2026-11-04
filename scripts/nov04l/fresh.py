import sys;sys.path.insert(0,'scripts/nov04l')
from lib import *
CN=[('usa','the US'),('uk','the UK'),('canada','Canada'),('netherlands','the Netherlands'),('france','France')]
def links(pat,label):
    return '<p><strong>'+label+'</strong> '+', '.join(f'<a href="/{pat.format(c=c)}/">{n}</a>' for c,n in CN if os.path.isdir(pat.format(c=c)))+'.</p>'
ACC=['When we checked on 4 November 2026, the old Instagram “my account was deactivated” form opened the Account Status help page and the Meta AI support assistant, not a form. Appeal from the notice in the app or from Accounts Center.',
 f'Meta says it has no general public phone number for customer service ({ext("https://www.facebook.com/help/1088016719924954","Meta Help Center")}). Its starting page for login and recovery problems is the Account Recovery Hub ({ext("https://www.meta.com/account-recovery-support/")}).',
 'In the EU, Appeals Centre Europe has reviewed Facebook and Instagram account suspensions since 2025, free for users, after Meta’s own appeal. In the UK, Report Fraud replaced Action Fraud on 4 December 2025 for reporting hacks and scams.']
ADS=[f'Meta says ad account reviews are limited, and once a review is completed the decision is final ({ext("https://www.facebook.com/business/help/530209463124901","Meta Business Help Center")}). Fix the cause named in Account Quality before you click Request review.',
 'Restrictions, reviews and business verification all sit in Business Support Home on a computer. Only an admin of the ad account or Business Portfolio can request a review.',
 'Meta has no general public phone line for Business Support. Eligible advertisers get chat support, and Meta Verified for business adds support access for accounts you can still log in to.']
UN=['Instagram still has no public form to request a username held by an inactive account. The only official request route with a form is a trademark report, for a registered mark.',
 'Buying or selling usernames is against Instagram’s terms. Sellers who promise a handle for crypto are a common scam.',
 'Your password stays with you. A claimed username is moved to an account you control.']
def blk(kind):
    b,cl=( (ACC,[('instagram-disabled-{c}-what-to-do','Instagram disabled in'),('facebook-account-disabled-{c}-what-to-do','Facebook disabled in'),('instagram-account-recovery-{c}','Instagram recovery in')]) if kind=='acc' else
          (ADS,[('best-meta-ad-account-recovery-service-{c}','Meta ad account help in')]) if kind=='ads' else
          (UN,[('instagram-username-claim-{c}','Username claims in')]))
    extra=''
    if kind=='acc': extra='<p><strong>Instagram suspended in</strong> <a href="/instagram-suspended-appeal-usa/">the US</a>, <a href="/instagram-suspended-appeal-uk/">the UK</a>, <a href="/instagram-suspended-appeal-canada/">Canada</a>, <a href="/instagram-account-suspended-netherlands-what-to-do/">the Netherlands</a>, <a href="/instagram-account-suspended-france-what-to-do/">France</a>.</p>'
    if kind=='ads': extra='<p><strong>Ad account disabled in</strong> <a href="/facebook-ad-account-restricted-us-business/">the US</a>, <a href="/facebook-ad-account-disabled-uk/">the UK</a>, <a href="/facebook-ad-account-disabled-canada/">Canada</a>, <a href="/meta-ad-account-disabled-netherlands/">the Netherlands</a>, <a href="/meta-ad-account-disabled-france/">France</a>.</p>'
    return ('<h2 id="updated-2026">What changed in 2026</h2><ul>'+''.join(f'<li>{x}</li>' for x in b)+'</ul>'
      '<h3>By country</h3>'+''.join(links(p,l) for p,l in cl)+extra)
pages={'acc':['facebook-account-recovery','instagram-account-recovery','facebook-unban-service','instagram-unban-service','unban','guides/facebook-account-disabled-appeal','guides/instagram-account-suspended-appeal','guides/instagram-disabled-no-appeal-button','instagram-account-help','instagram-appeal-denied','facebook-account-help','guides/instagram-account-disabled','guides/instagram-appeal-sent-no-response','guides/why-instagram-bans-accounts','facebook-hacked-account-recovery-service','instagram-account-disabled-appeal','instagram-hacked-account-recovery-service'],
 'ads':['ad-account-recovery','guides/meta-ad-account-restricted','meta-ad-account-help','meta-ad-account-appeal-rejected-what-next','how-long-does-meta-ad-account-review-take','agency-ad-account-recovery','white-label-account-recovery'],
 'un':['username','instagram-username-claim','inactive-instagram-username','best-instagram-username-claim-service']}
done=[]
for k,ps in pages.items():
    for p in ps:
        if not os.path.isdir(p): print('missing',p);continue
        if add_section(p,blk(k),anchor='updated-2026'): done.append(f'https://unbanz.com/{p}/')
print(len(done),bump_lastmod(done))
open('/tmp/b3.txt','w').write('\n'.join(done+['https://unbanz.com/sitemap.xml']))
