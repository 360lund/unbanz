# -*- coding: utf-8 -*-
from lib import *
import core, nl_services, nl_guides

SLUGS = {
 'home': '', 'services': 'diensten', 'pricing': 'prijs-account-terugkrijgen', 'faq': 'veelgestelde-vragen', 'contact': 'contact',
 'reviews': 'reviews', 'about': 'over-ons', 'how': 'hoe-het-werkt', 'legit': 'is-unbanz-betrouwbaar',
 'ig': 'instagram-account-terugkrijgen', 'fb': 'facebook-account-terugkrijgen', 'ad': 'advertentieaccount-terugkrijgen',
 'snap': 'snapchat-account-terugkrijgen', 'fake': 'nepaccount-melden', 'imp': 'imitatieaccount-melden',
 'har': 'intimidatie-account-melden', 'user': 'instagram-gebruikersnaam-claimen',
 'ig-disabled': 'instagram-account-uitgeschakeld', 'ig-hacked': 'instagram-account-gehackt',
 'appeal-time': 'hoe-lang-duurt-instagram-bezwaar', 'appeal-denied': 'instagram-bezwaar-afgewezen',
 'deleted': 'instagram-account-verwijderd-of-uitgeschakeld', 'no-button': 'instagram-geen-bezwaarknop',
 'blocked': 'instagram-actie-geblokkeerd', 'ad-disabled': 'facebook-advertentieaccount-uitgeschakeld',
 'fb-appeal': 'facebook-account-uitgeschakeld-bezwaar', 'fb-hacked': 'facebook-account-gehackt',
 'inactive-user': 'instagram-gebruikersnaam-inactief-account', 'report-fake': 'nepaccount-met-mijn-foto-melden',
 'scams': 'oplichting-account-herstel-waarschuwing', 'sextortion': 'sextortion-instagram-wat-te-doen',
 'support': 'instagram-meta-contact-nederland', 'rights': 'dsa-recht-op-beroep-meta',
}

WA_DEFAULT = 'Hoi%20Unbanz%2C%20ik%20heb%20hulp%20nodig%20met%20een%20account%20(NL)'

