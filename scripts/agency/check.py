import re,sys
BAN=[r'\bcases?\b',r'we review',r'fixed.price',r'fast turnaround',r'guarantee',r'garantí',r'garanti',r'turnaround',r'\bwithin a (week|day)',r'\d+\s*[-–]\s*\d+ days',r'trustpilot',r'aggregaterating',r'"review"',r'\+44',r'7723',r'whatsapp ban',r'bypass',r'[\U0001F300-\U0001FAFF\u2600-\u27BF]',r'—',r'\bfast\b',r'\bseamless',r'leverage',r'robust',r'cutting-edge',r'\bsolution\b']
def scan(text,name):
    bad=[]
    for p in BAN:
        for m in re.finditer(p,text,re.I):
            bad.append((p,text[max(0,m.start()-40):m.end()+40].replace('\n',' ')))
    return bad
if __name__=='__main__':
    import glob
    for f in sys.argv[1:]:
        for p,c in scan(open(f).read(),f): print(f,p,c)
