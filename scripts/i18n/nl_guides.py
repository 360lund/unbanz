# -*- coding: utf-8 -*-
from lib import *

def P(*t):
    return ''.join('<p>%s</p>' % x for x in t)
def UL(*t):
    return '<ul>' + ''.join('<li>%s</li>' % x for x in t) + '</ul>'
def OL(*t):
    return '<ol>' + ''.join('<li>%s</li>' % x for x in t) + '</ol>'

HELP_IG = P('Lukt het niet met de officiële knop, of heb je liever hulp? Stuur ons je gebruikersnaam, een screenshot van de melding en de datum. We zeggen eerlijk of we kunnen helpen en noemen de prijs in het gesprek, voordat het werk begint. Vragen kost niets. Support is voornamelijk in het Engels.')
HELP_FB = P('Stuur ons de profiellink, een screenshot van de melding en de datum. We zeggen eerlijk of we kunnen helpen en noemen de prijs in het gesprek, voordat het werk begint. Support is voornamelijk in het Engels.')
HELP_AD = P('Stuur ons het account-ID, een screenshot van de melding en de datum. We zeggen eerlijk of we kunnen helpen en noemen de prijs in het gesprek, voordat het werk begint. Support is voornamelijk in het Engels.')
HELP_REP = P('Stuur ons de links naar de accounts en screenshots. We helpen een duidelijke melding voor te bereiden en in te dienen via de officiële tools; het platform beslist. De prijs hoor je in het gesprek, voordat het werk begint. Support is voornamelijk in het Engels.')

