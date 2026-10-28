# -*- coding: utf-8 -*-
"""English white label agency pages (hub + one page per country), 2026-10-28."""
import html, os
from urllib.parse import quote
from oct28e_data import C, ORDER, REGIONS

DATE = '2026-10-28'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
def esc(s): return html.escape(s, quote=True)
def exists(slug): return os.path.exists(os.path.join(ROOT, slug, 'index.html'))
def A(u, t): return '<a href="%s">%s</a>' % (u, esc(t))
NICE = {'usa': 'United States', 'uk': 'United Kingdom', 'uae': 'United Arab Emirates'}
def official(c):
    return NICE.get(c['slug'], c['name'].replace('the ', '', 1) if c['name'].startswith('the ') else c['name'])
HUB = '/white-label-agency/'
def wl(slug): return '/white-label-agency-%s/' % slug

RELQ = [('/how-it-works/', 'How Unbanz works'), ('/faq/', 'Unbanz FAQ'), ('/refund-policy/', 'Payment and refund policy'), ('/is-unbanz-legit/', 'Is Unbanz legit?')]
SERVICES = [('/agency-ad-account-recovery/', 'Agency ad account recovery'), ('/instagram-account-recovery/', 'Instagram account recovery'),
            ('/facebook-account-recovery/', 'Facebook account recovery'), ('/instagram-username-claim/', 'Instagram username claim')]

# native twins (set in oct28e_native): slug -> [(lang, url, label)]
TWINS = {
 '': [('nl', '/nl/white-label-bureau/', 'In het Nederlands'), ('es', '/es/white-label-agencias/', 'En español'), ('pt-br', '/pt-br/white-label-agencias/', 'Em português'), ('fr', '/fr/white-label-agences/', 'En français')],
 'netherlands': [('nl', '/nl/white-label-bureau-nederland/', 'In het Nederlands')],
 'belgium': [('nl', '/nl/white-label-bureau-belgie/', 'In het Nederlands'), ('fr', '/fr/white-label-agences-belgique/', 'En français')],
 'france': [('fr', '/fr/white-label-agences-france/', 'En français')],
 'switzerland': [('fr', '/fr/white-label-agences-suisse/', 'En français')],
 'luxembourg': [('fr', '/fr/white-label-agences-luxembourg/', 'En français')],
 'spain': [('es', '/es/white-label-agencias-espana/', 'En español')],
 'brazil': [('pt-br', '/pt-br/white-label-agencias-brasil/', 'Em português')],
}

def meaning(c, v):
    n = c['name']
    if v == 0:
        return ('<h2 id="white-label">What white label means here</h2><p>You sell account recovery or username claims to your own clients, under your own name. '
                'Unbanz does the platform work in the background. In practice:</p><ul>'
                '<li>Your client deals with you. You stay the contact and keep the relationship.</li>'
                '<li>You send us the details by WhatsApp or email, and we tell you honestly if we can help.</li>'
                '<li>We prepare the appeal or username claim and send it through the platform’s official process.</li>'
                '<li>What you charge your client is up to you. Terms between you and Unbanz are agreed before work starts.</li>'
                '<li>Meta, or the platform concerned, makes the final decision. Nobody can promise an outcome.</li></ul>')
    if v == 1:
        return ('<h2 id="white-label">How the white label arrangement works</h2><p>The client sees your agency. Behind it, Unbanz handles the Instagram or Facebook side. '
                'For an agency in %s that means:</p><ul>'
                '<li>You keep the client relationship, the communication and the invoice to your client.</li>'
                '<li>Intake is by WhatsApp or email, between you and us.</li>'
                '<li>We handle the appeal or the username claim through the official process of the platform.</li>'
                '<li>The platform decides. We cannot promise the account or handle will come back, and neither can you.</li></ul>' % n)
    return ('<h2 id="white-label">Behind your brand</h2><p>White label is a simple split of work. You are the face to your client in %s. '
            'Unbanz is the specialist you hand the account problem to.</p><ul>'
            '<li><strong>You:</strong> talk to the client, collect their go-ahead and the details, and decide how to present the service.</li>'
            '<li><strong>Unbanz:</strong> prepares the appeal or username claim and files it through the official route, then keeps you updated.</li>'
            '<li><strong>The platform:</strong> Meta makes the final decision on every appeal and claim.</li></ul>' % n)

