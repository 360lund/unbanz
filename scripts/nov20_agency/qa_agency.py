# Nov 20 2026: agency & white-label Q&A pages. Facts: white-label rate $1,200 per case (account or handle); volume pricing for 5+ cases/month
# agreed in writing after a first test case; paid upfront by bank transfer to our US or UK business bank account (no card);
# usually 7-14 days; 100% refund if not reinstated within 14 days, paid the same business day; 6-month re-ban cover;
# signed agreement with a named authorised signatory on request; official platform routes only; the platform decides.
# No stats, no ratings, no "contacts at Meta", no guarantees. Company name stays off public pages (beneficiary line only).
IG_DISABLED = ("https://help.instagram.com/366993040048856", "Instagram Help: my account was disabled or suspended")
IG_HACKED = ("https://www.instagram.com/hacked/", "Instagram: my account was hacked (instagram.com/hacked)")
FB_HACKED = ("https://www.facebook.com/hacked", "Facebook: my account was hacked (facebook.com/hacked)")
FB_DISABLED = ("https://www.facebook.com/help/103873106370583", "Facebook Help: personal account suspended or disabled")
ACC = ("https://accountscenter.instagram.com/", "Meta Accounts Center (password, security, where you’re logged in)")
IG_STATUS = ("https://help.instagram.com/338481628002750", "Instagram Help: Account Status")
AQ = ("https://www.facebook.com/accountquality", "Meta Account Quality (restrictions on ad accounts, Pages and portfolios)")
ADS_TROUBLE = ("https://www.facebook.com/business/help/422289316306981", "Meta Business Help: troubleshoot a disabled or restricted ad account")
ADS_REVIEW = ("https://www.facebook.com/business/help/530209463124901", "Meta Business Help: request a review when restricted from advertising")
BIZ_VERIF = ("https://www.facebook.com/business/help/2058515294227817", "Meta Business Help: business verification")
BM_ADMIN = ("https://www.facebook.com/business/help/1580486349413648", "Meta Business Help: regain access when a portfolio has lost its admins")
TM_WHAT = ("https://help.instagram.com/101826856646059", "Instagram Help: what is a trademark violation")
TM_FORM = ("https://help.instagram.com/contact/230197320740525", "Instagram trademark report form")
IMP_FORM = ("https://help.instagram.com/contact/636276399721841", "Instagram impersonation report form")
CR_WHAT = ("https://help.instagram.com/126382350847838", "Instagram Help: copyright")
CR_FORM = ("https://help.instagram.com/contact/552695131608132", "Instagram copyright report form")
WA_BAN = ("https://faq.whatsapp.com/465883178708358", "WhatsApp Help Center: about account bans")
WA_POLICY = ("https://business.whatsapp.com/policy", "WhatsApp Business messaging and commerce policies")
TT_BANS = ("https://support.tiktok.com/en/safety-hc/account-and-user-safety/content-violations-and-bans", "TikTok Support: content violations and bans")
TT_SAFETY = ("https://support.tiktok.com/en/safety-hc/account-and-user-safety/account-safety", "TikTok Support: account safety (hacked accounts)")

TERMS = ("The white-label rate is $1,200 per case (one account or handle). Agencies that send 5+ cases a month get volume pricing, agreed in writing after a first test case. "
         "Payment is upfront by bank transfer to our US or UK business bank account (no card payments). Usually 7–14 days from the day we start, "
         "with a 100% refund if the account isn’t reinstated within 14 days, paid the same business day. A signed agreement with a named authorised signatory is available before you pay.")

P = []
def A(**k): P.append(k)

