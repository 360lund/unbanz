# -*- coding: utf-8 -*-
"""Country facts for the white label agency pages (2026-10-28). Every fact here is taken from the existing
country recovery pages (already researched) or is a plain, stable fact about a named authority or law.
Keys: name, h1 (adjective/short label for the H1), region, num, lang, biz, fraud, legal, priv, ad."""

DSA_TAIL = ' Appeals Centre Europe accepts some account decisions from EU users, but not hacked accounts, and Instagram’s own review comes first.'
def dsa(who):
    return 'Under the Digital Services Act, %s supervises platforms in the country. It does not decide an individual appeal.' % who + DSA_TAIL
DSA_GEN = 'Under the Digital Services Act, Instagram and Facebook must offer an internal complaint route against many account decisions, and national authorities supervise platforms. They do not decide an individual appeal.' + DSA_TAIL
BIZ = 'company name, website and registration number'

C = {}
def add(slug, name, h1, region, num, lang, biz, fraud, legal, priv, ad=None):
    C[slug] = dict(slug=slug, name=name, h1=h1, region=region, num=num, lang=lang, biz=biz, fraud=fraud, legal=legal, priv=priv, ad=ad)

# ---------------- Europe
add('uk', 'the UK', 'UK', 'Europe',
    'Text codes go to the +44 number on the account, so a lost SIM or a ported number needs sorting with the network first.',
    'Notices appear in English, so screenshots can be sent as they are.',
    'trading name, website and Companies House details',
    'Report Fraud (reportfraud.police.uk) covers England, Wales and Northern Ireland, and Police Scotland takes reports on 101. The National Cyber Security Centre publishes a plain-English guide called Recovering a hacked account.',
    None, 'The Information Commissioner’s Office (ICO) is the UK data protection authority.',
    'The Advertising Standards Authority (ASA) administers the UK advertising codes.')
add('netherlands', 'the Netherlands', 'Dutch', 'Europe',
    'A Dutch mobile written 06 12345678 is entered as +31 6 12345678, without the zero.',
    'The options in a Dutch notice are the same as in English. Screenshot it as it appears.',
    'company name, website and KvK number',
    'File an aangifte with the police at politie.nl, online or at a station. The Fraudehelpdesk (fraudehelpdesk.nl) also takes reports, and Offlimits (offlimits.nl) supports people dealing with online sexual abuse and blackmail.',
    dsa('the Autoriteit Consument & Markt (ACM)'), 'The Autoriteit Persoonsgegevens is the Dutch data protection authority.',
    'The Stichting Reclame Code runs the Dutch advertising code system.')
add('belgium', 'Belgium', 'Belgian', 'Europe',
    'A Belgian mobile written 0470 12 34 56 is entered as +32 470 12 34 56, without the zero.',
    'Belgium has three official languages, so a notice may be in Dutch, French or German. The review options are the same in each.',
    'company name, website and company number (ondernemingsnummer / numéro d’entreprise)',
    'Police on Web (police-on-web.be) takes online reports of fraud, blackmail and identity misuse. Forward a suspicious email to verdacht@safeonweb.be, and Card Stop on 078 170 170 blocks a bank card at any hour.',
    DSA_GEN, 'The Data Protection Authority (Gegevensbeschermingsautoriteit / Autorité de protection des données) handles complaints about personal data.',
    'The Jury for Ethical Practices in Advertising (JEP) is the Belgian advertising self-regulatory body.')
add('luxembourg', 'Luxembourg', 'Luxembourg', 'Europe',
    'Luxembourg numbers have no leading zero, so a mobile is +352 followed by nine digits starting with 6.',
    'Residents use French, German, English and Luxembourgish. The notice options are the same in whichever language shows.',
    'company name, website and RCS number',
    'The Grand-Ducal Police take reports of fraud, threats and identity misuse. BEE SECURE (bee-secure.lu) runs a helpline and a Stopline for reporting illegal content.',
    DSA_GEN, 'The CNPD (cnpd.lu) is the national data protection authority.')
