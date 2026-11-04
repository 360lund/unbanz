import sys;sys.path.insert(0,'scripts/nov04m');from loc import add
F='<h2 id="related-2026">Voir aussi (2026)</h2><p><a href="/fr/delai-appel-facebook-desactive/">Combien de temps dure un appel Facebook</a> : délais, suivi et vérification d’identité.</p>'
N='<h2 id="related-2026">Zie ook (2026)</h2><p><a href="/nl/hoe-lang-duurt-facebook-bezwaar/">Hoe lang duurt een Facebook-bezwaar</a>: wachttijd, volgen en identiteitscontrole.</p>'
u=[]
for sl in ['compte-facebook-desactive-faire-appel','faire-appel-instagram-desactive-delai','compte-facebook-desactive']:
    if add('fr',sl,F,'related-2026'): u.append(f'https://unbanz.com/fr/{sl}/')
for sl in ['facebook-account-uitgeschakeld-bezwaar','hoe-lang-duurt-instagram-bezwaar','facebook-account-terugkrijgen']:
    if add('nl',sl,N,'related-2026'): u.append(f'https://unbanz.com/nl/{sl}/')
u+=['https://unbanz.com/fr/delai-appel-facebook-desactive/','https://unbanz.com/nl/hoe-lang-duurt-facebook-bezwaar/','https://unbanz.com/how-long-does-a-facebook-appeal-take/']
open('/tmp/b15.txt','w').write('\n'.join(u));print(len(u))
