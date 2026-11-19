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

## WhatsApp for US/CA/GB/NL/AE only (Nov 19 2026)
`/api/geo/` returns `wa` (447723162824) and `wd` (+44 7723 162824) ONLY when Vercel's `x-vercel-ip-country` is US, CA, GB, NL or AE. `assets/contact-policy.<hash>.js` (source: `scripts/nov19_geo/contact-policy.js`) injects WhatsApp links (header pill, mobile bar, footer, contact-page line) only when that field is present. The number is never in static HTML/JS, so every other country stays email-only. Do not add wa.me links to HTML. The strip_whatsapp script remains safe to run.

## Country SEO (Nov 19 2026)
`scripts/nov19_geo/`: content.py + build_pages.py (hubs /us/ /uk/ /ca/, TikTok and WhatsApp x US/UK/CA, nl/whatsapp-account-geblokkeerd) and site_pass.py (hreflang clusters en-US/en-GB/en-CA/en-NL + language alternates, og:locale, footer country links, sitemap/llms, copy compliance: no "guaranteed" timing, no "contacts at Meta").
