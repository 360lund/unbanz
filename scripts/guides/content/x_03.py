EXPAND = {}
def add(slug, secs, faq=None):
    d = dict(secs=secs)
    if faq: d['faq'] = faq
    EXPAND[slug] = d

add('meta-ad-payment-declined-fix', [
 ('types', 'Three kinds of billing problem that look alike',
  '<ul><li><strong>Declined charge:</strong> your bank or card refused it. Fix the card or call the bank, then pay the balance.</li><li><strong>Payment restriction:</strong> Meta has limited how you can pay, often after unusual activity. Follow the steps in the banner and the help article on restrictions.</li><li><strong>Disabled ad account:</strong> a policy decision, not billing. Paying the balance doesn’t reverse it; it needs an appeal.</li></ul>'
  '<p>The wording in the banner usually tells you which one you’re dealing with. If it mentions your balance or payment method, it’s billing. If it mentions policies or circumventing systems, go to the appeal route and don’t spend time re-entering cards.</p>'),
 ('records', 'Keep records for your accountant',
  '<p>Download the transaction history from Billing & payments after each fix. If a charge was made twice or you were charged while ads were paused, you’ll want the dates and amounts when you speak to Meta’s support or your card issuer. Unauthorised charges should go to your bank straight away.</p>')])

add('meta-ad-rejected-request-review', [
 ('examples', 'Reading rejection reasons in practice',
  '<ul><li><strong>“Personal attributes”</strong> usually means the copy addresses the viewer’s health, finances or identity. Rewrite around the offer.</li><li><strong>“Landing page”</strong> means the page behind the ad has a problem: errors, a mismatch or content that breaks a policy.</li><li><strong>“Misleading claims”</strong> means a promise, price or result the ad can’t support. Make it specific and true.</li><li><strong>“Sensitive content”</strong> often relates to images, such as close-ups of bodies or shocking visuals.</li><li><strong>“Restricted goods or services”</strong> means the product is in a category with special rules. Check the policy for permissions or age limits.</li></ul>'
  '<p>If the notice is vague, test the ad with each element removed in a duplicate, so you can see which one triggers the problem. Don’t do this on the ad that’s under review.</p>')],
 faq=[('Should I delete a rejected ad?', 'There’s no need. Keep it for the record, and duplicate it if you want to try a fix.')])

add('meta-domain-verification-steps', [
 ('who', 'Who should own this task?',
  '<p>Domain verification sits between marketing and whoever manages the website, which is why it often stalls. Decide in advance who has the registrar login and who can edit the site. If an agency built your website, ask them to add the tag or record, and make sure the domain is registered in your business’s name, not theirs. Verification tells Meta your business controls the domain; if someone else controls it, you’re stuck whenever they’re unavailable.</p>')])

add('meta-business-portfolio-two-factor', [
 ('rollout', 'A simple rollout plan',
  '<ol><li>Remove inactive people from the portfolio.</li><li>Send the team a short message explaining the change, the date and what to prepare.</li><li>Ask everyone to set up an authentication app and save recovery codes before the date.</li><li>Switch the setting on.</li><li>Check the people list a few days later to see who hasn’t completed setup and help them.</li></ol>'
  '<p>For contractors, include a note in their onboarding. For people who share a workstation, agree on how they’ll handle codes without sharing a single device.</p>')])

add('meta-business-portfolio-lost-admin-access', [
 ('triage', 'Triage: what is the risk right now?',
  '<p>Before the paperwork, work out what’s exposed. Are ads still running? Is the payment method still attached? Are other people able to edit your Pages? If money is at stake, contact your bank to review charges or temporarily suspend the card. For ad accounts you can still reach, lower or pause budgets. Then work on the access request with a clear head.</p>'
  '<p>Write a one-page timeline: when you last had access, who had it, what changed and when you noticed. A tidy timeline speeds up any conversation about the portfolio.</p>')])

add('meta-agency-partner-access', [
 ('contract', 'What to put in the contract',
  '<ul><li>Which assets the agency can access and at what level.</li><li>That ad accounts and Pages remain owned by your business.</li><li>Who pays Meta, and how invoices work.</li><li>What happens to data, pixels and creative at the end of the contract.</li><li>That neither party shares logins, and both use two-factor authentication.</li></ul>'
  '<p>A few clear lines up front prevent the most painful disputes later, which usually involve an ad account that’s in the agency’s portfolio when the relationship ends.</p>')])

add('meta-special-ad-categories', [
 ('examples', 'Examples that trip people up',
  '<ul><li>A recruitment agency advertising a role, even in a general way, is employment.</li><li>An estate agent promoting a property is housing, but a furniture store is not.</li><li>A lender or a card offer is credit. A budgeting app that doesn’t offer credit may not be.</li><li>A charity campaign tied to a political issue can count as a social issue ad. A general fundraising ad may not.</li></ul>'
  '<p>When it’s borderline, read the definitions on Meta’s policy page and, if the choice is still unclear, pick the category rather than risk a rejection.</p>')])

add('meta-ads-health-wellness-personal-attributes', [
 ('rewrite', 'Rewrite examples',
  '<ul><li><strong>Instead of:</strong> “Struggling with anxiety?” <strong>Try:</strong> “Online counselling sessions, evenings and weekends.”</li><li><strong>Instead of:</strong> “Lose your belly fat fast.” <strong>Try:</strong> “Small-group strength classes for beginners.”</li><li><strong>Instead of:</strong> “Are you in debt?” <strong>Try:</strong> “Free budgeting workshop on Thursday.”</li></ul>'
  '<p>Notice what changes. The rewrite says what you offer, when and how, and leaves the viewer’s situation unmentioned. It’s also more useful for people who aren’t in the situation you assumed.</p>')])

add('meta-ads-landing-page-rejected', [
 ('checks', 'A reviewer-style checklist',
  '<ul><li>Business name and contact details visible.</li><li>Clear description of what is being sold.</li><li>Prices and fees shown, including shipping.</li><li>Return, refund and privacy policies reachable.</li><li>No fake countdown timers or invented stock levels.</li><li>No sudden redirects to unrelated sites.</li></ul>'
  '<p>Print this list and go through your top five pages. It takes ten minutes and catches most problems before a review does.</p>')])

add('meta-account-quality-status-walkthrough', [
 ('terms', 'What the common statuses mean in plain language',
  '<ul><li><strong>Limited or restricted:</strong> some features or ad spending are held back while the issue is fixed.</li><li><strong>Disabled:</strong> the asset can’t be used until the decision changes. Look for a review option.</li><li><strong>Disapproved ad:</strong> one ad was rejected. The account may be fine.</li><li><strong>Warning:</strong> Meta is telling you about a risk. Fix the cause before it becomes a restriction.</li></ul>'
  '<p>Statuses can differ across a portfolio. A Page can be fine while an ad account is restricted, so check each asset in turn.</p>'),
 ('flow', 'A weekly five-minute routine',
  '<p>Open Account Quality, scan each portfolio for new notices, open any ad rejections from the last week, and check that payment methods are valid. Then record anything new in a shared log. If you see a warning, fix it that day rather than waiting for a restriction.</p>')])
