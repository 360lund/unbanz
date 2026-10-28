# -*- coding: utf-8 -*-
from lib import *

RS = ['white-label-account-recovery', 'how-white-label-account-recovery-works']

mk('become-a-white-label-recovery-partner', 'Become a partner', 'start',
 'Become a White Label Account Recovery Partner',
 'How an agency or freelancer starts working with Unbanz as a white label partner: who it suits, what to send first and how terms are agreed.',
 'Become a white label account recovery partner.',
 'If your clients keep asking about locked accounts, you can offer recovery without building the skill. This is how to start.',
 'To become a white label recovery partner, message Unbanz on WhatsApp +1 934 201 2490 or email team@unbanz.com, say what your agency or freelance practice does and agree the terms in writing. After that you send requests with the intake details, and Unbanz works behind the scenes. Your clients never hear from us.',
 [('Who it suits', 'Agencies and freelancers whose clients lose access to accounts.'),
  ('Simple start', 'One message, written terms, then your first request.'),
  ('Your brand stays in front', 'Unbanz never contacts your clients.')],
 [('who', 'Who this is for',
   UL(['Social media, ad, web and local marketing agencies.', 'Influencer, talent, UGC and PR firms.', 'Branding studios, freelancers and community managers.']) +
   P('Audience pages: [[white-label-recovery-for-social-media-agencies|social media agencies]], [[white-label-recovery-for-ad-agencies|ad agencies]] and [[white-label-recovery-for-community-managers-freelancers|freelancers]].')),
  ('steps', 'How to start',
   OL(['Send a short message saying what you do and which platforms your clients use.', 'Agree terms in writing before any request.', 'Complete the [[agency-onboarding-checklist-white-label-partner|onboarding checklist]].', 'Send your first request with the [[agency-intake-form-checklist-account-recovery|intake details]].'])),
  ('expect', 'What to expect',
   UL(['You are the only contact for your client.', 'Unbanz reports to you in plain words.', 'The platform makes the final decision, and no result is promised.', 'No passwords or login codes are ever requested.'])),
  ('not', 'What this is not',
   UL(['It is not a referral scheme where your client deals with us.', 'It is not an account supply service.', 'It is not a way to get around a platform’s rules.']) +
   P('The difference between models is explained in [[white-label-vs-referral-vs-in-house-recovery|white label vs referral vs in-house]].')),
  ('contact', 'Contact',
   P('WhatsApp +1 934 201 2490 or email team@unbanz.com. Mention your agency type and the platforms you work with.'))],
 [('How do I become a partner?', 'Message Unbanz by WhatsApp or email, say what you do and agree terms in writing.'),
  ('Is there a minimum number of clients?', 'There is no set size. Say what you do and we will tell you whether it fits.'),
  ('Do my clients hear from Unbanz?', 'No.'),
  ('Can freelancers join?', 'Yes. Freelancers and community managers are welcome.'),
  ('What if I only need help once?', 'Send the details of that one request. You can decide later whether to set up a longer arrangement.')],
 RS + ['agency-onboarding-checklist-white-label-partner', 'how-to-choose-a-white-label-recovery-partner', 'agency-pricing-models-reselling-recovery'],
 'How to start as a white label partner: who it suits and the first steps.')

