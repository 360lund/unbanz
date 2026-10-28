import json, gzip, urllib.request, urllib.error, time, secrets
from common import *
def post(qs, body, ua=UA_D, headers=None, base=BASE):
    h={"User-Agent":ua,"Content-Type":"text/plain"}; h.update(headers or {})
    r=urllib.request.Request(base+"/api/users/rp/?"+qs, data=body, headers=h, method="POST")
    try: return urllib.request.urlopen(r).status
    except urllib.error.HTTPError as e: return e.code
now=int(time.time()*1000)
ev=lambda n,t0=now:[{"type":4 if i==0 else 3,"timestamp":t0+i*10,"data":{}} for i in range(n)]
def q(s,g="aaaa",i=0,z=0,n=3,x=1,a=now,b=now+100): return f"s={s}&g={g}&i={i}&z={z}&x={x}&a={a}&b={b}&n={n}"
# make a real visit row via tracker
import urllib.parse
sid="abuse"+secrets.token_hex(6)
t=urllib.request.Request(BASE+"/api/t/", data=json.dumps({"e":"view","id":sid,"x":1,"p":"/","landing":"/","ref":"","dev":"Desktop"}).encode(), headers={"User-Agent":UA_D,"Content-Type":"application/json","Origin":BASE})
try: print("visit create", urllib.request.urlopen(t).status)
except Exception as e: print("visit create err", e)
body=json.dumps(ev(3)).encode()
print("valid plain json        ->", post(q(sid),body))
print("valid gzip              ->", post(q(sid,i=1,z=1),gzip.compress(body)))
print("unknown session (404)   ->", post(q("nosuchsession123"),body))
print("bot UA (204 ignored)    ->", post(q(sid,i=2),body,ua="Googlebot/2.1"))
print("bad json (400)          ->", post(q(sid,i=3),b"not json"))
print("count mismatch (400)    ->", post(q(sid,i=3,n=9),body))
print("bad session id (400)    ->", post(q("../../x"),body))
print("oversize 500KB (413)    ->", post(q(sid,i=4),b"x"*500000))
bomb=gzip.compress(json.dumps(ev(1)+[{"type":3,"timestamp":now,"data":{"x":"a"*30_000_000}}]).encode())
print("gzip bomb (413/400)     ->", post(q(sid,i=5,z=1,n=2),bomb))
print("events w/o type (400)   ->", post(q(sid,i=6),json.dumps([{"a":1},{"a":2},{"a":3}]).encode()))
print("stale timestamps (400)  ->", post(q(sid,i=7,a=1000,b=2000),json.dumps(ev(3,1000)).encode()))
print("GET not allowed         ->", (lambda: (urllib.request.urlopen(urllib.request.Request(BASE+"/api/users/rp/?"+q(sid)))).status)() if False else "skipped")
codes=[post(q(sid,i=10+k),body) for k in range(40)]
print("flood 40 chunks codes   ->", {c:codes.count(c) for c in set(codes)})
tok=login()
print("replays no auth         ->", urllib.request.urlopen(urllib.request.Request(BASE+"/api/users/replays/")).status if False else None)
try: urllib.request.urlopen(urllib.request.Request(BASE+"/api/users/replays/"))
except urllib.error.HTTPError as e: print("replays w/o auth        ->", e.code)
try: urllib.request.urlopen(urllib.request.Request(BASE+"/api/users/replays/?sid="+sid))
except urllib.error.HTTPError as e: print("replay fetch w/o auth   ->", e.code)
# delete via DELETE needs same-origin
d=urllib.request.Request(BASE+"/api/users/replays/?sid="+sid, method="DELETE", headers={"X-Users-Token":tok})
try: print("DELETE no origin        ->", urllib.request.urlopen(d).status)
except urllib.error.HTTPError as e: print("DELETE no origin        ->", e.code)
d=urllib.request.Request(BASE+"/api/users/replays/?sid="+sid, method="DELETE", headers={"X-Users-Token":tok,"Origin":BASE})
print("DELETE same-origin      ->", urllib.request.urlopen(d).status)
