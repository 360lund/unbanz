# -*- coding: utf-8 -*-
from lib import *
G = 'country'
DSA = ('In the EU, the Digital Services Act may apply to decisions like this. Meta can give you a statement of reasons, and you may have access to an out-of-court dispute body as well as the normal review. Keep every message Meta sends you.')

def country(slug, name, short, title, desc, hero, answer, cards, local_h, local, regulated, extra_h, extra, faq, who, eu=False, send=(), area=None):
    body = [S(local_h, ul(local)),
            S('Regulated advertising in %s' % short, regulated),
            S('First steps, in order', ol([
                'Open Account Quality and screenshot the notice and the date.',
                'Check the people on the portfolio and remove any admin you do not know. Turn on two-factor for the rest.',
                'Clear any unpaid balance and make sure the payment method is yours and current.',
                'Check the business name, address and website match your %s registration.' % short,
                'Request the review once, with a short note on what you sell and what you changed.'])),
            S(extra_h, extra)]
    if eu: body.append(S('Your rights in the EU', DSA))
    body.append(S('How Unbanz helps', 'We help %s businesses get the documents in line and prepare the appeal for Meta’s official review. You can read about the notice types on our page on ' % short + A('/meta-ad-account-restricted-vs-disabled/', 'restricted versus disabled') + ' and the main service page for ' + A('/facebook-ad-account-disabled/', 'disabled ad accounts') + '. Meta makes the final decision.'))
    page(slug, G, title, desc, 'Ad account disabled or restricted in %s?' % name, 'Ad account help in %s' % name, hero, answer, cards, body, faq, who,
         send_extra=list(send), area=area or [{'@type': 'Country', 'name': name}], audience='Advertisers and businesses in %s' % name)

country('meta-ad-account-disabled-ireland', 'Ireland', 'Irish', 'Meta Ad Account Disabled in Ireland: Appeal Help',
 'Irish business with a disabled or restricted Meta ad account? What to check for Ireland, from CRO details to VAT, and how to request a review.',
 'Irish advertisers contract with Meta’s European business, and several checks depend on your business details. This page is for Irish companies and sole traders with a restricted ad account.',
 'Irish advertisers with a disabled or restricted ad account should check the notice in Account Quality, make the business details match the CRO entry or sole trader registration, clear any balance and request one review. Unbanz can prepare the appeal with the Irish documents Meta may ask for.',
 [('Match the registers', 'Use the exact name in the Companies Registration Office or your sole trader registration.'), ('Add VAT', 'Irish VAT numbers should be added to billing if you are registered.'), ('Keep EUR consistent', 'Changing currency means a new ad account and can look like a workaround.')],
 'Checks specific to Ireland',
 ['Use the company name exactly as shown by the Companies Registration Office, including Limited, Ltd or DAC.', 'Sole traders can show a Revenue registration or a bank statement in the trading name.', 'If you are VAT-registered, add the Irish VAT number in billing.', 'Keep the ad account currency in euro if you invoice in Ireland.', 'Make sure the website shows the registered address and contact details.'],
 'Financial services, health, alcohol, gambling and housing ads have extra rules in Ireland. If you are in one of these areas, check your ads and pages against both Meta’s policies and the local rules before you appeal.',
 'If you serve customers in Ireland and Northern Ireland',
 'Many Irish businesses advertise to both sides of the border. Keep one business identity and one billing setup for both, rather than separate ad accounts with different names. Different entities for the same business are a common reason for linked-account notices.',
 [('Does Meta handle Irish advertisers differently?', 'Irish advertisers follow the same policies. Local business details and EU rules can affect what Meta asks for.'), ('What documents do I need?', 'Usually a CRO extract or sole trader registration, a utility or bank statement and the website.'), ('Can Unbanz help Northern Ireland businesses too?', 'Yes. See our UK page for UK-specific checks.'), ('Is the appeal different for an Irish company?', 'The process is the same. The documents are local.')],
 ['Irish limited companies and sole traders.', 'Irish agencies managing local clients.', 'Advertisers selling across the EU from Ireland.'], eu=True)

