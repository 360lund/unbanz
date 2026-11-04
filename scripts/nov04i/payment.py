# Card-only payment wording (BBB flags crypto). Idempotent.
import re,glob
R=[('"Credit Card, Cryptocurrency"','"Credit Card"'),('"paymentAccepted": "Credit Card, Cryptocurrency"','"paymentAccepted": "Credit Card"'),
(' Card and crypto accepted.',' Card payment accepted.'),(' Payment is by card or crypto.',' Payment is by card.'),
('Do I have to pay Unbanz in crypto?','How do I pay Unbanz?'),
('No. You can pay by card or by crypto, whichever you prefer. Nothing is charged for asking.','By card. Nothing is charged for asking.'),
(' If someone says they’re Unbanz and will only take crypto, email team@unbanz.com to check.',' If someone says they’re Unbanz and asks for any other kind of payment, email team@unbanz.com to check.'),
(' You can pay by card or by crypto, whichever you prefer.',' You pay by card.'),('Yes. Card and crypto are both accepted, and you pick.','Yes. Card is how you pay.'),
('You pay only by card or crypto,','You pay by card,'),('Unbanz takes card or crypto only.','Unbanz takes card payment.'),
('Unbanz accepts card and crypto, so you choose.','Unbanz takes card payment.'),('Pay by card or crypto.','Pay by card.'),('By card or crypto.','By card.'),
('Card or crypto, your choice.','By card.'),('Card or crypto.','By card.'),('Payment by card or crypto.','Payment by card.'),('Card or crypto, whichever you prefer.','By card.'),
('Card or crypto only.','By card.'),('Card and crypto are both accepted and the client picks.','Payment is by card.'),('card and crypto accepted)','card payment)'),
('We accept card and crypto; the method is agreed in your chat or email first.','Payment is by card, agreed in your chat or email first.'),
('Payment: card or crypto.','Payment: card.'),('How do I pay? By card or crypto.','How do I pay? By card.'),('Do I have to pay Unbanz in crypto? No.','How do I pay Unbanz? By card.'),
('You pay for a clear service, by card or crypto.','You pay for a clear service, by card.'),('We accept card and crypto.','We accept card payment.'),
('Unbanz: never asks for logins, and takes card or crypto.','Unbanz: never asks for logins, and takes card payment.'),('final call; card or crypto;','final call; payment by card;'),
('card or crypto','card'),('Card or crypto','Card'),('card and crypto','card'),('Card and crypto','Card'),('crypto or card','card'),('Crypto or card','Card')]
QD=re.compile(r'<details><summary>Why does Unbanz accept crypto\?.*?</details>',re.S)
QJ=re.compile(r'\{"@type":"Question","name":"Why does Unbanz accept crypto\?".*?\}\},?')
ch=[]
for f in glob.glob('**/index.html',recursive=True)+['llms.txt','llms-full.txt']:
    if f.startswith(('users/','scripts/')): continue
    s=open(f).read();o=s
    for a,b in R: s=s.replace(a,b)
    s=QD.sub('',s);s=QJ.sub('',s);s=s.replace(',]',']')
    if s!=o: open(f,'w').write(s); ch.append(f)
print(len(ch))
