#!/usr/bin/env python3
"""Insert the Whop Pixel into the <head> of every public HTML page.

The snippet is copied exactly. The script is idempotent: a page that
already has this business-id install is left unchanged.
Skips /users (internal analytics) and /apply (redirect stub).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Exact snippet provided by the owner. Do not alter a single character.
SNIPPET = '<script>!function(w,d,s,u,n,a,b){if(w[n])return;a=w[n]={q:[],t:+new Date,s:[],o:u,track:function(){a.q.push([+new Date].concat([].slice.call(arguments)))},setScope:function(){a.s=[].slice.call(arguments).filter(function(x){return typeof x==="string"});a.q.push([+new Date,"setScope"].concat(a.s))},scope:function(){var c=[].slice.call(arguments);return{track:function(){a.q.push([+new Date].concat([].slice.call(arguments)).concat([{__scope:c}]))}}}};b=d.createElement(s);b.async=1;b.src=u+"/s.js";d.getElementsByTagName(s)[0].parentNode.insertBefore(b,d.getElementsByTagName(s)[0])}(window,document,"script","https://t.whop.tw","whop");whop.setScope("biz_0UQGhR9KoyPUCk");whop.track("page");</script>'

ALREADY = 'whop.setScope("biz_0UQGhR9KoyPUCk")'
HEAD_CLOSE = re.compile(r"</head>", re.IGNORECASE)

SKIP_DIRS = {
    "users",
    "apply",
    "assets",
    "redesign",
    "scripts",
    "marketing",
    "research",
    "node_modules",
    ".git",
    ".vercel",
    ".agents",
}


def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return any(part in SKIP_DIRS for part in rel.parts)


def iter_html():
    for path in sorted(ROOT.rglob("*.html")):
        if should_skip(path):
            continue
        yield path


def install(path: Path) -> str:
    original = path.read_text(encoding="utf-8")
    if ALREADY in original:
        if SNIPPET in original:
            return "exists"
        return "exists-other"
    match = HEAD_CLOSE.search(original)
    if not match:
        return "no-head"
    updated = original[: match.start()] + SNIPPET + original[match.start() :]
    # Safety: snippet must appear exactly once, unchanged, inside head.
    if updated.count(SNIPPET) != 1:
        raise RuntimeError(f"snippet count abnormal on {path}")
    if SNIPPET not in updated[ : match.start() + len(SNIPPET) + 20] and SNIPPET not in updated:
        raise RuntimeError(f"snippet missing after write plan for {path}")
    path.write_text(updated, encoding="utf-8")
    return "inserted"


def main() -> int:
    only = [ROOT / p for p in sys.argv[1:]] if sys.argv[1:] else list(iter_html())
    counts = {"inserted": 0, "exists": 0, "exists-other": 0, "no-head": 0}
    other = []
    for path in only:
        if path.is_dir():
            continue
        status = install(path)
        counts[status] = counts.get(status, 0) + 1
        if status in {"exists-other", "no-head"}:
            other.append((status, str(path.relative_to(ROOT))))
    print(
        "inserted={inserted} exists={exists} exists-other={exists-other} no-head={no-head} total={total}".format(
            total=sum(counts.values()), **counts
        )
    )
    for row in other:
        print(" ", *row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
