import sys,os,re,glob,zlib;sys.path.insert(0,'scripts/nov04l');from lib import add_section,bump_lastmod
A='sub-questions-2026'
T={'fr':dict(h='Questions fréquentes (2026)',
AC=('Où faire appel dans l’Espace comptes ?','Ouvrez l’Espace comptes Meta, puis Statut du compte ou la notification reçue, et utilisez l’option de contestation si elle s’affiche. Gardez une capture d’écran de la confirmation.'),
TIME=('Combien de temps prend un réexamen ?','Meta ne publie pas de délai. Évitez d’envoyer plusieurs demandes identiques ; suivez plutôt le statut dans l’Espace comptes et dans vos e-mails.'),
ACE=('Et si l’appel est refusé ?','Dans l’Union européenne, le règlement sur les services numériques (DSA) permet de saisir un organisme de règlement extrajudiciaire certifié, comme l’Appeals Centre Europe (appealscentre.eu), après la décision de Meta.'),
HACK=('Compte piraté puis désactivé : par où commencer ?','Commencez par instagram.com/hacked ou facebook.com/hacked, depuis un téléphone ou un ordinateur déjà utilisé sur le compte. En France, cybermalveillance.gouv.fr aide aussi les victimes de piratage.'),
ADR=('Où demander l’examen d’un compte publicitaire ?','Dans Meta Business Suite, ouvrez Qualité du compte (business.facebook.com/accountquality), choisissez le compte publicitaire et utilisez Demander un examen si le bouton apparaît.'),
ADT=('Faut-il ouvrir un nouveau compte publicitaire en attendant ?','Non. Ouvrir un autre compte ou déplacer les dépenses vers un nouveau profil peut être vu comme un contournement des systèmes. Suivez le statut dans Qualité du compte.'),
ADV=('Vérification de l’entreprise en attente : qu’est-ce qui aide ?','Des documents dont le nom et l’adresse correspondent exactement au portefeuille business, par exemple un extrait Kbis ou un avis de situation SIREN.')),
'nl':dict(h='Veelgestelde vragen (2026)',
AC=('Waar maak ik bezwaar in het Accountcentrum?','Open het Meta Accountcentrum, ga naar Accountstatus of de melding die je kreeg, en gebruik de bezwaaroptie als die zichtbaar is. Maak een screenshot van de bevestiging.'),
TIME=('Hoe lang duurt een beoordeling?','Meta noemt geen termijn. Stuur niet steeds hetzelfde verzoek opnieuw; volg de status in het Accountcentrum en in je e-mail.'),
ACE=('Wat als het bezwaar wordt afgewezen?','In de Europese Unie geeft de Digital Services Act (DSA) je het recht om na het besluit van Meta naar een gecertificeerde geschilbeslechtingsinstantie te gaan, zoals het Appeals Centre Europe (appealscentre.eu).'),
HACK=('Gehackt en daarna uitgeschakeld: waar begin ik?','Begin bij instagram.com/hacked of facebook.com/hacked, vanaf een telefoon of computer die je eerder op het account gebruikte. Bij oplichting kun je ook terecht bij de Fraudehelpdesk.'),
ADR=('Waar vraag ik een beoordeling van een advertentieaccount aan?','Open in Meta Business Suite Accountkwaliteit (business.facebook.com/accountquality), kies het advertentieaccount en gebruik Beoordeling aanvragen als die knop er staat.'),
ADT=('Moet ik intussen een nieuw advertentieaccount openen?','Nee. Een nieuw account openen of uitgaven naar een ander profiel verplaatsen kan worden gezien als het omzeilen van systemen. Volg de status in Accountkwaliteit.'),
ADV=('Bedrijfsverificatie in behandeling: wat helpt?','Documenten waarvan naam en adres precies overeenkomen met het bedrijfsportfolio, zoals een KvK-uittreksel.'))}
SKIP=re.compile(r'white-label|avis|reviews|contact|faq|veelgestelde|services|diensten|comment-ca-marche|hoe-het-werkt|prix|prijs|unbanz|sextor|sextortion|plainte|aangifte|over-ons|fiable|betrouwbaar|faux-hackers|oplichting|vertrouwelijk|confidentialite|ce-que-voit|wat-je-klant|white|rgpd|avg-|dsa|appeals-centre|^$')
urls=[]
for L,D in T.items():
    for f in sorted(glob.glob(L+'/*/index.html')):
        p=f[:-11];slug=p[len(L)+1:]
        if SKIP.search(slug): continue
        s=open(f).read()
        if 'noindex' in s[:3000] or re.search(r'id="[a-z-]*-2026"',s): continue
        if re.search(r'publicitaire|business|portefeuille|advertentie|bedrijfsportfolio',slug): it=['ADR','ADT','ADV']
        elif re.search(r'pirate|gehackt',slug): it=['HACK','AC','TIME']
        else: it=['AC','TIME','ACE']
        it=[D[k] for k in it if D[k][0] not in s]
        if not it: continue
        h=f'<h2 id="{A}">{D["h"]}</h2>'+''.join(f'<h3>{q}</h3><p>{a}</p>' for q,a in it)
        assert 'en cas de' not in h
        if add_section(p,h,anchor=A): urls.append(f'https://unbanz.com/{p}/')
print(bump_lastmod(urls),len(urls));open('/tmp/b29.txt','w').write('\n'.join(urls));print('\n'.join(urls))