A(slug="how-does-white-label-instagram-account-recovery-work", topic="ig_disabled",
 q="How does white-label Instagram account recovery work for agencies?",
 title="How Does White-Label Instagram Account Recovery Work for Agencies? (2026)",
 desc="The exact handoff: what your agency sends, what Unbanz does behind the scenes, what your client sees, and what it costs. Official routes only; Instagram decides.",
 answer="Your agency stays the only name your client sees. You send Unbanz the client’s @username, a screenshot of the notice and the date; we review it, tell you honestly if it’s doable, then prepare and run the appeal through Instagram’s official process while you relay updates in your own words. The white-label rate is $1,200 per case, usually 7–14 days, with a 100% refund if the account isn’t reinstated within 14 days.",
 sections=[
  ("handoff", "The handoff, step by step", "<ol><li><strong>Intake (you):</strong> collect the @username or profile link, a screenshot of every notice (in-app and email), the date it started, and which email and phone are on the account. Never collect the password.</li><li><strong>Case review (us):</strong> we read the notice, check the account’s status and tell you within a working day whether there is a realistic route, and which one: a disabled-account appeal, a hacked-account route, an identity check, or none.</li><li><strong>Terms:</strong> you get the fee and timing in writing. You charge your client whatever you want; we never contact them.</li><li><strong>Work:</strong> we prepare the appeal and supporting details and take it through Instagram’s official channels. If Instagram needs a selfie video or ID check from the account holder, we tell you exactly what to ask your client for.</li><li><strong>Updates:</strong> you get short, unbranded progress notes you can forward as your own.</li><li><strong>Close:</strong> account back, or a refund if it isn’t reinstated within 14 days.</li></ol>"),
  ("client-sees", "What your client sees (and doesn’t)", "<ul><li>Your agency’s name, your updates and your invoice. Nothing from Unbanz.</li><li>Any check Instagram itself asks for, such as a video selfie on the account holder’s phone. Those come from Instagram, not from us, so they don’t reveal the partner.</li><li>No logins are shared. We work from the username and the notice, so the client never hands over a password.</li></ul>"),
  ("cases", "Which Instagram cases fit white label", "<ul><li><strong>Disabled or suspended</strong> for “account integrity”, impersonation flags or mistaken age.</li><li><strong>Hacked</strong> accounts where the email and phone were changed.</li><li><strong>Username claims</strong> for a client brand whose handle is held by an inactive or infringing account (see <a href=\"/can-reputation-firms-white-label-instagram-username-claims/\">username claims for reputation firms</a>).</li><li><strong>Not a fit:</strong> accounts genuinely used for scams, bought or rented accounts, or anything needing mass reports. We say no to those.</li></ul>"),
  ("terms", "Fees and terms for agencies", "<p>" + TERMS + "</p><p>6-month re-ban cover: if a reinstated account is banned again within 6 months, we recover it free or refund 100%. See <a href=\"/white-label-social-media-unbanning-cost-for-agencies/\">what white-label unbanning costs</a>.</p>"),
 ],
 links=[IG_DISABLED, IG_HACKED, IG_STATUS, ACC],
 faqs=[("Does my client need to know about Unbanz?", "No. In white label you are the provider to your client. We never contact them and our updates carry no Unbanz branding."),
  ("Do you need the client’s Instagram password?", "No. We work from the username, the notice and the date. Your client keeps their password and login codes."),
  ("How fast do you reply to a new case?", "We review new agency cases within a working day and tell you if there is a realistic route before anything is agreed."),
  ("What if Instagram asks for a video selfie?", "We tell you exactly what Instagram is asking for so your client can complete it on their own phone. It comes from Instagram, not from us."),
  ("Can you guarantee the account comes back?", "No one can: Instagram makes the final decision. That is why there is a 100% refund if the account isn’t reinstated within 14 days."),
  ("How do we start?", "Send one real case as a test: the @username, a screenshot of the notice and the date. Partner terms follow after that first case.")],
 related=[("white-label-agency", "White label for agencies"), ("white-label-instagram-account-recovery", "White label Instagram recovery"), ("how-do-social-media-agencies-recover-hacked-client-instagram", "Hacked client accounts"), ("white-label-social-media-unbanning-cost-for-agencies", "What it costs")])

