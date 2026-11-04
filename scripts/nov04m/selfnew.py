import sys;sys.path.insert(0,'scripts/nov04m');from clone import make;from loc import add
B='https://unbanz.com';EN='facebook-video-selfie-verification-stuck'
HF='<p>Si la vérification reste bloquée ou si la demande n’aboutit pas, voyez notre page <a href="/fr/compte-facebook-desactive/">compte Facebook désactivé</a>. Le prix vous est indiqué avant le début du travail, et votre mot de passe reste chez vous.</p>'
f=make('fr','faire-appel-instagram-desactive-delai','facebook-verification-selfie-video-bloquee',EN,
 'Vérification selfie vidéo Facebook bloquée | Unbanz',
 'La vidéo selfie demandée par Facebook ne passe pas ou reste en attente ? Ce qui bloque le plus souvent, quoi essayer et quand attendre.',
 'Selfie vidéo Facebook bloqué','Vérification par selfie vidéo Facebook bloquée : que faire ?',
 'Si la vidéo selfie de Facebook ne se charge pas, échoue ou reste « en cours d’examen », vérifiez d’abord l’éclairage, l’application à jour et la connexion, puis réessayez une seule fois. Si elle a bien été envoyée, attendez : la renvoyer plusieurs fois n’accélère rien.',
 [('causes','Ce qui bloque le plus souvent','<ul><li>Une application ou un navigateur pas à jour.</li><li>Une caméra refusée dans les autorisations du téléphone.</li><li>Un contre-jour, des lunettes de soleil ou une casquette.</li><li>Une connexion instable pendant l’envoi.</li></ul>'),
  ('essayer','Quoi essayer','<ol><li>Mettez l’application à jour ou essayez un autre navigateur.</li><li>Autorisez la caméra et fermez les autres applications.</li><li>Placez-vous face à une lumière douce et suivez les consignes à l’écran.</li><li>Réessayez une seule fois.</li></ol>'),
  ('attente','Si elle est « en cours d’examen »','<p>La vidéo a été reçue. Ne la renvoyez pas. Meta ne publie aucun délai ; voyez <a href="/fr/delai-appel-facebook-desactive/">combien de temps dure un appel Facebook</a>.</p>'),
  ('refus','Si elle est refusée','<p>Voyez <a href="/fr/compte-facebook-desactive-faire-appel/">faire appel d’un compte Facebook désactivé</a>. En Europe, le <a href="/fr/droit-de-recours-dsa-meta/">recours prévu par le DSA</a> peut être une piste.</p>')],HF,
 [('Pourquoi Facebook demande-t-il une vidéo selfie ?','Pour vérifier qu’une vraie personne est derrière le compte, par exemple après une activité inhabituelle ou lors d’un appel.'),
  ('Puis-je renvoyer la vidéo si rien ne se passe ?','Si elle a été envoyée, non : attendez. Si l’envoi a échoué, réessayez une fois après avoir vérifié l’éclairage et la connexion.'),
  ('Quelqu’un d’autre peut-il faire la vidéo pour moi ?','Non. Ce doit être votre propre visage. Ne donnez jamais votre mot de passe ni vos codes.')],
 [('/fr/compte-facebook-desactive-faire-appel/','Faire appel (Facebook)'),('/fr/delai-appel-facebook-desactive/','Délai d’un appel Facebook'),('/fr/instagram-verification-selfie-video/','Selfie vidéo Instagram'),('/fr/compte-facebook-desactive/','Compte Facebook désactivé')])