S = dict(
 code='nl', dir='nl', html_lang='nl', og_locale='nl_NL', country='Nederland', js_code='nl', tag='(NL)',
 wa_default=WA_DEFAULT, mail_subj='Hulp%20met%20mijn%20account',
 offer_desc='De prijs hoor je in het gesprek, nadat je je situatie hebt uitgelegd en voordat het werk begint. Vragen kost niets.',
 og_alt='Unbanz: hulp bij Instagram-, Facebook- en Snapchat-accounts',
 skip='Naar de inhoud', nav_aria='Hoofdmenu', mnav_aria='Mobiel menu',
 n_home='Home', n_services='Diensten', n_user='Gebruikersnamen', n_reviews='Reviews', n_faq='Vragen', n_contact='Contact', n_how='Hoe het werkt',
 menu_open='Menu openen', menu_close='Menu sluiten',
 foot_links=[('services', 'Diensten'), ('ig', 'Instagram'), ('fb', 'Facebook'), ('snap', 'Snapchat'), ('ad', 'Advertentieaccounts'),
             ('fake', 'Nepaccounts'), ('imp', 'Imitatie'), ('har', 'Intimidatie'), ('user', 'Gebruikersnamen'), ('pricing', 'Prijs'),
             ('how', 'Hoe het werkt'), ('faq', 'FAQ'), ('reviews', 'Reviews'), ('legit', 'Is Unbanz betrouwbaar?'), ('contact', 'Contact')],
 foot_tag='Accounts terugkrijgen &amp; meldingen.<br>Praat rechtstreeks met ons.',
 foot_indep='Onafhankelijke dienst. Niet verbonden aan Meta.',
 mc_wa='Stuur ons een bericht op WhatsApp', mc_mail='E-mail',
 cta_quote='Vraag een prijs op WhatsApp', cta_mail='Mail ons',
 hero_wa='Laten we praten op WhatsApp', hero_mail='Liever mailen?',
 write_us='Schrijf ons', see_detail='Bekijk de details',
 faq_eyebrow='VEELGESTELDE VRAGEN', faq_eyebrow2='JOUW VRAGEN', faq_title='Goed om te weten.',
 proof_title='Vertel ons wat er is gebeurd.', related='Gerelateerde pagina\'s', related_services='Alle diensten',
 crumb_guides='Gidsen', crumb_services='Diensten', help_h2='Wil je hulp?', guides_h2='Gerelateerde gidsen',
 std_howto=('<h2 id="met-unbanz">Zo gaat het met Unbanz</h2><ol><li>Je stuurt ons je gebruikersnaam en een screenshot van de melding via WhatsApp of e-mail.</li>'
            '<li>We zeggen eerlijk of we kunnen helpen. De prijs hoor je in het gesprek, nadat je je situatie hebt uitgelegd en voordat het werk begint. Vragen kost niets.</li>'
            '<li>We bereiden het verzoek voor en dienen het in via het officiële proces van het platform.</li>'
            '<li>We houden je op de hoogte tot er een antwoord is.</li></ol>'
            '<p>We communiceren voornamelijk in het Engels; een kort bericht met je gebruikersnaam, de screenshot en de datum is genoeg om te beginnen.</p>'),
 std_safe=('<h2 id="voorzichtig">Blijf voorzichtig</h2><p>Niemand heeft je wachtwoord of inlogcodes nodig om je te helpen. Wij niet, en anderen ook niet. '
           'Biedt iemand je in een privébericht aan om "alles te regelen", vraagt iemand je in te loggen via een link of zegt iemand een contact bij Meta te hebben? Ga er niet op in. '
           'Unbanz vraagt nooit om je inloggegevens en doet zich niet voor alsof we een speciale toegang hebben: we gebruiken dezelfde officiële routes als jij.</p>'),
 std_about=('<h2 id="over-unbanz">Over Unbanz</h2><p>Unbanz (unbanz.com) is een onafhankelijke dienst die particulieren, bedrijven en bureaus helpt met verzoeken om uitgeschakelde Instagram-, Facebook- en Snapchat-accounts '
            'opnieuw te laten beoordelen, met het melden van accounts die de regels overtreden via de officiële meldtools, met gebruikersnaam-verzoeken en met het terugkrijgen van Meta-advertentieaccounts. '
            'Unbanz is niet Unbanx of unbanx.me en we zijn niet verbonden aan Meta. Zie ook <a href="@@legit@@">Is Unbanz betrouwbaar?</a></p>'),
 block3=[('Waar je ook woont', 'We werken op afstand, via WhatsApp of e-mail, met klanten in Nederland, Europa en de rest van de wereld. Support is voornamelijk in het Engels.'),
         ('Eerst de prijs', 'Je kent de prijs voordat het werk begint: we noemen die in het gesprek, nadat je je situatie hebt uitgelegd.'),
         ('Je wachtwoord blijft bij jou', 'We hebben alleen je gebruikersnaam en de melding nodig. Je wachtwoord en je codes blijven bij jou.')],
 price_h2='Weet de prijs<br>voordat je begint.', price_p='Stuur ons een bericht op WhatsApp of per e-mail, leg de situatie uit en je hoort van ons wat het kost.',
 price_link='Hoe de prijs wordt bepaald',
 vt_transcript='Transcript (in het Engels)', vt_play='Video afspelen',
 vt_titles=[('Client on claiming an inactive Instagram username with Unbanz', 'Video afspelen: klant over het claimen van een inactieve Instagram-gebruikersnaam', 'Klant: videoreview over een Instagram-gebruikersnaam-verzoek', 'Username claim', 'Gebruikersnaam'),
            ('Management agency owner on working with Unbanz', 'Video afspelen: eigenaar van een marketingbureau over het werken met Unbanz', 'Bureau-eigenaar: videoreview over het werken met Unbanz', 'Agency owner', 'Bureau-eigenaar'),
            ('Restricted Facebook ad account restored by Unbanz', 'Video afspelen: beperkt Facebook-advertentieaccount weer actief', 'Klant: videoreview over een beperkt advertentieaccount', 'Ad account', 'Advertentieaccount')],
 # ---- JS (contact modal)
 js_services="['unban', 'Mijn account terugkrijgen'], ['ban', 'Account melden'], ['username', 'Gebruikersnaam'], ['ad', 'Advertentieaccount'], ['other', 'Anders']",
 js_eyebrow='SCHRIJF ONS', js_title='Waar heb je hulp bij nodig?', js_legend_service='Dienst', js_legend_platform='Platform',
 js_reason_label='Korte reden <span>(optioneel)</span>', js_placeholder='bijv. uitgeschakeld na inloggen op een nieuwe telefoon',
 js_continue='Verder op WhatsApp', js_email='Liever per e-mail', js_note='Stuur nooit wachtwoorden of inlogcodes.', js_close='Sluiten',
 js_mail_subject='Hulp met mijn account',
 js_sentence=("""    const base = s === 'unban' ? `Ik wil mijn ${pl}-account terugkrijgen`
      : s === 'ban' ? `Ik wil een ${pl}-account laten melden`
      : s === 'username' ? `Ik wil een ${pl}-gebruikersnaam claimen`
      : s === 'ad' ? (pl === 'Instagram' || pl === 'Facebook' ? `Ik heb hulp nodig met mijn Meta-advertentieaccount (${pl})` : `Ik heb hulp nodig met een advertentieaccount op ${pl}`)
      : `Ik heb hulp nodig met mijn ${pl}-account`;
    const reason = modal.querySelector('#cm-reason').value.replace(/\\s+/g, ' ').trim();
    return `Hoi Unbanz, ${base}.` + (reason ? ` Reden: ${reason}` : '') + ' %TAG%' + (window.unbanzViaTag ? ` ${window.unbanzViaTag}` : '');"""),
 llms=dict(
   header='## Nederlands (Nederland)',
   intro='Unbanz is er ook in het Nederlands, voor mensen in Nederland (en Nederlandstalig België) die hulp zoeken bij een uitgeschakeld, geblokkeerd of gehackt Instagram-, Facebook- of Snapchat-account. Support is voornamelijk in het Engels.',
   facts_label='### Kerngegevens (Nederlands)',
   facts=('- Unbanz is een onafhankelijke dienst en niet verbonden aan Meta. Alles loopt via de officiële routes van het platform; het platform beslist altijd zelf.\n'
          '- Je hoort de prijs in het gesprek, nadat je de situatie hebt uitgelegd en voordat het werk begint. Vragen kost niets.\n'
          '- Unbanz vraagt nooit om je wachtwoord of inlogcodes.\n'
          '- Alleen bij gebruikersnaam-verzoeken: mislukt het verzoek, dan krijg je 100% van je geld terug (zie /refund-policy/).\n'
          '- Contact: WhatsApp +1 934 201 2490 of team@unbanz.com.'),
   pages_label='### Nederlandse pagina\'s', qa_label='### Korte antwoorden (Nederlands)',
   qa=[('Hoe krijg ik mijn Instagram-account terug na een uitschakeling?', 'Open de melding in de app, maak één keer bezwaar via het officiële formulier en bewaar een screenshot; lukt dat niet, dan kan Unbanz het verzoek voor je voorbereiden en indienen.', 'ig-disabled'),
       ('Wat kost het om een account terug te krijgen?', 'De prijs hangt af van het account en de situatie. Unbanz noemt die in het gesprek, voordat het werk begint; vragen kost niets.', 'pricing'),
       ('Is Unbanz betrouwbaar?', 'Unbanz is een onafhankelijke dienst met één website, één e-mailadres, schriftelijke voorwaarden en video-reviews van klanten; het vraagt nooit om je wachtwoord.', 'legit')]),
)

