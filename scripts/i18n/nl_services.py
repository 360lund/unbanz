# -*- coding: utf-8 -*-
from lib import *

OFF = 'Support is voornamelijk in het Engels.'

def add(site):
    sv = site.service
    # ---------- Instagram
    sv('ig', 'Instagram account terugkrijgen na uitschakeling of hack', 'Instagram-account terugkrijgen',
       'Instagram account terugkrijgen: uitgeschakeld, opgeschort of gehackt.',
       'Is je Instagram-account uitgeschakeld, opgeschort of gehackt? Stuur ons je gebruikersnaam en een screenshot van de melding: we bereiden het bezwaar voor en dienen het in via het officiële proces van Instagram. Je wachtwoord blijft bij jou. Er zijn video-reviews van klanten beschikbaar.',
       'Unbanz helpt bij het terugkrijgen van uitgeschakelde, opgeschorte, vergrendelde of gehackte Instagram-accounts, altijd via de officiële routes van het platform. Je hoort de prijs in het gesprek, nadat je je situatie hebt uitgelegd en voordat het werk begint.',
       [('Uitgeschakeld of opgeschort', 'Persoonlijke, creator- en zakelijke profielen die Instagram heeft beperkt of offline heeft gehaald. Vertel ons wat het inlogscherm laat zien en wanneer het gebeurde.'),
        ('Gehackt of toegang kwijt', 'E-mailadres en telefoonnummer gewijzigd, gebruikersnaam gestolen, een verificatielus die nergens heen leidt: we helpen je weer binnen te komen en het account daarna te beveiligen.'),
        ('Het account dat je hebt opgebouwd', 'Je foto\'s, berichten en volgers tellen. Wij kennen de officiële stappen en weten hoe je een verzoek duidelijk indient.')],
       [('1. Stuur de gegevens', 'Je @gebruikersnaam of profiellink, een screenshot van de melding en de datum waarop je geen toegang meer had.'),
        ('2. Wij noemen de prijs', 'Na jouw uitleg zeggen we of we kunnen helpen en wat het kost, voordat het werk begint. Beheert iemand anders het account, vertel ons dan wie bevoegd is.'),
        ('3. Wij dienen het verzoek in', 'We bereiden het verzoek voor en dienen het in via het officiële proces van Instagram. Daarna houden we je op de hoogte van de reacties.')],
       [('Is mijn uitgeschakelde Instagram-account voorgoed weg?', 'Niet per se. Toont Instagram een optie om bezwaar te maken, dan kan dat meestal ongeveer 180 dagen. Stuur ons de exacte melding, dan zeggen we eerlijk wat mogelijk is.'),
        ('Kan ik een gehackt account terugkrijgen als het e-mailadres is gewijzigd?', 'Vaak wel, via de officiële hulpmiddelen van Instagram (instagram.com/hacked en de videoselfie-verificatie). Vertel ons waar je nog bij kunt, dan wijzen we je de weg.'),
        ('Helpen jullie ook met kleine accounts?', 'Ja. Persoonlijke, creator- en zakelijke accounts: het aantal volgers maakt voor onze hulp niet uit.'),
        ('Moet ik mijn wachtwoord geven?', 'Nee. We beginnen met de profiellink en de melding. Je wachtwoord en inlogcodes blijven bij jou.'),
        ('Wat kost het om een Instagram-account terug te krijgen?', 'De prijs hangt af van het account en de situatie. We noemen die in het gesprek, nadat je hebt uitgelegd wat er is gebeurd en voordat het werk begint. Vragen kost niets.'),
        ('Hoe lang duurt het om een Instagram-account terug te krijgen?', 'Instagram publiceert geen behandeltijd: het varieert van een paar dagen tot enkele weken. We kunnen geen datum beloven, maar houden je op de hoogte.')],
       ['ig-disabled', 'appeal-time', 'ig-hacked', 'no-button', 'appeal-denied', 'deleted', 'blocked', 'support'],
       meta('Instagram-account terugkrijgen', 'Account terugkrijgen', 'Hulp bij uitgeschakelde, opgeschorte of gehackte Instagram-accounts via de officiële routes van het platform.'),
       desc='Instagram-account uitgeschakeld, opgeschort of gehackt? Stuur je gebruikersnaam en de melding; wij bereiden het bezwaar voor via het officiële proces.')

    # ---------- Facebook
    sv('fb', 'Facebook account terugkrijgen: uitgeschakeld of gehackt', 'Facebook-account terugkrijgen',
       'Facebook account terugkrijgen: uitgeschakeld, gehackt of beperkt.',
       'Is je Facebook-profiel uitgeschakeld, gehackt of je pagina beperkt? Stuur ons de profiellink en een screenshot van de melding: we bereiden het verzoek voor en dienen het in via het officiële proces van Facebook. Je wachtwoord blijft bij jou.',
       'Unbanz helpt bij uitgeschakelde en gehackte Facebook-profielen en bij beperkte Facebook-pagina\'s, via de officiële routes van het platform. De prijs hoor je in het gesprek, voordat het werk begint.',
       [('Profiel uitgeschakeld', 'Facebook zegt dat je account is uitgeschakeld of beperkt. Stuur ons de melding en de datum, dan bekijken we welke officiële route past.'),
        ('Gehackt profiel', 'Wachtwoord, e-mailadres of naam gewijzigd en je komt er niet meer in: we helpen je het herstel via de officiële hulpmiddelen aan te pakken.'),
        ('Beperkte pagina', 'Een pagina die niet meer gepubliceerd is of beperkt is gemaakt. Wij helpen bij het duidelijk indienen van de beoordelingsaanvraag.')],
       [('1. Stuur de gegevens', 'De profiel- of paginalink, een screenshot van de melding en de datum.'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of we kunnen helpen en wat het kost, voordat het werk begint.'),
        ('3. Wij dienen het verzoek in', 'We dienen de beoordelingsaanvraag in via het officiële proces van Facebook en houden je op de hoogte.')],
       [('Is een uitgeschakeld Facebook-account definitief?', 'Niet altijd. Toont Facebook een knop om beoordeling aan te vragen, gebruik die dan binnen de aangegeven termijn. Stuur ons de melding en we zeggen eerlijk wat mogelijk is.'),
        ('Kan ik een gehackt Facebook-account terugkrijgen?', 'Vaak wel, via facebook.com/hacked en de officiële herstelstappen. Vertel ons waar je nog bij kunt.'),
        ('Helpen jullie ook met een zakelijke pagina?', 'Ja, we helpen bij beperkte pagina\'s en bij advertentieaccounts die daaraan gekoppeld zijn.'),
        ('Moet ik mijn wachtwoord delen?', 'Nee. Een profiellink en een screenshot van de melding zijn genoeg.'),
        ('Wat kost het?', 'Dat hangt af van het account en de situatie. We noemen de prijs in het gesprek, voordat het werk begint. Vragen kost niets.')],
       ['fb-appeal', 'fb-hacked', 'ad-disabled', 'appeal-time'],
       meta('Facebook-account terugkrijgen', 'Account terugkrijgen', 'Hulp bij uitgeschakelde of gehackte Facebook-accounts en beperkte pagina\'s via de officiële routes.'),
       desc='Facebook-profiel uitgeschakeld, gehackt of pagina beperkt? Stuur de link en de melding; wij dienen het verzoek in via het officiële proces van Facebook.')

    # ---------- Ad accounts
    sv('ad', 'Facebook-advertentieaccount terugkrijgen: beperkt of uit', 'Advertentieaccount terugkrijgen',
       'Meta-advertentieaccount terugkrijgen: beperkt of uitgeschakeld.',
       'Is je Facebook- of Instagram-advertentieaccount beperkt of uitgeschakeld en kun je geen advertenties meer draaien? Stuur ons het account-ID en de melding: we bereiden de beoordelingsaanvraag voor en dienen die in via de officiële processen van Meta.',
       'Unbanz helpt bedrijven en bureaus met beperkte of uitgeschakelde Meta-advertentieaccounts en Business Portfolio\'s. Alles loopt via de officiële beoordelingsroutes; Meta beslist altijd zelf. De prijs hoor je in het gesprek, voordat het werk begint.',
       [('Advertentieaccount beperkt', 'Advertenties staan stil of je betaalmethode werkt niet meer. We kijken met je naar de melding en de reden die Meta noemt.'),
        ('Business Portfolio beperkt', 'Beperkingen op het Business Portfolio raken vaak meerdere accounts tegelijk. Stuur ons de details, dan zeggen we wat we kunnen doen.'),
        ('Voor bureaus', 'Beheer je advertentieaccounts voor klanten? We helpen ook als er meerdere accounts tegelijk geraakt zijn.')],
       [('1. Stuur de gegevens', 'Het account-ID, een screenshot van de melding en de datum waarop de advertenties stopten.'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of we kunnen helpen en wat het kost, voordat het werk begint.'),
        ('3. Wij dienen de aanvraag in', 'We bereiden de beoordelingsaanvraag voor en dienen die in via het officiële proces van Meta. Daarna houden we je op de hoogte.')],
       [('Kunnen jullie een uitgeschakeld advertentieaccount terugkrijgen?', 'Dat hangt van de reden en de melding af. We bekijken die en zeggen eerlijk of een beoordelingsaanvraag zinvol is. Meta beslist altijd zelf.'),
        ('Wat heb je van mij nodig?', 'Het account-ID, een screenshot van de melding en de datum. Nooit je wachtwoord of inlogcodes.'),
        ('Helpen jullie ook bureaus?', 'Ja. Bureaus en bedrijven met meerdere advertentieaccounts zijn welkom.'),
        ('Wat kost het?', 'Dat hangt af van het aantal accounts en de situatie. De prijs hoor je in het gesprek, voordat het werk begint.'),
        ('Hoe lang duurt het?', 'Meta publiceert geen behandeltijd. Het kan variëren van enkele dagen tot weken; we beloven geen datum.')],
       ['ad-disabled', 'fb-appeal', 'appeal-denied'],
       meta('Advertentieaccount terugkrijgen', 'Account terugkrijgen', 'Hulp bij beperkte of uitgeschakelde Meta-advertentieaccounts en Business Portfolio\'s.'),
       desc='Meta-advertentieaccount beperkt of uitgeschakeld? Stuur het account-ID en de melding; wij dienen de beoordelingsaanvraag in via de officiële processen.', svc='ad')

    # ---------- Snapchat
    sv('snap', 'Snapchat account terugkrijgen: vergrendeld of uit', 'Snapchat-account terugkrijgen',
       'Snapchat account terugkrijgen: vergrendeld of uitgeschakeld.',
       'Is je Snapchat-account vergrendeld of uitgeschakeld? Stuur ons je gebruikersnaam en een screenshot van de melding: we bereiden het verzoek voor en dienen het in via het officiële proces van Snapchat. Je wachtwoord blijft bij jou.',
       'Unbanz helpt bij vergrendelde en uitgeschakelde Snapchat-accounts via de officiële ondersteuningsroutes van Snapchat. De prijs hoor je in het gesprek, voordat het werk begint.',
       [('Tijdelijk vergrendeld', 'Snapchat heeft je account vergrendeld na ongebruikelijke activiteit. Vertel ons wat de melding zegt en wanneer het gebeurde.'),
        ('Uitgeschakeld', 'Een melding dat je account is uitgeschakeld. We bekijken welke officiële route daarvoor bestaat.'),
        ('Gehackt', 'Gebruikersnaam of e-mailadres gewijzigd? We helpen je de officiële herstelstappen te volgen.')],
       [('1. Stuur de gegevens', 'Je gebruikersnaam, een screenshot van de melding en de datum.'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of we kunnen helpen en wat het kost, voordat het werk begint.'),
        ('3. Wij dienen het verzoek in', 'We dienen het verzoek in via het officiële proces van Snapchat en houden je op de hoogte.')],
       [('Hoe lang blijft een Snapchat-account vergrendeld?', 'Snapchat publiceert geen vaste termijn en de melding zelf noemt vaak geen datum. Wij kunnen geen datum beloven.'),
        ('Kan een permanent uitgeschakeld Snapchat-account terugkomen?', 'Soms, via het officiële bezwaarformulier. Snapchat beslist. Stuur ons de melding en we zeggen eerlijk wat mogelijk is.'),
        ('Moet ik mijn wachtwoord delen?', 'Nee. Een gebruikersnaam en een screenshot van de melding zijn genoeg.'),
        ('Wat kost het?', 'De prijs hoor je in het gesprek, voordat het werk begint. Vragen kost niets.')],
       ['appeal-time', 'ig-hacked'],
       meta('Snapchat-account terugkrijgen', 'Account terugkrijgen', 'Hulp bij vergrendelde of uitgeschakelde Snapchat-accounts via de officiële routes.'),
       desc='Snapchat-account vergrendeld of uitgeschakeld? Stuur je gebruikersnaam en de melding; wij dienen het verzoek in via het officiële proces van Snapchat.')

    # ---------- fake accounts
    sv('fake', 'Nepaccount melden op Instagram, Facebook en Snapchat', 'Nepaccounts melden',
       'Nepaccount melden: nepprofielen laten verwijderen.',
       'Gebruikt iemand een nepaccount om zich voor te doen als jij, om te intimideren of om mensen op te lichten? Stuur ons de profiellink en de details: we helpen het account te melden via de officiële meldtools van Instagram, Facebook of Snapchat.',
       'Unbanz helpt bij het melden van nepaccounts, oplichtersprofielen en accounts die de regels overtreden, uitsluitend via de officiële meldtools van het platform. Het platform beslist zelf of een account wordt verwijderd.',
       [('Nepprofielen', 'Profielen met gestolen foto\'s of een verzonnen identiteit. We verzamelen wat nodig is voor een duidelijke melding.'),
        ('Oplichting', 'Accounts die geld vragen, valse aanbiedingen doen of mensen proberen te misleiden. Meld ze via de officiële tools; doe zo nodig ook aangifte bij de politie.'),
        ('Voor merken en bedrijven', 'Een nepaccount dat je klanten misleidt? We helpen je de melding goed voor te bereiden.')],
       [('1. Stuur de gegevens', 'De link naar het account, screenshots van wat het doet en, als het over jou gaat, een bewijs van jouw identiteit of merk.'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of we kunnen helpen en wat het kost, voordat het werk begint.'),
        ('3. Wij melden het account', 'We dienen de melding in via de officiële meldtools van het platform en houden je op de hoogte.')],
       [('Kunnen jullie een nepaccount laten verwijderen?', 'Wij melden het account via de officiële tools en bereiden die melding zorgvuldig voor. Of het account wordt verwijderd, beslist het platform.'),
        ('Wat als iemand mijn foto\'s gebruikt?', 'Dat kun je melden als imitatie. Zie onze gids over een nepaccount met jouw foto\'s.'),
        ('Gebruiken jullie valse of massale meldingen?', 'Nooit. We gebruiken alleen echte meldingen via de officiële tools.'),
        ('Wat kost het?', 'De prijs hoor je in het gesprek, voordat het werk begint. Vragen kost niets.')],
       ['report-fake', 'scams', 'sextortion'],
       meta('Nepaccounts melden', 'Account melden', 'Hulp bij het melden van nep- en oplichtersaccounts via de officiële meldtools van het platform.'),
       desc='Nepaccount of oplichtersprofiel? Wij helpen het te melden via de officiële meldtools van Instagram, Facebook en Snapchat.', svc='ban')

    # ---------- impersonation
    sv('imp', 'Imitatieaccount melden: iemand geeft zich voor mij uit', 'Imitatieaccounts melden',
       'Imitatieaccount melden: iemand geeft zich voor jou uit.',
       'Geeft iemand zich op Instagram, Facebook of Snapchat voor jou of je bedrijf uit? Stuur ons de profiellink en bewijs van wie je bent: we helpen een duidelijke imitatiemelding in te dienen via de officiële tools.',
       'Unbanz helpt bij het melden van accounts die zich voordoen als een persoon of bedrijf, via de officiële imitatie-meldroutes van het platform. Het platform beslist zelf.',
       [('Iemand gebruikt jouw naam', 'Een profiel met jouw naam en foto\'s dat je volgers of klanten benadert. Verzamel de links en screenshots; wij helpen met de melding.'),
        ('Iemand imiteert je bedrijf', 'Een account dat zich voordoet als jouw merk. We helpen je de melding met de juiste gegevens in te dienen.'),
        ('Je hebt bewijs nodig', 'Een identiteitsbewijs of bedrijfsgegevens zijn vaak nodig. We vertellen je wat het platform vraagt, zonder dat je gevoelige gegevens onnodig rondstuurt.')],
       [('1. Stuur de gegevens', 'De link naar het account, screenshots en een korte uitleg van hoe het zich voordoet als jij.'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of we kunnen helpen en wat het kost, voordat het werk begint.'),
        ('3. Wij melden het account', 'We dienen de imitatiemelding in via het officiële proces en houden je op de hoogte.')],
       [('Hoe meld ik een account dat zich voor mij uitgeeft?', 'Via het officiële meldformulier voor imitatie van het platform. Wij helpen met het voorbereiden ervan. Het platform beslist.'),
        ('Heb ik een identiteitsbewijs nodig?', 'Soms vraagt het platform daarom. We vertellen je vooraf wat nodig is.'),
        ('Wat kost het?', 'De prijs hoor je in het gesprek, voordat het werk begint. Vragen kost niets.')],
       ['report-fake', 'scams'],
       meta('Imitatieaccounts melden', 'Account melden', 'Hulp bij het melden van accounts die zich voordoen als een persoon of bedrijf, via de officiële tools.'),
       desc='Geeft iemand zich voor jou of je bedrijf uit? Wij helpen de imitatie te melden via de officiële meldtools van het platform.', svc='ban')

    # ---------- harassment
    sv('har', 'Intimiderend account melden op Instagram en Facebook', 'Intimidatie melden',
       'Intimiderend account melden: pesten, bedreigen, lastigvallen.',
       'Wordt je lastiggevallen of bedreigd door een account op Instagram, Facebook of Snapchat? Stuur ons de links en screenshots: we helpen het account te melden via de officiële meldtools. Is er direct gevaar, bel dan eerst 112.',
       'Unbanz helpt bij het melden van accounts die intimideren, bedreigen of lastigvallen, via de officiële meldtools van het platform. Het platform beslist zelf. Bij bedreiging kun je ook aangifte doen bij de politie.',
       [('Pesten en intimidatie', 'Herhaalde berichten, bedreigingen of het delen van je gegevens. Bewaar screenshots met datum en tijd.'),
        ('Wat je zelf direct kunt doen', 'Blokkeer het account, beperk wie je kan berichten en meld de berichten in de app. Verwijder niets voordat je bewijs hebt bewaard.'),
        ('Wanneer je extra hulp zoekt', 'Gaat het door of word je bedreigd, doe dan aangifte bij de politie (politie.nl) en vraag ons het account te laten melden.')],
       [('1. Stuur de gegevens', 'De links naar de accounts, screenshots met datum en een korte uitleg.'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of we kunnen helpen en wat het kost, voordat het werk begint.'),
        ('3. Wij melden het account', 'We dienen de melding in via de officiële tools en houden je op de hoogte.')],
       [('Kunnen jullie een intimiderend account laten blokkeren?', 'Wij melden het via de officiële tools; het platform beslist of het account wordt verwijderd of beperkt.'),
        ('Moet ik ook aangifte doen?', 'Bij bedreiging, chantage of stalking is aangifte bij de politie verstandig. Bewaar je bewijs.'),
        ('Wat kost het?', 'De prijs hoor je in het gesprek, voordat het werk begint. Vragen kost niets.')],
       ['sextortion', 'report-fake', 'scams'],
       meta('Intimidatie melden', 'Account melden', 'Hulp bij het melden van accounts die intimideren of lastigvallen via de officiële meldtools.'),
       desc='Word je lastiggevallen of bedreigd door een account? Wij helpen het te melden via de officiële tools. Bij direct gevaar: bel 112.', svc='ban')

    # ---------- username
    refund = ('<section class="service-price container"><h2>Refund policy<br>voor gebruikersnamen.</h2><div><p>Mislukt een gebruikersnaam-verzoek, dan krijg je 100% van je geld terug. '
              'Dit geldt alleen voor gebruikersnaam-verzoeken.</p>'
              '<a href="/refund-policy/" hreflang="en" lang="en">Lees het refund policy (in het Engels) ↗︎</a></div></section>')
    sv('user', 'Instagram gebruikersnaam claimen: inactief of bezet', 'Gebruikersnaam claimen',
       'Instagram-gebruikersnaam claimen: inactief of al bezet.',
       'Wil je een Instagram-gebruikersnaam die bezet of van een inactief account is? Stuur ons de gewenste naam en je profiel: we bekijken welke officiële route past en dienen het verzoek in. Mislukt het verzoek, dan krijg je 100% van je geld terug.',
       'Unbanz helpt bij gebruikersnaam-verzoeken op Instagram, Facebook en Snapchat via de officiële processen van het platform, zoals een merkrechtmelding, een imitatiemelding of de route voor een inactief account. Het platform beslist zelf. Wij kopen of verkopen nooit accounts.',
       [('Inactieve gebruikersnaam', 'Het account lijkt verlaten? Dan bestaat soms een officiële route. We bekijken of die voor jouw gebruikersnaam past.'),
        ('Merk of bedrijfsnaam', 'Is de gebruikersnaam jouw geregistreerde merk of bedrijfsnaam, dan is een merkrechtmelding soms de juiste route.'),
        ('Imitatie', 'Gebruikt iemand je naam om je volgers of klanten te misleiden, dan kan een imitatiemelding passen.')],
       [('1. Stuur de gegevens', 'De gewenste gebruikersnaam, je huidige profiel en waarom de naam bij jou hoort (bijvoorbeeld je merk).'),
        ('2. Wij noemen de prijs', 'We zeggen eerlijk of een verzoek kansrijk is en wat het kost, voordat het werk begint. Het platform beslist altijd zelf.'),
        ('3. Wij dienen het verzoek in', 'We gebruiken het officiële proces dat bij de gebruikersnaam past en houden je op de hoogte.')],
       [('Kan ik iemands gebruikersnaam gewoon overnemen?', 'Nee. Er is geen knop om een gebruikersnaam te kopen of over te nemen. Er zijn alleen officiële processen die per situatie verschillen, en het platform beslist.'),
        ('Verkopen jullie gebruikersnamen of accounts?', 'Nooit. We kopen, verkopen of nemen geen accounts over. We gebruiken alleen de officiële routes van het platform.'),
        ('Wat als mijn verzoek mislukt?', 'Dan krijg je 100% van je geld terug. Dit geldt alleen voor gebruikersnaam-verzoeken. Zie het <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels).'),
        ('Wat kost het?', 'De prijs hangt af van de gebruikersnaam en de route. Je hoort die in het gesprek, voordat het werk begint. Vragen kost niets.'),
        ('Wie beslist uiteindelijk?', 'Het platform. Wij bereiden het verzoek voor en dienen het in; wij kunnen niet beslissen of namens het platform iets toezeggen.'),
        ('Kunnen gewone mensen een gebruikersnaam claimen?', 'Ja, het is niet voorbehouden aan bedrijven. De route hangt af van de situatie: een inactief account, een merk of imitatie.')],
       ['inactive-user', 'pricing'],
       meta('Gebruikersnaam claimen', 'Gebruikersnaam-verzoek', 'Hulp bij het claimen van inactieve of bezette gebruikersnamen via de officiële processen van het platform.'),
       desc='Instagram-gebruikersnaam bezet of inactief? Wij helpen het verzoek in te dienen via het officiële proces. Mislukt het, dan krijg je 100% terug.', svc='username', extra=refund)