def before(c):
    return ('<h2 id="before">Before you message us</h2><p>Collect this from your client first. It saves a round of questions.</p><ul>'
            '<li>The username or profile link, and the email and phone number on the account.</li>'
            '<li>An unedited screenshot of the notice, and the date it appeared.</li>'
            '<li>A short note on what happened: hacked, disabled, suspended or a handle they want.</li>'
            '<li>The client’s go-ahead for you and Unbanz to act on their account. Never ask for their password or login codes.</li>'
            '<li>For a business account in %s: the %s.</li></ul>' % (c['name'], c['biz']))

def local(c):
    items = [('Notice language', c['lang']), ('Phone number', c['num']), ('Business details', 'Have the %s ready if the platform asks for proof the business is real.' % c['biz']),
             ('If fraud or blackmail is involved', c['fraud'] + ' That runs alongside the platform appeal.')]
    if c['legal']: items.append(('Platform rules', c['legal']))
    items.append(('Client data', c['priv'] + ' Send us only what the appeal needs.'))
    if c['ad']: items.append(('Advertising rules', c['ad'] + ' Meta’s own ad policies still apply on top.'))
    return ('<h2 id="local">Details that matter in %s</h2><p>These are the points that differ for clients based in %s.</p><ul>%s</ul>' %
            (c['name'], c['name'], ''.join('<li><strong>%s:</strong> %s</li>' % (esc(k), esc(v)) for k, v in items)))

def services(c):
    links = [A('/instagram-account-recovery-%s/' % c['slug'], 'Instagram recovery in %s' % c['name'])] if exists('instagram-account-recovery-%s' % c['slug']) else []
    if exists('facebook-account-recovery-%s' % c['slug']): links.append(A('/facebook-account-recovery-%s/' % c['slug'], 'Facebook recovery in %s' % c['name']))
    if exists('instagram-username-claim-%s' % c['slug']): links.append(A('/instagram-username-claim-%s/' % c['slug'], 'Username claims in %s' % c['name']))
    more = ('<p>Read the local guides first so you know what your client can do alone: %s.</p>' % ', '.join(links)) if links else ''
    return ('<h2 id="services">What you can hand over</h2><ul>'
            '<li><strong>Instagram and Facebook accounts</strong> that are disabled, suspended or hacked. See <a href="/instagram-account-recovery/">Instagram account recovery</a> and <a href="/facebook-account-recovery/">Facebook account recovery</a>.</li>'
            '<li><strong>Username claims</strong> for a client’s brand handle. See <a href="/instagram-username-claim/">Instagram username claim</a>. Our refund policy: 100% refund if a username claim fails.</li>'
            '<li><strong>Ad accounts</strong> that were restricted or disabled. See <a href="/agency-ad-account-recovery/">agency ad account recovery</a>.</li></ul>' + more)

def how(c):
    return ('<h2 id="how">How it works with Unbanz</h2><ol>'
            '<li>Message us on WhatsApp or email with the client’s username, a screenshot of the notice and the date. You do not need to name the client.</li>'
            '<li>We tell you honestly if we can help. Terms are agreed with you before any work starts.</li>'
            '<li>We prepare the appeal or username claim and send it through the platform’s official process.</li>'
            '<li>We keep you posted. You pass the update to your client in your own words.</li></ol>')

def whofor(c):
    return ('<h2 id="who-for">Who this is for</h2><ul>'
            '<li>Marketing and social media agencies in %s whose clients lose access to Instagram or Facebook.</li>'
            '<li>Resellers and freelancers who want an account recovery option to offer without building the know-how.</li>'
            '<li>Agencies that need a handle claimed for a client brand.</li>'
            '<li>Not for accounts that were really used to scam or abuse people.</li></ul>' % c['name'])

ORDERS = [('meaning', 'before', 'local', 'services', 'how', 'whofor'), ('meaning', 'local', 'before', 'how', 'services', 'whofor'), ('meaning', 'services', 'local', 'before', 'how', 'whofor')]

def faq(c):
    n = c['name']
    f = [('What does white label mean for an agency in %s?' % n,
          'You offer Instagram and Facebook account recovery and username claims to your clients under your own brand. You keep the client relationship, and Unbanz handles the appeal or claim behind the scenes. The platform makes the final decision.'),
         ('Does my client need to know Unbanz is involved?',
          'That is up to you. We work with you, not with your client, and you stay the point of contact. Intake is by WhatsApp or email between you and us.'),
         ('What should I collect from a client in %s before I contact Unbanz?' % n,
          'The username or profile link, an unedited screenshot of the notice with its date, the email and number on the account, and the client’s go-ahead. For a business account, also the %s. Never ask for a password.' % c['biz']),
         ('Can you promise the account or username will come back?',
          'No. Meta, or the platform concerned, makes the final decision, and nobody can promise an outcome. We tell you honestly if we can help, then prepare and send the appeal through the official process.'),
         ('Is there a refund policy for username claims?',
          'Yes. Our refund policy is a 100% refund if a username claim fails. The full wording is on the payment and refund policy page.'),
         ('What if a client in %s was hacked and money or blackmail is involved?' % n,
          c['fraud'] + ' Tell your client to report it, since that runs alongside the account appeal.')]
    return f

