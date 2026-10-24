import sys, json, urllib.request, glob
ROOT='/workspace/site'
key=open(glob.glob(ROOT+'/*.txt')[0] if False else ROOT+'/bc75a36f7b6c87ab24b9175a1cb19f8e.txt').read().strip()
urls=[l.strip() for l in open(sys.argv[1]) if l.strip()]
body=json.dumps({"host":"unbanz.com","key":key,"keyLocation":f"https://unbanz.com/{key}.txt","urlList":urls}).encode()
for ep in ("https://api.indexnow.org/indexnow","https://www.bing.com/indexnow"):
    r=urllib.request.Request(ep,data=body,headers={'Content-Type':'application/json; charset=utf-8'})
    try:
        print(ep, urllib.request.urlopen(r,timeout=30).status)
    except Exception as e:
        print(ep, getattr(e,'code',str(type(e).__name__)))