A(slug="can-pr-and-talent-agencies-outsource-instagram-tiktok-recovery", topic="tiktok",
 q="Can PR and talent agencies outsource disabled Instagram and TikTok recoveries?",
 title="Can PR and Talent Agencies Outsource Disabled Instagram and TikTok Recoveries? (2026)",
 desc="Yes. How PR firms and talent managers hand over disabled Instagram and TikTok accounts for clients and creators, keep it confidential, and run the press side in parallel.",
 answer="Yes. PR firms and talent managers can hand disabled or banned Instagram and TikTok accounts to a white-label partner like Unbanz while they handle the client and the press. You send the handle, the notice and the date; we run the appeal through Instagram’s or TikTok’s own process and you stay the only contact your client or creator deals with. The white-label rate is $1,200 per case; the platform makes the final decision.",
 sections=[
  ("two-tracks", "Run two tracks at once", "<p>When a high-profile account goes down, there are two jobs: the <strong>platform track</strong> (getting the account back) and the <strong>communication track</strong> (what fans, brands and journalists hear). Agencies usually keep the communication track in-house and outsource the platform track, because appeal work needs specific know-how and patience, not a press release.</p><ul><li>Platform track: appeal, identity checks, follow-ups. That is the part we do.</li><li>Communication track: a holding line for brand partners, a backup channel for announcements, and no public speculation about why the account is down.</li></ul>"),
  ("instagram", "Instagram: what we need", "<ul><li>The @username and a screenshot of the disabled or suspended notice.</li><li>The date it happened and anything posted or changed just before.</li><li>Whether the creator has already appealed, and the outcome.</li></ul><p>Instagram gives a set window to disagree with a decision, so send it early.</p>"),
  ("tiktok", "TikTok: what we need", "<ul><li>The @handle and screenshots from <strong>Settings › Account status</strong>, which lists violations and appeal options.</li><li>Whether the ban is permanent, temporary, or a feature restriction (live, comments, monetisation).</li><li>For a hacked TikTok, the email and phone originally on the account.</li></ul><p>TikTok decides appeals itself; we prepare the case and handle follow-up through its in-app and web support routes.</p>"),
  ("confidential", "Keeping it confidential", "<ul><li>You don’t have to name the client: a handle and the notice are enough.</li><li>We never contact your client, their brand partners or the press.</li><li>Updates are unbranded so you can forward them as your own.</li><li>A signed agreement, including confidentiality, is available before you pay.</li></ul>"),
  ("terms", "Fees and terms", "<p>" + TERMS + "</p>"),
 ],
 links=[IG_DISABLED, IG_STATUS, TT_BANS, TT_SAFETY],
 faqs=[("Do you work with creators directly or only through the agency?", "In white label we work only through your agency. The creator deals with you."),
  ("Can you recover a creator’s TikTok after a permanent ban?", "Sometimes, if the ban was a mistake or the account was hacked. We check the Account status screen first and tell you honestly if a route is open."),
  ("Will the creator have to do anything?", "Only what the platform itself asks for, such as confirming identity from their own device. We tell you exactly what that is."),
  ("Can you help with the press side?", "No. We focus on the platform track. Your team keeps the communication with fans, brands and media."),
  ("How long does it usually take?", "Usually 7–14 days from the day we start, with a 100% refund if the account isn’t reinstated within 14 days."),
  ("Do you take on accounts that really broke the rules?", "Not for scams, bought accounts or anything needing mass reports. For borderline content strikes we tell you honestly what the odds are.")],
 related=[("white-label-recovery-for-pr-firms", "White label for PR firms"), ("white-label-recovery-for-influencer-talent-agencies", "For talent agencies"), ("white-label-tiktok-account-recovery", "White label TikTok recovery"), ("talent-agencies-false-copyright-impersonation-bans-client-accounts", "False copyright and impersonation bans")])

A(slug="how-do-social-media-agencies-recover-hacked-client-instagram", topic="ig_hacked",
 q="How do social media agencies recover hacked client Instagram accounts?",
 title="How Do Social Media Agencies Recover Hacked Client Instagram Accounts? (2026)",
 desc="A practical playbook for agencies: the first hour after a client’s Instagram is hacked, Instagram’s official recovery routes, what to send a white-label partner, and how to stop it happening again.",
 answer="Start with Instagram’s own route at instagram.com/hacked from a device the client has used before, check the client’s email for Instagram’s security message to undo an email change, and lock down any linked Facebook Page and ad account. If the email and phone were both changed and the official flow loops, a white-label partner like Unbanz can take the case on behind your agency. Never pay anyone who promises a “hack back”.",
 sections=[
  ("first-hour", "The first hour", "<ol><li>Ask the client to search their inbox for an email from security@mail.instagram.com about an email change and tap <strong>revert this change</strong> if it is there.</li><li>Go to instagram.com/hacked on the phone the client usually uses and follow the options (my account was hacked).</li><li>If the account is linked to a Facebook Page or Business portfolio, check who has admin access in Meta Business Suite and remove anyone unknown.</li><li>Pause scheduled posts and ads linked to the account so the attacker can’t spend or post in the brand’s name.</li><li>Warn the client’s audience from another channel (website, Facebook Page, story from a team account) not to send money or codes.</li></ol>"),
  ("evidence", "Evidence to collect", "<ul><li>The original email and phone on the account.</li><li>Screenshots of Instagram’s security emails and any messages from the attacker.</li><li>The date and time access was lost.</li><li>Any earlier photo of the account owner that appears on the account (helps with Instagram’s video selfie check).</li></ul>"),
  ("handoff", "When to hand it to a partner", "<p>Hand it over when the official flow keeps failing: the email and phone were both changed, the security code goes to the attacker, or the account was disabled after the takeover. Send us the @username, the evidence above and the date. We run the recovery through Instagram’s own process and give you unbranded updates. " + TERMS + "</p>"),
  ("prevent", "Prevent the next one", "<ul><li>Turn on two-factor authentication with an authenticator app, not SMS.</li><li>Keep a second admin on linked Pages and portfolios.</li><li>Never log in through links in DMs promising verification or copyright help; that is how most agency clients get phished.</li><li>Keep a one-page incident sheet per client (handles, original email, admins). See our <a href=\"/account-recovery-incident-report-template-for-agencies/\">incident report template</a>.</li></ul>"),
 ],
 links=[IG_HACKED, FB_HACKED, ACC, IG_STATUS],
 faqs=[("Can you hack the account back?", "No, and nobody legitimate will. Recovery goes through Instagram’s own process. Anyone offering a “hack back” is usually a second scam."),
  ("The hacker changed the email and phone. Is it still recoverable?", "Often, through Instagram’s identity check. It depends on the account having photos of the owner or earlier login history we can point to."),
  ("Do you need the client’s login details?", "No. We never ask for passwords or login codes."),
  ("What if the hacker got the account disabled?", "That becomes a combined case: takeover plus disabled account. Send both notices and we’ll tell you which route fits."),
  ("How long does recovery usually take?", "Usually 7–14 days from the day we start, with a 100% refund if the account isn’t reinstated within 14 days."),
  ("Will our client know you were involved?", "No. Updates are unbranded and we never contact your client.")],
 related=[("white-label-hacked-account-recovery", "White label hacked account recovery"), ("white-label-recovery-for-social-media-agencies", "For social media agencies"), ("account-recovery-incident-report-template-for-agencies", "Incident report template"), ("how-does-white-label-instagram-account-recovery-work", "How white label works")])

