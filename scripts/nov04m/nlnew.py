import sys;sys.path.insert(0,'scripts/nov04m');from clone import make
H='<p>Lukt het niet met de officiële knop, of heb je liever hulp? Kijk op onze pagina <a href="/nl/facebook-account-terugkrijgen/">Facebook-account terugkrijgen</a>. We noemen de prijs in het gesprek, voordat het werk begint, en je wachtwoord blijft bij jou.</p>'
u=make('nl','hoe-lang-duurt-instagram-bezwaar','hoe-lang-duurt-facebook-bezwaar','how-long-does-a-facebook-appeal-take',
 'Hoe lang duurt een Facebook-bezwaar? | Unbanz',
 'Facebook noemt geen vaste termijn voor bezwaren: een antwoord kan binnen een paar dagen of pas na weken komen. Wat je tijdens het wachten kunt doen.',
 'Hoe lang duurt een Facebook-bezwaar','Facebook-account uitgeschakeld: hoe lang duurt het bezwaar?',
 'Facebook noemt geen vaste termijn voor bezwaren: een antwoord kan binnen een paar dagen of pas na weken komen, en een identiteitscontrole kan het wachten verlengen. Dien het bezwaar niet opnieuw in, houd het e-mailadres van het account in de gaten (ook spam) en bewaar een screenshot van de bevestiging.',
 [('wacht','Wat je kunt verwachten','<p>Er is geen officiële termijn. Hoe lang het duurt hangt af van de reden, een eventuele identiteitscontrole en de drukte. Niemand kan een datum beloven.</p>'),
  ('volgen','Waar je het bezwaar volgt','<p>Log in op Facebook: het scherm van de uitschakeling laat meestal zien hoe het ervoor staat. Kijk ook in het Accountcentrum en in de mailbox van het account, ook bij spam.</p>'),
  ('selfie','Als om een videoselfie of ID wordt gevraagd','<p>Stuur die één keer, met goed licht en een leesbaar document op de naam van het account. Blijft het scherm hangen, wacht dan voordat je het opnieuw probeert: vaker insturen versnelt niets.</p>'),
  ('doen','Wat je tijdens het wachten kunt doen','<ul><li>Dien het bezwaar niet opnieuw in.</li><li>Maak geen nieuw account om de beslissing te omzeilen.</li><li>Wees voorzichtig met wie een direct antwoord belooft.</li></ul>'),
  ('na','Als er niets gebeurt','<p>Wordt het bezwaar afgewezen of hoor je na weken niets, lees dan <a href="/nl/facebook-account-uitgeschakeld-bezwaar/">bezwaar tegen een uitgeschakeld Facebook-account</a>. In de EU kun je ook kijken naar <a href="/nl/dsa-recht-op-beroep-meta/">het beroepsrecht onder de DSA</a>.</p>')],H,
 [('Hoe lang duurt een Facebook-bezwaar?','Facebook noemt geen termijn. Het kan een paar dagen tot enkele weken duren, en niemand kan een datum beloven.'),
  ('Moet ik het bezwaar opnieuw indienen als ik niets hoor?','Nee. Opnieuw indienen versnelt niets. Bewaar de screenshot van de bevestiging en houd je e-mail in de gaten.'),
  ('Waar krijg ik het antwoord?','Meestal per e-mail op het adres van het account, en bij het inloggen op Facebook. Kijk ook in je spam.'),
  ('Kan een betaalde dienst het antwoord versnellen?','Geen externe dienst kan Meta een termijn opleggen. Wees voorzichtig met wie een direct antwoord belooft.')],
 [('/nl/facebook-account-uitgeschakeld-bezwaar/','Bezwaar Facebook-account'),('/nl/facebook-account-terugkrijgen/','Facebook-account terugkrijgen'),('/nl/hoe-lang-duurt-instagram-bezwaar/','Hoe lang duurt een Instagram-bezwaar'),('/nl/dsa-recht-op-beroep-meta/','DSA-beroep (EU)')],
 twins={'fr':'https://unbanz.com/fr/delai-appel-facebook-desactive/'})
print(u)