add('france', 'France', 'French', 'Europe',
    'A French mobile written 06 12 34 56 78 is entered as +33 6 12 34 56 78, without the zero.',
    'Notices may appear in French. The options are the same in French and English, and there are French pages on this site.',
    'company name, website and SIREN number',
    'Cybermalveillance.gouv.fr is the national service for people hit by cybercrime. The Thésée platform takes complaints about online scams, and Pharos (internet-signalement.gouv.fr) is the portal for illegal content.',
    dsa('Arcom'), 'The CNIL (cnil.fr) is the French data protection authority.',
    'The ARPP is the French advertising self-regulatory body.')
add('germany', 'Germany', 'German', 'Europe',
    'A German mobile written 0151 1234567 is entered as +49 151 1234567, without the zero.',
    'Notices may appear in German. The options are the same in German and English.',
    BIZ,
    'Each federal state runs an Onlinewache where fraud, threats or identity misuse can be reported. The Verbraucherzentrale consumer advice centres give free guidance on phishing and account takeovers.',
    dsa('the Bundesnetzagentur'), 'Data protection is supervised by the federal and state data protection authorities.',
    'The Deutscher Werberat is the German advertising self-regulatory body.')
add('austria', 'Austria', 'Austrian', 'Europe',
    'An Austrian mobile written 0664 1234567 is entered as +43 664 1234567, without the zero.',
    'Notices may appear in German. The options are the same in German and English.',
    BIZ,
    'The police are on 133, and the Federal Criminal Police Office takes cybercrime tips at against-cybercrime@bmi.gv.at. Watchlist Internet (watchlist-internet.at) lists current fake shops and phishing campaigns.',
    dsa('KommAustria'), 'The Datenschutzbehörde is the Austrian data protection authority.',
    'The Österreichischer Werberat is the Austrian advertising self-regulatory body.')
add('switzerland', 'Switzerland', 'Swiss', 'Europe',
    'A Swiss mobile written 079 123 45 67 is entered as +41 79 123 45 67, without the zero.',
    'Notices appear in German, French or Italian depending on the phone. The options are the same.',
    'company name, website and UID number',
    'Two routes, not one: the Federal Office for Cybersecurity (BACS) takes phishing and incident reports at report.ncsc.admin.ch, while a criminal complaint goes to the local police or Suisse ePolice (suisse-epolice.ch).',
    None, 'The Federal Data Protection and Information Commissioner (FDPIC) supervises the revised Federal Act on Data Protection.',
    'The Swiss Fair Trading Commission (Schweizerische Lauterkeitskommission) is the advertising self-regulatory body.')
add('liechtenstein', 'Liechtenstein', 'Liechtenstein', 'Europe',
    'Numbers have seven digits after +423 and no leading zero.',
    'Notices may appear in German. The options are the same in German and English.',
    BIZ,
    'The Landespolizei (landespolizei.li) in Vaduz takes reports of fraud, threats and identity misuse.',
    None, 'The Datenschutzstelle (dss.li) is the data protection authority, and the GDPR applies through the EEA agreement.')
add('monaco', 'Monaco', 'Monaco', 'Europe',
    'A Monaco mobile written 06 12 34 56 78 is entered as +377 6 12 34 56 78, without the zero.',
    'Monaco is French-speaking, so a notice may appear in French. The options are the same in French and English.',
    BIZ,
    'The Sûreté Publique takes reports of fraud, blackmail and identity misuse. The Agence Monégasque de Sécurité Numérique (AMSN) is the national digital security agency.',
    'Monaco is outside the EU, so rights that depend on EU law, such as out-of-court appeal bodies under the Digital Services Act, are not available on that basis. Instagram’s own review is the route.',
    'The CCIN (ccin.mc) is Monaco’s data protection authority.')
add('italy', 'Italy', 'Italian', 'Europe',
    'An Italian mobile starts with 3 and keeps all its digits, so 333 123 4567 is +39 333 123 4567.',
    'Notices may appear in Italian. The options are the same in Italian and English.',
    'partita IVA and business name',
    'The Polizia Postale handles online fraud, blackmail and impersonation, and reports can be filed through the online police station at commissariatodips.it.',
    dsa('AGCOM'), 'The Garante per la protezione dei dati personali (garanteprivacy.it) is the Italian data protection authority.',
    'The Istituto dell’Autodisciplina Pubblicitaria (IAP) is the Italian advertising self-regulatory body.')