def build_country(slug, idx):
    c = C[slug]; n = c['name']; v = idx % 3
    sec = {'meaning': meaning(c, v), 'before': before(c), 'local': local(c), 'services': services(c), 'how': how(c), 'whofor': whofor(c)}
    body = [sec[k] for k in ORDERS[v]]
    tw = TWINS.get(slug, [])
    if tw: body.append('<p>%s</p>' % ' · '.join(A(u, t) for _, u, t in tw))
    neigh = [s for s in ORDER if C[s]['region'] == c['region'] and s != slug]
    i = neigh.index(ORDER[ORDER.index(slug) + 1]) if False else 0
    pos = [s for s in ORDER if C[s]['region'] == c['region']]
    k = pos.index(slug); nb = [pos[(k + 1) % len(pos)], pos[(k - 1) % len(pos)]]
    related = [(HUB, 'White label agency hub')]
    if exists('instagram-account-recovery-%s' % slug): related.append(('/instagram-account-recovery-%s/' % slug, 'Instagram recovery in %s' % n))
    if exists('facebook-account-recovery-%s' % slug): related.append(('/facebook-account-recovery-%s/' % slug, 'Facebook recovery in %s' % n))
    if exists('instagram-username-claim-%s' % slug): related.append(('/instagram-username-claim-%s/' % slug, 'Username claims in %s' % n))
    related += SERVICES + [(wl(s), 'White label in %s' % C[s]['name']) for s in nb] + [(u, t) for _, u, t in tw]
    answer = ('White label means your agency stays the face to the client while Unbanz handles the appeal or username claim behind the scenes. '
              'Agencies in %s send us the details by WhatsApp or email and keep the client relationship. The platform makes the final decision, and no outcome is promised.' % n)
    title = 'White Label Recovery for %s Agencies | Unbanz' % c['h1']
    desc = 'White label Instagram and Facebook account recovery and username claims for %s agencies. You keep the client, Unbanz handles the platform side.' % c['h1']
    wa = quote('Hey Unbanz, I run an agency in %s and want to talk about white label account recovery' % n, safe='')
    return dict(slug='white-label-agency-%s' % slug, title=title, desc=desc, lang='en-US', crumb='White label agency in %s' % n,
                h1='White label recovery for %s agencies.' % c['h1'],
                hero='Run an agency or a reselling business in %s? Offer Instagram and Facebook account recovery and username claims under your own brand, and hand the platform work to Unbanz.' % n,
                answer=answer, wa=wa, subj='White%20label%20agency', ws='unban', svc='White label account recovery for agencies in %s' % n,
                body=body, faq=faq(c), related=related, relq=RELQ, v2=True, area={'@type': 'Country', 'name': official(c)},
                cards=[('You keep the client', 'Your client deals with you, not with us. You stay the contact and you keep the relationship.'),
                       ('We do the platform work', 'You send the details by WhatsApp or email. We prepare the appeal or username claim and send it through the official process.'),
                       ('Checks for %s' % n, 'Phone formats, business details and where to report fraud differ by country. The sections below cover %s.' % n)],
                crumb_parent=('White label agency', HUB), country=slug)

