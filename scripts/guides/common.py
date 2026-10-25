import re, hashlib, glob, os
from urllib.parse import quote
ROOT = '/workspace/site'
WA = 'https://wa.me/19342012490'
MAIL = 'mailto:team@unbanz.com'

def wa_link(text):
    return f'{WA}?text=' + quote(text, safe='')

def mail_link(subject):
    return f'{MAIL}?subject=' + quote(subject, safe='')

def attrs(service, platform):
    a = ''
    if service: a += f' data-service="{service}"'
    if platform: a += f' data-platform="{platform}"'
    return a

def top_cta(wa_text, subject, service, platform):
    return ('<div class="guide-cta-top"><p class="gct-lead">Want us to handle it?</p>'
            f'<a class="button button-light" href="{wa_link(wa_text)}"{attrs(service, platform)}>Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
            f'<a class="gct-mail" href="{mail_link(subject)}">Or email us</a></div>')

def cta_card(kind, kicker, title, text, wa_text, subject, service, platform):
    cls = 'guide-cta-card' + (' guide-cta-card-close' if kind == 'close' else '')
    return (f'<aside class="{cls}" aria-label="Contact us"><p class="gcc-kicker">{kicker}</p><p class="gcc-title">{title}</p><p class="gcc-text">{text}</p>'
            f'<div class="gcc-actions"><a class="button button-blue" href="{wa_link(wa_text)}"{attrs(service, platform)}>Message us on WhatsApp <span aria-hidden="true">↗︎</span></a>'
            f'<a class="gcc-mail" href="{mail_link(subject)}">Or email us</a></div></aside>')

def toc_html(inner_ol):
    return ('<nav class="guide-toc" aria-label="Contents"><details open><summary>In this guide</summary>' + inner_ol + '</details></nav>'
            '<script>if(matchMedia("(max-width:900px)").matches){var d=document.querySelector(".guide-toc details");d&&d.removeAttribute("open")}</script>')

STEP_RE = re.compile(r'^(?:Step\s+)?(\d{1,2})[.:]\s*(.+)$', re.S)

def step_heading(tag, attrs_str, inner):
    """Turn 'Step 1: Title' / '1. Title' headings into badge headings. Returns new html or None."""
    plain = re.sub(r'<[^>]+>', '', inner)
    m = STEP_RE.match(plain.strip())
    if not m: return None
    n = m.group(1)
    # strip the label from the inner HTML (keeps any markup after it)
    rest = re.sub(r'^\s*(?:Step\s+)?\d{1,2}[.:]\s*', '', inner)
    cls = ' class="step-h"'
    return (f'<{tag}{cls}{attrs_str}><span class="step-n" aria-hidden="true">{n}</span>'
            f'<span class="sr-only">Step {n}: </span><span>{rest}</span></{tag}>')

WARN_RE = re.compile(r'mistake|what not to do|what to avoid', re.I)
INFO_RE = re.compile(r'checklist|what to gather|what to prepare|before you submit|evidence worth|billing checklist', re.I)

def wrap_tables(html):
    return re.sub(r'(<table.*?</table>)', r'<div class="table-wrap">\1</div>', html, flags=re.S)

def split_sections(body):
    """split on top-level <h2 ...>; returns [prefix, sec1, sec2...]"""
    parts = re.split(r'(?=<h2[ >])', body)
    return parts

def convert_body(body):
    """body = html between TOC and sources. Returns list of section htmls (headings converted, callouts wrapped)."""
    parts = split_sections(body)
    out = []
    for p in parts:
        if not p.strip(): continue
        m = re.match(r'<h2([^>]*)>(.*?)</h2>(.*)$', p, re.S)
        if m:
            at, inner, rest = m.groups()
            plain = re.sub(r'<[^>]+>', '', inner)
            sh = step_heading('h2', at, inner)
            if sh:
                h2 = sh
            else:
                h2 = f'<h2{at}>{inner}</h2>'
            # h3 step headings
            def h3r(mm):
                r = step_heading('h3', mm.group(1), mm.group(2))
                return r or mm.group(0)
            rest = re.sub(r'<h3([^>]*)>(.*?)</h3>', h3r, rest, flags=re.S)
            rest = wrap_tables(rest)
            if not sh and WARN_RE.search(plain):
                p = f'<div class="guide-callout guide-callout-warn" role="note">{h2}{rest}</div>'
            elif not sh and INFO_RE.search(plain):
                p = f'<div class="guide-callout guide-callout-info">{h2}{rest}</div>'
            else:
                p = h2 + rest
        else:
            p = wrap_tables(p)
        out.append(p)
    return out

def css_hash_swap(new_css_path_name):
    pass
