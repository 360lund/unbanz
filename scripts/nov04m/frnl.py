import sys;sys.path.insert(0,'scripts/nov04m');from loc import qa,add,bump_lastmod
A='questions-2026'
FRT='Vos autres questions, en bref (2026)';NLT='Meer vragen, kort beantwoord (2026)'
ACF='Depuis 2025, l’Appeals Centre Europe examine aussi les suspensions de comptes Facebook et Instagram pour les utilisateurs de l’UE. C’est gratuit et non contraignant, et il faut d’abord avoir épuisé l’appel interne de Meta.'
ACN='Sinds 2025 behandelt het Appeals Centre Europe ook opschortingen van Facebook- en Instagram-accounts voor gebruikers in de EU. Het is gratis en niet bindend, en je moet eerst het interne bezwaar bij Meta hebben doorlopen.'
FR={
'compte-instagram-desactive-comment-recuperer':[
('Où se trouve la contestation dans l’Espace comptes ?','Si vous pouvez encore vous connecter, ouvrez Paramètres, puis Espace comptes, puis Qualité du compte ou la notification de désactivation. Sinon, la page de connexion affiche en général le bouton de contestation. Les intitulés changent selon la version de l’application.'),
('Désactivé sans pièce d’identité à envoyer : que faire ?','Meta propose souvent un selfie vidéo plutôt qu’un document. Faites-le dans un endroit bien éclairé, sans lunettes ni filtre, et une seule fois. Si aucune option ne s’affiche, notez-le avec une capture d’écran : cela compte pour la suite.'),
('Piraté puis désactivé : par où commencer ?','Commencez par instagram.com/hacked, pas par la contestation classique. Signalez aussi l’incident sur 17Cyber (17cyber.gouv.fr) et, en cas d’escroquerie, déposez plainte sur THESEE. Changez le mot de passe de l’adresse e-mail liée.'),
('Et si l’appel interne est refusé ?',ACF),
],
'compte-facebook-desactive-faire-appel':[
('Combien de temps pour faire appel ?','Meta indique en général une fenêtre d’environ 180 jours après la désactivation. Passé ce délai, le compte peut être supprimé définitivement. Notez la date affichée sur la notification.'),
('Où suivre la demande ?','Dans l’Espace comptes, puis Qualité du compte, ou dans la boîte de réception d’assistance de Facebook. Vérifiez aussi l’adresse e-mail liée, y compris les courriers indésirables.'),
('Facebook désactivé et piraté en même temps ?','Utilisez d’abord facebook.com/hacked pour reprendre la main, puis contestez la désactivation. Un signalement sur 17Cyber aide à documenter le piratage.'),
('Recours hors de Meta ?',ACF+' L’Arcom est le coordinateur français des services numériques, mais elle ne tranche pas les contestations individuelles.'),
],
'compte-publicitaire-facebook-desactive':[
('Quelles raisons reviennent le plus souvent ?','Un moyen de paiement refusé ou contesté, un changement de pays de facturation, une forte hausse des dépenses, des annonces refusées à répétition, un accès depuis un nouvel appareil ou un nouveau pays, ou un compte personnel administrateur lui-même restreint.'),
('Où demander un réexamen ?','Dans la Qualité du compte (Account Quality) du Business Manager ou de l’Espace comptes. Ouvrez le compte publicitaire concerné et choisissez Demander un réexamen si le bouton apparaît.'),
('La vérification d’identité ou d’entreprise bloque : que faire ?','Utilisez des documents qui correspondent exactement au nom et à l’adresse du portefeuille business, par exemple un extrait Kbis récent ou un avis de situation SIREN. Une différence de nom est une cause fréquente de refus.'),
('Le délai de réexamen est-il connu ?','Non. Meta ne s’engage pas sur un délai. Évitez de créer de nouveaux comptes publicitaires pendant l’attente : cela peut être vu comme un contournement.'),
],
'faire-appel-instagram-desactive-delai':[
('Que se passe-t-il pendant l’attente de la vérification ?','Le compte reste en général invisible pour les autres. Évitez d’envoyer plusieurs demandes ou plusieurs selfies vidéo : cela n’accélère rien et peut compliquer le suivi.'),
('Les 180 jours, c’est à partir de quand ?','À partir de la notification de désactivation, selon la date affichée par Instagram. Faites une capture d’écran de cette date.'),
('Recours après un refus ?',ACF),
],
'pseudo-instagram-deja-pris-compte-inactif':[
('Une marque déposée à l’INPI aide-t-elle ?','Elle peut aider si le pseudo correspond exactement à la marque et que le compte actuel l’utilise d’une façon qui crée une confusion. Instagram décide seul ; une marque ne donne pas automatiquement droit au pseudo.'),
('Instagram libère-t-il les comptes inactifs ?','Instagram n’a pas de procédure publique pour réclamer un pseudo inactif. Il peut se libérer si le compte est supprimé par son titulaire ou par Meta, sans date annoncée.'),
],
'compte-instagram-pirate-que-faire':[
('Piraté et désactivé : quel ordre suivre ?','D’abord instagram.com/hacked pour signaler le piratage, ensuite la contestation de la désactivation si elle s’affiche. Gardez les e-mails de security@mail.instagram.com qui signalent les changements.'),
('Où signaler en France ?','Sur 17Cyber (17cyber.gouv.fr) pour être orienté, et sur THESEE pour une plainte en ligne en cas d’escroquerie. Pour la sextorsion, voyez aussi Pharos.'),
],
}
NL={
'instagram-account-uitgeschakeld':[
('Waar vind ik het bezwaar in Accountcentrum?','Kun je nog inloggen, ga dan naar Instellingen, Accountcentrum en Accountstatus, of open de melding over de uitschakeling. Anders toont het inlogscherm meestal de knop om bezwaar te maken. De namen verschillen per app-versie.'),
('Uitgeschakeld zonder ID-optie: wat nu?','Meta vraagt vaak een videoselfie in plaats van een document. Doe die bij goed licht, zonder bril of filter, en één keer. Zie je geen enkele optie, maak dan een screenshot; dat helpt later.'),
('Gehackt en daarna uitgeschakeld?','Begin bij instagram.com/hacked, niet bij het gewone bezwaar. Meld oplichting bij de Fraudehelpdesk (fraudehelpdesk.nl) en doe aangifte bij de politie. Wijzig ook het wachtwoord van je gekoppelde e-mail.'),
('Bezwaar afgewezen: is er nog een route?',ACN),
],
'facebook-account-uitgeschakeld-bezwaar':[
('Hoe lang heb ik om bezwaar te maken?','Meta noemt meestal een termijn van ongeveer 180 dagen na de uitschakeling. Daarna kan het account definitief worden verwijderd. Noteer de datum uit de melding.'),
('Waar volg ik mijn bezwaar?','In Accountcentrum onder Accountstatus en in de supportinbox van Facebook. Controleer ook de gekoppelde e-mail, inclusief spam.'),
('Buiten Meta om?',ACN+' De ACM is in Nederland de coördinator digitale diensten, maar beslist niet over individuele bezwaren.'),
],
'facebook-advertentieaccount-uitgeschakeld':[
('Wat zijn de meest voorkomende redenen?','Een geweigerde of betwiste betaling, een ander factuurland, een plotselinge stijging van de uitgaven, herhaald afgekeurde advertenties, inloggen vanaf een nieuw apparaat of land, of een beheerder wiens eigen account beperkt is.'),
('Waar vraag ik een herbeoordeling aan?','In Accountkwaliteit (Account Quality) in Business Manager of Accountcentrum. Open het betreffende advertentieaccount en kies Beoordeling aanvragen als die knop er staat.'),
('Bedrijfsverificatie loopt vast?','Gebruik documenten die exact overeenkomen met de naam en het adres in het bedrijfsportfolio, zoals een recent KvK-uittreksel of btw-gegevens. Een afwijkende naam is een veelvoorkomende reden voor afwijzing.'),
('Is de wachttijd bekend?','Nee. Meta noemt geen vaste termijn. Maak tijdens het wachten geen nieuwe advertentieaccounts aan; dat kan worden gezien als omzeiling.'),
],
'hoe-lang-duurt-instagram-bezwaar':[
('Wat gebeurt er tijdens het wachten op verificatie?','Het account is meestal niet zichtbaar voor anderen. Stuur niet meerdere verzoeken of videoselfies; dat versnelt niets en kan het volgen lastiger maken.'),
('Vanaf wanneer tellen de 180 dagen?','Vanaf de melding van uitschakeling, volgens de datum die Instagram toont. Maak daar een screenshot van.'),
('Na een afwijzing?',ACN),
],
'instagram-account-gehackt':[
('Gehackt en uitgeschakeld: welke volgorde?','Eerst instagram.com/hacked om de hack te melden, daarna het bezwaar tegen de uitschakeling als dat verschijnt. Bewaar de e-mails van security@mail.instagram.com over wijzigingen.'),
('Waar meld ik het in Nederland?','Bij de Fraudehelpdesk voor advies en bij de politie voor aangifte, online of op het bureau. Bij sextortion kun je ook terecht bij Helpwanted.nl.'),
],
'instagram-gebruikersnaam-inactief-account':[
('Helpt een merkregistratie bij het BOIP of EUIPO?','Het kan helpen als de naam exact overeenkomt met je merk en het huidige account verwarring veroorzaakt. Instagram beslist zelf; een merk geeft niet automatisch recht op de naam.'),
('Geeft Instagram inactieve namen vrij?','Er is geen openbare procedure om een inactieve naam op te eisen. Een naam kan vrijkomen als het account wordt verwijderd, zonder aangekondigde datum.'),
],
}
urls=[]
import sys as _s
RUN=__name__=="__main__"
for s,it in (FR.items() if RUN else []):
    u=add('fr',s,qa(FRT,it,A),A); urls+= [u] if u else []
for s,it in (NL.items() if RUN else []):
    u=add('nl',s,qa(NLT,it,A),A); urls+= [u] if u else []
RUN and print(bump_lastmod(urls));RUN and open('/tmp/b5.txt','w').write('\n'.join(urls));print(len(urls))