add('spain', 'Spain', 'Spanish', 'Europe',
    'Spanish numbers have nine digits and no leading zero, so a mobile is +34 612 345 678.',
    'Notices may appear in Spanish. The options are the same in Spanish and English, and there are Spanish pages on this site.',
    'company name, website and NIF',
    'INCIBE’s free cybersecurity helpline, 017, gives confidential advice on hacked accounts and scams. The Policía Nacional (denuncias.policia.es) and the Guardia Civil take reports.',
    dsa('the CNMC'), 'The AEPD (aepd.es) is the Spanish data protection agency.',
    'Autocontrol is the Spanish advertising self-regulatory body.')
add('portugal', 'Portugal', 'Portuguese', 'Europe',
    'Portuguese numbers have nine digits and no leading zero, so a mobile is +351 912 345 678.',
    'Notices may appear in Portuguese. The options are the same in Portuguese and English.',
    BIZ,
    'The Queixa Eletrónica portal (queixaselectronicas.mai.gov.pt) takes online complaints about certain crimes, and the Polícia Judiciária investigates cybercrime. APAV gives free help to victims of crime.',
    dsa('ANACOM'), 'The CNPD is the Portuguese data protection authority.',
    'The ICAP is the Portuguese advertising self-regulatory body.')
add('ireland', 'Ireland', 'Irish', 'Europe',
    'An Irish mobile written 087 123 4567 is entered as +353 87 123 4567, without the zero.',
    'Notices appear in English, so screenshots can be sent as they are.',
    BIZ,
    'Report fraud, threats or blackmail to the local Garda station. Hotline.ie takes reports about child sexual abuse material and other illegal content.',
    dsa('Coimisiún na Meán') + ' Meta’s EU entity is based in Ireland, but posting letters or turning up does not speed anything up.',
    'The Data Protection Commission is the Irish data protection authority.',
    'The ASAI is the Irish advertising self-regulatory body.')
add('denmark', 'Denmark', 'Danish', 'Europe',
    'Danish numbers have eight digits and no leading zero.',
    'Notices may appear in Danish or English with the same options.',
    BIZ,
    'Fraud, threats and blackmail can be reported at politi.dk, and 114 is the non-emergency number. A message saying a MitID has expired is a common bait, and a MitID prompt that was not started by the client should never be approved.',
    dsa('the Danish Competition and Consumer Authority'), 'Datatilsynet is the Danish data protection authority.',
    'The Consumer Ombudsman supervises marketing under Danish law.')
add('sweden', 'Sweden', 'Swedish', 'Europe',
    'A Swedish mobile written 070-123 45 67 is entered as +46 70 123 45 67, without the zero.',
    'Notices may appear in Swedish or English with the same options.',
    BIZ,
    'Use the police non-emergency number 114 14 or report online at polisen.se. A BankID request that the client did not start should never be approved, and Swish requests from a hijacked friend are a usual pattern.',
    DSA_GEN, 'The IMY is the Swedish data protection authority.',
    'The Reklamombudsmannen is the Swedish advertising self-regulatory body.')
add('norway', 'Norway', 'Norwegian', 'Europe',
    'Norwegian numbers have eight digits and no leading zero.',
    'Notices may appear in Norwegian or English. The options are the same.',
    BIZ,
    'Fraud, threats and blackmail can be reported online at politi.no. Messages saying BankID or Vipps needs updating are phishing, and Slettmeg.no gives advice on getting unwanted content removed.',
    None, 'Datatilsynet is the Norwegian data protection authority.',
    'The Reklameombudet is the Norwegian advertising self-regulatory body.')
