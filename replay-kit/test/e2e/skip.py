import json
from playwright.sync_api import sync_playwright
from common import *
def run(name, init, ua=UA_D, path="/", expect_rp=False):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        ctx = b.new_context(user_agent=ua); ctx.add_init_script(init)
        pg = ctx.new_page(); n=[]
        pg.on("request", lambda r: "/api/users/rp/" in r.url and n.append(1))
        pg.goto(BASE+path, wait_until="domcontentloaded"); pg.wait_for_load_state("load"); pg.wait_for_timeout(5000)
        ctx.close(); b.close()
    print(f"{name:34s} ingest requests={len(n)}  {'OK' if (len(n)>0)==expect_rp else 'UNEXPECTED'}")
run("normal (override for webdriver)", "localStorage.setItem('ubz_rec_test','1')", expect_rp=True)
run("owner flag ubz_norec=1", "localStorage.setItem('ubz_rec_test','1');localStorage.setItem('ubz_norec','1')")
run("?norec=1 param", "localStorage.setItem('ubz_rec_test','1')", path="/?norec=1")
run("test session ubz_test=1", "localStorage.setItem('ubz_test','1')")
run("webdriver (automation) no override", "0")
run("bot UA (webdriver masked, no override)", "Object.defineProperty(navigator,\"webdriver\",{get:()=>false})", ua="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
run("real UA, webdriver masked (control)", "Object.defineProperty(navigator,\"webdriver\",{get:()=>false})", expect_rp=False)
run("/users/ page", "localStorage.setItem('ubz_rec_test','1')", path="/users/")
run("HeadlessChrome UA", "Object.defineProperty(navigator,\"webdriver\",{get:()=>false})", ua=UA_D.replace("Chrome/","HeadlessChrome/"))