def add(site):
    g = site.guide
    S = site.S

    # ================= core trust pages =================
    site.reg('pricing', 'guide', 'Prijs: wat kost het om een account terug te krijgen?',
             'Wat kost hulp bij een Instagram- of Facebook-account? De prijs hangt af van het account en de situatie en je hoort die in het gesprek, voordat het werk begint.', 'Prijs')
    site.build['pricing'] = lambda: site.guide_page('pricing',
        'Wat kost het om een Instagram- of Facebook-account terug te krijgen?',
        'De prijs hangt af van het account, het platform en het werk dat nodig is. Bij Unbanz noemen we die in het gesprek, nadat je je situatie hebt uitgelegd en voordat het werk begint; vragen kost niets. Meta publiceert geen behandeltijden en wij kunnen er geen beloven.',
        [('prijs', 'Wat de prijs bepaalt', UL('Het platform: Instagram, Facebook, Snapchat of een Meta-advertentieaccount.',
                                              'Het soort situatie: uitgeschakeld, opgeschort, gehackt, een nepaccount melden of een gebruikersnaam-verzoek.',
                                              'Het aantal accounts of meldingen.',
                                              'Het werk dat nodig is: bewijsstukken, controles en opvolging.') + P('Een prijs zonder dat iemand je situatie kent, is niets waard. Daarom vragen we eerst wat er is gebeurd.')),
         ('nodig', 'Wat we nodig hebben om te antwoorden', P('Je gebruikersnaam of profiellink, een screenshot van de melding en de datum. Bij een advertentieaccount het account-ID. Nooit een wachtwoord of code.')),
         ('gratis', 'De officiële stappen zijn gratis', P('Bezwaar maken tegen een uitschakeling, het herstelformulier voor gehackte accounts en het melden van een account kosten niets: het zijn officiële stappen die je zelf kunt zetten. Wij helpen als ze vastlopen, als de melding onduidelijk is of als je het liever uit handen geeft. Lees eerst de gids <a href="@@appeal-denied@@">bezwaar afgewezen</a>.')),
         ('refund', 'Gebruikersnaam-verzoek: refund policy', P('Mislukt een gebruikersnaam-verzoek, dan krijg je 100% van je geld terug. Dit geldt alleen voor gebruikersnaam-verzoeken. Zie het <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels).')),
         ('tijd', 'En hoe lang duurt het?', P('Meta en Snapchat publiceren geen behandeltijd. Afhankelijk van de situatie kan een antwoord na enkele dagen komen of na meerdere weken. We beloven geen datum, maar houden je op de hoogte. Zie <a href="@@appeal-time@@">hoe lang een Instagram-bezwaar duurt</a>.')),
         ('waarschuwing', 'Waarschuwingssignalen bij prijzen', UL('Een prijs zonder vragen over jouw situatie.', 'Een dienst die jou als eerste benadert.', 'Een verzoek om je wachtwoord, een code of toegang tot je e-mail.', 'Een belofte van een zeker resultaat.') + P('Zie ook <a href="@@scams@@">oplichting bij account herstel</a>.'))],
        [('Wat kost hulp bij een Instagram-account?', 'Dat hangt af van het account en de situatie. We noemen de prijs in het gesprek, nadat je hebt uitgelegd wat er is gebeurd en voordat het werk begint.'),
         ('Kost een prijsopgave iets?', 'Nee. Vragen kost niets en verplicht tot niets.'),
         ('Hoe lang duurt het om een account terug te krijgen?', 'Meta publiceert geen behandeltijd. Het varieert van enkele dagen tot meerdere weken. We kunnen geen datum beloven.'),
         ('Kan ik het gratis zelf doen?', 'Ja, de officiële stappen (bezwaar, herstelformulier, melding) zijn gratis. Onze hulp is voor wie het liever uitbesteedt of waarvan het verzoek vastloopt.'),
         ('Moet ik mijn wachtwoord sturen voor een prijs?', 'Nee. Een gebruikersnaam en een screenshot zijn genoeg. Deel nooit je wachtwoord of codes.'),
         ('Wat als mijn gebruikersnaam-verzoek mislukt?', 'Dan krijg je 100% van je geld terug. Dit geldt alleen voor gebruikersnaam-verzoeken; zie het <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels).')],
        ['ig', 'fb', 'user', 'appeal-time', 'how', 'legit'], HELP_IG, crumb_label=S['crumb_services'], std=False)

    g('how', 'Hoe het werkt: account terugkrijgen met Unbanz', 'Hoe het werkt', 'Hoe het werkt.',
      'Je stuurt ons je gebruikersnaam en een screenshot van de melding. Wij zeggen eerlijk of we kunnen helpen, noemen de prijs voordat het werk begint en dienen het verzoek in via het officiële proces van het platform.',
      [('stappen', 'De stappen', OL('Stuur ons je gebruikersnaam of profiellink, een screenshot van de melding en de datum, via WhatsApp of e-mail.',
                                    'Wij bekijken de situatie en zeggen eerlijk of we kunnen helpen. De prijs hoor je in het gesprek, voordat het werk begint.',
                                    'Zeg je ja, dan bereiden we het verzoek voor en dienen het in via het officiële proces: een bezwaar bij een uitschakeling, het herstelformulier bij een hack, de meldtools bij een nepaccount.',
                                    'We houden je op de hoogte van de reacties. Het platform beslist altijd zelf.')),
       ('routes', 'De officiële routes die we gebruiken', P('Bezwaren lopen via de officiële beroeps- en beoordelingsprocessen. Nep-, imitatie- en oplichtersaccounts melden we via de eigen meldtools van het platform. Gebruikersnaam-verzoeken gebruiken de officiële route die bij de gebruikersnaam past: een merkrechtmelding, een imitatiemelding of de route voor een inactief account.')),
       ('nooit', 'Wat we nooit doen', UL('We vragen nooit om je wachtwoord of inlogcodes.', 'We kopen, verkopen of nemen nooit accounts over.', 'We gebruiken geen bots, sniping-tools of valse meldingen.', 'We doen ons niet voor als iemand bij Meta.')),
       ('taal', 'Taal en contact', P('Support is voornamelijk in het Engels. Een kort bericht met je gebruikersnaam, screenshot en datum is genoeg om te beginnen.'))],
      [('Hoe begin ik?', 'Stuur ons een bericht op WhatsApp of per e-mail met je gebruikersnaam, een screenshot van de melding en de datum.'),
       ('Wanneer hoor ik de prijs?', 'In het gesprek, nadat je je situatie hebt uitgelegd en voordat het werk begint.'),
       ('Heb ik een wachtwoord nodig?', 'Nee. We vragen er nooit om.'),
       ('Beslissen jullie of mijn account terugkomt?', 'Nee. Het platform beslist altijd zelf. Wij bereiden het verzoek voor en dienen het in.'),
       ('Praten jullie Nederlands?', 'Support is voornamelijk in het Engels. Een kort bericht is genoeg om te beginnen.')],
      ['ig', 'fb', 'user', 'pricing', 'legit', 'faq'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Zo werkt Unbanz: je stuurt je gebruikersnaam en de melding, hoort de prijs voordat het werk begint en wij dienen het verzoek in via de officiële routes.')

    g('legit', 'Is Unbanz betrouwbaar? Dit moet je weten', 'Is Unbanz betrouwbaar?', 'Is Unbanz betrouwbaar?',
      'Unbanz is een onafhankelijke dienst met één website, één e-mailadres, schriftelijke voorwaarden en video-reviews van klanten. We vragen nooit om je wachtwoord, we noemen de prijs voordat het werk begint en we gebruiken alleen de officiële routes van het platform.',
      [('feiten', 'Feiten die je zelf kunt controleren', UL('Eén website (unbanz.com), één e-mailadres (team@unbanz.com) en één WhatsApp-nummer.', 'Schriftelijke <a href="/terms/" hreflang="en" lang="en">voorwaarden</a> en een <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a>.', 'Video-reviews van klanten, met transcript, op de pagina <a href="@@reviews@@">Reviews</a>.', 'Je betaalt niets voor een prijsopgave.')),
       ('niet', 'Wat Unbanz niet is', P('Unbanz is niet verbonden aan Meta of Snapchat en heeft geen speciale toegang tot hun medewerkers. Unbanz is ook niet Unbanx of unbanx.me; beoordelingen van Unbanx gaan niet over ons.')),
       ('routes', 'Hoe we werken', P('Alles loopt via de officiële routes van het platform: bezwaarformulieren, herstelformulieren en meldtools. Het platform beslist altijd zelf. Wij beloven daarom nooit een uitkomst.')),
       ('veilig', 'Zo herken je een betrouwbare dienst', UL('Ze vragen nooit om je wachtwoord of inlogcodes.', 'Ze noemen de prijs voordat het werk begint.', 'Ze leggen uit welke officiële route ze gebruiken.', 'Ze doen geen uitspraken over een contact bij Meta.') + P('Meer in <a href="@@scams@@">oplichting bij account herstel</a>.'))],
      [('Is Unbanz verbonden aan Meta?', 'Nee. Unbanz is een onafhankelijke dienst en gebruikt dezelfde officiële routes als jij.'),
       ('Is Unbanz hetzelfde als Unbanx?', 'Nee. Unbanz (met een z) is de dienst op unbanz.com. Unbanx of unbanx.me is iets anders.'),
       ('Vragen jullie om mijn wachtwoord?', 'Nooit. Een gebruikersnaam en een screenshot zijn genoeg.'),
       ('Waar kan ik reviews zien?', 'Op de pagina <a href="@@reviews@@">Reviews</a> staan video\'s van klanten met transcripten, in het Engels.'),
       ('Wat als ik niet tevreden ben?', 'Mail ons op team@unbanz.com. Bij gebruikersnaam-verzoeken krijg je 100% terug als het verzoek mislukt; zie het <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels).')],
      ['reviews', 'pricing', 'how', 'scams', 'contact'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Onafhankelijk, geen wachtwoord nodig, de prijs vooraf en alleen officiële routes. Lees hoe je kunt controleren of Unbanz betrouwbaar is.')

    g('about', 'Over Unbanz: een onafhankelijke dienst', 'Over ons', 'Over Unbanz.',
      'Unbanz (unbanz.com) is een onafhankelijke online dienst voor Instagram, Facebook en Snapchat: hulp bij uitgeschakelde accounts, het melden van nep- en imitatieaccounts, gebruikersnaam-verzoeken en Meta-advertentieaccounts.',
      [('wat', 'Wat we doen', UL('<a href="@@ig@@">Accounts terugkrijgen</a> na een uitschakeling, opschorting of hack.', 'Nep-, imitatie- en intimiderende accounts <a href="@@fake@@">melden</a> via de officiële tools.', '<a href="@@user@@">Gebruikersnaam-verzoeken</a> via de officiële processen.', '<a href="@@ad@@">Meta-advertentieaccounts</a> en Business Portfolio\'s.')),
       ('hoe', 'Hoe we werken', P('Je stuurt de gebruikersnaam en de melding. We zeggen eerlijk of we kunnen helpen en noemen de prijs voordat het werk begint. Alles gaat via de officiële routes van het platform, dat altijd zelf beslist. Lees <a href="@@how@@">hoe het werkt</a>.')),
       ('nooit', 'Wat we nooit doen', P('We vragen nooit om je wachtwoord of inlogcodes, kopen of verkopen geen accounts en gebruiken geen bots of valse meldingen.')),
       ('onafh', 'Onafhankelijk', P('Unbanz is niet verbonden aan Meta of Snapchat. We zijn niet Unbanx of unbanx.me. Je vindt ons als @unbanzhq op Instagram en X. Voor gebruikersnaam-verzoeken geldt een <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels): mislukt het verzoek, dan krijg je 100% terug.')),
       ('taal', 'Taal', P('We werken voor klanten in Nederland, Europa en daarbuiten. Support is voornamelijk in het Engels.'))],
      [('Wat is Unbanz?', 'Een onafhankelijke online dienst voor Instagram, Facebook en Snapchat: hulp bij uitgeschakelde accounts, het melden van nepaccounts, gebruikersnaam-verzoeken en advertentieaccounts.'),
       ('Is Unbanz verbonden aan Meta?', 'Nee. Unbanz is onafhankelijk.'),
       ('Hoe neem ik contact op?', 'Via WhatsApp of per e-mail naar team@unbanz.com. Zie <a href="@@contact@@">contact</a>.')],
      ['how', 'legit', 'reviews', 'pricing', 'contact'], HELP_IG, crumb_label=S['crumb_services'], std=False,
      desc='Unbanz is een onafhankelijke online dienst voor Instagram, Facebook en Snapchat. Lees wat we doen, hoe we werken en wat we nooit doen.')

    # ================= guides =================
    g('ig-disabled', 'Instagram-account uitgeschakeld: bezwaar maken', 'Instagram-account uitgeschakeld',
      'Instagram-account uitgeschakeld: zo maak je bezwaar.',
      'Toont Instagram dat je account is uitgeschakeld, log dan in, open de melding en maak één keer bezwaar via het officiële formulier. Dat kan vaak ongeveer 180 dagen. Maak een screenshot van de melding voordat je iets doet.',
      [('stappen', 'Wat je nu kunt doen', OL('Log in met het account en open de melding. Maak een screenshot.', 'Kies de optie om bezwaar te maken of een beoordeling aan te vragen, als die verschijnt.', 'Volg de stappen, bijvoorbeeld met een videoselfie of een code, en dien één keer in.', 'Controleer je e-mail, ook de spammap, op het antwoord van Instagram.')),
       ('fout', 'Veelgemaakte fouten', UL('Meerdere keren achter elkaar bezwaar maken.', 'Een nieuw account maken om de beperking te omzeilen.', 'Je wachtwoord delen met iemand die "alles regelt".')),
       ('geen', 'Geen knop of geen antwoord?', P('Zie <a href="@@no-button@@">Instagram: geen bezwaarknop</a> en <a href="@@appeal-denied@@">bezwaar afgewezen</a>.'))],
      [('Is mijn uitgeschakelde Instagram-account permanent weg?', 'Niet per se. Toont de melding een optie om bezwaar te maken, dan kan dat nog. De melding laat zien welke termijn voor jouw account geldt.'),
       ('Hoe vaak mag ik bezwaar maken?', 'Eén keer is genoeg; herhaald indienen helpt niet en kan verwarring geven.'),
       ('Heb ik hulp nodig om bezwaar te maken?', 'Niet per se. Het is gratis en je kunt het zelf doen. Wij helpen als het vastloopt.'),
       ('Hoe lang duurt het antwoord?', 'Instagram publiceert geen behandeltijd. Zie <a href="@@appeal-time@@">hoe lang een bezwaar duurt</a>.'),
       ('Vragen jullie mijn wachtwoord?', 'Nooit.')],
      ['ig', 'appeal-time', 'no-button', 'appeal-denied', 'deleted'], HELP_IG,
      desc='Instagram-account uitgeschakeld? Open de melding, maak één keer bezwaar via het officiële formulier en bewaar een screenshot. Zo pak je het aan.')

    g('ig-hacked', 'Instagram-account gehackt: zo krijg je het terug', 'Instagram-account gehackt',
      'Instagram-account gehackt: wat nu?',
      'Is je Instagram-account gehackt en zijn je e-mailadres of wachtwoord gewijzigd? Gebruik eerst de officiële herstelroute (instagram.com/hacked) en de videoselfie-verificatie. Deel je wachtwoord of codes met niemand.',
      [('stappen', 'Direct doen', OL('Zoek in je e-mail naar een bericht van Instagram over een wijziging van je e-mailadres of telefoonnummer en gebruik de link om de wijziging ongedaan te maken.', 'Ga naar instagram.com/hacked en volg de stappen.', 'Kies, als dat wordt aangeboden, de videoselfie-verificatie.', 'Zet na herstel een nieuw wachtwoord en tweestapsverificatie aan.')),
       ('oplicht', 'Pas op voor nepherstel', P('Wie je via een privébericht aanbiedt om je account "terug te halen" en om je wachtwoord of een code vraagt, is niet te vertrouwen. Zie <a href="@@scams@@">oplichting bij account herstel</a>.')),
       ('vast', 'Lukt het niet?', P('Zijn alle gegevens gewijzigd en werkt de link niet meer? Dan kunnen we kijken welke officiële stappen nog openstaan.'))],
      [('Kan ik een gehackt Instagram-account terugkrijgen?', 'Vaak wel, via de officiële hulpmiddelen. Het hangt af van wat er is gewijzigd en wat je nog kunt bewijzen.'),
       ('Wat als hackers mijn e-mailadres hebben gewijzigd?', 'Zoek een bericht van Instagram in je oude e-mail om de wijziging ongedaan te maken, of gebruik instagram.com/hacked.'),
       ('Wat is de videoselfie?', 'Een verificatiestap waarmee Instagram controleert of jij de eigenaar bent. Volg de stappen in de app.'),
       ('Moet ik mijn wachtwoord delen om het te laten herstellen?', 'Nee. Niemand heeft je wachtwoord nodig.'),
       ('Wat kost hulp?', 'De prijs hoor je in het gesprek, voordat het werk begint.')],
      ['ig', 'scams', 'no-button', 'ig-disabled'], HELP_IG,
      desc='Instagram-account gehackt en e-mail of wachtwoord gewijzigd? Gebruik instagram.com/hacked en de videoselfie. Zo pak je het stap voor stap aan.')

    g('appeal-time', 'Hoe lang duurt een Instagram-bezwaar?', 'Hoe lang duurt een bezwaar?',
      'Hoe lang duurt een Instagram-bezwaar?',
      'Instagram publiceert geen vaste behandeltijd. Een antwoord kan na enkele dagen komen of na meerdere weken. Wij kunnen geen datum beloven; wat wel helpt is één duidelijk bezwaar en geduld.',
      [('wacht', 'Wat je kunt verwachten', P('Er is geen officiële termijn. Sommige mensen horen na enkele dagen iets, anderen pas na weken. Het antwoord komt meestal per e-mail en in de app.')),
       ('doen', 'Wat je tijdens het wachten kunt doen', UL('Controleer je e-mail en spammap.', 'Maak niet steeds opnieuw bezwaar.', 'Maak geen nieuw account om de beperking te omzeilen.', 'Bewaar je screenshots.')),
       ('na', 'Als het antwoord nee is', P('Zie <a href="@@appeal-denied@@">Instagram-bezwaar afgewezen</a>.'))],
      [('Hoe lang duurt een Instagram-bezwaar?', 'Instagram noemt geen vaste termijn. Het varieert van enkele dagen tot meerdere weken.'),
       ('Kan ik het versnellen?', 'Niet via een officiële knop. Eén volledig en duidelijk bezwaar is het beste.'),
       ('Kan Unbanz het versnellen?', 'We kunnen geen datum beloven. We helpen het verzoek duidelijk in te dienen en houden je op de hoogte.'),
       ('Moet ik opnieuw bezwaar maken?', 'Meestal niet. Herhaald indienen helpt niet.')],
      ['ig-disabled', 'appeal-denied', 'no-button', 'ig'], HELP_IG,
      desc='Hoe lang duurt een Instagram-bezwaar? Er is geen vaste termijn: enkele dagen tot meerdere weken. Dit kun je wel doen terwijl je wacht.')

    g('appeal-denied', 'Instagram-bezwaar afgewezen: wat kun je nog doen?', 'Bezwaar afgewezen',
      'Instagram-bezwaar afgewezen: wat nu?',
      'Is je bezwaar tegen de uitschakeling van je Instagram-account afgewezen, dan is het account niet automatisch voor altijd weg. Lees de melding goed, kijk of er nog een optie staat en bewaar bewijs; niet elk account kan terugkomen.',
      [('lezen', 'Lees de melding goed', P('Staat er een knop om opnieuw een beoordeling aan te vragen of een link naar een formulier? Gebruik die. Staat er alleen een eindoordeel, dan is de interne route meestal gesloten.')),
       ('opties', 'Wat er soms nog mogelijk is', UL('Een andere officiële route, als de reden dat toelaat (bijvoorbeeld een gehackt account).', 'Bij een uitschakeling in de EU: een beroep via een onafhankelijke geschillenbeslechtingsinstantie onder de DSA. Zie <a href="@@rights@@">het recht op beroep onder de DSA</a>.')),
       ('niet', 'Wat niet helpt', UL('Een nieuw account maken om de beperking te omzeilen.', 'Betalen aan iemand die zegt "een contact bij Meta" te hebben.'))],
      [('Mijn bezwaar is afgewezen. Is het voorbij?', 'Niet altijd, maar vaak is de interne route dan gesloten. Kijk welke opties de melding nog toont.'),
       ('Kan ik opnieuw bezwaar maken?', 'Alleen als de melding daar een optie voor geeft.'),
       ('Kan ik naar een onafhankelijke instantie?', 'In de EU kan onder de DSA soms een geschillenbeslechtingsinstantie worden ingeschakeld. Zie <a href="@@rights@@">DSA-recht op beroep</a>.'),
       ('Kan Unbanz het account terugkrijgen?', 'We kijken eerlijk wat mogelijk is. Het platform beslist en we beloven geen uitkomst.')],
      ['rights', 'ig-disabled', 'no-button', 'ig'], HELP_IG,
      desc='Bezwaar tegen de uitschakeling van je Instagram-account afgewezen? Zo lees je de melding, wat er soms nog kan en waarom nieuwe accounts niet helpen.')

    g('deleted', 'Instagram-account verwijderd of uitgeschakeld?', 'Verwijderd of uitgeschakeld?',
      'Is je Instagram-account verwijderd of uitgeschakeld?',
      'Een uitgeschakeld account kun je soms met een bezwaar terugkrijgen; een door jou of door Instagram permanent verwijderd account meestal niet. De melding bij het inloggen laat zien welke van de twee het is.',
      [('uitgeschakeld', 'Uitgeschakeld', P('Je ziet bij het inloggen een melding dat je account is uitgeschakeld. Staat er een optie om bezwaar te maken, dan kun je het account mogelijk terugkrijgen. Zie <a href="@@ig-disabled@@">Instagram-account uitgeschakeld</a>.')),
       ('verwijderd', 'Verwijderd', P('Heb je het account zelf verwijderd, dan kan dat een bepaalde tijd ongedaan worden gemaakt; daarna niet meer. Is het door Instagram permanent verwijderd, dan is terugkeren zeldzaam.')),
       ('check', 'Zo controleer je het', UL('Probeer in te loggen en lees de melding.', 'Zoek in je e-mail naar berichten van Instagram.', 'Open de profielpagina in een browser en kijk of die nog bestaat.'))],
      [('Hoe weet ik of mijn account is uitgeschakeld?', 'Je ziet een melding bij het inloggen dat het account is uitgeschakeld, vaak met een optie voor bezwaar.'),
       ('Kan een verwijderd account terugkomen?', 'Alleen binnen de periode die Instagram noemt, en meestal niet als het permanent is verwijderd.'),
       ('Waarom is mijn profiel niet vindbaar?', 'Het kan uitgeschakeld, verwijderd of door een ander account geblokkeerd zijn.'),
       ('Kan Unbanz helpen?', 'Bij een uitgeschakeld account kijken we eerlijk wat mogelijk is.')],
      ['ig-disabled', 'ig', 'appeal-denied'], HELP_IG,
      desc='Is je Instagram-account verwijderd of uitgeschakeld? Zo zie je het verschil en wat er nog mogelijk is.')

    g('no-button', 'Instagram toont geen bezwaarknop: wat nu?', 'Geen bezwaarknop',
      'Instagram toont geen knop om bezwaar te maken.',
      'Ontbreekt de knop om bezwaar te maken, dan is de termijn soms verlopen, is het account permanent uitgeschakeld of is de melding een andere soort. Kijk eerst welke melding je ziet.',
      [('redenen', 'Mogelijke redenen', UL('De termijn voor bezwaar is verlopen.', 'Je hebt al bezwaar gemaakt en de beslissing is definitief.', 'Het gaat om een beperking of een gehackt account in plaats van een uitschakeling.', 'Een tijdelijke storing in de app.')),
       ('proberen', 'Wat je kunt proberen', UL('Log in via een browser op instagram.com in plaats van de app.', 'Probeer het op een ander apparaat en netwerk dat je normaal gebruikt.', 'Update de app.', 'Is het account gehackt: gebruik instagram.com/hacked.')),
       ('rechten', 'In de EU', P('Is de interne route gesloten, kijk dan naar het <a href="@@rights@@">recht op beroep onder de DSA</a>.'))],
      [('Waarom zie ik geen bezwaarknop?', 'Meestal is de termijn verlopen, is de beslissing definitief of gaat het om een ander soort melding.'),
       ('Helpt een nieuw account?', 'Nee, en het kan het erger maken, omdat omzeilen tegen de regels is.'),
       ('Kan Unbanz een knop laten verschijnen?', 'Nee. We kunnen wel kijken welke officiële route nog openstaat.'),
       ('Wat als het account gehackt is?', 'Dan is er een aparte route: instagram.com/hacked.')],
      ['ig-disabled', 'appeal-denied', 'rights', 'ig-hacked'], HELP_IG,
      desc='Geen knop om bezwaar te maken bij Instagram? Dit zijn de meest voorkomende redenen en wat je nog kunt proberen.')

    g('blocked', 'Instagram: "We beperken bepaalde activiteit"', 'Actie geblokkeerd',
      'Instagram: "We beperken bepaalde activiteit".',
      'Deze melding betekent dat Instagram tijdelijk bepaalde acties beperkt, vaak na veel activiteit in korte tijd. Het is meestal geen uitschakeling. Neem een pauze, stop met automatiseren en bezwaar maken kan als er een knop staat.',
      [('wat', 'Wat de melding betekent', P('Instagram beperkt tijdelijk acties zoals liken, volgen of reageren. Het account blijft bestaan.')),
       ('doen', 'Wat je kunt doen', UL('Pauzeer een dag of twee en gebruik de app normaal.', 'Stop met apps van derden of automatisering.', 'Staat er "Ik ben het niet" of "Meld een probleem", gebruik die dan één keer.', 'Controleer of er een melding in je e-mail staat.')),
       ('lang', 'Blijft het terugkomen?', P('Controleer of je account is gehackt, wijzig je wachtwoord en zet tweestapsverificatie aan.'))],
      [('Hoe lang duurt de beperking?', 'Instagram noemt geen vaste termijn; het varieert van uren tot dagen.'),
       ('Is mijn account uitgeschakeld?', 'Nee, deze melding is een tijdelijke beperking.'),
       ('Kan ik het laten opheffen?', 'Niet direct. Pauzeren en geen automatisering gebruiken helpt het meest.'),
       ('Kan Unbanz helpen?', 'Is de beperking blijvend of is er meer aan de hand, stuur ons dan de melding.')],
      ['ig-disabled', 'ig-hacked', 'ig'], HELP_IG,
      desc='Instagram meldt dat bepaalde activiteit wordt beperkt? Dit betekent het, hoe lang het duurt en wat je er zelf aan kunt doen.')

    g('ad-disabled', 'Facebook-advertentieaccount uitgeschakeld: wat nu?', 'Advertentieaccount uitgeschakeld',
      'Facebook-advertentieaccount uitgeschakeld: wat nu?',
      'Is je advertentieaccount uitgeschakeld, kijk dan in Accountkwaliteit welke reden Meta noemt en vraag via de officiële route een beoordeling aan. Wijzig de advertenties niet blind en maak geen nieuw account om het te omzeilen.',
      [('lezen', 'Zoek de reden', P('Open in Meta Business Suite of Advertentiebeheer de pagina Accountkwaliteit. Daar staat vaak de reden en of een beoordeling kan worden aangevraagd.')),
       ('doen', 'Wat je kunt doen', OL('Maak screenshots van de melding en de afgewezen advertenties.', 'Vraag een beoordeling aan als de knop beschikbaar is.', 'Controleer of je betaalmethode en bedrijfsgegevens kloppen.', 'Wacht op het antwoord en dien niet steeds opnieuw in.')),
       ('niet', 'Wat je niet moet doen', UL('Een nieuw advertentieaccount maken om de beperking te omzeilen.', 'Je accounttoegang delen met iemand die "alles regelt".'))],
      [('Waarom is mijn advertentieaccount uitgeschakeld?', 'De reden staat meestal in Accountkwaliteit: bijvoorbeeld een overtreding van het advertentiebeleid of een betaalprobleem.'),
       ('Kan ik een beoordeling aanvragen?', 'Ja, als Meta die optie toont. Doe het één keer, duidelijk en volledig.'),
       ('Kan ik gewoon een nieuw account maken?', 'Dat wordt vaak ook beperkt en is tegen de regels als het een omzeiling is.'),
       ('Kan Unbanz helpen?', 'Ja, we kijken eerlijk wat mogelijk is. Meta beslist.')],
      ['ad', 'fb-appeal', 'appeal-denied'], HELP_AD, svc='ad',
      desc='Facebook-advertentieaccount uitgeschakeld? Zoek de reden in Accountkwaliteit, vraag één duidelijke beoordeling aan en vermijd veelgemaakte fouten.')

    g('fb-appeal', 'Facebook-account uitgeschakeld: bezwaar maken', 'Facebook uitgeschakeld: bezwaar',
      'Facebook-account uitgeschakeld: zo maak je bezwaar.',
      'Is je Facebook-account uitgeschakeld, log dan in, open de melding en vraag een beoordeling aan via de officiële knop. Doe dat één keer, binnen de termijn die Facebook toont, en bewaar een screenshot.',
      [('stappen', 'Stappen', OL('Log in en lees de melding. Maak een screenshot.', 'Kies "Beoordeling aanvragen" of de vergelijkbare knop.', 'Voeg, als gevraagd, een identiteitsbewijs toe via de officiële pagina.', 'Wacht op het antwoord per e-mail en in je meldingen.')),
       ('letop', 'Let op', UL('Dien niet meerdere keren in.', 'Stuur je identiteitsbewijs alleen via de officiële Facebook-pagina.', 'Betaal niemand die een zeker resultaat belooft: niemand kan dat.')),
       ('geen', 'Geen knop?', P('Zie <a href="@@appeal-denied@@">bezwaar afgewezen</a> en <a href="@@rights@@">het recht op beroep onder de DSA</a>.'))],
      [('Hoe maak ik bezwaar bij Facebook?', 'Via de knop om een beoordeling aan te vragen in de melding bij het inloggen.'),
       ('Moet ik een identiteitsbewijs sturen?', 'Soms. Doe dat alleen via de officiële Facebook-pagina.'),
       ('Hoe lang duurt het?', 'Facebook noemt geen vaste termijn.'),
       ('Kan Unbanz helpen?', 'Ja, we kijken eerlijk wat mogelijk is. Facebook beslist.')],
      ['fb', 'fb-hacked', 'appeal-time', 'ad-disabled'], HELP_FB,
      desc='Facebook-account uitgeschakeld? Vraag één keer een beoordeling aan via de officiële knop en bewaar een screenshot. Zo doe je dat stap voor stap.')

    g('fb-hacked', 'Facebook-account gehackt: wat moet je doen?', 'Facebook-account gehackt',
      'Facebook-account gehackt: wat nu?',
      'Is je Facebook-account gehackt, ga dan naar facebook.com/hacked en volg de officiële stappen. Controleer ook of je e-mailadres is gewijzigd en wijzig daarna je wachtwoord. Deel nooit codes met anderen.',
      [('stappen', 'Direct doen', OL('Ga naar facebook.com/hacked en volg de stappen.', 'Zoek in je e-mail naar een bericht over een gewijzigd e-mailadres en gebruik de link om dat ongedaan te maken.', 'Wijzig je wachtwoord en log op andere apparaten uit.', 'Zet tweestapsverificatie aan en controleer gekoppelde pagina\'s en advertentieaccounts.')),
       ('oplicht', 'Pas op', P('Iemand die je een "herstel" aanbiedt en om je wachtwoord of een code vraagt, is niet te vertrouwen. Zie <a href="@@scams@@">oplichting bij account herstel</a>.')),
       ('bedrijf', 'Zakelijk account', P('Staan er pagina\'s of advertentieaccounts aan gekoppeld, controleer dan ook wie beheerder is en wat er is gewijzigd.'))],
      [('Hoe krijg ik mijn gehackte Facebook-account terug?', 'Via facebook.com/hacked en de officiële herstelstappen.'),
       ('Wat als het e-mailadres is gewijzigd?', 'Gebruik de link in het bericht van Facebook in je oude e-mail om de wijziging ongedaan te maken.'),
       ('Zijn mijn pagina\'s en advertentieaccounts ook in gevaar?', 'Mogelijk. Controleer beheerders en betaalmethoden zodra je weer binnen bent.'),
       ('Moet ik mijn wachtwoord delen om het terug te krijgen?', 'Nooit.')],
      ['fb', 'fb-appeal', 'scams', 'ig-hacked'], HELP_FB,
      desc='Facebook-account gehackt? Gebruik facebook.com/hacked, herstel je e-mailadres en beveilig je account met tweestapsverificatie. Zo pak je het aan.')

    g('inactive-user', 'Gebruikersnaam van een inactief Instagram-account', 'Inactieve gebruikersnaam',
      'Kun je de gebruikersnaam van een inactief Instagram-account claimen?',
      'Er is geen knop om de gebruikersnaam van een inactief account over te nemen. Instagram heeft alleen officiële processen, zoals een merkrechtmelding of een imitatiemelding, en beslist zelf.',
      [('regels', 'Hoe het werkt', P('Een gebruikersnaam is niet te koop en niet over te nemen. Is het account echt inactief, dan kan een officiële route bestaan; of Instagram die toestaat, beslist het platform.')),
       ('routes', 'Welke routes bestaan', UL('Een merkrechtmelding als de naam je geregistreerde merk is.', 'Een imitatiemelding als iemand zich voor jou uitgeeft.', 'De officiële route voor een inactief account, als die van toepassing is.')),
       ('niet', 'Wat je moet vermijden', UL('Gebruikersnamen kopen van mensen die dat aanbieden.', 'Iemand die zegt "een contact bij Meta" te hebben.'))],
      [('Kan ik de gebruikersnaam van een inactief account gewoon overnemen?', 'Nee. Er is alleen een officieel proces, en Instagram beslist.'),
       ('Kan ik een gebruikersnaam kopen?', 'Nee, en wie dat aanbiedt, handelt tegen de regels of is een oplichter.'),
       ('Wat kost hulp bij een gebruikersnaam-verzoek?', 'De prijs hoor je in het gesprek, voordat het werk begint.'),
       ('Wat als het verzoek mislukt?', 'Dan krijg je 100% van je geld terug. Zie het <a href="/refund-policy/" hreflang="en" lang="en">refund policy</a> (in het Engels).')],
      ['user', 'pricing', 'scams'], P('Stuur ons de gewenste gebruikersnaam en je profiel. We zeggen eerlijk welke officiële route past en noemen de prijs in het gesprek, voordat het werk begint. Mislukt een gebruikersnaam-verzoek, dan krijg je 100% van je geld terug. Support is voornamelijk in het Engels.'),
      svc='username', desc='Kun je de gebruikersnaam van een inactief Instagram-account claimen? Er is geen knop; alleen officiële processen. Lees welke en wat dat betekent.')

    g('report-fake', 'Nepaccount met mijn foto\'s melden op Instagram', 'Nepaccount met mijn foto\'s',
      'Nepaccount met jouw foto\'s: zo meld je het.',
      'Gebruikt iemand jouw foto\'s voor een nepaccount, meld het dan als imitatie via de drie puntjes op het profiel. Bewaar eerst screenshots met de link en de datum, en vraag vrienden niet massaal te melden.',
      [('stappen', 'Zo meld je het', OL('Bewaar screenshots en de link naar het profiel.', 'Open het profiel, tik op de drie puntjes en kies Melden.', 'Kies de optie dat iemand zich voordoet als jij of als iemand die je kent.', 'Volg de stappen en bewaar de bevestiging.')),
       ('extra', 'Extra stappen', UL('Waarschuw je volgers dat het account nep is.', 'Is er geld gevraagd of ben je bedreigd: doe aangifte bij de politie (politie.nl).', 'Bij gestolen intieme beelden: zie <a href="@@sextortion@@">sextortion</a>.')),
       ('niet', 'Wat niet werkt', P('Massale of valse meldingen. Eén duidelijke melding is beter en is wat het platform beoordeelt.'))],
      [('Hoe meld ik een account dat mijn foto\'s gebruikt?', 'Via Melden op het profiel en de optie voor imitatie.'),
       ('Moet ik massaal laten melden?', 'Nee. Dat werkt niet en is tegen de regels.'),
       ('Kan Unbanz het melden?', 'We helpen de melding duidelijk voor te bereiden en in te dienen via de officiële tools. Het platform beslist.'),
       ('Moet ik aangifte doen?', 'Bij oplichting, bedreiging of chantage is dat verstandig.')],
      ['fake', 'imp', 'har', 'scams'], HELP_REP, svc='ban',
      desc='Gebruikt iemand jouw foto\'s voor een nepaccount op Instagram? Zo meld je het als imitatie en welke bewijzen je moet bewaren.')

    g('scams', 'Oplichting bij account herstel: waarschuwing', 'Oplichting bij herstel',
      'Oplichting bij account herstel: zo herken je het.',
      'Niemand heeft je wachtwoord of een inlogcode nodig om je account terug te krijgen. Wie daarom vraagt, belooft een zeker resultaat of zegt een contact bij Meta te hebben, is een oplichter.',
      [('signalen', 'Waarschuwingssignalen', UL('Ze benaderen jou, meestal in een privébericht of een reactie.', 'Ze vragen om je wachtwoord, een code of toegang tot je e-mail.', 'Ze beloven een zeker resultaat of zeggen een contact bij Meta te hebben.', 'Ze willen betaling in cadeaubonnen, crypto of via een link.')),
       ('doen', 'Wat je kunt doen', UL('Reageer niet en blokkeer het account.', 'Meld het in de app.', 'Heb je al betaald of gegevens gedeeld: wijzig je wachtwoorden en neem contact op met je bank.', 'Meld het bij de Fraudehelpdesk (fraudehelpdesk.nl) en doe zo nodig aangifte bij de politie.')),
       ('anders', 'Hoe betrouwbare hulp eruitziet', P('Een betrouwbare dienst vraagt nooit om je wachtwoord, noemt de prijs voordat het werk begint en legt uit welke officiële route wordt gebruikt. Zie <a href="@@legit@@">Is Unbanz betrouwbaar?</a>'))],
      [('Hoe herken ik een oplichter bij account herstel?', 'Ze benaderen jou, vragen om je wachtwoord of een code en beloven een zeker resultaat.'),
       ('Wat als ik al heb betaald?', 'Neem contact op met je bank, wijzig je wachtwoorden en meld het bij de Fraudehelpdesk en de politie.'),
       ('Kent iemand echt een contact bij Meta?', 'Dat kun je niet controleren en het is een bekend oplichtingsverhaal.'),
       ('Vragen jullie om mijn wachtwoord?', 'Nooit.')],
      ['legit', 'ig-hacked', 'fake', 'pricing'], HELP_IG,
      desc='Niemand heeft je wachtwoord nodig om je account terug te krijgen. Dit zijn de waarschuwingssignalen van oplichting bij account herstel.')

    g('sextortion', 'Sextortion op Instagram: wat moet je doen?', 'Sextortion',
      'Sextortion op Instagram: wat moet je doen?',
      'Wordt je op Instagram afgeperst met intieme beelden, betaal dan niet en stop het contact. Bewaar het bewijs, blokkeer en meld het account, en doe aangifte bij de politie. Je bent niet alleen en je hebt niets verkeerd gedaan.',
      [('direct', 'Wat je direct kunt doen', OL('Betaal niet en stuur geen extra beelden.', 'Maak screenshots van de berichten, het profiel en de gebruikersnaam; verwijder niets.', 'Blokkeer en meld het account in de app.', 'Doe aangifte bij de politie (politie.nl, of 112 bij direct gevaar).')),
       ('hulp', 'Hulp in Nederland', UL('Helpwanted.nl (Offlimits) helpt bij online seksueel misbruik en seksuele chantage.', 'Voor andere oplichting: de Fraudehelpdesk (fraudehelpdesk.nl).', 'Praat met iemand die je vertrouwt.')),
       ('beelden', 'Beelden laten verwijderen', P('Meld verspreide beelden bij het platform. Stuur nooit geld om verspreiding te voorkomen: dat leidt meestal tot meer eisen.'))],
      [('Moet ik betalen?', 'Nee. Betalen stopt het meestal niet en leidt tot nieuwe eisen.'),
       ('Moet ik aangifte doen?', 'Ja, dat is verstandig. Bewaar het bewijs eerst.'),
       ('Waar vind ik hulp?', 'Bij de politie en bij Helpwanted.nl (Offlimits). Bij direct gevaar bel je 112.'),
       ('Kan Unbanz helpen?', 'We kunnen helpen het account te melden via de officiële tools. Doe eerst aangifte en bewaar bewijs.')],
      ['har', 'fake', 'scams'], HELP_REP, svc='ban',
      desc='Afgeperst met intieme beelden op Instagram? Betaal niet, bewaar bewijs, blokkeer en meld het account en doe aangifte. Zo pak je het aan.')

    g('support', 'Contact met Instagram of Meta opnemen vanuit Nederland', 'Contact met Instagram of Meta',
      'Contact met Instagram of Meta opnemen vanuit Nederland.',
      'Instagram en Meta hebben geen telefoonnummer voor gewone gebruikers. Je bereikt hen via het Helpcentrum, de optie Meld een probleem in de app en de officiële formulieren. Nummers die online circuleren zijn bijna altijd nep.',
      [('routes', 'De officiële routes', UL('Het Helpcentrum van Instagram en Facebook.', 'In de app: Instellingen, Help, Meld een probleem.', 'Officiële formulieren voor bezwaar, hack en imitatie.', 'Alleen voor wie Meta Verified heeft: de ondersteuning die daarbij hoort.')),
       ('nep', 'Nep-supportnummers', P('Zoek je een telefoonnummer van Instagram en vind je er een, dan is het vrijwel zeker oplichting. Zie <a href="@@scams@@">oplichting bij account herstel</a>.')),
       ('eu', 'Je rechten in de EU', P('Is je account beperkt of verwijderd, dan heb je onder de DSA recht op een uitleg en op beroep. Zie <a href="@@rights@@">het recht op beroep</a>.'))],
      [('Hoe bel ik Instagram?', 'Dat kan niet voor gewone gebruikers. Gebruik het Helpcentrum en Meld een probleem in de app.'),
       ('Is een telefoonnummer van Instagram op internet echt?', 'Vrijwel altijd niet. Wees voorzichtig.'),
       ('Heeft Meta een kantoor in Nederland?', 'Meta\'s Europese entiteit zit in Ierland. Voor geschillen zijn de officiële online routes de weg.'),
       ('Kan Unbanz helpen als de officiële route vastloopt?', 'Ja, we kijken eerlijk wat mogelijk is. We zijn niet verbonden aan Meta.')],
      ['rights', 'scams', 'ig-disabled', 'ig'], HELP_IG,
      desc='Hoe neem je contact op met Instagram of Meta vanuit Nederland? Geen telefoonnummer, wel officiële routes. Zo herken je ook nep-supportnummers.')

    g('rights', 'DSA: recht op beroep bij Meta in Nederland en de EU', 'DSA: recht op beroep',
      'DSA: je recht op beroep tegen een beslissing van Meta.',
      'Onder de Digitaledienstenverordening (DSA) krijg je in de EU een uitleg als je account wordt beperkt of uitgeschakeld, kun je intern in beroep gaan en daarna een onafhankelijke geschillenbeslechtingsinstantie inschakelen. Het oordeel is niet bindend, maar Meta moet wel meewerken.',
      [('uitleg', 'Wat je recht is', UL('Een onderbouwde uitleg van de beslissing.', 'Een interne klachtenprocedure (bezwaar), kosteloos.', 'Daarna de mogelijkheid om een erkende, onafhankelijke instantie voor geschillenbeslechting te vragen te kijken.')),
       ('hoe', 'Hoe je het aanpakt', OL('Maak eerst bezwaar via de interne route van Instagram of Facebook en bewaar de beslissing.', 'Zoek een erkende instantie, zoals Appeals Centre Europe, en volg de aanmeldprocedure.', 'Voeg de melding, de datum en je argumenten toe.')),
       ('toezicht', 'Toezicht in Nederland', P('De Autoriteit Consument &amp; Markt (ACM) is in Nederland de toezichthouder voor de DSA. Je kunt daar ook een klacht indienen over het gedrag van een platform.')),
       ('let', 'Let op', P('Het oordeel van zo\'n instantie is niet bindend en een uitkomst is niet verzekerd. Wij zijn geen jurist en dit is geen juridisch advies.'))],
      [('Wat is het DSA-recht op beroep?', 'Het recht om bij beperkingen een uitleg te krijgen, intern in beroep te gaan en daarna een onafhankelijke instantie in te schakelen.'),
       ('Is het oordeel bindend voor Meta?', 'Nee, maar Meta moet te goeder trouw meewerken.'),
       ('Wat kost het?', 'De instanties mogen van gebruikers geen of slechts een symbolisch bedrag vragen.'),
       ('Kan Unbanz dit voor me doen?', 'We kunnen kijken welke route past en je helpen het duidelijk in te dienen. Het is geen juridisch advies.')],
      ['appeal-denied', 'no-button', 'support', 'ig'], HELP_IG,
      desc='Wat is het DSA-recht op beroep bij Meta? Uitleg over intern bezwaar, geschillenbeslechting en de rol van de ACM in Nederland.')
