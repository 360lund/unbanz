#!/usr/bin/env python3
"""Add the hashed Whop custom-events script to every public HTML page.

Does not alter the base Whop Pixel snippet by a single character.
Skips /users and /apply.
Idempotent: pages that already include the current hashed file are left unchanged.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PIXEL = (
    '<script>!function(w,d,s,u,n,a,b){if(w[n])return;a=w[n]={q:[],t:+new Date,s:[],o:u,track:function()'
    '{a.q.push([+new Date].concat([].slice.call(arguments)))},setScope:function(){a.s=[].slice.call(arguments)'
    '.filter(function(x){return typeof x==="string"});a.q.push([+new Date,"setScope"].concat(a.s))},scope:function()'
    '{var c=[].slice.call(arguments);return{track:function(){a.q.push([+new Date].concat([].slice.call(arguments))'
    '.concat([{__scope:c}]))}}}};b=d.createElement(s);b.async=1;b.src=u+"/s.js";d.getElementsByTagName(s)[0]'
    '.parentNode.insertBefore(b,d.getElementsByTagName(s)[0])}(window,document,"script","https://t.whop.tw","whop");'
    'whop.setScope("biz_0UQGhR9KoyPUCk");whop.track("page");</script>'
)

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

SOURCE = ROOT / "assets" / "whop-events.js"


def sha12(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return any(part in SKIP_DIRS for part in rel.parts)


def iter_html():
    for path in sorted(ROOT.rglob("*.html")):
        if should_skip(path):
            continue
        yield path


def main() -> int:
    source = SOURCE.read_text(encoding="utf-8")
    digest = sha12(source)
    hashed_rel = f"assets/whop-events.{digest}.js"
    hashed_path = ROOT / hashed_rel
    hashed_path.write_text(source, encoding="utf-8")
    tag = f'<script defer="" src="/{hashed_rel}"></script>'

    counts = {"inserted": 0, "exists": 0, "no-pixel": 0, "users-apply-skipped": 0}
    problems = []

    for path in iter_html():
        original = path.read_text(encoding="utf-8")
        if PIXEL not in original:
            counts["no-pixel"] += 1
            problems.append(("no-pixel", str(path.relative_to(ROOT))))
            continue
        if tag in original:
            # Pixel must still be exact.
            if original.count(PIXEL) != 1:
                problems.append(("pixel-count", str(path.relative_to(ROOT))))
            counts["exists"] += 1
            continue
        # Drop any older hashed include of this script, then insert the current tag
        # immediately after the unchanged pixel snippet (still before </head>).
        updated = original
        # Remove prior /assets/whop-events.*.js script tags only.
        import re

        updated = re.sub(
            r'<script defer="" src="/assets/whop-events\.[0-9a-f]{12}\.js"></script>',
            "",
            updated,
        )
        if PIXEL + "</head>" in updated:
            updated = updated.replace(PIXEL + "</head>", PIXEL + tag + "</head>", 1)
        elif PIXEL in updated:
            idx = updated.find(PIXEL)
            insert_at = idx + len(PIXEL)
            updated = updated[:insert_at] + tag + updated[insert_at:]
        else:
            counts["no-pixel"] += 1
            problems.append(("lost-pixel-before-insert", str(path.relative_to(ROOT))))
            continue

        if PIXEL not in updated or updated.count(PIXEL) != 1:
            raise RuntimeError(f"pixel snippet changed or duplicated on {path}")
        # Exact snippet bytes must still match.
        start = updated.find(PIXEL)
        if updated[start : start + len(PIXEL)] != PIXEL:
            raise RuntimeError(f"pixel snippet mutated on {path}")
        if tag not in updated:
            raise RuntimeError(f"events tag missing after insert on {path}")
        path.write_text(updated, encoding="utf-8")
        counts["inserted"] += 1

    # Confirm users/ and apply/ were not touched by this run (they are skipped).
    for rel in ("users/index.html", "apply/index.html"):
        path = ROOT / rel
        if path.exists() and PIXEL in path.read_text(encoding="utf-8"):
            problems.append(("unexpected-pixel", rel))

    print(
        "hashed={hashed} inserted={inserted} exists={exists} no-pixel={no-pixel} total={total}".format(
            hashed=hashed_rel,
            total=counts["inserted"] + counts["exists"] + counts["no-pixel"],
            **counts,
        )
    )
    for row in problems:
        print(" ", *row)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