A(slug="white-label-social-media-unbanning-cost-for-agencies", topic="other",
 q="What does white-label social media unbanning cost for agencies?",
 title="What Does White-Label Social Media Unbanning Cost for Agencies? (2026)",
 desc="Unbanz white-label fees for agencies: $1,200 per case, volume pricing for 5+ cases a month after a test case, bank transfer, refund terms and what you can charge your client.",
 answer="With Unbanz, white-label unbanning is $1,200 per case (one account or handle) on every platform (Instagram, Facebook, TikTok, YouTube, Snapchat, WhatsApp, ad accounts). Agencies that send 5+ cases a month get volume pricing, agreed in writing after a first test case. Payment is upfront by bank transfer, with a 100% refund if the account isn’t reinstated within 14 days, paid the same business day. You set your own price to your client.",
 sections=[
  ("what-you-pay", "What you pay", "<ul><li><strong>White-label rate:</strong> $1,200 per case (one account or handle), any platform.</li><li><strong>Volume pricing:</strong> for agencies with 5+ cases a month, agreed in writing after one test case.</li><li><strong>How:</strong> upfront bank transfer to our US or UK business bank account. No card payments, no crypto, no gift cards.</li><li><strong>Refund:</strong> 100% if the account isn’t reinstated within 14 days, paid the same business day.</li><li><strong>Re-ban cover:</strong> if it is banned again within 6 months, we recover it free or refund 100%.</li></ul>"),
  ("what-you-charge", "What you can charge your client", "<p>That’s your decision. Agencies usually price it as a fixed recovery fee or include it in a retainer’s crisis allowance. Whatever you choose, be straight with the client that the platform decides the outcome and that you work through official routes. See <a href=\"/agency-pricing-models-reselling-recovery/\">pricing models for reselling recovery</a>.</p>"),
  ("not-included", "What is not included", "<ul><li>Passwords or account access: never needed, never requested.</li><li>Ad spend refunds from Meta, which only Meta can decide.</li><li>Fake reports, bought followers or anything against platform rules.</li></ul>"),
  ("red-flags", "Price red flags elsewhere", "<ul><li>“$50 guaranteed unban in 24 hours.”</li><li>Payment in gift cards or crypto, or a “release fee” after the first payment.</li><li>Claims of private contacts inside the platform.</li></ul><p>See <a href=\"/how-to-vet-an-account-recovery-partner-for-your-agency/\">how to vet a recovery partner</a>.</p>"),
 ],
 links=[IG_DISABLED, FB_DISABLED, AQ, TT_BANS],
 faqs=[("Is the $1,200 per account or per platform?", "Per account or handle. Several accounts for one client are priced per account, and partner pricing applies to regular volume."),
  ("When do we get partner pricing?", "After a first test case. Terms are agreed in writing before the next cases start."),
  ("Can we pay by card?", "No. Payment is by bank transfer only, to our US or UK business bank account."),
  ("When is the refund paid?", "The same business day it becomes due: if the account isn’t reinstated within 14 days, you get 100% back."),
  ("Do you charge for reviewing a case?", "No. Asking is free; we tell you if a case is worth taking before anything is paid."),
  ("Do you invoice the agency?", "Yes. We invoice your agency, not your client, and a signed agreement is available before payment.")],
 related=[("white-label-recovery-fixed-fees-for-agencies", "Fixed fees for agencies"), ("agency-pricing-models-reselling-recovery", "Pricing models for reselling"), ("pricing", "Pricing"), ("agencies-bulk-instagram-disablements-one-agreement", "Bulk cases under one agreement")])

