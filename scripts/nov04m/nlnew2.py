import sys;sys.path.insert(0,'scripts/nov04m');from clone import make
B='https://unbanz.com'
H='<p>Lukt het niet met de officiële stappen, of heb je liever hulp? Kijk op onze pagina <a href="/nl/instagram-account-terugkrijgen/">Instagram-account terugkrijgen</a>. We noemen de prijs in het gesprek, voordat het werk begint, en je wachtwoord blijft bij jou.</p>'
u=make('nl','hoe-lang-duurt-instagram-bezwaar','instagram-videoselfie-verificatie','guides/instagram-video-selfie-verification',
 'Instagram videoselfie-verificatie: zo werkt het | Unbanz',
 'Instagram vraagt soms om een videoselfie om te bevestigen dat het account van jou is. Hoe je die opneemt, wat er misgaat en wat je daarna kunt doen.',
 'Videoselfie-verificatie Instagram','Instagram vraagt om een videoselfie: wat nu?',
 'Instagram vraagt soms om een korte videoselfie waarin je je hoofd draait, om te bevestigen dat er een echt persoon achter het account zit. Neem die één keer op, met goed licht en zonder filters, en wacht daarna het antwoord af. Opnieuw insturen versnelt niets.',
 [('wat','Wat de videoselfie is','<p>Een korte opname van je gezicht vanuit verschillende hoeken. Instagram gebruikt die om te controleren dat het account bij een echt persoon hoort, en volgens Meta wordt de video na de controle verwijderd.</p>'),
  ('opnemen','Zo neem je hem op','<ul><li>Zorg voor gelijkmatig licht van voren, geen tegenlicht.</li><li>Zet een eventuele pet of zonnebril af.</li><li>Houd de telefoon stil op ooghoogte en volg de aanwijzingen op het scherm.</li><li>Gebruik een stabiele verbinding en de nieuwste versie van de app.</li></ul>'),
  ('mis','Als het misgaat','<p>Blijft het scherm hangen of wordt de selfie afgewezen, wacht dan voordat je het opnieuw probeert. Staan er geen foto’s van jou op het account, dan kan de controle lastiger zijn. Zie ook <a href="/nl/instagram-bezwaar-afgewezen/">bezwaar afgewezen</a>.</p>'),
  ('wachten','Hoe lang het duurt','<p>Instagram noemt geen vaste termijn. Lees <a href="/nl/hoe-lang-duurt-instagram-bezwaar/">hoe lang een Instagram-bezwaar duurt</a> voor wat je tijdens het wachten kunt doen.</p>')],H,
 [('Waarom vraagt Instagram om een videoselfie?','Om te bevestigen dat er een echt persoon achter het account zit, bijvoorbeeld na verdachte activiteit of bij een bezwaar.'),
  ('Wat als er geen foto’s van mij op het account staan?','De controle kan dan lastiger zijn. Volg toch de stappen op het scherm en bewaar screenshots.'),
  ('Mag ik de videoselfie vaker insturen?','Probeer het één keer goed. Vaker insturen versnelt niets.'),
  ('Kan iemand anders de selfie voor mij doen?','Nee. Het moet je eigen gezicht zijn. Geef ook nooit je wachtwoord of inlogcodes aan iemand anders.')],
 [('/nl/instagram-account-uitgeschakeld/','Instagram-account uitgeschakeld'),('/nl/hoe-lang-duurt-instagram-bezwaar/','Hoe lang duurt een Instagram-bezwaar'),('/nl/instagram-bezwaar-afgewezen/','Bezwaar afgewezen'),('/nl/instagram-account-terugkrijgen/','Instagram-account terugkrijgen')],
 twins={'fr':B+'/fr/instagram-verification-selfie-video/','es':B+'/es/instagram-verificacion-selfie-en-video/','pt-br':B+'/pt-br/instagram-verificacao-selfie-em-video/'})
print(u)