add('finland', 'Finland', 'Finnish', 'Europe',
    'A Finnish mobile written 040 123 4567 is entered as +358 40 123 4567, without the zero.',
    'Finnish and Swedish are the national languages. The review options are the same in both and in English.',
    BIZ,
    'The National Cyber Security Centre Finland at Traficom takes reports and publishes warnings about phishing. The police take online reports at poliisi.fi, and Victim Support Finland (RIKU) helps victims of crime.',
    dsa('Traficom'), 'The Office of the Data Protection Ombudsman is the Finnish data protection authority.',
    'The Council of Ethics in Advertising (Mainonnan eettinen neuvosto) is the Finnish self-regulatory body.')
add('iceland', 'Iceland', 'Icelandic', 'Europe',
    'Icelandic numbers have seven digits and no leading zero.',
    'Notices may appear in Icelandic or English. The options are the same.',
    BIZ,
    'CERT-IS (cert.is) publishes warnings about phishing and takes incident reports, and the police (logreglan.is) take reports of fraud and identity misuse.',
    None, 'Persónuvernd (personuvernd.is) is the Icelandic data protection authority, and the GDPR applies through the EEA agreement.')
add('malta', 'Malta', 'Maltese', 'Europe',
    'Maltese numbers have eight digits and no leading zero.',
    'English is an official language in Malta, so notices are often read in English. The review options are the same in every language.',
    BIZ,
    'The Malta Police Force has a Cyber Crime Unit. BeSmartOnline! (besmartonline.gov.mt) is Malta’s safer internet centre and has a way to report harmful content.',
    dsa('the Malta Communications Authority'), 'The Information and Data Protection Commissioner (idpc.org.mt) is the Maltese data protection authority.')
add('cyprus', 'Cyprus', 'Cypriot', 'Europe',
    'Cypriot numbers have eight digits and no leading zero.',
    'Notices may appear in Greek or English. The review options are the same in both.',
    BIZ,
    'The Cyprus Police has a cybercrime subdivision, and CSIRT-CY, run by the Digital Security Authority, publishes advice on phishing and incidents.',
    DSA_GEN, 'The Commissioner for Personal Data Protection (dataprotection.gov.cy) handles complaints about personal data.')
add('czech-republic', 'the Czech Republic', 'Czech', 'Europe',
    'Czech numbers have nine digits and no leading zero, so a mobile is +420 601 234 567.',
    'The review options are the same in Czech and English. Screenshot the notice as it appears.',
    BIZ,
    'The Czech Police (Policie ČR) take reports of fraud, threats and identity misuse. Messages posing as a bank, a parcel service or a classifieds buyer, with a link to a fake login, are a common way in.',
    dsa('the Czech Telecommunication Office (ČTÚ)'), 'The Office for Personal Data Protection (ÚOOÚ) is the Czech data protection authority.',
    'The Rada pro reklamu is the Czech advertising self-regulatory body.')
add('poland', 'Poland', 'Polish', 'Europe',
    'Polish numbers have nine digits and no leading zero, so a mobile is +48 512 345 678.',
    'The review options are the same in Polish and English. Screenshot the notice as it appears.',
    BIZ,
    'CERT Polska (cert.pl) takes reports of phishing, and a suspicious text can be forwarded to 8080. The police take reports of fraud and identity misuse at any station.',
    DSA_GEN, 'The UODO (uodo.gov.pl) is the Polish data protection authority.',
    'The Rada Reklamy is the Polish advertising self-regulatory body.')
add('estonia', 'Estonia', 'Estonian', 'Europe',
    'Estonian numbers have no leading zero, so a mobile is +372 followed by its seven or eight digits.',
    'The review options are the same in Estonian and English. Screenshot the notice as it appears.',
    BIZ,
    'The Police and Border Guard Board (politsei.ee) takes reports online, and CERT-EE, run by the Information System Authority, handles reports of phishing and incidents.',
    dsa('the Consumer Protection and Technical Regulatory Authority (TTJA)'), 'The Data Protection Inspectorate (aki.ee) is the Estonian data protection authority.')
