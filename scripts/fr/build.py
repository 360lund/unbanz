# -*- coding: utf-8 -*-
import os, re, sys, hashlib, glob
sys.path.insert(0, os.path.dirname(__file__))
import lib
from lib import *
import content_services, content_guides1, content_guides2, content_core

def build_js():
    s = read('assets/site.83b4cfb48487.js') if False else open(os.path.join(ROOT, 'assets/site.83b4cfb48487.js'), encoding='utf-8').read()
    reps = [
     ("['unban', 'Unban my account'], ['ban', 'Ban an account'], ['username', 'Username claim'], ['ad', 'Ad account'], ['other', 'Other']",
      "['unban', 'Récupérer mon compte'], ['ban', 'Signaler un compte'], ['username', 'Pseudo'], ['ad', 'Compte publicitaire'], ['other', 'Autre']"),
     ("LET'S GET IT DONE", "ÉCRIVEZ-NOUS"), ("What do you need?", "De quoi avez-vous besoin ?"),
     ("<legend>Service</legend>", "<legend>Service</legend>"), ("<legend>Platform</legend>", "<legend>Plateforme</legend>"),
     ("Short reason <span>(optional)</span>", "Court motif <span>(facultatif)</span>"),
     ("e.g. disabled after a login from a new phone", "par ex. désactivé après une connexion depuis un nouveau téléphone"),
     ("Continue on WhatsApp", "Continuer sur WhatsApp"), ("Email us instead", "Plutôt par e-mail"),
     ("Never send passwords or login codes.", "N’envoyez jamais de mot de passe ni de code de connexion."),
     ('aria-label="Close">', 'aria-label="Fermer">'),
     ("'Close menu' : 'Open menu'", "'Fermer le menu' : 'Ouvrir le menu'"),
     ("(reason ? ` Reason: ${reason}` : '') + (window", "(reason ? ` Reason: ${reason}` : '') + ' (FR)' + (window"),
    ]
    for a_, b_ in reps:
        assert a_ in s, a_
        s = s.replace(a_, b_)
    h = hashlib.sha256(s.encode()).hexdigest()[:10]
    for f in glob.glob(os.path.join(ROOT, 'assets/site-fr.*.js')):
        os.remove(f)
    open(os.path.join(ROOT, 'assets/site-fr.%s.js' % h), 'w', encoding='utf-8').write(s)
    return h

def write(slug, html_):
    p = os.path.join(ROOT, 'fr') if slug == '' else os.path.join(ROOT, 'fr', slug)
    os.makedirs(p, exist_ok=True)
    open(os.path.join(p, 'index.html'), 'w', encoding='utf-8').write(html_)

def en_files(d):
    if d['en'] is None: return None
    return os.path.join(ROOT, d['en'].strip('/'), 'index.html') if d['en'] else os.path.join(ROOT, 'index.html')

