import sys;sys.path.insert(0,'scripts/nov04m');from loc import qa,add,bump_lastmod
from frnl import ACF,ACN,FRT,NLT,A
FR={
'instagram-verification-selfie-video':[
('L’écran « nous examinons vos informations » reste bloqué ?','Cela veut dire que le selfie a été reçu. N’en envoyez pas un autre sauf si Instagram le demande. Meta ne publie pas de délai.'),
('Le selfie vidéo est refusé : que changer ?','Une lumière douce et régulière, le visage entier visible, sans lunettes, casquette ni filtre, et des mouvements de tête lents. Le profil doit montrer au moins une photo nette de vous.'),
('Le selfie est-il public ?','Non. Meta indique que le selfie vidéo sert à la vérification et n’apparaît pas sur votre profil.')],
'compte-facebook-pirate-que-faire':[
('Piraté puis désactivé : quel ordre ?','D’abord facebook.com/hacked pour signaler le piratage, ensuite la contestation de la désactivation si un bouton apparaît. Sécurisez l’e-mail et le téléphone liés avant tout.'),
('Une plainte aide-t-elle l’appel ?','Meta n’en demande pas, mais un numéro de plainte (THESEE) ou un signalement 17Cyber est utile si de l’argent a été pris.'),
('Recours après un refus ?',ACF)],
'verification-entreprise-meta-kbis':[
('Quels documents passent le mieux ?','Un extrait Kbis récent ou un avis de situation SIREN, avec la raison sociale et l’adresse identiques à celles du portefeuille business. Un nom différent est une cause fréquente de refus.'),
('La vérification reste en attente : que faire ?','Ne renvoyez pas les mêmes documents plusieurs fois. Vérifiez dans le Centre de sécurité du Business Manager que le nom de domaine ou le numéro de téléphone indiqué fonctionne.')],
'instagram-appel-refuse':[
('Peut-on refaire appel après un refus ?','En général, non : une décision marquée comme définitive ne propose plus de bouton. Faites une capture d’écran de la décision et de sa date.'),
('Et ensuite ?',ACF+' L’Arcom ne tranche pas les contestations individuelles.')],
'pseudo-instagram-marque-deposee-inpi':[
('Une marque de l’Union européenne (EUIPO) suffit-elle ?','Elle peut appuyer la demande au même titre qu’une marque INPI. Instagram décide seul, et une marque ne donne pas automatiquement droit au pseudo.'),
('Faut-il un avocat ?','Pas pour le formulaire de signalement de marque d’Instagram. Un avocat peut aider si le titulaire actuel crée une vraie confusion avec votre marque.')],
'compte-instagram-supprime-ou-desactive':[
('Comment savoir si le compte est désactivé ou supprimé ?','Un compte désactivé affiche une notification à la connexion, souvent avec un bouton de contestation. Un compte supprimé n’accepte plus le mot de passe et le profil n’existe plus.'),
('Où vérifier l’état du compte ?','Paramètres, puis Espace comptes, puis Statut du compte, si un autre compte Meta lié est encore accessible.')],
}
NL={
'instagram-bezwaar-afgewezen':[
('Kun je opnieuw bezwaar maken na een afwijzing?','Meestal niet: bij een definitieve beslissing staat er geen knop meer. Maak een screenshot van de beslissing en de datum.'),
('En daarna?',ACN)],
'facebook-account-gehackt':[
('Gehackt en uitgeschakeld: welke volgorde?','Eerst facebook.com/hacked om de hack te melden, daarna bezwaar tegen de uitschakeling als er een knop verschijnt. Beveilig eerst je e-mail en telefoon.'),
('Helpt aangifte bij het bezwaar?','Meta vraagt er niet om, maar een aangiftenummer of een melding bij de Fraudehelpdesk is handig als er geld is weggenomen.'),
('Na een afwijzing?',ACN)],
'meta-bedrijfsverificatie-kvk-documenten':[
('Welke documenten werken het best?','Een recent KvK-uittreksel of btw-gegevens, met exact dezelfde naam en hetzelfde adres als in het bedrijfsportfolio. Een afwijkende naam is een veelvoorkomende reden voor afwijzing.'),
('Verificatie blijft hangen?','Stuur dezelfde documenten niet steeds opnieuw. Controleer in het Beveiligingscentrum van Business Manager of het opgegeven domein of telefoonnummer werkt.')],
'instagram-geen-bezwaarknop':[
('Waar staat de knop in Accountcentrum?','Instellingen, Accountcentrum, Accountstatus. Kun je niet inloggen, dan staat de knop meestal op het meldingsscherm na het inloggen.'),
('Geen knop en geen antwoord?',ACN)],
'instagram-gebruikersnaam-claimen-met-merkregistratie':[
('Werkt een EU-merk (EUIPO) net zo goed als een Benelux-merk?','Beide kunnen je verzoek ondersteunen. Instagram beslist zelf, en een merk geeft niet automatisch recht op de naam.'),
('Heb ik een advocaat nodig?','Niet voor het merkenformulier van Instagram. Een advocaat kan helpen als de huidige houder echt verwarring met je merk veroorzaakt.')],
'instagram-account-opgeschort-180-dagen':[
('Vanaf wanneer tellen de 180 dagen?','Vanaf de melding van de opschorting, volgens de datum die Instagram toont. Maak er een screenshot van.'),
('Wat gebeurt er na 180 dagen?','Zonder bezwaar kan het account definitief worden verwijderd. Na een afgewezen bezwaar: '+ACN)],
}
urls=[]
for s,it in FR.items():
    u=add('fr',s,qa(FRT,it,A),A); urls+= [u] if u else []
for s,it in NL.items():
    u=add('nl',s,qa(NLT,it,A),A); urls+= [u] if u else []
print(bump_lastmod(urls),len(urls));open('/tmp/b10.txt','w').write('\n'.join(urls))
