import sys, json
from playwright.sync_api import sync_playwright
from common import *
errs=[]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    ctx = b.new_context(viewport={"width":1360,"height":860}, user_agent=UA_D, timezone_id="Asia/Karachi")
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errs.append("pageerror: "+str(e)))
    pg.on("console", lambda m: m.type=="error" and errs.append("console: "+m.text[:200]))
    pg.goto(BASE+"/users/", wait_until="domcontentloaded")
    pg.fill("#luser","harness-user"); pg.click("#lform button"); pg.wait_for_selector("#app:not([hidden])"); pg.wait_for_timeout(1500)
    pg.screenshot(path="shots/dash_analytics.png")
    print("norec:", pg.evaluate("localStorage.getItem('ubz_norec')"))
    print("watch links:", pg.locator(".rwatch").count())
    pg.click('#views button[data-v=r]'); pg.wait_for_selector(".rp-row, .rpx .rp-empty, .rp-row", timeout=8000); pg.wait_for_timeout(800)
    pg.screenshot(path="shots/dash_replays.png")
    print("rows:", pg.locator(".rp-row").count(), "hash:", pg.evaluate("location.hash"))
    print(json.dumps(errs))
    b.close()