country('meta-ad-account-disabled-new-zealand', 'New Zealand', 'New Zealand', 'Meta Ad Account Disabled in New Zealand: Appeal Help',
 'New Zealand business with a disabled or restricted Meta ad account? NZBN, GST and billing checks, and how to request a review.',
 'New Zealand advertisers often run lean setups with one owner and one card. This page is for NZ businesses whose Meta ad account was disabled or restricted.',
 'A New Zealand business with a restricted ad account should open Account Quality, check that the name matches the Companies Office entry and NZBN, clear any balance, and request one review. Unbanz can prepare the appeal and help with the documents Meta may ask for.',
 [('Use your NZBN', 'The New Zealand Business Number and Companies Office name should match what you entered.'), ('Check GST', 'Add your GST number in billing if you are registered.'), ('Keep NZD', 'Currency changes require a new ad account.')],
 'Checks specific to New Zealand',
 ['Use the exact registered name from the Companies Office and your NZBN if you have one.', 'Sole traders can use a bank statement or IRD document in the trading name.', 'Add your GST number in billing if you are registered for GST.', 'Keep the ad account in New Zealand dollars if you trade in NZ.', 'Check that the website shows an NZ contact route and clear returns terms.'],
 'Finance, health, alcohol, gambling and housing ads have extra rules in New Zealand. If you work in one, check your ads and pages against both Meta’s policies and local rules before you appeal.',
 'Small teams and shared logins',
 'Many New Zealand teams share one login between the owner and a contractor. Meta flags shared logins and logins from different places. Give each person a profile of their own on the portfolio.',
 [('Where do I find my NZBN?', 'On the New Zealand Business Number register. It is free to look up.'), ('Do NZ advertisers pay GST on Meta ads?', 'It depends on your registration and setup. Check your billing page and your accountant.'), ('Can Unbanz help overseas-based NZ businesses?', 'Yes, as long as the business details match.'), ('Is the time zone relevant?', 'Not for the appeal, but keep the ad account time zone aligned with your business.')],
 ['New Zealand companies and sole traders.', 'NZ agencies and freelancers.', 'Exporters selling to Australia from NZ.'])

country('meta-ad-account-disabled-germany', 'Germany', 'German', 'Meta Ad Account Disabled in Germany: Appeal Help',
 'German business with a disabled or restricted Meta ad account? Impressum, Handelsregister and VAT checks, and how to request a review.',
 'German sites must show a legal notice, and Meta’s checks often start with the site. This page is for German businesses whose Meta ad account was disabled or restricted.',
 'A German business with a restricted ad account should read the notice in Account Quality, check the Impressum and registration details match, clear any balance and request one review. Unbanz can prepare the appeal and the German documents Meta may ask for. Meta decides.',
 [('Check the Impressum', 'A complete legal notice on your site shows that a real business stands behind it.'), ('Match the register', 'Handelsregister entry or Gewerbeanmeldung should match the name in Meta.'), ('Check USt-IdNr', 'Add your VAT ID in billing if you are registered.')],
 'Checks specific to Germany',
 ['Make sure the Impressum shows the full legal name, address, contact details and register number.', 'Use the name from the Handelsregister, or the Gewerbeanmeldung for sole traders.', 'Add your USt-IdNr in billing if you are VAT registered.', 'Keep the ad account in euro if you invoice in Germany.', 'Check that the website has a Datenschutzerklärung and cookie consent that works.'],
 'Finance, health, alcohol, gambling and housing ads have extra rules in Germany, and advertising law is strict. If you work in a regulated area, check your ads and pages against Meta’s policies and local rules before you appeal.',
 'German and English documents',
 'Meta can ask for documents in English or accept German originals depending on the request. We can help you present them clearly with a short English summary.',
 [('Is the Impressum really important for Meta?', 'It is a legal requirement in Germany and also a clear signal of a real business on the landing page.'), ('Which documents does Meta accept?', 'Usually a Handelsregister extract, a tax document or a utility bill in the business name.'), ('Can I appeal in German?', 'You can, but Meta may reply in English. We can help you present the documents clearly.'), ('What about the Digital Services Act?', 'It may apply to decisions on your account. Keep all messages from Meta.')],
 ['German companies and Einzelunternehmer.', 'Agencies serving German-speaking clients.', 'E-commerce stores selling in the DACH region.'], eu=True)

country('meta-ad-account-disabled-netherlands', 'the Netherlands', 'Dutch', 'Meta Ad Account Disabled in the Netherlands: Help',
 'Dutch business with a disabled or restricted Meta ad account? KVK, BTW and billing checks, and how to request a review.',
 'Dutch advertisers usually have a clear business register entry, which helps an appeal when the details match. This page is for businesses in the Netherlands with a restricted Meta ad account.',
 'A Dutch business with a restricted ad account should check the notice in Account Quality, make sure the details match the KVK extract, clear any balance and request one review. Unbanz can prepare the appeal and the documents Meta may request. Meta makes the final decision.',
 [('Use the KVK extract', 'The name and address on your Kamer van Koophandel entry should match Meta.'), ('Add the BTW number', 'Enter your VAT number in billing if you are registered.'), ('Check the site', 'A clear contact page and returns policy help with ad review.')],
 'Checks specific to the Netherlands',
 ['Use the trade name and legal name from the KVK extract.', 'Sole traders (eenmanszaak) can use the KVK extract and a bank statement in the business name.', 'Add your BTW-id in billing if you are VAT registered.', 'Keep the ad account in euro if you invoice in the Netherlands.', 'Make sure the website shows your KVK number and contact details.'],
 'Finance, health, alcohol, gambling and housing ads have extra rules in the Netherlands. If you work in a regulated area, check your ads and pages against Meta’s policies and local rules before you appeal.',
 'Dutch advertisers selling across borders',
 'Many Dutch shops sell into Belgium and Germany. Make sure prices, shipping and returns on the landing page match the country the ad targets, since mismatches cause rejections. Our Dutch pages are at ' + A('/nl/', 'unbanz.com/nl/') + '.',
 [('Where do I find my KVK number?', 'On your KVK extract or the KVK business register.'), ('Does Meta accept Dutch documents?', 'Often yes. We can add a short English summary.'), ('Is there information in Dutch?', 'Yes. Our Dutch pages are at unbanz.com/nl/.'), ('What does the DSA mean for me?', 'It may give you extra rights to a statement of reasons and dispute options.')],
 ['Dutch companies and eenmanszaken.', 'Webshops selling in Benelux.', 'Agencies serving Dutch clients.'], eu=True)

