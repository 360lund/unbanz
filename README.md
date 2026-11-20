# Unbanz — static website

One website. No React, Vite, Firebase, backend, npm install or build step. All enquiries use email (team@unbanz.com). WhatsApp contact was removed on Nov 15 2026. No admin dashboard.

## Upload this ZIP to GitHub / Vercel

1. Unzip unbanz-website.zip. Upload ALL its extracted files and folders to the repository root. index.html and vercel.json must be at the root, with assets/ and the service folders beside them.
2. In Vercel, select that repository. Root Directory: repository root. Framework Preset: Other. Build Command: empty. Output Directory: . (a dot). The ZIP's vercel.json already declares this.
3. Redeploy. This package serves ready-to-use HTML; do not point it at src/main.tsx or use the previous AI Studio React configuration.
4. Add unbanz.com in Vercel Domains and follow the displayed DNS instructions. Canonicals and sitemap use https://unbanz.com/.

The Sites checkout serves dist/. Its shared styles and interactions are maintained in src/site.css and src/site.js; run python scripts/build-assets.py after editing them. This produces versioned assets and updates every HTML page. The export script places the ready-to-use dist/ contents at the ZIP root. Vercel does not need to run a build.

Every exported HTML page references the same CSS and JavaScript files under assets/site.[version].css and assets/site.[version].js. Those are the active bundles. styles.css, refresh.css and app.js are compatibility files for older open pages; do not edit only those aliases. If editing the ZIP directly, edit its active bundles and update their references on all pages when changing their names.

## Contact

Email: team@unbanz.com (only contact channel; our WhatsApp number was removed everywhere on Nov 15 2026 — do not re-add it).

Visitors send messages by email. Nothing is submitted to a website backend. No automatic delivery confirmation is shown. Contact numbers/mailbox deliverability must be checked by the owner before ads run.

## Pages

/ — main site
/instagram-account-recovery/
/facebook-account-recovery/
/ad-account-recovery/
/unban/ — recovery hub
/ban/ — legitimate ban requests
/username/ — Instagram only
/pricing/ — free initial check, custom case quotes
/contact/
/privacy/
/terms/
/apply/ — redirects old links to contact

## Files for you

marketing/ contains three revised Instagram posts, link-preview artwork and captions.
research/COMPETITOR_RESEARCH.md contains the seven-site comparison, pricing benchmarks and search/ad launch notes.
AI_STUDIO_HANDOFF.md tells an agent how to preserve the site.

## Launch status

The ChatGPT preview is private. This ZIP has not been pushed to the user's GitHub or unbanz-red Vercel project. No Search Console verification, analytics, Meta Pixel or ads were configured. Prices are quoted per case until supplier costs and refund terms are confirmed. Backend and former admin files have been removed.

## Assets
Never delete old hashed files in assets/ (site.*.css / site.*.js). Cached pages still request them.

