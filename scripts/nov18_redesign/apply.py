#!/usr/bin/env python3
"""Apply the cleaned inner-page redesign to the live Unbanz site.

Keeps every existing script (mail-pick onboarding, testimonials, contact-policy,
site.js) and every testimonial block. Does not add preview noindex. Idempotent.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[2]
CSS_HREF = "/redesign/style.css"
TODAY = "2026-11-18"

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

TOC_LABEL = {
    "en": "On this page",
    "fr": "Sur cette page",
    "nl": "Op deze pagina",
    "es": "En esta página",
    "pt": "Nesta página",
    "de": "Auf dieser Seite",
    "it": "In questa pagina",
    "tr": "Bu sayfada",
    "ar": "في هذه الصفحة",
    "zh": "本页内容",
}

# Visible <time> text formats found on the site, rewritten to 18 Nov 2026.
TIME_TEXT_PATTERNS = [
    (re.compile(r"\d{1,2} November 2026"), "18 November 2026"),
    (re.compile(r"\d{1,2} novembre 2026"), "18 novembre 2026"),
    (re.compile(r"\d{1,2} november 2026"), "18 november 2026"),
    (re.compile(r"\d{1,2}\. November 2026"), "18. November 2026"),
    (re.compile(r"\d{1,2} Kasım 2026"), "18 Kasım 2026"),
    (re.compile(r"\d{1,2} de noviembre de 2026"), "18 de noviembre de 2026"),
    (re.compile(r"\d{1,2} de novembro de 2026"), "18 de novembro de 2026"),
    (re.compile(r"\d{1,2} نوفمبر 2026"), "18 نوفمبر 2026"),
    (re.compile(r"2026\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日"), "2026 年 11 月 18 日"),
]


def lang_of(path: Path, soup) -> str:
    html = soup.find("html")
    lang = (html.get("lang") if html else "") or ""
    lang = lang.lower()
    if lang.startswith("zh"):
        return "zh"
    if lang.startswith("pt"):
        return "pt"
    if lang[:2] in TOC_LABEL:
        return lang[:2]
    parts = path.relative_to(ROOT).parts
    if parts and parts[0] in {"fr", "nl", "es", "de", "it", "tr", "ar"}:
        return parts[0]
    if parts and parts[0] == "pt-br":
        return "pt"
    if parts and parts[0] in {"zh-tw", "zh-hk"}:
        return "zh"
    return "en"


def asset_for(route: str) -> str:
    p = route.lower()
    if "username" in p:
        return "username.webp"
    if "youtube" in p:
        return "youtube.webp"
    if "tiktok" in p:
        return "tiktok.webp"
    if "snapchat" in p:
        return "snapchat.webp"
    if "whatsapp" in p:
        return "whatsapp.webp"
    if "facebook" in p:
        return "facebook-glass-600.webp"
    if "instagram" in p:
        return "instagram-glass-600.webp"
    return "meta.webp"


def route_of(path: Path) -> str:
    rel = path.parent.relative_to(ROOT)
    if str(rel) == ".":
        return "/"
    return "/" + str(rel).replace("\\", "/") + "/"


def ensure_class(tag, name: str) -> None:
    classes = list(tag.get("class") or [])
    if name not in classes:
        classes.append(name)
        tag["class"] = classes


def add_hero_art(soup, route: str) -> None:
    hero = soup.select_one(".service-hero")
    if not hero or hero.select_one(".ub-hero-art"):
        return
    box = hero.select_one(".container") or hero
    if not box.select_one(".ub-hero-copy"):
        copy = soup.new_tag("div", attrs={"class": "ub-hero-copy"})
        for child in list(box.contents):
            copy.append(child.extract())
        box.append(copy)
    art = soup.new_tag("div", attrs={"class": "ub-hero-art", "aria-hidden": "true"})
    img = soup.new_tag(
        "img",
        src="/redesign/assets/" + asset_for(route),
        width="620",
        height="620",
        alt="",
    )
    img["fetchpriority"] = "high"
    art.append(img)
    box.append(art)


def add_toc(soup, lang: str) -> None:
    article = soup.select_one("article.guide-body")
    if not article:
        return
    if article.find_parent(class_="ub-reading"):
        return
    headings = article.find_all("h2", recursive=False)
    if not headings:
        return
    seen = set()
    for n, h in enumerate(headings):
        hid = h.get("id")
        if hid in seen:
            h["id"] = f"{hid}-{n}"
        if h.get("id"):
            seen.add(h["id"])
    nav = soup.new_tag("nav", attrs={"class": "ub-toc", "aria-label": TOC_LABEL.get(lang, "On this page")})
    label = soup.new_tag("p")
    label.string = TOC_LABEL.get(lang, "On this page")
    nav.append(label)
    for i, h in enumerate(headings):
        if not h.get("id"):
            h["id"] = f"section-{i + 1}"
        a = soup.new_tag("a", href="#" + h["id"])
        a.string = h.get_text(" ", strip=True)
        nav.append(a)
    shell = soup.new_tag("div", attrs={"class": "ub-reading container"})
    article.wrap(shell)
    # keep guide-body class list intact
    shell.insert(0, nav)


def wrap_tables(soup) -> None:
    for table in soup.select("table"):
        if table.find_parent(class_="ub-table"):
            continue
        wrapper = soup.new_tag(
            "div",
            attrs={
                "class": "ub-table",
                "tabindex": "0",
                "role": "region",
                "aria-label": "Reference table",
            },
        )
        table.wrap(wrapper)


def ensure_css(soup) -> None:
    for link in soup.find_all("link", href=True):
        if link["href"] == CSS_HREF:
            return
    tag = soup.new_tag("link", rel="stylesheet", href=CSS_HREF)
    soup.head.append(tag)


def scripts_of(soup) -> list[str]:
    return [s.get("src") for s in soup.find_all("script", src=True)]


def rewrite_time_text(text: str) -> str:
    for pat, repl in TIME_TEXT_PATTERNS:
        if pat.fullmatch(text.strip()) or pat.search(text):
            return pat.sub(repl, text)
    return text


UPDATED_TIME = re.compile(
    r'(Updated|Mis à jour le|Bijgewerkt op|Aktualisiert am|Aggiornato il|'
    r'Güncellendi:|Actualizado el|Atualizado em|آخر تحديث|更新於)\s*'
    r'(<time datetime="20\d{2}-\d{2}-\d{2}">)([^<]*)(</time>)',
    re.I,
)

def update_dates_in_text(html: str) -> str:
    html = re.sub(
        r'"dateModified"\s*:\s*"20\d{2}-\d{2}-\d{2}"',
        f'"dateModified":"{TODAY}"',
        html,
    )

    def repl_time(m: re.Match) -> str:
        inner = rewrite_time_text(m.group(3))
        return f'{m.group(1)} <time datetime="{TODAY}">{inner}</time>'

    html = UPDATED_TIME.sub(repl_time, html)
    return html


def serialize(soup, original: str) -> str:
    html = str(soup)
    # BeautifulSoup may drop or lowercase the doctype
    if not re.match(r"<!doctype html>", html, re.I):
        html = "<!DOCTYPE html>\n" + html
    # Restore original doctype spelling if it was lowercase
    if original.lower().startswith("<!doctype html>") and original.startswith("<!doctype"):
        html = re.sub(r"^<!DOCTYPE html>", "<!doctype html>", html, count=1, flags=re.I)
    return html


def process(path: Path, homepage: bool = False) -> dict:
    original = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")
    if not soup.head or not soup.body:
        return {"path": str(path), "skipped": "no-head-body"}
    before_scripts = scripts_of(soup)
    before_vt = len(soup.select(".vt"))
    route = route_of(path)

    if not homepage:
        ensure_class(soup.body, "ub-inner")
        add_hero_art(soup, route)
        add_toc(soup, lang_of(path, soup))
        wrap_tables(soup)

    ensure_css(soup)
    html = serialize(soup, original)
    html = update_dates_in_text(html)

    # Safety: scripts and testimonials must survive
    after = BeautifulSoup(html, "html.parser")
    after_scripts = scripts_of(after)
    after_vt = len(after.select(".vt"))
    if before_scripts != after_scripts:
        raise RuntimeError(f"Script tags changed on {path}: {before_scripts} -> {after_scripts}")
    if after_vt < before_vt:
        raise RuntimeError(f"Testimonials dropped on {path}: {before_vt} -> {after_vt}")

    path.write_text(html, encoding="utf-8")
    return {
        "path": str(path.relative_to(ROOT)),
        "route": route,
        "hero": bool(after.select_one(".ub-hero-art")),
        "toc": bool(after.select_one(".ub-toc")),
        "scripts": len(after_scripts),
        "vt": after_vt,
    }


def iter_pages():
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield path


def update_sitemaps() -> int:
    n = 0
    for path in ROOT.glob("sitemap*.xml"):
        text = path.read_text(encoding="utf-8")
        new, c = re.subn(r"<lastmod>20\d{2}-\d{2}-\d{2}</lastmod>", f"<lastmod>{TODAY}</lastmod>", text)
        if c:
            path.write_text(new, encoding="utf-8")
            n += c
    return n


def main() -> int:
    only = sys.argv[1:]  # optional relative paths for a dry subset
    results = []
    home = ROOT / "index.html"
    targets = [ROOT / p for p in only] if only else list(iter_pages())
    if not only and home not in targets and home.exists():
        targets.append(home)
    for path in targets:
        is_home = path.resolve() == home.resolve()
        results.append(process(path, homepage=is_home))
    sm = 0 if only else update_sitemaps()
    heroes = sum(1 for r in results if r.get("hero"))
    tocs = sum(1 for r in results if r.get("toc"))
    print(f"processed={len(results)} hero_art={heroes} toc={tocs} sitemap_lastmod={sm}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