def hub():
    sections = []
    for r in REGIONS:
        items = ''.join('<li>%s</li>' % A(wl(s), 'White label recovery for agencies in %s' % C[s]['name']) for s in ORDER if C[s]['region'] == r)
        sections.append('<h3>%s</h3><ul>%s</ul>' % (esc(r), items))
    body = [
     '<h2 id="white-label">What white label means here</h2><p>You sell account recovery or username claims to your own clients, under your own name. Unbanz does the platform work in the background. In practice:</p><ul>'
     '<li>Your client deals with you. You stay the contact and keep the relationship.</li>'
     '<li>You send us the details by WhatsApp or email, and we tell you honestly if we can help.</li>'
     '<li>We prepare the appeal or username claim and send it through the platform’s official process.</li>'
     '<li>What you charge your client is up to you. Terms between you and Unbanz are agreed before work starts.</li>'
     '<li>Meta, or the platform concerned, makes the final decision. Nobody can promise an outcome.</li></ul>',
     '<h2 id="who">Who it suits</h2><ul><li>Marketing and social media agencies whose clients lose access to Instagram or Facebook.</li><li>Resellers and freelancers who want an account recovery option without building the know-how.</li><li>Agencies that need a handle claimed for a client brand.</li><li>Not for accounts that were really used to scam or abuse people.</li></ul>',
     '<h2 id="services">What you can hand over</h2><ul>'
     '<li><strong>Instagram and Facebook accounts</strong> that are disabled, suspended or hacked. See <a href="/instagram-account-recovery/">Instagram account recovery</a> and <a href="/facebook-account-recovery/">Facebook account recovery</a>.</li>'
     '<li><strong>Username claims</strong> for a client’s brand handle. See <a href="/instagram-username-claim/">Instagram username claim</a>. Our refund policy: 100% refund if a username claim fails.</li>'
     '<li><strong>Ad accounts</strong> that were restricted or disabled. See <a href="/agency-ad-account-recovery/">agency ad account recovery</a>.</li></ul>',
     '<h2 id="how">How it works with Unbanz</h2><ol><li>Message us on WhatsApp or email with the client’s username, a screenshot of the notice and the date. You do not need to name the client.</li>'
     '<li>We tell you honestly if we can help. Terms are agreed with you before any work starts.</li>'
     '<li>We prepare the appeal or username claim and send it through the platform’s official process.</li>'
     '<li>We keep you posted. You pass the update to your client in your own words.</li></ol>',
     '<h2 id="countries">White label pages by country</h2><p>Each page covers the local points that matter when your client is based there: phone formats, business details, where to report fraud and the platform rules that apply.</p>' + ''.join(sections),
     '<h2 id="languages">In your language</h2><p>%s</p>' % ' · '.join(A(u, t) for _, u, t in TWINS['']),
    ]
    faqs = [('What is white label account recovery?', 'You offer Instagram and Facebook account recovery and username claims to your own clients under your brand. Unbanz handles the appeal or claim behind the scenes, and you keep the client relationship. The platform makes the final decision.'),
            ('Who is it for?', 'Marketing and social media agencies, resellers and freelancers whose clients lose access to an account or want a username claimed.'),
            ('How do I send a client’s details?', 'By WhatsApp on +1 934 201 2490 or by email to team@unbanz.com. Send the username, an unedited screenshot of the notice and its date. Never send a password.'),
            ('Can you promise the account will come back?', 'No. Meta, or the platform concerned, makes the final decision, and nobody can promise an outcome. We tell you honestly if we can help.'),
            ('Is there a refund policy for username claims?', 'Yes. Our refund policy is a 100% refund if a username claim fails. See the payment and refund policy page for the wording.')]
    wa = quote('Hey Unbanz, I run an agency and want to talk about white label account recovery', safe='')
    return dict(slug='white-label-agency', title='White Label Account Recovery for Agencies | Unbanz',
                desc='White label Instagram and Facebook account recovery and username claims for agencies and resellers. You keep the client, Unbanz does the platform work.',
                lang='en-US', crumb='White label agency', h1='White label account recovery for agencies.',
                hero='Offer Instagram and Facebook account recovery and username claims to your clients under your own brand. Unbanz handles the platform side, and you keep the client.',
                answer='White label means your agency stays the face to the client while Unbanz handles the appeal or username claim behind the scenes. You send the details by WhatsApp or email and keep the client relationship. The platform makes the final decision, and no outcome is promised.',
                wa=wa, subj='White%20label%20agency', ws='unban', svc='White label account recovery for agencies', body=body, faq=faqs,
                related=[('/account-recovery-by-country/', 'Recovery by country')] + SERVICES + [(wl(s), 'White label in %s' % C[s]['name']) for s in ('uk', 'usa', 'canada', 'australia', 'germany', 'uae')] + [(u, t) for _, u, t in TWINS['']],
                relq=RELQ, v2=True, area=None,
                cards=[('You keep the client', 'Your client deals with you, not with us. You stay the contact and you keep the relationship.'),
                       ('We do the platform work', 'You send the details by WhatsApp or email. We prepare the appeal or username claim and send it through the official process.'),
                       ('Meta decides', 'We use the platform’s official process. Meta makes the final decision on every appeal and claim.')],
                crumb_parent=None, country='')

def pages():
    return [hub()] + [build_country(s, i) for i, s in enumerate(ORDER)]