country('meta-ad-account-disabled-singapore', 'Singapore', 'Singapore', 'Meta Ad Account Disabled in Singapore: Appeal Help',
 'Singapore business with a disabled or restricted Meta ad account? UEN, ACRA and GST checks, and how to request a review.',
 'Singapore advertisers often run regional campaigns from a local entity. This page is for Singapore businesses whose Meta ad account was disabled or restricted.',
 'A Singapore business with a restricted ad account should check the Account Quality notice, make sure the details match the ACRA record and UEN, clear any balance and request one review. Unbanz can prepare the appeal and the supporting documents. Meta makes the final decision.',
 [('Use the ACRA name', 'The legal name and UEN should match what you entered in Meta.'), ('Check GST', 'Add your GST number in billing if you are registered.'), ('Be clear on markets', 'If you run ads in other countries, say so in the appeal.')],
 'Checks specific to Singapore',
 ['Use the entity name and UEN from ACRA.', 'Sole proprietors can use their business registration and a bank statement.', 'Add your GST number in billing if you are GST registered.', 'Keep currency consistent with how you invoice.', 'Check that your website lists a Singapore address or a clear way to reach you.'],
 'Financial services, health products, alcohol and gambling ads are tightly regulated in Singapore. If you are in one of these areas, check your ads and pages against Meta’s policies and local rules before you appeal.',
 'Regional campaigns from a Singapore entity',
 'Many Singapore companies run ads for customers in other Asian countries from one ad account. Meta may see logins from several places and different billing countries. Keep the setup consistent, give each team member a profile of their own, and explain the regional model in the appeal.',
 [('Do I need a UEN to appeal?', 'It helps to show a registered business, but it is not the only proof.'), ('Can I run ads in other countries from Singapore?', 'Yes, but the policies and local rules of those markets still apply.'), ('Does the ad account currency matter?', 'Keep it consistent with how you pay.'), ('Can Unbanz work in English only?', 'Yes. We work in English.')],
 ['Singapore companies and sole proprietors.', 'Agencies running regional ads.', 'E-commerce brands selling across Southeast Asia.'])

country('meta-ad-account-disabled-uae', 'the United Arab Emirates', 'UAE', 'Meta Ad Account Disabled in the UAE: Appeal Help',
 'UAE business with a disabled or restricted Meta ad account? Trade licence, TRN and billing checks, and how to request a review.',
 'UAE advertisers often operate through free zone or mainland licences, and the licence details matter for appeals. This page is for UAE businesses with a restricted Meta ad account.',
 'A business in the UAE with a restricted ad account should open Account Quality, check that the details match the trade licence, add the TRN if registered, clear any balance and request one review. Unbanz can prepare the appeal with the licence and supporting documents. Meta decides.',
 [('Use the trade licence', 'The business name and address should match the licence from your free zone or the DED.'), ('Add the TRN', 'The Tax Registration Number goes in billing if you are VAT registered.'), ('Check local rules', 'Some categories are restricted in the UAE regardless of Meta’s policy.')],
 'Checks specific to the United Arab Emirates',
 ['Use the legal name and licence number from your trade licence or free zone licence.', 'Add your TRN in billing if you are registered for VAT.', 'Keep the ad account currency consistent with how you invoice, for example AED.', 'Make sure the website shows a UAE address or a clear contact route.', 'Make sure signatories and admins match the business.'],
 'Health, finance, real estate, alcohol and gambling ads are regulated in the UAE and some categories are not allowed. Check your ads and pages against Meta’s policies and local rules before you appeal.',
 'Free zones, agencies and regional work',
 'Many UAE companies advertise across the Gulf from a free zone entity. Meta may see billing in one country and customers in another. Explain the structure in the appeal and keep each team member on a profile of their own.',
 [('Is a trade licence enough proof?', 'It is strong proof for the entity. We can help you present it with a short summary.'), ('Does Meta accept free zone licences?', 'Usually yes. Make sure the name matches what you entered.'), ('Can I run ads across the Gulf?', 'Yes, with attention to local rules in each market.'), ('Do you work in Arabic?', 'We work in English.')],
 ['UAE companies on mainland and free zone licences.', 'Agencies serving Gulf clients.', 'Real estate and e-commerce brands in Dubai and Abu Dhabi.'])