A(slug="how-agencies-recover-client-business-manager-or-ad-account", topic="ad",
 q="How can marketing agencies recover a disabled Meta Business Manager or ad account for a client?",
 title="How Can Marketing Agencies Recover a Client’s Disabled Business Manager or Ad Account? (2026)",
 desc="Where the restriction sits, how to request a review in Account Quality, what to fix first, and when to hand a client’s Business Portfolio or ad account to a white-label partner.",
 answer="First find where the restriction sits: the ad account, the Business Portfolio (Business Manager), or the admin’s personal profile. Open Account Quality, read the exact reason and request a review from there, after fixing the cause (payment method, unverified business, policy-breaking ads). If the review fails or the whole portfolio is disabled, a white-label partner like Unbanz can run the case behind your agency. Meta makes the final decision.",
 sections=[
  ("where", "1. Find where the restriction sits", "<ul><li><strong>Ad account disabled:</strong> one account can’t run ads; others in the portfolio may still work.</li><li><strong>Business Portfolio restricted:</strong> every ad account inside is affected; often triggered by an admin profile or an unverified business.</li><li><strong>Admin profile restricted:</strong> the person can’t advertise anywhere. Fix this first or every review will fail.</li></ul>"),
  ("fix", "2. Fix the cause before you appeal", "<ul><li>Payment: failed or disputed charges, a card the client doesn’t recognise, a new card added the same day as a spike in spend.</li><li>Verification: complete business verification with documents that match the legal name and website.</li><li>Ads: remove or edit the rejected ads named in Account Quality.</li><li>Access: remove unknown admins and partners added recently.</li></ul>"),
  ("review", "3. Request the review the right way", "<p>Request it from Account Quality, from an admin with a clean profile, once. Multiple reviews from different admins in a short time can slow things down. Keep screenshots of every reason and response.</p>"),
  ("handoff", "4. When to hand it over", "<p>When the review is rejected, the portfolio is disabled with no review button, or the client’s spend is on hold for more than a few days. Send us the ad account ID or portfolio ID, Account Quality screenshots and the date. We work through Meta’s official process and send unbranded updates. " + TERMS + "</p>"),
 ],
 links=[AQ, ADS_TROUBLE, ADS_REVIEW, BIZ_VERIF, BM_ADMIN],
 faqs=[("Can you recover a Business Portfolio with no admins left?", "Often, through Meta’s admin recovery and verification routes, if the business can prove it owns the portfolio."),
  ("Do you need admin access to the client’s portfolio?", "No. We work from IDs and screenshots; any step that needs an admin is explained so your team can do it."),
  ("Will Meta refund the ad spend lost during the restriction?", "Only Meta decides that. We focus on getting the account or portfolio running again."),
  ("How many ad accounts can you handle for one client?", "As many as needed. Several accounts under one portfolio are usually handled as one coordinated case, priced per account."),
  ("How long does it usually take?", "Usually 7–14 days from the day we start, with a 100% refund if it isn’t reinstated within 14 days."),
  ("Is it safe to keep creating new ad accounts?", "No. New accounts linked to a restricted profile or portfolio are often restricted too.")],
 related=[("agency-ad-account-recovery", "Agency ad account recovery"), ("white-label-business-portfolio-recovery", "White label Business Portfolio recovery"), ("agency-business-portfolio-disabled-all-client-ad-accounts-down", "Portfolio disabled, all client ad accounts down"), ("white-label-recovery-for-ad-agencies", "For ad agencies")])

A(slug="can-reputation-firms-white-label-instagram-username-claims", topic="username",
 q="Can a reputation management firm white-label Instagram username claims?",
 title="Can a Reputation Management Firm White-Label Instagram Username Claims? (2026)",
 desc="When an inactive, squatted or infringing account holds a client’s brand handle: what Instagram allows, the trademark and impersonation routes, and how firms resell username claims under their own brand.",
 answer="Yes. A reputation management firm can offer Instagram username claims to clients under its own brand, with Unbanz doing the claim behind the scenes. Claims work through Instagram’s own policies: trademark reports when an account infringes a registered mark, impersonation reports when it pretends to be the client, and inactive-account routes. The white-label rate is $1,200 per handle, with a 100% refund if the claim fails. Instagram makes the final decision.",
 sections=[
  ("routes", "The routes that exist", "<ul><li><strong>Trademark:</strong> the client owns a registered mark and the handle is used in a way that confuses people. Uses Instagram’s trademark report form.</li><li><strong>Impersonation:</strong> the account pretends to be the client or their business. Uses the impersonation form.</li><li><strong>Inactive accounts:</strong> handles held by long-inactive accounts. There is no public form; outcomes depend on the account and the claim.</li><li><strong>Not a route:</strong> buying a handle from its owner (against Instagram’s terms) or mass-reporting it.</li></ul>"),
  ("send", "What to send", "<ul><li>The handle wanted and the client’s current handle.</li><li>Trademark registration number and country, if any.</li><li>Proof the client uses the name: website, other social accounts, press.</li><li>Screenshots of the account holding the handle.</li></ul>"),
  ("reputation", "Why reputation firms use it", "<p>A squatted or fake handle can rank for the client’s name, collect DMs meant for the brand and run scams. Claiming it removes a risk and gives the client the clean, matching handle. In white label, the client only ever deals with your firm.</p>"),
  ("terms", "Fees and terms", "<p>A white-label rate of $1,200 per handle, including handles held by inactive or banned accounts, with a 100% refund if the claim fails, paid the same business day. Partner pricing for firms with regular claims is agreed in writing after a first test case. Paid upfront by bank transfer, no cards.</p>"),
 ],
 links=[TM_WHAT, TM_FORM, IMP_FORM, IG_STATUS],
 faqs=[("Can you claim any handle we want?", "No. Only where Instagram’s policies give a route: trademark, impersonation or inactivity. We tell you honestly which handles are realistic."),
  ("Does the client need a registered trademark?", "It helps a lot for the trademark route, but impersonation and inactive-handle claims don’t always need one."),
  ("Is buying the handle from the owner allowed?", "No. Instagram’s terms don’t allow buying or selling usernames, and bought handles can be removed."),
  ("Will the client’s name appear in the claim?", "The client is the rights holder, so claims are made in their name or their brand’s name. We never contact them directly; your firm stays the contact."),
  ("How long do username claims take?", "Many finish within one to two weeks, but it depends on the route and on Instagram."),
  ("What if the claim fails?", "100% refund, paid the same business day.")],
 related=[("white-label-username-claim", "White label username claims"), ("white-label-recovery-for-reputation-management-firms", "For reputation management firms"), ("white-label-impersonation-fake-account-removal", "Impersonation and fake account removal"), ("username", "Username claims")])

