import json, gzip, struct
from playwright.sync_api import sync_playwright
from common import *
SECRETS = ["TopSecretPassw0rd!", "visible-name-XYZ", "textarea-secret-QQQ", "select-me-ZZZ"]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    ctx = b.new_context(viewport={"width":1200,"height":800}, user_agent=UA_D)
    ctx.add_init_script("localStorage.setItem('ubz_rec_test','1')")
    pg = ctx.new_page()
    pg.goto(BASE+"/", wait_until="domcontentloaded"); pg.wait_for_load_state("load"); pg.wait_for_timeout(2500)
    sid = pg.evaluate("JSON.parse(sessionStorage.getItem('ubz1')).id")
    # inject a form post-snapshot AND ensure initial-DOM inputs too: add before reload? add now (mutation path)
    pg.evaluate("""() => { const f=document.createElement('form'); f.id='pf'; f.style.cssText='position:fixed;top:10px;left:10px;z-index:99999;background:#fff;padding:10px';
      f.innerHTML='<input id=pw type=password value=TopSecretPassw0rd!><input id=tx type=text name=email><textarea id=ta></textarea><select id=sl><option>a<option>select-me-ZZZ</select><input id=ck type=checkbox><input id=pre type=text value=visible-name-XYZ>'; document.body.appendChild(f) }""")
    pg.wait_for_timeout(600)
    pg.fill("#pw","TopSecretPassw0rd!"); pg.fill("#tx","visible-name-XYZ"); pg.fill("#ta","textarea-secret-QQQ"); pg.select_option("#sl","select-me-ZZZ"); pg.check("#ck")
    pg.keyboard.type("xyz"); pg.wait_for_timeout(8000)
    ctx.close()
tok = login()
buf = get("/api/users/replays/?sid="+sid, tok)
o=0; raw=b""
while o+5<=len(buf):
    gz=buf[o]; n=struct.unpack(">I",buf[o+1:o+5])[0]; d=buf[o+5:o+5+n]; o+=5+n
    raw += gzip.decompress(d) if gz else d
txt = raw.decode("utf8","replace")
print("bytes", len(txt), "events~", txt.count('"timestamp"'))
for s in SECRETS: print(s, "LEAK" if s in txt else "ok")
print("password type present:", '"type":"password"' in txt)
import re
print("sample masked:", re.findall(r'"id=pw[^}]{0,0}', txt)[:1], txt.count("****")>0)
evs=[]
for part in re.findall(r'\{"type":3,"data":\{"source":5,[^}]*\}', txt): evs.append(part)
print("input events:", [e[:120] for e in evs][:8])
