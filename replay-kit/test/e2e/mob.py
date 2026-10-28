import json
from playwright.sync_api import sync_playwright
from common import *
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    ctx=b.new_context(viewport={"width":390,"height":844},user_agent=UA_M,is_mobile=True,has_touch=True,device_scale_factor=2)
    pg=ctx.new_page(); pg.on("pageerror",lambda e:errs.append(str(e))); pg.on("console",lambda m:m.type=="error" and errs.append(m.text[:150]))
    pg.goto(BASE+"/users/#replays",wait_until="domcontentloaded"); pg.fill("#luser","harness-user"); pg.click("#lform button"); pg.wait_for_selector(".rp-row")
    pg.wait_for_timeout(500); pg.screenshot(path="shots/m_list.png")
    n0=pg.locator(".rp-row").count()
    pg.select_option("#rp-dev","Desktop"); pg.wait_for_timeout(900); print("rows all",n0,"desktop",pg.locator(".rp-row").count())
    pg.select_option("#rp-dev",""); pg.wait_for_timeout(600)
    pg.select_option("#rp-src","ChatGPT"); pg.wait_for_timeout(900); print("src ChatGPT",pg.locator(".rp-row").count()); pg.select_option("#rp-src",""); pg.wait_for_timeout(600)
    pg.click("#rp-clk"); pg.wait_for_timeout(900); print("clicked-only rows",pg.locator(".rp-row").count())
    pg.click("#rp-cv"); pg.wait_for_timeout(900); print("converted too rows",pg.locator(".rp-row").count())
    pg.locator(".rp-row").first.click(); pg.wait_for_selector(".rp-ov"); pg.wait_for_timeout(2500)
    pg.screenshot(path="shots/m_player.png")
    pg.click("[aria-label=\"Session details\"]"); pg.wait_for_timeout(500); pg.screenshot(path="shots/m_side.png")
    pg.click("[aria-label='Session details']")
    pg.click(".rp-ov [data-s='4']"); pg.keyboard.press("Escape"); pg.wait_for_timeout(500)
    print("closed overlay:", pg.locator(".rp-ov").count()==0, "hash:", repr(pg.evaluate("location.hash")))
    print("errors",errs); b.close()