add('slovenia', 'Slovenia', 'Slovenian', 'Europe',
    'A Slovenian mobile written 031 123 456 is entered as +386 31 123 456, without the zero.',
    'The review options are the same in Slovenian and English. Screenshot the notice as it appears.',
    BIZ,
    'SI-CERT (cert.si) takes reports of phishing and internet fraud, and Spletno oko (spletno-oko.si) is the hotline for illegal online content.',
    dsa('AKOS, the Agency for Communication Networks and Services,'), 'The Information Commissioner (ip-rs.si) is the Slovenian data protection authority.')

# ---------------- North America, Latin America, Oceania
add('usa', 'the USA', 'US', 'North America, Latin America and Oceania',
    'Text codes go to the US number on the account. SIM swapping is a known way accounts get hijacked, so ask the carrier about port-out protection.',
    'Notices appear in English, so screenshots can be sent as they are.',
    'business name, website and state registration details',
    'ReportFraud.ftc.gov takes fraud reports, and ic3.gov (the FBI’s Internet Crime Complaint Center) takes serious cybercrime reports. That is separate from getting the account back.',
    None, 'Privacy rules differ by state, so check the client’s own obligations before sending personal data.')
add('canada', 'Canada', 'Canadian', 'North America, Latin America and Oceania',
    'Canada shares the +1 country code with the USA, so enter the full ten digits.',
    'The notice follows the phone or account language, so it may be in English or French.',
    BIZ,
    'The Canadian Anti-Fraud Centre (antifraudcentre-centreantifraude.ca) takes fraud and cybercrime reports, and Cybertip.ca takes reports about online sexual exploitation of young people.',
    'Since August 2023 Meta has blocked news links and posts for Canadian users after the Online News Act. That is a separate matter from a disabled account.',
    'The Office of the Privacy Commissioner of Canada oversees federal privacy law.',
    'Ad Standards is the Canadian advertising self-regulatory body.')
add('australia', 'Australia', 'Australian', 'North America, Latin America and Oceania',
    'An Australian mobile written 04xx xxx xxx is entered as +61 4xx xxx xxx, without the zero.',
    'Notices appear in English, so screenshots can be sent as they are.',
    'ABN, trading name and website',
    'Scamwatch (scamwatch.gov.au) takes scam reports, ReportCyber at cyber.gov.au is the national route for cybercrime reports, and IDCARE (idcare.org) supports people whose accounts have been compromised.',
    'From 10 December 2025, Instagram and Facebook must take reasonable steps to stop Australians under 16 from holding accounts. An appeal does not change that rule.',
    'The Office of the Australian Information Commissioner (OAIC) oversees the Privacy Act.',
    'Ad Standards is the Australian advertising self-regulatory body.')
add('new-zealand', 'New Zealand', 'New Zealand', 'North America, Latin America and Oceania',
    'A New Zealand mobile written 021 123 4567 is entered as +64 21 123 4567, without the zero.',
    'Notices appear in English, so screenshots can be sent as they are.',
    'trading name, NZBN and website',
    'Report fraud and blackmail to NZ Police on 105, and cyber incidents to the National Cyber Security Centre. Netsafe (netsafe.org.nz) gives free advice on scams and harassment.',
    'Netsafe is the approved agency under the Harmful Digital Communications Act 2015. It does not restore accounts.',
    'The Office of the Privacy Commissioner oversees the Privacy Act 2020.',
    'The Advertising Standards Authority is the New Zealand self-regulatory body.')
add('brazil', 'Brazil', 'Brazilian', 'North America, Latin America and Oceania',
    'Brazilian mobile numbers are entered with +55, the two-digit area code and the nine-digit number.',
    'Notices appear in Portuguese, and there are Portuguese pages on this site. The review options are the same as in English.',
    'CNPJ (company tax ID), or the MEI registration for a sole trader',
    'SaferNet Brasil (safernet.org.br) takes reports and gives guidance on online crimes, and serious fraud or blackmail can be reported to the police. A hijacked account asking contacts for a Pix transfer is a pattern to warn clients about.',
    'The Marco Civil da Internet (Law 12.965/2014) sets the basic rules for internet use in Brazil. It does not restore a social media account.',
    'The LGPD (Law 13.709/2018) is Brazil’s data protection law, and the ANPD is the authority.',
    'CONAR is the Brazilian advertising self-regulatory council.')