A(slug="talent-agencies-false-copyright-impersonation-bans-client-accounts", topic="ig_disabled",
 q="How do talent management agencies handle false copyright or impersonation bans on client accounts?",
 title="How Talent Agencies Handle False Copyright or Impersonation Bans on Client Accounts (2026)",
 desc="When a creator is disabled for copyright strikes they didn’t earn or flagged as impersonating themselves: the evidence to gather, the official counter routes, and when to hand it to a white-label partner.",
 answer="Treat it as a documentation job. Collect every copyright or impersonation notice, prove the creator owns the content or is the real person (originals, licences, ID that matches the profile), and use the platform’s own routes: the appeal on the disabled notice, a counter to the copyright report where offered, and Instagram’s impersonation form against the fake account. If the creator’s account is disabled and appeals loop, a white-label partner like Unbanz can run it behind your agency.",
 sections=[
  ("copyright", "False copyright strikes", "<ul><li>Screenshot each removal notice: the reporter’s name, the post and the date.</li><li>Gather proof: original files with metadata, licence agreements, brand contracts allowing the use.</li><li>Use the dispute or appeal option shown on the removal where available, and keep it factual.</li><li>Watch for a pattern of strikes from one reporter: coordinated false reports are a reason to escalate, not to delete content in a panic.</li></ul>"),
  ("impersonation", "When the creator is flagged as the impersonator", "<p>This happens when a fan or fake account reports the real creator first. The fix is identity: an ID that matches the profile name, links from the creator’s other verified channels, and a clean appeal on the disabled notice. Report the actual fake account through Instagram’s impersonation form at the same time.</p>"),
  ("roster", "Protect the roster", "<ul><li>Keep a rights folder per creator: originals, licences, brand contracts.</li><li>Link every official channel from each profile so identity is easy to prove.</li><li>Enable two-factor authentication with an authenticator app on every creator account.</li></ul>"),
  ("handoff", "When to hand it over", "<p>When the account is disabled and the appeal was rejected, or there is no appeal button. Send the handle, all notices and your evidence. " + TERMS + "</p>"),
 ],
 links=[CR_WHAT, CR_FORM, IMP_FORM, IG_DISABLED],
 faqs=[("Can false copyright reports really get an account disabled?", "Yes. Repeated copyright strikes can lead to disabling, even if the reports were wrong. That is why the evidence matters."),
  ("Should the creator delete the reported posts?", "Not automatically. Deleting can remove the evidence you need. Decide per post with the rights folder in hand."),
  ("Can you find out who filed the false reports?", "The notice usually names the reporter. We don’t do investigations, but we use that information in the appeal."),
  ("What if the creator has no ID that matches the profile name?", "Tell us. Stage names are common; other proof such as verified channels and contracts can help."),
  ("How long does it usually take?", "Usually 7–14 days from the day we start, with a 100% refund if the account isn’t reinstated within 14 days."),
  ("Do you contact the creator?", "No. We work only through your agency.")],
 related=[("white-label-recovery-for-influencer-talent-agencies", "For talent agencies"), ("white-label-impersonation-fake-account-removal", "Impersonation and fake account removal"), ("can-pr-and-talent-agencies-outsource-instagram-tiktok-recovery", "Outsourcing Instagram and TikTok recoveries"), ("white-label-instagram-account-recovery", "White label Instagram recovery")])