mk('how-to-choose-a-white-label-recovery-partner', 'How to choose a partner', 'start',
 'How to Choose a White Label Recovery Partner',
 'A buyer’s checklist for agencies choosing a white label account recovery partner: method, honesty, confidentiality, terms and fit.',
 'How to choose a white label recovery partner.',
 'Handing client accounts to a partner is a trust decision. This checklist helps you test one before you commit.',
 'Choose a white label recovery partner by testing five things: the official routes it uses, how honest it is about outcomes, how it protects your clients’ details, how clear its terms are and whether it stays behind your brand. Avoid anyone who promises results, asks for passwords or claims inside contacts.',
 [('Method', 'Official routes, explained plainly.'),
  ('Honesty', 'No promised results.'),
  ('Discretion', 'Stays behind your brand.')],
 [('five', 'The five tests',
   TABLE(['Test', 'A good answer', 'A bad answer'],
         [['Method', 'Describes the platform’s official routes', 'Vague talk of secret methods'],
          ['Honesty', 'Says the platform decides', 'Promises results'],
          ['Data', 'Asks for the minimum, never passwords', 'Asks for logins or codes'],
          ['Terms', 'Clear and in writing', 'Vague or verbal only'],
          ['Brand', 'Works behind yours, never contacts your clients', 'Wants to talk to your client']])),
  ('questions', 'Questions to ask',
   OL(['What do you do when the platform says no?', 'What do you need from my client, and what never?', 'Do you ever contact my client?', 'What happens with the details I send?', 'What are your terms, and can I have them in writing?'])),
  ('test', 'A small test before you commit',
   P('Start with a single request, ideally a straightforward one, and judge how clear the communication is. Reply times matter less than clarity. A provider who tells you plainly when a request has no honest route is worth more than one who says yes to everything.')),
  ('compare', 'How the models compare',
   P('If you are also weighing referral or in-house options, read [[white-label-vs-referral-vs-in-house-recovery|white label vs referral vs in-house]] and [[white-label-vs-freelancer-vs-referral-recovery|white label vs freelancer vs referral]].')),
  ('flags', 'Red flags',
   P('See the full list on [[agency-account-recovery-red-flags|red flags for agencies]].'))],
 [('What matters most when choosing a partner?', 'Honesty about outcomes and respect for your client’s details. Everything else is secondary.'),
  ('Should the partner ever contact my client?', 'In a white label arrangement, no.'),
  ('How should I test a new partner?', 'Start with one straightforward request and judge the clarity of communication.'),
  ('Is a cheaper partner better?', 'Price is one input. Clear terms and honest answers matter more.'),
  ('Can I ask for references?', 'You can ask. Be wary of anyone who offers ratings or reviews you cannot verify.')],
 RS + ['agency-account-recovery-red-flags', 'become-a-white-label-recovery-partner', 'white-label-vs-in-house-account-recovery'],
 'A five-test checklist for choosing a white label recovery partner.')

mk('white-label-agency-faq', 'Agency FAQ', 'start',
 'White Label Account Recovery FAQ for Agencies',
 'Short answers to the questions agencies ask about white label account recovery: clients, confidentiality, pricing, outcomes and starting.',
 'White label account recovery FAQ.',
 'Everything agencies usually ask before they start, in one place, with links to the full pages.',
 'White label account recovery means an agency offers recovery under its own brand while Unbanz works behind the scenes. Clients do not know Unbanz, and the agency keeps the relationship. The platform makes the final decision, no outcome is promised, and the sections below answer the common questions.',
 [('Clients', 'Do they know you? No.'),
  ('Outcomes', 'Who decides? The platform.'),
  ('Start', 'Message us and agree terms.')],
 [('basics', 'The basics',
   DEFN('White label account recovery', 'A service where an agency presents account recovery as its own while a partner does the platform work behind the scenes.') +
   P('The long version is on [[white-label-account-recovery|the white label account recovery page]], and the process is in [[how-white-label-account-recovery-works|how it works]].')),
  ('clients', 'About your clients',
   P('Your clients do not know Unbanz. Unbanz works for your agency and does not contact them. The platform sends its own emails and identity checks to the account owner, and the client should complete those. See [[what-your-client-sees-white-label-recovery|what your client sees]].')),
  ('outcomes', 'About outcomes',
   P('The platform decides every request. Unbanz cannot promise a result, a date or a restored account. Be honest with clients about that. See [[how-to-tell-client-account-disabled-template|how to tell a client]].')),
  ('money', 'About price and terms',
   P('Unbanz agrees its terms with you in writing before work starts. Your own client price is your decision. See [[agency-pricing-models-reselling-recovery|pricing models]] and [[how-to-price-account-recovery-for-agencies|how to price]]. The refund policy covers Instagram username claims: a 100% refund if a claim fails.')),
  ('safety', 'About safety',
   P('Unbanz never asks for passwords or codes, uses only official routes, does not buy or sell accounts and does not use fake or mass reports. See [[agency-account-recovery-red-flags|red flags]].')),
  ('start', 'Platforms and starting',
   P('Covered: Instagram, Facebook, Meta ad accounts and business portfolios, Threads and Snapchat. The client pays your agency, not Unbanz. Unbanz agrees terms with you. Message WhatsApp +1 934 201 2490 or email team@unbanz.com. See [[become-a-white-label-recovery-partner|become a partner]].'))],
 [('What is white label account recovery?', 'A service where an agency offers account recovery under its own brand while a partner does the platform work behind the scenes.'),
  ('Do my clients know Unbanz?', 'No. Unbanz works only for your agency and never contacts your clients.'),
  ('Can you promise the account will come back?', 'No. The platform decides every request.'),
  ('Is there a refund policy?', 'Yes, for Instagram username claims: a 100% refund if a claim fails.'),
  ('How do I start?', 'Message WhatsApp +1 934 201 2490 or email team@unbanz.com, say what you do and agree terms in writing.')
  ],
 RS + ['white-label-agency-glossary', 'become-a-white-label-recovery-partner', 'agency-account-recovery-red-flags'],
 'Short answers to common agency questions about white label recovery.')