C = {}
C['services'] = dict(
 title='Instagram, Facebook en Snapchat account terugkrijgen: diensten',
 desc='Hulp bij uitgeschakelde, geblokkeerde of gehackte accounts, bij het melden van nep- en imitatieaccounts en bij gebruikersnaam-verzoeken. Via de officiële routes.',
 nav='Diensten', h1='Diensten: account terugkrijgen en accounts melden.',
 lead='Instagram, Facebook, Snapchat en Meta-advertentieaccounts. Stuur ons je gebruikersnaam en de melding, dan zeggen we eerlijk of we kunnen helpen. Alles gaat via de officiële routes van het platform.',
 eyebrow='JOUW SITUATIE', h2='Waar heb je hulp bij nodig?',
 rows=[('Instagram-account terugkrijgen', 'Uitgeschakeld, opgeschort of gehackt: bezwaar en herstel via de officiële routes.', 'ig', 'unban'),
       ('Facebook-account terugkrijgen', 'Uitgeschakelde of gehackte profielen en beperkte pagina\'s.', 'fb', 'unban'),
       ('Snapchat-account terugkrijgen', 'Vergrendelde of uitgeschakelde Snapchat-accounts.', 'snap', 'unban'),
       ('Advertentieaccounts', 'Beperkte of uitgeschakelde Meta-advertentieaccounts en Business Portfolio\'s.', 'ad', 'ad'),
       ('Nepaccounts melden', 'Nepprofielen melden via de officiële meldtools van het platform.', 'fake', 'ban'),
       ('Imitatieaccounts melden', 'Iemand die zich voor jou of je bedrijf uitgeeft.', 'imp', 'ban'),
       ('Intimidatie melden', 'Accounts die je lastigvallen of bedreigen.', 'har', 'ban'),
       ('Gebruikersnaam claimen', 'Inactieve of bezette gebruikersnamen, via de officiële processen van het platform.', 'user', 'username')],
 faq=[('Voor welke platforms bieden jullie hulp?', 'Instagram, Facebook, Snapchat en Meta-advertentieaccounts.'),
      ('Hoe werkt het?', 'Je stuurt de gebruikersnaam en een screenshot van de melding. Wij zeggen eerlijk of we kunnen helpen en noemen de prijs in het gesprek, voordat het werk begint.'),
      ('Kan ik het ook zelf doen?', 'Ja. Bezwaar maken, het herstelformulier voor gehackte accounts en het melden van een account zijn gratis en officieel. Wij helpen als het vastloopt of als je het liever uit handen geeft.'),
      ('Is Unbanz verbonden aan Meta?', 'Nee. Unbanz is onafhankelijk en gebruikt dezelfde officiële routes als jij. Het platform beslist altijd zelf.')],
 related=['ig', 'fb', 'snap', 'ad', 'user', 'pricing', 'how', 'legit'])