A(slug="white-label-whatsapp-business-unban-for-agencies", topic="whatsapp",
 q="Is there a white-label WhatsApp Business unban service for agencies?",
 title="Is There a White-Label WhatsApp Business Unban Service for Agencies? (2026)",
 desc="Yes. How agencies hand over banned WhatsApp and WhatsApp Business numbers for clients, what WhatsApp’s review needs, common ban triggers for business numbers, and what it costs.",
 answer="Yes. Unbanz takes banned WhatsApp and WhatsApp Business numbers from agencies on a white-label basis: you send the number, a screenshot of the ban message and how the number was used, and we prepare and follow up the review through WhatsApp’s own process while you stay the client’s contact. Only WhatsApp can lift a ban. The white-label rate is $1,200 per number, with a 100% refund if it isn’t reinstated within 14 days.",
 sections=[
  ("triggers", "Why business numbers get banned", "<ul><li>Bulk messages to people who didn’t opt in, or many users blocking and reporting the number.</li><li>Unofficial apps or “WhatsApp mods” and some automation tools.</li><li>Sending content or selling items that break WhatsApp’s Business and Commerce policies.</li><li>A brand-new number sending a lot of messages straight away.</li></ul>"),
  ("first", "What the client should do first", "<ol><li>Open WhatsApp and use the in-app review request on the ban screen, once.</li><li>Stop any automation or unofficial app on the number.</li><li>Don’t reinstall repeatedly or move the SIM to another phone to get around it.</li></ol>"),
  ("send", "What to send us", "<ul><li>The full number with country code and whether it is WhatsApp or WhatsApp Business (app or API).</li><li>A screenshot of the ban message and the date.</li><li>How the number is used: support, sales, broadcast lists, tools connected.</li></ul>"),
  ("terms", "Fees and terms", "<p>" + TERMS + "</p>"),
 ],
 links=[WA_BAN, WA_POLICY],
 faqs=[("Can you unban a WhatsApp Business API number?", "API numbers are managed through the business’s provider and Meta. Tell us the provider; we explain which route applies."),
  ("Will the chats be lost?", "If the ban is lifted, chats backed up to the phone or cloud can usually be restored. Without a backup, they may be gone."),
  ("Can the client just use a new number?", "They can, but repeating the same behaviour gets new numbers banned fast. Fix the cause first."),
  ("Do you need access to the phone?", "No. The client requests the review on their own phone; we prepare the case and follow-up."),
  ("How long does it usually take?", "Usually 7–14 days from the day we start, with a 100% refund if the number isn’t reinstated within 14 days."),
  ("Is this the same as the WhatsApp contact on unbanz.com?", "No. This page is about banned WhatsApp numbers we help agencies recover for clients.")],
 related=[("white-label-whatsapp-number-unban", "White label WhatsApp number help"), ("whatsapp-banned-number", "Banned WhatsApp number"), ("white-label-agency", "White label for agencies"), ("white-label-social-media-unbanning-cost-for-agencies", "What it costs")])

A(slug="how-to-vet-an-account-recovery-partner-for-your-agency", topic="other",
 q="How do you vet a legitimate account recovery partner for your agency?",
 title="How to Vet a Legitimate Account Recovery Partner for Your Agency (Contracts, Invoicing, Refunds) (2026)",
 desc="A checklist for agencies: written agreement, a registered company behind the bank account, refund terms in writing, no password requests, official routes only, and the red flags that mean walk away.",
 answer="A legitimate partner puts terms in writing before you pay, invoices from a registered company with a business bank account, offers a clear refund if the case fails, never asks for passwords or login codes, works only through the platform’s official routes, and never promises a guaranteed result or “contacts inside Meta”. Start with one test case. Unbanz meets each of these: signed agreement, upfront bank transfer to a US or UK business bank account, 100% refund within 14 days.",
 sections=[
  ("checklist", "The checklist", "<ol><li><strong>Written agreement</strong> with the scope, fee, timing and refund, signed by a named authorised signatory.</li><li><strong>A registered company</strong> receiving the money, with a business bank account in its name; not a personal account, not crypto, not gift cards.</li><li><strong>Refund terms in writing:</strong> when a refund is due and how fast it is paid.</li><li><strong>No credentials:</strong> no passwords, login codes or remote access to client devices.</li><li><strong>Official routes only:</strong> appeals and forms the platform itself provides.</li><li><strong>Honest triage:</strong> some cases get a “no”.</li><li><strong>A test case</strong> before volume or partner pricing.</li></ol>"),
  ("red-flags", "Red flags", "<ul><li>“Guaranteed unban” or results in hours.</li><li>Claims of private contacts or staff inside Meta, TikTok or WhatsApp.</li><li>A second “release” or “tool” fee after the first payment.</li><li>Pressure to pay before any review of the case.</li><li>Requests for the client’s password or a code sent to their phone.</li></ul>"),
  ("unbanz", "How Unbanz answers the checklist", "<p>" + TERMS + " We never need passwords, we use the platforms’ official processes, and the platform makes the final decision. Unbanz is independent and not affiliated with Meta, TikTok, WhatsApp or Google. See <a href=\"/is-unbanz-legit/\">is Unbanz legit</a> and <a href=\"/agency-account-recovery-red-flags/\">agency red flags</a>.</p>"),
 ],
 links=[IG_HACKED, FB_HACKED, AQ],
 faqs=[("Should we pay a partner before they review the case?", "No. A legitimate partner reviews it first and tells you if it is worth paying for."),
  ("Is upfront payment normal?", "Yes, when it comes with a written agreement and a clear refund. Upfront plus no refund terms is the problem."),
  ("Why does the bank account matter?", "Payment to a registered company’s business account gives you an invoice trail and someone accountable. Personal accounts and crypto give you neither."),
  ("Can a partner promise a result?", "No. The platform makes the final decision. Promises of a guaranteed result are a red flag."),
  ("Do you sign NDAs with agencies?", "A signed agreement covering confidentiality is available before payment."),
  ("How should we test a new partner?", "Send one real, typical case. Judge the triage, the updates and how the refund terms are handled.")],
 related=[("agency-account-recovery-red-flags", "Agency red flags"), ("is-unbanz-legit", "Is Unbanz legit"), ("agency-onboarding-checklist-white-label-partner", "Onboarding checklist"), ("white-label-social-media-unbanning-cost-for-agencies", "What it costs")])