# ---------------- Middle East
add('uae', 'the UAE', 'UAE', 'Middle East',
    'Codes are sent by text to the +971 number on the account. If the client changed number or runs two, tell us which one is on the account.',
    'Notices may show in Arabic or English. Send the screenshot unedited, in whatever language it shows.',
    'business name, website and trade licence details',
    'If there was fraud, blackmail or stolen money, report it to UAE police through an official e-service such as Dubai Police’s eCrime platform (ecrime.ae) or the Ministry of Interior’s e-services.',
    'The UAE is on Gulf Standard Time (UTC+4). Notice deadlines are counted in days, so check the date on the notice.',
    'The UAE has a federal Personal Data Protection Law (Federal Decree-Law No. 45 of 2021).')
add('israel', 'Israel', 'Israeli', 'Middle East',
    'An Israeli mobile written 050-123-4567 is entered as +972 50 123 4567, without the leading zero.',
    'Hebrew and Arabic notices read right to left. The options are the same, so screenshot the notice as shown.',
    BIZ,
    'The Israel National Cyber Directorate runs a 24/7 hotline on 119 that gives free, confidential first guidance on a hacked social media account. Do not pay blackmail, and report to Israel Police on 100 for urgent matters.',
    None, 'The Privacy Protection Authority supervises the Protection of Privacy Law.')
add('kuwait', 'Kuwait', 'Kuwaiti', 'Middle East',
    'Kuwaiti numbers have eight digits and no leading zero.',
    'Notices may appear in Arabic or English. The review options are the same.',
    BIZ,
    'Do not pay or reply to blackmail. Save screenshots and links, then report to the Ministry of Interior through a police station or its official channels.',
    'Law No. 63 of 2015 on combating information technology crimes covers offences such as unauthorised access to accounts and online threats.',
    'CITRA, the Communication and Information Technology Regulatory Authority, regulates telecom and internet services.')
add('qatar', 'Qatar', 'Qatari', 'Middle East',
    'Qatari numbers have eight digits and no leading zero. Lines are registered to a Qatar ID, so a lost SIM is replaced by Ooredoo or Vodafone Qatar after identification.',
    'Notices may appear in Arabic or English. The review options are the same.',
    'commercial registration and trade name',
    'Do not pay or reply to blackmail. Report to the Ministry of Interior’s Economic and Cyber Crimes Combating Department through the Metrash2 app or its hotline on 66815757.',
    'Qatar’s Cybercrime Prevention Law of 2014 covers offences such as unauthorised access to accounts and online blackmail.',
    'Qatar’s Law No. 13 of 2016 covers personal data privacy.')
add('saudi-arabia', 'Saudi Arabia', 'Saudi', 'Middle East',
    'A Saudi mobile written 05x xxx xxxx is entered as +966 5x xxx xxxx, without the zero. SIMs are registered to a national ID or iqama.',
    'Notices may appear in Arabic or English. The options are the same.',
    'Mawthooq licence details or the Maroof store listing, plus the business name',
    'Do not pay or reply to blackmail. Report through the Ministry of Interior’s Kollona Amn service or Absher.',
    'The Anti-Cyber Crime Law covers offences such as unauthorised access and online blackmail, and the National Cybersecurity Authority publishes guidance for individuals.',
    'The Personal Data Protection Law is overseen by SDAIA.')
add('bahrain', 'Bahrain', 'Bahraini', 'Middle East',
    'Bahraini numbers have eight digits and no leading zero.',
    'Notices may appear in Arabic or English. The review options are the same.',
    BIZ,
    'The Ministry of Interior has an anti-cybercrime directorate that takes reports of blackmail, fraud and unauthorised access. Do not pay or reply to blackmail.',
    'Law No. 60 of 2014 on information technology crimes covers offences such as unauthorised access and online threats.',
    'Law No. 30 of 2018 is Bahrain’s Personal Data Protection Law.')