FAQ_ALL = [
 ('Mijn Instagram-account is uitgeschakeld. Wat kan ik doen?', 'Log in, open de melding en maak één keer bezwaar via het officiële formulier; meestal heb je daarvoor ongeveer 180 dagen. Maak een screenshot van de melding. Zie de gids <a href="@@ig-disabled@@">Instagram-account uitgeschakeld</a>.'),
 ('Mijn account is gehackt en het e-mailadres is gewijzigd. Is er nog hoop?', 'Vaak wel, via de officiële hulpmiddelen van Instagram (instagram.com/hacked en de videoselfie-verificatie). Zie <a href="@@ig-hacked@@">Instagram-account gehackt</a>.'),
 ('Wat kost het om een account terug te krijgen?', 'De prijs hangt af van het account en de situatie. We noemen die in het gesprek, nadat je hebt uitgelegd wat er is gebeurd en voordat het werk begint. Vragen kost niets. Zie <a href="@@pricing@@">prijs</a>.'),
 ('Hoe lang duurt het?', 'Meta en Snapchat publiceren geen vaste behandeltijd. Een antwoord kan na een paar dagen komen of na een aantal weken. We beloven geen datum, maar houden je op de hoogte.'),
 ('Heb jullie mijn wachtwoord nodig?', 'Nee, nooit. Een gebruikersnaam of profiellink en een screenshot van de melding zijn genoeg. Deel je wachtwoord en inlogcodes met niemand.'),
 ('Is Unbanz verbonden aan Meta?', 'Nee. Unbanz is een onafhankelijke dienst. We gebruiken de officiële routes van het platform en het platform beslist altijd zelf. Zie <a href="@@legit@@">Is Unbanz betrouwbaar?</a>'),
 ('Helpen jullie ook met het melden van nepaccounts?', 'Ja, we helpen met het melden van nep-, imitatie- en intimiderende accounts via de officiële meldtools van het platform. Zie <a href="@@fake@@">nepaccount melden</a>.'),
 ('Kunnen jullie een gebruikersnaam voor me claimen?', 'We helpen bij verzoeken om een inactieve of bezette gebruikersnaam via de officiële processen van het platform, bijvoorbeeld bij een merkrecht- of imitatiemelding. Het platform beslist. Zie <a href="@@user@@">gebruikersnaam claimen</a>.'),
 ('Wat als een gebruikersnaam-verzoek mislukt?', 'Dan krijg je 100% van je geld terug. Dit geldt alleen voor gebruikersnaam-verzoeken; zie het <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels).'),
 ('Hoe neem ik contact op?', 'Via WhatsApp of per e-mail naar team@unbanz.com. Support is voornamelijk in het Engels; een kort bericht met je gebruikersnaam, een screenshot en de datum is genoeg. Zie <a href="@@contact@@">contact</a>.'),
 ('Kan ik mijn Meta-advertentieaccount terugkrijgen?', 'We helpen bij beperkte of uitgeschakelde advertentieaccounts en Business Portfolio\'s via de officiële beoordelingsprocessen. Zie <a href="@@ad@@">advertentieaccount terugkrijgen</a>.'),
 ('Is het gratis om het zelf te proberen?', 'Ja. Bezwaar maken, het herstelformulier en meldingen zijn gratis. Probeer dat eerst als de officiële knop beschikbaar is.'),
]
C['faq'] = dict(
 title='Veelgestelde vragen over account terugkrijgen',
 desc='Antwoorden op de vragen die we het vaakst krijgen over uitgeschakelde, gehackte en geblokkeerde accounts, prijs, wachtwoord en de officiële routes.',
 nav='Veelgestelde vragen', crumb='Vragen', h1='Veelgestelde vragen.',
 lead='Korte, eerlijke antwoorden over Instagram-, Facebook- en Snapchat-accounts, onze werkwijze en wat je zelf gratis kunt doen.',
 items=FAQ_ALL, faq_h2='Goed om te weten.', related=['ig', 'fb', 'user', 'pricing', 'how', 'legit', 'contact'])