A(slug="agencies-bulk-instagram-disablements-one-agreement", topic="ig_disabled",
 q="How do agencies handle multi-account or bulk Instagram disablements under one agreement?",
 title="How Agencies Handle Bulk Instagram Disablements Under One Agreement (2026)",
 desc="When several client accounts go down at once: triage, a single intake sheet, one agreement with per-account terms, partner pricing and how updates are reported.",
 answer="Triage first, then put everything under one written agreement. List every affected account with its notice and date on one intake sheet, check for a shared cause (same admin, same device, same Business Portfolio, same tool), and send the batch. Unbanz prices per account, applies partner pricing for volume after a test case, and reports progress per account with unbranded updates. Each account carries its own 14-day refund.",
 sections=[
  ("triage", "1. Triage the batch", "<ul><li>Group accounts by cause: a shared admin profile, a scheduling or automation tool, a portfolio restriction, or a wave of reports.</li><li>Stop the shared cause first (remove the tool, secure the admin) or new disablements will follow.</li><li>Prioritise by client impact: revenue accounts and those near the end of their appeal window first.</li></ul>"),
  ("sheet", "2. One intake sheet", "<p>One row per account: handle, client reference (no names needed), notice screenshot, date, appeal already filed (yes/no), linked Pages or ad accounts. It keeps both teams on the same list. See the <a href=\"/agency-intake-form-checklist-account-recovery/\">agency intake checklist</a>.</p>"),
  ("agreement", "3. One agreement, per-account terms", "<ul><li>$1,200 per account (case); partner pricing for the batch agreed in writing after a first test case.</li><li>Upfront by bank transfer to our US or UK business bank account.</li><li>Each account has its own result: 100% refund for any account not reinstated within 14 days, paid the same business day.</li><li>6-month re-ban cover per account.</li></ul>"),
  ("reporting", "4. Reporting", "<p>You get a per-account status list and short, unbranded notes you can forward to each client. See <a href=\"/white-label-private-label-case-reports/\">private-label case reports</a> and <a href=\"/white-label-bulk-recovery-cases-for-agencies/\">how batches work</a>.</p>"),
 ],
 links=[IG_DISABLED, IG_STATUS, AQ],
 faqs=[("Is there a minimum batch size?", "No. Partner pricing starts after a first test case; batches can be any size."),
  ("Are refunds per account or for the whole batch?", "Per account. Any account not reinstated within 14 days is refunded in full, the same business day."),
  ("Why did several of our client accounts go down at once?", "Usually a shared factor: one admin profile, one device or IP, a third-party tool, or a portfolio restriction. Finding it matters more than appealing fast."),
  ("Do you need all client names?", "No. A handle and your client reference are enough."),
  ("How long does a batch take?", "Usually 7–14 days per account from the day we start; accounts run in parallel."),
  ("Can new accounts be added to the same agreement later?", "Yes. New cases are added under the same terms.")],
 related=[("white-label-bulk-recovery-cases-for-agencies", "Bulk cases for agencies"), ("white-label-private-label-case-reports", "Private-label case reports"), ("agency-intake-form-checklist-account-recovery", "Intake checklist"), ("how-to-vet-an-account-recovery-partner-for-your-agency", "Vetting a partner")])