country('meta-ad-account-disabled-sweden', 'Sweden', 'Swedish', 'Meta Ad Account Disabled in Sweden: Appeal Help',
 'Swedish business with a disabled or restricted Meta ad account? Organisationsnummer, moms and billing checks, and how to request a review.',
 'Swedish businesses usually have a clear organisation number, which helps an appeal when the details match. This page is for advertisers in Sweden with a restricted Meta ad account.',
 'A Swedish business with a restricted ad account should check the Account Quality notice, make sure the details match the Bolagsverket record and organisation number, clear any balance and request one review. Unbanz can prepare the appeal and documents. Meta makes the final decision.',
 [('Use the org number', 'The name and organisationsnummer should match what you entered in Meta.'), ('Add the VAT number', 'Add your momsregistreringsnummer in billing if you are registered.'), ('Check the site', 'A clear contact page and terms help with ad review.')],
 'Checks specific to Sweden',
 ['Use the legal name from Bolagsverket and your organisationsnummer.', 'Sole traders (enskild firma) can show a Skatteverket registration or a bank statement in the business name.', 'Add your VAT number in billing if you are VAT registered.', 'Keep the ad account in Swedish krona if you invoice in Sweden.', 'Make sure the website shows your company details and a way to reach you.'],
 'Finance, health, alcohol, gambling and housing ads have extra rules in Sweden. If you work in a regulated area, check your ads and pages against Meta’s policies and local rules before you appeal.',
 'Nordic campaigns',
 'Swedish companies often run ads across the Nordics. Keep prices, currency and delivery terms on the landing page consistent with each market, since mismatches cause rejections.',
 [('What is the organisationsnummer for?', 'It identifies your company in Sweden and helps prove it is real.'), ('Can I use Swedish documents?', 'Often yes. A short English summary helps.'), ('Does the DSA matter?', 'It may give you rights to a statement of reasons and dispute options.'), ('Do you work in Swedish?', 'We work in English.')],
 ['Swedish aktiebolag and enskilda firmor.', 'Nordic webshops.', 'Agencies serving Swedish clients.'], eu=True)

country('meta-ad-account-disabled-denmark', 'Denmark', 'Danish', 'Meta Ad Account Disabled in Denmark: Appeal Help',
 'Danish business with a disabled or restricted Meta ad account? CVR, moms and billing checks, and how to request a review.',
 'Danish businesses are easy to verify through the CVR register, which helps when the details match Meta. This page is for advertisers in Denmark with a restricted ad account.',
 'A Danish business with a restricted ad account should open Account Quality, make sure the details match the CVR entry, add the VAT number if registered, clear any balance and request one review. Unbanz can prepare the appeal. Meta decides, and nobody can promise the outcome.',
 [('Use the CVR record', 'The legal name, CVR number and address should match what you entered.'), ('Add the VAT number', 'Add your CVR or VAT number in billing if registered.'), ('Check the site', 'A clear contact page, terms and returns help with ad review.')],
 'Checks specific to Denmark',
 ['Use the company name and CVR number from the Central Business Register.', 'Sole proprietors (enkeltmandsvirksomhed) can use the CVR entry and a bank statement.', 'Add the VAT number in billing if you are registered.', 'Keep the ad account in Danish krone if you invoice in Denmark.', 'Make sure the website shows your CVR number and contact details.'],
 'Finance, health, alcohol, gambling and housing ads have extra rules in Denmark. If you work in a regulated area, check your ads and pages against Meta’s policies and local rules before you appeal.',
 'Webshops and Nordic markets',
 'Danish shops often sell in Sweden, Norway and Germany. Keep prices, delivery times and returns terms consistent with each market, and do not use separate ad accounts with different business names for the same company.',
 [('Is the CVR register accepted as proof?', 'It is a strong public record of the business. We can help present it with other documents.'), ('Do I need a Danish bank statement?', 'It can help if the name matches the business.'), ('What does the DSA mean?', 'It may give you extra rights to a reasons statement and dispute options in the EU.'), ('Do you work in Danish?', 'We work in English.')],
 ['Danish ApS and A/S companies and sole proprietors.', 'Webshops selling in the Nordics.', 'Agencies serving Danish clients.'], eu=True)