C['contact'] = dict(
 title='Contact: hulp bij je Instagram- of Facebook-account',
 desc='Neem contact op via WhatsApp of e-mail. Stuur je gebruikersnaam en een screenshot van de melding; support is voornamelijk in het Engels.',
 nav='Contact', eyebrow='CONTACT', h1='Vertel ons wat er is gebeurd.',
 p1='Kies wat je nodig hebt en we openen WhatsApp met een bericht dat al klaarstaat. Je kunt het nog aanpassen voordat je het verstuurt.',
 opts=[('Instagram-account terugkrijgen', 'Hoi Unbanz, ik wil mijn Instagram-account terugkrijgen.', 'unban'),
       ('Facebook-account terugkrijgen', 'Hoi Unbanz, ik wil mijn Facebook-account terugkrijgen.', 'unban'),
       ('Snapchat-account terugkrijgen', 'Hoi Unbanz, ik wil mijn Snapchat-account terugkrijgen.', 'unban'),
       ('Een account melden', 'Hoi Unbanz, ik wil een account laten melden.', 'ban'),
       ('Gebruikersnaam claimen', 'Hoi Unbanz, ik wil een gebruikersnaam claimen.', 'username'),
       ('Advertentieaccount', 'Hoi Unbanz, ik heb hulp nodig met een Meta-advertentieaccount.', 'ad')],
 mail_h2='Liever per e-mail?', mail_p='Schrijf naar team@unbanz.com en vermeld je gebruikersnaam of profiellink, een screenshot van de melding en de datum waarop het misging.',
 what_h2='Wat je mee kunt sturen', what_p='Je @gebruikersnaam of profiellink, een screenshot van de melding en de datum. Bij een advertentieaccount ook het account-ID. Stuur nooit een wachtwoord of inlogcode.',
 social_h2='Ook te vinden op', social_p='We zijn @unbanzhq op Instagram en X. Voor accountdetails kun je het best WhatsApp of e-mail gebruiken.',
 lang_h2='Taal', lang_p='Support is voornamelijk in het Engels. Een kort bericht met gebruikersnaam, screenshot en datum is genoeg om te beginnen.',
 note='Onafhankelijke dienst. Niet verbonden aan Meta. We vragen nooit om je wachtwoord.')