mk('white-label-agency-glossary', 'Agency glossary', 'start',
 'White Label Account Recovery Glossary',
 'Plain definitions of the terms agencies meet in account recovery: white label, referral, appeal, business portfolio, account quality and more.',
 'White label account recovery glossary.',
 'Terms used across the agency pages, in plain words, so your team and your clients mean the same thing.',
 'This glossary defines the terms used in white label account recovery: white label, referral, appeal, disabled, suspended, restricted, business portfolio, Account Quality, impersonation and intake. Definitions are short and plain, and each links to the page that explains it in more detail.',
 [('Plain words', 'Short definitions, no jargon.'),
  ('Linked', 'Each term points to a full page.'),
  ('Updated', 'Last updated October 2026.')],
 [('a', 'Account and platform terms',
   DEFN('Disabled', 'The platform has switched the account off. The owner sees a notice and may have an option to appeal.') +
   DEFN('Suspended', 'The account is paused, often for a set time or until a check is passed.') +
   DEFN('Restricted', 'The account works, but some actions are limited.') +
   DEFN('Appeal', 'A request asking the platform to review its own decision. See [[/instagram-account-disabled-appeal/|Instagram account disabled appeal]].') +
   DEFN('Account Quality', 'A Meta screen that shows the state of advertising and business assets, including restrictions.') +
   DEFN('Business portfolio', 'The Meta tool, formerly Business Manager, that holds Pages, ad accounts and access for a business. See [[white-label-business-portfolio-recovery|business portfolio recovery]].')),
  ('b', 'Model terms',
   DEFN('White label', 'The agency presents the service as its own. The partner works behind the scenes and does not contact the client. See [[white-label-account-recovery|white label account recovery]].') +
   DEFN('Referral', 'The agency passes the client to another company, which deals with the client directly.') +
   DEFN('In-house', 'The agency does the recovery work with its own team.') +
   DEFN('Partner', 'The company the agency works with behind the scenes. Here, Unbanz.') +
   P('The three models are compared in [[white-label-vs-referral-vs-in-house-recovery|white label vs referral vs in-house]].')),
  ('c', 'Process terms',
   DEFN('Intake', 'Collecting the details needed to start a request. See [[agency-intake-form-checklist-account-recovery|the intake checklist]].') +
   DEFN('Handoff', 'Passing the details from the agency to the partner.') +
   DEFN('SOP', 'Standard operating procedure: the written steps a team follows each time. See [[account-recovery-sop-template-for-agencies|the SOP template]].') +
   DEFN('Go-ahead', 'The client’s permission for the agency to act on the account.')),
  ('d', 'Problem terms',
   DEFN('Impersonation', 'An account pretending to be someone else. See [[white-label-impersonation-fake-account-removal|impersonation removal]].') +
   DEFN('Hacked account', 'An account where someone else changed the login details or took control. See [[white-label-hacked-account-recovery|hacked account recovery]].') +
   DEFN('Username claim', 'A request for a handle held by another account, using an official route such as a trademark report. See [[white-label-username-claim|username claim]].')),
  ('e', 'More help',
   P('Questions that are not here may be in [[white-label-agency-faq|the agency FAQ]].'))],
 [('What does white label mean in account recovery?', 'The agency offers the service as its own, while the partner works behind the scenes and does not contact the client.'),
  ('What is the difference between disabled and suspended?', 'Disabled means the account is switched off. Suspended usually means paused, often for a time or until a check is passed.'),
  ('What is a business portfolio?', 'The Meta tool, formerly Business Manager, holding Pages, ad accounts and access.'),
  ('What is intake?', 'Collecting the details needed to start a recovery request.'),
  ('What is a go-ahead?', 'The client’s permission for the agency to act on the account.')],
 RS + ['white-label-agency-faq', 'agency-intake-form-checklist-account-recovery', 'white-label-business-portfolio-recovery'],
 'Plain definitions of the terms used in white label recovery.')
