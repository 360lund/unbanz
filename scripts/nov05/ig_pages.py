import sys,json,html; sys.path.insert(0,'scripts/nov05')
from uclaims import page
P=[]
HUB=('/username-claim-questions/','All username claim questions')
REL=[('/instagram-username-claim/','Instagram username claims'),('/inactive-instagram-username/','Inactive usernames'),('/trademark-username-claim/','Trademark claims'),('/instagram-username-claim-links-and-forms-directory/','Official links'),HUB]
def X(u,t=None): return '<a href="%s" rel="noopener" target="_blank">%s</a>'%(u,t or u.replace('https://',''))
L={'inactive':('Inactive username help article',X('https://help.instagram.com/513717858639392'),'Instagram’s own answer for a handle on an account that seems inactive: pick an available version. There is no request form.'),
 'tmhow':('Report a username for trademark',X('https://help.instagram.com/2039132876317734'),'How Instagram handles usernames that may infringe a trademark. Usernames are first-come, first-served.'),
 'tmwhat':('What is a trademark violation',X('https://help.instagram.com/101826856646059'),'What counts and what does not. Use of a mark unrelated to its goods or services is not a violation.'),
 'tmform':('Trademark Report Form',X('https://help.instagram.com/contact/230197320740525'),'The form rights owners file. Your name, email and the nature of the report are shared with the reported account.'),
 'imp':('Report impersonation',X('https://help.instagram.com/1291391774792379'),'In-app report for accounts pretending to be you, someone you represent or a business.'),
 'impform':('Impersonation form',X('https://help.instagram.com/contact/636276399721841'),'Web form when you cannot report from the app.'),
 'hacked':('Hacked account',X('https://www.instagram.com/hacked/'),'Start here if a hacker took the account or changed your username.'),
 'terms':('Instagram Terms of Use',X('https://help.instagram.com/581066165581870'),'Bans buying, selling or transferring accounts and usernames.'),
 'uspto':('USPTO',X('https://www.uspto.gov/trademarks'),'United States trademark office.'),
 'ukipo':('UKIPO',X('https://www.gov.uk/topic/intellectual-property/trade-marks','gov.uk trade marks'),'United Kingdom trade mark office.'),
 'cipo':('CIPO',X('https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en','Canadian Intellectual Property Office'),'Canada trademark office.'),
 'euipo':('EUIPO',X('https://www.euipo.europa.eu/'),'EU trade mark, one registration for all EU countries.'),
 'inpi':('INPI',X('https://www.inpi.fr/'),'France trademark office.'),
 'boip':('BOIP',X('https://www.boip.int/'),'Benelux office: Netherlands, Belgium and Luxembourg.'),
 'wipo':('WIPO Madrid System',X('https://www.wipo.int/madrid/en/'),'International registrations that designate several countries.')}
def table(*keys,title='Official links'):
  return ('links',title,'<div class="table-wrap"><table><thead><tr><th>Link</th><th>What it is for</th></tr></thead><tbody>'+''.join('<tr><td><strong>%s</strong><br>%s</td><td>%s</td></tr>'%L[k] for k in keys)+'</tbody></table></div>')
def A(slug,title,desc,h1,lead,answer,cards,secs,faqs,rel=None,tbl=None):
  ids=[x[0] for x in secs]
  secs=secs+[GLANCE]+([] if 'before' in ids else [B0])+([] if 'eu' in ids else [EU])
  if tbl: secs=secs+[table(*tbl)]
  P.append(page(slug,title,desc,h1,lead,answer,secs,faqs,'Instagram',(rel or [])+REL,cards=cards))
GLANCE=('glance','Instagram username routes at a glance','<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Official route</th><th>What decides it</th></tr></thead><tbody><tr><td>Handle on an inactive account</td><td>None by itself; Instagram suggests a variation</td><td>Whether another route applies</td></tr><tr><td>Handle uses your brand</td><td>Trademark Report Form</td><td>A registered mark and related use</td></tr><tr><td>Account pretends to be you</td><td>Impersonation report</td><td>Proof of identity or business</td></tr><tr><td>Your own handle was taken in a hack</td><td>instagram.com/hacked, then a report</td><td>Proof the handle was yours</td></tr><tr><td>Handle on a deleted account</td><td>Wait; first-come, first-served</td><td>Deletion finishing</td></tr></tbody></table></div><p>Usernames on Instagram are first-come, first-served and cannot be reserved. No service, including ours, has special access.</p>')
exec(open('scripts/nov05/ig_content.py').read())
json.dump(P,open('/tmp/ig.json','w'),ensure_ascii=False); print(len(P))