C['reviews'] = dict(
 title='Reviews: video\'s van klanten van Unbanz',
 desc='Video\'s van klanten die met Unbanz werkten: een gebruikersnaam-verzoek, een bureau en een beperkt advertentieaccount. In het Engels.',
 nav='Reviews', h1='Klanten aan het woord.',
 p='Drie klanten vertellen in hun eigen woorden hoe het werken met Unbanz ging. De video\'s en transcripten zijn in het Engels.',
 video_aria='Video-reviews van klanten', mail='Of stuur een e-mail', pick='Waar gaat het over?',
 pick_opts=[('Account terugkrijgen', 'Hoi Unbanz, ik wil mijn account terugkrijgen.', 'unban'), ('Gebruikersnaam', 'Hoi Unbanz, ik wil een gebruikersnaam claimen.', 'username'), ('Advertentieaccount', 'Hoi Unbanz, ik heb hulp nodig met een advertentieaccount.', 'ad')],
 q_h2='Vragen over deze reviews.',
 faq=[('Waar komen deze reviews vandaan?', 'Het zijn video\'s van klanten die met Unbanz hebben gewerkt. Je kunt ze hier zelf bekijken en het transcript lezen.'),
      ('In welke taal zijn de video\'s?', 'In het Engels. Onder elke video staat het transcript, ook in het Engels.'),
      ('Kan ik zelf een vraag stellen voordat ik beslis?', 'Ja. Stuur ons een bericht op WhatsApp of per e-mail. Vragen kost niets.')])