add('oman', 'Oman', 'Omani', 'Middle East',
    'Omani numbers have eight digits and no leading zero.',
    'Notices may appear in Arabic or English. The review options are the same.',
    BIZ,
    'The Royal Oman Police takes reports of blackmail, fraud and unauthorised access to accounts. Do not pay or reply to blackmail.',
    'The Cyber Crime Law (Royal Decree 12/2011) covers offences such as unauthorised access and online threats.',
    'Royal Decree 6/2022 is Oman’s Personal Data Protection Law.')

# ---------------- Asia
add('south-korea', 'South Korea', 'South Korean', 'Asia',
    'A Korean mobile written 010-1234-5678 is entered as +82 10 1234 5678, without the leading zero. Lines are registered to a named holder.',
    'The review options are the same in Korean and English. Screenshot the notice as it appears.',
    BIZ,
    'The Korean National Police Agency runs a cybercrime reporting system at ecrm.police.go.kr. KISA runs the 118 cyber centre for questions about hacking and phishing.',
    None, 'The Personal Information Protection Commission oversees the Personal Information Protection Act.')
add('hong-kong', 'Hong Kong', 'Hong Kong', 'Asia',
    'Hong Kong numbers have eight digits and no leading zero. Prepaid SIMs have been registered under real names since 2022.',
    'The review options are the same in Chinese and English. Screenshot the notice as it appears.',
    BIZ,
    'The Anti-Deception Coordination Centre runs the 18222 hotline for scam advice, and the Cyber Security and Technology Crime Bureau of the Hong Kong Police investigates hacking and online fraud.',
    None, 'The Privacy Commissioner for Personal Data (pcpd.org.hk) deals with doxxing and has had powers since 2021 to ask for harmful content to be removed.')
add('japan', 'Japan', 'Japanese', 'Asia',
    'A Japanese mobile written 090-1234-5678 is entered as +81 90 1234 5678, with the leading zero dropped.',
    'The options are the same in Japanese and English. Screenshot the notice as it appears.',
    BIZ,
    'The prefectural police run cybercrime consultation desks, and #9110 is the national police consultation line. Emails or SMS claiming a copyright or policy violation are a common way in.',
    'Under the Information Distribution Platform Act, Meta must run a deletion request channel for rights-violating content. That is about a post, not about restoring an account.',
    'The Personal Information Protection Commission oversees the APPI.',
    'JARO is Japan’s advertising review organisation.')
add('singapore', 'Singapore', 'Singapore', 'Asia',
    'Singapore numbers have no leading zero, so it is +65 followed by the eight digits.',
    'Notices appear in English, so screenshots can be sent as they are.',
    'business name and registration details',
    'The ScamShield Helpline on 1799 is open 24/7 for advice, and reports are lodged through the police e-service at police.gov.sg.',
    'The Online Safety Commission began work on 29 June 2026 and takes reports about harms such as harassment and intimate image abuse. It does not restore accounts.',
    'The Personal Data Protection Commission oversees the PDPA.',
    'The Advertising Standards Authority of Singapore (ASAS) is the self-regulatory body.')
add('taiwan', 'Taiwan', 'Taiwanese', 'Asia',
    'A Taiwan mobile written 0912 345 678 is entered as +886 912 345 678, without the zero.',
    'The review options are the same in Chinese and English. Screenshot the notice as it appears.',
    BIZ,
    '165 is the national anti-fraud hotline, where a message or account can be checked and fraud reported. The police and the Criminal Investigation Bureau take reports of fraud and threats.',
    None, 'Personal data is covered by the Personal Data Protection Act.')

ORDER = ['uk','usa','canada','australia','new-zealand','brazil','netherlands','belgium','luxembourg','france','germany','austria','switzerland','liechtenstein','monaco','italy','spain','portugal','ireland','denmark','sweden','norway','finland','iceland','malta','cyprus','czech-republic','poland','estonia','slovenia','uae','israel','kuwait','qatar','saudi-arabia','bahrain','oman','south-korea','hong-kong','japan','singapore','taiwan']
assert set(ORDER) == set(C), set(C) ^ set(ORDER)
REGIONS = ['Europe', 'North America, Latin America and Oceania', 'Middle East', 'Asia']
