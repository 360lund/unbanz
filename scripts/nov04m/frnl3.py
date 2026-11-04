import sys;sys.path.insert(0,'scripts/nov04m');from loc import qa,add,bump_lastmod
from frnl import ACF,ACN,FRT,NLT,A
FAD=[('Pourquoi un compte publicitaire est-il restreint ?','Le plus souvent : un paiement refusé ou contesté, un changement de pays de facturation ou de devise, une hausse soudaine des dépenses, des publicités refusées à répétition, une connexion depuis un nouveau pays, ou un administrateur dont le profil est lui-même restreint.'),
('Où demander le réexamen ?','Dans Qualité du compte (business.facebook.com/accountquality). Choisissez le compte publicitaire et utilisez Demander un réexamen si le bouton apparaît. Meta ne publie pas de délai.'),
('Quels documents pour la vérification d’entreprise en France ?','Un extrait Kbis récent ou un avis de situation SIREN, au nom et à l’adresse exacts du portefeuille business.')]
NAD=[('Waarom wordt een advertentieaccount beperkt?','Meestal door een geweigerde of betwiste betaling, een ander factuurland of andere valuta, een plotselinge stijging van de uitgaven, herhaald afgekeurde advertenties, inloggen vanuit een nieuw land, of een beheerder wiens eigen profiel beperkt is.'),
('Waar vraag ik de herbeoordeling aan?','In Accountkwaliteit (business.facebook.com/accountquality). Kies het advertentieaccount en gebruik Beoordeling aanvragen als die knop er staat. Meta noemt geen termijn.'),
('Welke documenten voor bedrijfsverificatie in Nederland?','Een recent KvK-uittreksel of btw-gegevens, met exact dezelfde naam en hetzelfde adres als in het bedrijfsportfolio.')]
FAC=[('Où faire appel dans l’Espace comptes ?','Paramètres, puis Espace comptes, puis Statut du compte. Si vous ne pouvez pas vous connecter, le bouton se trouve sur la notification affichée à la connexion.'),
('Désactivé sans possibilité d’envoyer une pièce d’identité ?','Meta propose souvent un selfie vidéo. Faites-le une seule fois, dans une bonne lumière. Si rien ne s’affiche, faites une capture d’écran datée.'),
('Piraté puis désactivé ?','Commencez par le formulaire de piratage officiel (instagram.com/hacked ou facebook.com/hacked), puis contestez la désactivation. Signalez aussi sur 17Cyber.'),
('Recours après un refus ?',ACF)]
NAC=[('Waar maak ik bezwaar in Accountcentrum?','Instellingen, Accountcentrum, Accountstatus. Kun je niet inloggen, dan staat de knop op de melding na het inloggen.'),
('Uitgeschakeld zonder optie voor een ID?','Meta vraagt vaak een videoselfie. Doe die één keer, bij goed licht. Zie je niets, maak dan een screenshot met datum.'),
('Gehackt en uitgeschakeld?','Begin bij het officiële hackformulier (instagram.com/hacked of facebook.com/hacked) en maak daarna bezwaar. Meld oplichting bij de Fraudehelpdesk.'),
('Na een afwijzing?',ACN)]
FUN=[('Instagram libère-t-il les pseudos inactifs ?','Il n’existe pas de procédure publique pour réclamer un pseudo inactif. Une marque enregistrée (INPI ou EUIPO) qui correspond exactement peut appuyer une demande, mais Instagram décide seul.')]
NUN=[('Geeft Instagram inactieve namen vrij?','Er is geen openbare procedure om een inactieve naam op te eisen. Een merk (BOIP of EUIPO) dat exact overeenkomt kan een verzoek ondersteunen, maar Instagram beslist zelf.')]
J=[('fr','compte-publicitaire-meta-restreint',FAD),('fr','compte-publicitaire-meta-demande-de-reexamen-quoi-ecrire',FAD[:1]),('fr','recuperer-compte-instagram',FAC),('fr','compte-facebook-desactive',FAC),('fr','pseudo-instagram',FUN),
('nl','advertentieaccount-terugkrijgen',NAD),('nl','advertentieaccount-bezwaar-wat-schrijven',NAD[:1]),('nl','facebook-account-terugkrijgen',NAC),('nl','instagram-account-terugkrijgen',NAC),('nl','instagram-gebruikersnaam-claimen',NUN)]
urls=[]
for l,s,it in J:
    u=add(l,s,qa(FRT if l=='fr' else NLT,it,A),A); urls+=[u] if u else []
print(bump_lastmod(urls),len(urls));open('/tmp/b12.txt','w').write('\n'.join(urls))