## Testimonials on every page
`python3 scripts/testimonials_all.py` (idempotent, run after any page generator): puts ALL video testimonials (same `vt-page` carousel as /reviews/: larger cards, phone auto-swipe + loop) before the FAQ on every service, country, white-label and agency page, EN and fr/nl/es/pt-br (cards copied from each language's reviews page). It writes hashed `assets/testimonials.<hash>.css/.js` from `scripts/testimonials.{css,js}` and updates the head refs. Add new testimonials in `scripts/testimonials.json` + `build_testimonials.py` (home, /reviews/), rebuild the native reviews pages, then run it.

## Paid-service note (human-only)
`assets/cta-note.<hash>.js` shows a one-line note ("Unbanz is a paid professional service...", translated per page language) to human visitors from IN, PK, BD, NG, KE, NP, LK, GH, EG, IQ, DZ, MA, PH, ID (country from `/api/geo/`). Client-side only, skipped for bots/automation, never on the homepage or locale homes. Generators call `scripts/cta_note.py` (`write_page` / `with_cta_note`) so new pages get the tag; `scripts/apply_cta_note.py` re-applies it site-wide. If the JS changes, make a new hashed file, keep the old one, update `CTA_ASSET`, and re-run `apply_cta_note.py`.

## Email-only contact (Nov 15 2026)
Our WhatsApp is restricted. Every wa.me link, the WhatsApp number and WhatsApp-contact copy were removed; `assets/contact-policy.js` now sets `data-contact="email"` for every country. Older page generators in `scripts/` still emit wa.me links: after running any generator, run `python3 /workspace/nowa/run_all.py site` (or the copy in `scripts/strip_whatsapp_contact/`) before deploying.

## Email CTA and email-only contact pass (Nov 15 2026)
- `scripts/email_cta/` adds: a primary "Email us" button in every page header (`.ecta-hdr`; mobile-only `.ecta-m` on pages whose header already has an email link), an email-only statement under the H1 on contact/FAQ pages (`.ecta-only`), a visible and JSON-LD "How do I contact Unbanz?" Q&A on home/contact/FAQ pages, an email-only ContactPoint on our Organization/ProfessionalService JSON-LD, an end-of-page email band (`.ecta-band`) only on pages without an existing end CTA, a "How to contact" block at the top of llms.txt / llms-full.txt, and a prefilled subject+body on every `mailto:team@unbanz.com` link (the mail-pick topic picker still intercepts clicks; the href is the no-JS fallback).
- Styles live in `assets/ecta.<hash>.css` (generated from `scripts/email_cta/ecta.css`; never delete old hashed files).
- Generators: `scripts/cta_note.py` `with_cta_note()` / `write_page()` now also run the WhatsApp strip (`scripts/strip_whatsapp_contact/strip_one.py`) and this pass, so new pages get it automatically.
- After any bulk build, also run: `python3 scripts/strip_whatsapp_contact/run_all.py . && python3 scripts/email_cta/run_ecta.py unbanz` (idempotent; `--check` reports without writing).

## Email topic picker v3 (Nov 15 2026)
- `assets/mail-pick.<hash>.js` is built from `scripts/nov15_picker/` (main.js + strings.js + picker.css; `python3 scripts/nov15_picker/build.py`). Two steps: grouped topic cards with icons, then username + optional "how did you hear" + sticky "Write the email". Bottom sheet with drag-to-close on mobile, centered modal on desktop, RTL, reduced motion, focus trap, scroll lock.
- Same output as v2 (same topic values, subject/body template, "How I heard about Unbanz" line; the select keeps id `ubz-hear-mail` so hear-source.js leaves it alone). Tracking unchanged (.cm-dialog, .cm-pill[data-group=service][aria-pressed], data-service/data-platform on .mp-go).
- Languages: en, fr, nl (v2 strings), plus es, pt, de, it, tr, ar, zh (new; v2 skipped these locales).

## Recovery timeframe 7–14 days (Nov 15 2026)
User rule Nov 15 12:14 PKT: the recovery time is "guaranteed 7–14 days", with "100% refund if not reinstated within 14 days" wherever the refund clause sits next to the timeframe. `scripts/email_cta/timeframe.py` (`fix()`) holds the per-language rules (en, fr, nl, es, pt, de, it, tr, ar, zh). `run_ecta._strip()` runs it, so every page that goes through `scripts/cta_note.py` `with_cta_note()` keeps 7–14 days even if an old generator string says 3–7. To run it over the built output, use `/workspace/nowa/timeframe/apply_tf.py <root>`. It is idempotent and does not touch prices, the 6-month guarantee or other numbers.

## WhatsApp for US/CA/GB/NL/AE only, strict (Nov 20 2026)
`/api/geo/?tz=<browser IANA time zone>` returns `wa` ONLY when BOTH: Vercel's `x-vercel-ip-country` is exactly US, CA, GB, NL or AE, AND `tz` is one of the 91 tzdb zones/aliases of those five countries (list in `api/geo.mjs`). VPN users from PK/IN/IR/MA/AF etc. keep their home time zone (Asia/Karachi...) and get nothing; missing country, missing tz or UTC = nothing (fail closed). No URL/cookie/header override. Headers: `private, no-store, no-cache, must-revalidate, max-age=0`, `CDN-Cache-Control: no-store`, `Vercel-CDN-Cache-Control: no-store`, `Vary: x-vercel-ip-country`. `assets/contact-policy.<hash>.js` (source `scripts/nov20_wa/contact-policy.js`) checks the same tz list before even asking, skips automation (navigator.webdriver), and injects WhatsApp buttons (`a[data-wa]`, href `#whatsapp`, number never printed on the page). Clicking opens the email topic picker in WhatsApp mode (`assets/mail-pick.<hash>.js`, built by `scripts/nov20_wa/patch_mailpick.py`): same 12 topics, username, optional note, how-heard, then `wa.me/<number>?text=` pre-filled. Do not add wa.me links or the number to HTML/JS.

## Country SEO (Nov 19 2026)
`scripts/nov19_geo/`: content.py + build_pages.py (hubs /us/ /uk/ /ca/, TikTok and WhatsApp x US/UK/CA, nl/whatsapp-account-geblokkeerd) and site_pass.py (hreflang clusters en-US/en-GB/en-CA/en-NL + language alternates, og:locale, footer country links, sitemap/llms, copy compliance: no "guaranteed" timing, no "contacts at Meta").

## No contact for India, Pakistan, Iran (Nov 20 2026)
IN/PK/IR visitors see zero email and zero WhatsApp. Triggers: browser time zone Asia/Karachi, Asia/Kolkata, Asia/Calcutta, Asia/Tehran, Iran (inline `#ubz-noc` script right after `<meta charset>`, source `scripts/nov20_noc/`, injector `inject.py`), or the `ubz_noc` cookie, which `middleware.js` sets on human page requests from IN/PK/IR IPs (bots never) and `/api/geo/` sets when it answers `contactAllowed:false`. The guard hides the body until it has removed mailto/WhatsApp links, contact sections, email text, JSON-LD with the email and email in meta attributes, then shows the page (/contact/ gets "Direct support is currently unavailable in your region."). Static HTML, JSON-LD, sitemaps and llms files are unchanged, all pages stay 200, so crawlers see the same content as before. New pages: run `python3 scripts/nov20_noc/inject.py` and `python3 scripts/nov20_agency/band.py` (both idempotent).

## Agencies band on every page (Nov 20 2026)
`scripts/nov20_agency/band.py` adds a localized "Agencies & white-label" band above the footer on every page, linking the agency hub for that language (/white-label-agency/, /fr/white-label-agences/, /nl/white-label-bureau/, /es/white-label-agencias/, /pt-br/white-label-agencias/; others link to English). It has an email button (removed for IN/PK/IR), and contact-policy.js adds WhatsApp there for US/CA/GB/NL/AE only.

## Agency onboarding page and agency Q&A (Nov 20 2026)
- `/white-label-agency/` is a short closing page: hero, 5-step onboarding picker (`scripts/nov20_agency/onboard.js` → `assets/agency-onboard.<hash>.js`), How it works, partner terms. Built by `scripts/nov20_agency/hub.py` (source = git HEAD hub, re-runnable; CSS in `hub.css`). The final step follows the 3-tier rule from `/api/geo/`: WhatsApp + email (US/CA/GB/NL/AE IP + tz), email only (others), nothing (IN/PK/IR IP or tz). No address or number in the HTML. No agency band on this page.
- The old long hub moved to `/white-label-agency/guides/` (Agency resources), which also lists the 10 agency Q&A pages (`qa_agency.py` + `build_agency.py`, rebuild with `build_agency.py rebuild`).
- Homepage pricing card (en/fr/nl/es/pt-br) has the agency CTA (`.pn-agency`, `site_pass_agency.py`); contact-policy adds WhatsApp to `.pn-agency .pn-act` for the top tier.
- Agency white-label rate shown: $1,200 per case.
- Nov 20 (d): `agency_1200.py` sets $1,200 on all agency/white-label pages (consumer pages stay $1,000) and removes the Meta logo hero art there; `loc_hubs.py` gives fr/nl/es/pt-br agency hubs the localized onboarding hero (`onboard_ui.py` holds all strings; `onboard.js` reads `data-i18n`); `sitewide_links.py` adds "For agencies" to header/mobile nav + footer and one contextual line (`.ag-ctx`) on service/Q&A pages; `add_service.py` adds the Service node to agency pages lacking one. Order to rebuild: build_agency.py rebuild → hub.py → loc_hubs.py → agency_1200.py → add_service.py → sitewide_links.py → band.py → nov20_noc/inject.py.

## Google tag (Nov 20 2026)
- GTM-PGDPS7SK snippet sits immediately after `<head>` on every public HTML page (not `/users`). `scripts/nov20_gtm/gtm_tag.py` adds it idempotently (exactly one per page); run it last after any page build. No CSP on public pages (the only CSP is on `/users`), so nothing to allow-list.

## Nov 20 2026 CRO pass
- Homepage: clearer hero copy, primary CTA "Get a free case review" (opens picker), hero trust chips, 3-step How it works (#how), 4 objection FAQs (+FAQPage JSON-LD), 3–14 -> 7–14 days. /contact/: trust row. Script: scripts/nov20_cro/cro.py
- GTM events: /assets/lead-events.*.js on every public page (scripts/nov20_cro/lead_inject.py) pushes dataLayer {event: lead_email|lead_whatsapp, lead_source, lead_topic, page_path} when the picker or agency onboarding opens email / WhatsApp.