HN='<p>Blijft de verificatie hangen of lukt het niet, kijk dan op onze pagina <a href="/nl/facebook-account-terugkrijgen/">Facebook-account terugkrijgen</a>. We noemen de prijs in het gesprek, voordat het werk begint, en je wachtwoord blijft bij jou.</p>'
n=make('nl','hoe-lang-duurt-instagram-bezwaar','facebook-videoselfie-verificatie-blijft-hangen',EN,
 'Facebook videoselfie-verificatie blijft hangen | Unbanz',
 'Lukt de videoselfie voor Facebook niet of blijft die in behandeling? Wat het vaakst misgaat, wat je kunt proberen en wanneer je beter wacht.',
 'Videoselfie Facebook hangt','Facebook videoselfie-verificatie blijft hangen: wat nu?',
 'Laadt de videoselfie van Facebook niet, mislukt die of blijft die op ‘in behandeling’ staan, controleer dan eerst het licht, of de app is bijgewerkt en je verbinding, en probeer het één keer opnieuw. Is de video wel verstuurd, wacht dan: vaker insturen versnelt niets.',
 [('oorzaken','Wat het vaakst misgaat','<ul><li>Een verouderde app of browser.</li><li>Geen toestemming voor de camera in de telefooninstellingen.</li><li>Tegenlicht, een zonnebril of een pet.</li><li>Een wisselende verbinding tijdens het uploaden.</li></ul>'),
  ('proberen','Wat je kunt proberen','<ol><li>Werk de app bij of probeer een andere browser.</li><li>Geef de camera toestemming en sluit andere apps.</li><li>Ga met je gezicht naar zacht licht en volg de aanwijzingen.</li><li>Probeer het één keer opnieuw.</li></ol>'),
  ('wachten','Als het ‘in behandeling’ staat','<p>De video is ontvangen. Stuur hem niet opnieuw. Meta noemt geen termijn; lees <a href="/nl/hoe-lang-duurt-facebook-bezwaar/">hoe lang een Facebook-bezwaar duurt</a>.</p>'),
  ('afgewezen','Als hij wordt afgewezen','<p>Lees <a href="/nl/facebook-account-uitgeschakeld-bezwaar/">bezwaar tegen een uitgeschakeld Facebook-account</a>. In de EU kun je ook kijken naar <a href="/nl/dsa-recht-op-beroep-meta/">het beroepsrecht onder de DSA</a>.</p>')],HN,
 [('Waarom vraagt Facebook om een videoselfie?','Om te controleren dat er een echt persoon achter het account zit, bijvoorbeeld na ongebruikelijke activiteit of bij een bezwaar.'),
  ('Mag ik de video opnieuw sturen als er niets gebeurt?','Is hij verstuurd, dan niet: wacht. Is het uploaden mislukt, probeer het één keer opnieuw na het controleren van licht en verbinding.'),
  ('Kan iemand anders de video voor mij doen?','Nee. Het moet je eigen gezicht zijn. Geef nooit je wachtwoord of inlogcodes weg.')],
 [('/nl/facebook-account-uitgeschakeld-bezwaar/','Bezwaar Facebook-account'),('/nl/hoe-lang-duurt-facebook-bezwaar/','Hoe lang duurt een Facebook-bezwaar'),('/nl/instagram-videoselfie-verificatie/','Videoselfie Instagram'),('/nl/facebook-account-terugkrijgen/','Facebook-account terugkrijgen')],twins={'fr':f})
p='fr/facebook-verification-selfie-video-bloquee/index.html';s=open(p).read()
if n not in s: open(p,'w').write(s.replace('<link rel="alternate" hreflang="x-default"',f'<link rel="alternate" hreflang="nl" href="{n}"><link rel="alternate" hreflang="nl-NL" href="{n}"><link rel="alternate" hreflang="x-default"',1))
u=[f,n,B+'/'+EN+'/']
for sl in ['instagram-verification-selfie-video','compte-facebook-pirate-que-faire']:
    if add('fr',sl,'<h2 id="related-2026">Voir aussi (2026)</h2><p><a href="/fr/facebook-verification-selfie-video-bloquee/">Selfie vidéo Facebook bloqué</a> : causes fréquentes et quoi essayer.</p>','related-2026'): u.append(f'{B}/fr/{sl}/')
for sl in ['facebook-account-gehackt','facebook-account-terugkrijgen']:
    if add('nl',sl,'<h2 id="related-2026">Zie ook (2026)</h2><p><a href="/nl/facebook-videoselfie-verificatie-blijft-hangen/">Videoselfie voor Facebook blijft hangen</a>: oorzaken en wat je kunt proberen.</p>','related-2026'): u.append(f'{B}/nl/{sl}/')
open('/tmp/b19.txt','w').write('\n'.join(u));print(u)