C['home'] = dict(
 title='Instagram account terugkrijgen? Hulp bij geblokkeerd account',
 desc='Instagram- of Facebook-account uitgeschakeld, opgeschort of gehackt? Stuur je gebruikersnaam en de melding: we bereiden het verzoek voor via de officiële routes.',
 skip='Naar de diensten', home_aria='Unbanz, naar boven',
 h1a='Instagram account', h1b='terugkrijgen.',
 hero_p='Uitgeschakeld, opgeschort of gehackt? Stuur ons je gebruikersnaam en de melding: wij bereiden het verzoek voor via de officiële routes van Instagram, Facebook en Snapchat.',
 intro_eyebrow='ACCOUNTS &amp; MELDINGEN', intro_h2='Account geblokkeerd? Stuur ons de details.',
 intro_p=('Unbanz (unbanz.com) is een onafhankelijke dienst voor Instagram, Facebook en Snapchat: bezwaar en herbeoordeling bij uitgeschakelde of vergrendelde accounts, het melden van nepaccounts via de officiële tools, '
          'gebruikersnaam-verzoeken en hulp bij Meta-advertentieaccounts. Je stuurt de gebruikersnaam en een screenshot van de melding, en we zeggen eerlijk of we kunnen helpen. '
          'Onafhankelijke dienst, niet verbonden aan Meta en niets te maken met Unbanx. Liever zelf beginnen? Lees eerst de gids <a href="@@appeal-denied@@">bezwaar maken bij Instagram</a>.'),
 exp_eyebrow='JOUW SITUATIE', exp_h2='Waar heb je hulp bij nodig?',
 rows=[('Instagram-account terugkrijgen', 'Uitgeschakeld, opgeschort of gehackt.', 'ig', 'unban'),
       ('Facebook-account', 'Uitgeschakelde of gehackte profielen, beperkte pagina\'s.', 'fb', 'unban'),
       ('Nepaccounts en imitatie', 'Melden via de officiële tools.', 'fake', 'ban'),
       ('Gebruikersnamen', 'Inactieve of bezette gebruikersnamen.', 'user', 'username'),
       ('Advertentieaccounts', 'Beperkte advertentieaccounts en Business Portfolio\'s.', 'ad', 'ad')],
 vt_eyebrow='KLANTEN', vt_h2='In hun eigen woorden.', vt_note='Video\'s en transcripten in het Engels.', vt_all='Alle reviews',
 pw_eyebrow='JOUW WACHTWOORD', pw_zero='wachtwoorden gevraagd', pw_note='Een gebruikersnaam en een screenshot zijn genoeg. We houden je de hele tijd op de hoogte.',
 how_eyebrow='HOE HET WERKT', how_h2='Stuur de details. Wij regelen de rest.',
 steps=['Stuur je gebruikersnaam en de melding.', 'Hoor de prijs, voordat het werk begint.', 'Wij dienen het verzoek in via het officiële proces.'], how_link='Hoe het werkt',
 pr_eyebrow='PRIJS', pr_h2='De prijs, voordat het werk begint.',
 pr_p='De prijs hangt af van het account, de situatie en het werk dat nodig is. We noemen die in het gesprek, nadat je hebt uitgelegd wat er is gebeurd. Vragen kost niets.',
 pr_cta='Vraag een prijs',
 pr_notes=[('Eerst de prijs', 'Je weet het voordat het werk begint.'), ('Officiële routes', 'Bezwaren en meldingen, zonder omwegen.'), ('Zonder wachtwoord', 'Je wachtwoord blijft bij jou.')],
 pr_link='Prijs en wat die bepaalt',
 faq_eyebrow='KORTE ANTWOORDEN', faq_h2='Voordat je ons schrijft.',
 faq=[('Mijn Instagram-account is uitgeschakeld. Wat nu?', 'Log in, open de melding en maak één keer bezwaar; meestal kan dat ongeveer 180 dagen. Maak een screenshot. Zie de <a href="@@ig-disabled@@">gids</a>.'),
      ('Is Unbanz betrouwbaar?', 'Unbanz is een onafhankelijke dienst: één website, één e-mailadres, schriftelijke voorwaarden en video-reviews van klanten. We vragen nooit om je wachtwoord. Zie <a href="@@legit@@">Is Unbanz betrouwbaar?</a>'),
      ('Wat kost het?', 'Dat hangt af van het account en de situatie. Je hoort de prijs in het gesprek, voordat het werk begint. Vragen kost niets.'),
      ('Heb je mijn wachtwoord nodig?', 'Nee. Een gebruikersnaam en een screenshot van de melding zijn genoeg.'),
      ('Praten jullie ook Nederlands?', 'Support is voornamelijk in het Engels. Een kort bericht met je gebruikersnaam, screenshot en datum is genoeg om te beginnen.'),
      ('Kan ik een inactieve gebruikersnaam claimen?', 'Dat kan soms, via de officiële processen van het platform. Het platform beslist. Mislukt een gebruikersnaam-verzoek, dan krijg je 100% van je geld terug. Zie <a href="@@user@@">gebruikersnaam claimen</a>.')],
 cl_eyebrow='CONTACT', cl_h2='Vertel ons wat er is gebeurd.',
 cl_p='Support is voornamelijk in het Engels. Je gebruikersnaam, een screenshot en de datum zijn genoeg om te beginnen.')

def make():
    site = Site(S, SLUGS)
    core.home_page(site, C); core.services_page(site, C); core.faq_page(site, C); core.contact_page(site, C); core.reviews_page(site, C)
    nl_services.add(site); nl_guides.add(site)
    return site
