# -*- coding: utf-8 -*-
"""Country-page CTA and published-fee rules.

WhatsApp and email enquiries are removed from public landing pages whose
slug is specifically Brazil, Mexico, Saudi Arabia, Afghanistan, Iran, Iraq
or Indonesia. The decision is the page, not the visitor's IP address.

Priority pages keep enquiries: USA, Canada, UK, France, Netherlands, UAE,
Dubai and Italy, plus global hubs. Gulf pages that also cover the UAE keep
enquiries.
"""
import re

# Segments that keep WhatsApp and email even on a country URL.
PRIORITY_SEGMENTS = {
    "usa", "uk", "canada", "france", "netherlands", "uae", "dubai", "italy",
}

HOLD_FROM_SEGMENT = {
    "brazil": "Brazil",
    "brasil": "Brazil",
    "mexico": "Mexico",
    "méxico": "Mexico",
    "afghanistan": "Afghanistan",
    "indonesia": "Indonesia",
    "iran": "Iran",
    "iraq": "Iraq",
}

NO_ENQUIRY = (
    "This page does not offer a WhatsApp or email enquiry. "
    "It explains the official steps. Unbanz is independent and is not affiliated with Meta."
)

FEE_QUESTION = {
    "ig": "What is the published fee for this Instagram account service?",
    "fb": "What is the published fee for this Facebook account service?",
    "ad": "What are the published fees for these account services?",
    "menu": "What are the published fees for these account services?",
    "username": "What does an Instagram username claim cost?",
}

FEE_ANSWER = {
    "ig": (
        "The published fee for this service is $800 for one disabled, suspended or hacked Instagram account. "
        "It covers preparing and filing through Instagram’s own process for that one account. "
        "Instagram decides the outcome. This is not a guarantee of reinstatement. "
        "Scope is confirmed in writing before payment. Payment is by card."
    ),
    "fb": (
        "The published fee for this service is $900 for one disabled, suspended or hacked Facebook profile. "
        "It covers preparing and filing through Facebook’s own process for that one profile. "
        "Facebook decides the outcome. This is not a guarantee of reinstatement. "
        "Scope is confirmed in writing before payment. Payment is by card."
    ),
    "ad": (
        "The published fee for this service is $1,200 for one Instagram ad-account restriction. "
        "The platform decides the outcome. This is not a guarantee. "
        "A Business Portfolio case or more than one account is a separate scope at $1,500. "
        "Scope is confirmed in writing before payment. Payment is by card."
    ),
    "username": (
        "An Instagram username claim is priced after the handle is reviewed. "
        "For a standard claim assessment the indicative range is $800–$1,200. "
        "That range is not a fixed price and not a guarantee. Complex handles are quoted separately."
    ),
}
FEE_ANSWER["menu"] = FEE_ANSWER["ad"]

# Pages that explain the law or a directory, or that are not one of the priced services.
NO_FEE_KINDS = {"info", "snap", "agency"}


def segments(path):
    return set(re.split(r"[^a-z0-9áéíóúñü]+", path.lower()))


def hold_country(rel_path):
    """Return the low-priority country name, or None if this page keeps enquiries."""
    p = (rel_path or "").replace("\\", "/").lower()
    if p.endswith("/index.html"):
        p = p[: -len("index.html")]
    if "gulf" in segments(p):
        return None
    segs = segments(p)
    country = None
    if "saudi-arabia" in p or ({"saudi", "arabia"} <= segs):
        country = "Saudi Arabia"
    else:
        for seg, name in HOLD_FROM_SEGMENT.items():
            if seg in segs:
                country = name
                break
    if country and (segs & PRIORITY_SEGMENTS):
        return None
    return country


def service_kind(rel_path, title=""):
    s = (rel_path + " " + (title or "")).lower()
    if any(x in s for x in ("username", "gebruikersnaam", "nome-de-usuario", "reivindicar-nome", "pseudo")):
        return "username"
    if "white-label" in s or "agencias-brasil" in s or "agência" in s:
        return "agency"
    if "snapchat" in s:
        return "snap"
    if any(x in s for x in ("appeal-links", "onde-denunciar", "falar-com", "links-and-forms")):
        return "info"
    if "ad-account" in s or "conta-de-anuncios" in s or "ads-account" in s:
        return "ad"
    if "agency-client" in s:
        return "menu"
    if "facebook" in s and "instagram" in s:
        return "menu"
    if "facebook" in s:
        return "fb"
    if "instagram" in s or "marketplace" in s:
        return "ig"
    return "info"


def fee_html(kind, lang="en"):
    if kind not in FEE_ANSWER:
        return ""
    q = FEE_QUESTION[kind]
    a = FEE_ANSWER[kind]
    if lang == "pt" and kind == "username":
        q = "Quanto custa reivindicar um nome de usuário do Instagram?"
        a = (
            "Um pedido de nome de usuário do Instagram tem o preço definido depois da análise do @. "
            "Não há um preço público fixo para nome de usuário. A taxa de uma conta desativada é outro serviço."
        )
    return (
        '<section class="published-fee container" id="published-fee" data-fee="%s">'
        '<p class="aeo-kicker">Published fee</p>'
        '<h2>%s</h2><p>%s</p></section>' % (kind, q, a)
    )
