# Unbanz — static website

One website. No React, Vite, Firebase, backend, npm install or build step. All enquiries use WhatsApp or email. No admin dashboard.

## Upload this ZIP to GitHub / Vercel

1. Unzip unbanz-website.zip. Upload ALL its extracted files and folders to the repository root. index.html and vercel.json must be at the root, with assets/ and the service folders beside them.
2. In Vercel, select that repository. Root Directory: repository root. Framework Preset: Other. Build Command: empty. Output Directory: . (a dot). The ZIP's vercel.json already declares this.
3. Redeploy. This package serves ready-to-use HTML; do not point it at src/main.tsx or use the previous AI Studio React configuration.
4. Add unbanz.com in Vercel Domains and follow the displayed DNS instructions. Canonicals and sitemap use https://unbanz.com/.

The Sites checkout serves dist/. Its shared styles and interactions are maintained in src/site.css and src/site.js; run python scripts/build-assets.py after editing them. This produces versioned assets and updates every HTML page. The export script places the ready-to-use dist/ contents at the ZIP root. Vercel does not need to run a build.

Every exported HTML page references the same CSS and JavaScript files under assets/site.[version].css and assets/site.[version].js. Those are the active bundles. styles.css, refresh.css and app.js are compatibility files for older open pages; do not edit only those aliases. If editing the ZIP directly, edit its active bundles and update their references on all pages when changing their names.

## Contact

WhatsApp: +1 934 201 2490
Email: team@unbanz.com

Visitors send messages in WhatsApp or email. Nothing is submitted to a website backend. No automatic delivery confirmation is shown. Contact numbers/mailbox deliverability must be checked by the owner before ads run.

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