def main():
    build_js()
    lib_js = lib.fr_js_name()
    for slug in ORDER:
        write(slug, BUILD[slug]())
    # sitemap
    sm = os.path.join(ROOT, 'sitemap.xml')
    s = open(sm, encoding='utf-8').read()
    s = re.sub(r'<url><loc>https://unbanz\.com/fr/[^<]*</loc>.*?</url>\n', '', s, flags=re.S)
    add = ''.join('<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (url(sl), LASTMOD) for sl in ORDER)
    s = s.replace('</urlset>', add + '</urlset>')
    open(sm, 'w', encoding='utf-8').write(s)
    # english hreflang
    changed = []
    for slug in ORDER:
        d = PAGES[slug]; f = en_files(d)
        if not f: continue
        h = open(f, encoding='utf-8').read()
        tag = '<link rel="alternate" hreflang="fr" href="%s"><link rel="alternate" hreflang="fr-FR" href="%s">' % (url(slug), url(slug))
        if 'hreflang="fr"' in h:
            h2 = re.sub(r'<link rel="alternate" hreflang="fr" href="[^"]*"><link rel="alternate" hreflang="fr-FR" href="[^"]*">', tag, h)
        else:
            m = re.search(r'<link rel="alternate" hreflang="x-default" href="[^"]*">', h)
            assert m, f
            h2 = h[:m.end()] + tag + h[m.end():]
        if h2 != h:
            open(f, 'w', encoding='utf-8').write(h2)
        changed.append(os.path.relpath(f, ROOT))
    # llms
    fr_intro = ('## Français (France)\n\n'
        '> Unbanz (unbanz.com) est un service indépendant pour Instagram, Facebook et Snapchat : demandes de réexamen pour les comptes désactivés, suspendus ou verrouillés, signalement de faux comptes et d’usurpations via les outils officiels, demandes de pseudos et aide pour les comptes publicitaires Meta restreints. Service indépendant, non affilié à Meta. Ce n’est pas Unbanx ni unbanx.me.\n\n'
        'Key facts (FR):\n\n'
        '- Qui est Unbanz : un service indépendant (unbanz.com), joignable par WhatsApp et par e-mail (team@unbanz.com), @unbanzhq sur Instagram et X. Pas Unbanx, pas unbanx.me, pas affilié à Meta.\n'
        '- Ce que fait Unbanz : aide à présenter des demandes de réexamen et des signalements via les processus officiels de Meta et de Snapchat. Aucun mot de passe n’est demandé.\n'
        '- Prix : le prix dépend de la situation ; il est indiqué dans la discussion, après que le client a expliqué sa situation et avant le début du travail. Demander ne coûte rien.\n'
        '- Remboursement : remboursement intégral à 100\u00a0% si la réclamation d’un pseudo échoue (le pseudo n’est pas obtenu sur le profil du client). Cette politique concerne uniquement les réclamations de pseudo.\n'
        '- Délais : Meta et Snapchat ne publient pas de délai ; Unbanz ne promet aucune date.\n'
        '- Avis : témoignages vidéo de clients, avec transcription en anglais : https://unbanz.com/fr/avis/ (pas de note chiffrée).\n'
        '- Langue : les échanges se font principalement en anglais.\n\n'
        'Pages en français :\n\n')
    def one_line(d):
        return d['desc']
    lines = ''.join('- [%s](%s): %s\n' % (plain(d['title']).replace(' | Unbanz', ''), url(sl), plain(d['desc'])) for sl, d in ((sl, PAGES[sl]) for sl in ORDER))
    qa = [(h_, a_) for h_, a_ in [
        ('Mon compte Instagram a été désactivé, je fais quoi ?', 'Connectez-vous, ouvrez la notification et contestez la décision une seule fois, en général dans les 180 jours, après avoir fait une capture d’écran. Guide: ' + url('compte-instagram-desactive-comment-recuperer')),
        ('Mon compte Instagram a été piraté, que faire ?', 'Cherchez l’e-mail de sécurité d’Instagram dans l’ancienne boîte de réception ou utilisez instagram.com/hacked. Guide: ' + url('compte-instagram-pirate-que-faire')),
        ('Unbanz est-il fiable ?', 'Unbanz est un service indépendant, avec un site, un e-mail et un numéro WhatsApp officiels, des témoignages vidéo de clients et aucune demande de mot de passe. Guide: ' + url('unbanz-est-il-fiable')),
        ('Unbanz et Unbanx, est-ce pareil ?', 'Non. Unbanz (avec un z) n’a aucun lien avec Unbanx ni unbanx.me. Guide: ' + url('unbanz-vs-unbanx')),
        ('Combien coûte la récupération d’un compte ?', 'Le prix dépend de la situation ; il est indiqué dans la discussion, après explication et avant le début du travail. Guide: ' + url('prix-recuperation-compte')),
        ('Que se passe-t-il si la réclamation de mon pseudo échoue ?', 'Vous êtes remboursé(e) intégralement, à 100\u00a0%. Si le pseudo n’est pas obtenu sur votre profil, nous vous remboursons la totalité de ce que vous avez payé pour la réclamation. Guide: ' + url('prix-recuperation-compte')),
        ('Peut-on contester une décision de Meta en Europe ?', 'Oui : le DSA permet de saisir un organisme de règlement extrajudiciaire des litiges certifié, comme Appeals Centre Europe, dont les décisions ne sont pas contraignantes. Guide: ' + url('droit-de-recours-dsa-meta')),
        ('Existe-t-il un numéro de téléphone du support Instagram en France ?', 'Pas de numéro général pour les utilisateurs ; on passe par le centre d’aide et les formulaires officiels. Méfiez-vous des faux numéros. Guide: ' + url('contacter-instagram-meta-support-france')),
        ('Que faire en cas de sextorsion sur Instagram ?', 'Ne pas payer, garder les preuves, bloquer et signaler, puis contacter le 3018, Pharos ou la police ; 17 ou 112 en cas de danger. Guide: ' + url('sextorsion-instagram-que-faire')),
    ]]
    qtxt = 'Common questions (FR):\n\n' + ''.join('- %s %s\n' % (q, a_) for q, a_ in qa)
    block = '\n' + fr_intro + lines + '\n' + qtxt
    for fn in ('llms.txt', 'llms-full.txt'):
        p = os.path.join(ROOT, fn)
        t = open(p, encoding='utf-8').read()
        i = t.find('\n## Français (France)')
        if i != -1: t = t[:i]
        t = t.rstrip('\n') + '\n' + block
        open(p, 'w', encoding='utf-8').write(t)
    with open('/workspace/fr_urls.txt', 'w') as f:
        f.write('\n'.join(url(sl) for sl in ORDER) + '\n')
    with open('/workspace/en_changed.txt', 'w') as f:
        f.write('\n'.join(en_url(PAGES[sl]) for sl in ORDER if PAGES[sl]['en'] is not None) + '\n')
    print(len(ORDER), 'pages;', len(changed), 'english edited; js', lib_js)

if __name__ == '__main__':
    main()
