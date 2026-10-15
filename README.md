# Unbanz

Responsive HTML/CSS/JS website, plus a Vercel email function. No frontend dependencies or build step.

## GitHub and Vercel
1. Unzip this project. Create a private GitHub repository called unbanz.
2. Upload all extracted contents to its root (dist/, api/, tests/, vercel.json and docs). Do not upload the ZIP itself. Include .gitignore and .env.example if using Git locally.
3. Import the repository at https://vercel.com/new. Framework: Other. Build command: empty. Output directory: dist. The included vercel.json supplies these settings.
4. In Project Settings > Domains, add unbanz.com and www.unbanz.com. Use the DNS records Vercel provides and select your primary domain.
5. Future pushes to the linked production branch deploy automatically.

## Activate application email
The server function at api/application.js sends applications to team@unbanz.com through Resend. This recipient cannot be changed by visitors.
1. Create a Resend account and verify a sending domain you control, such as unbanz.com, using its DNS instructions. This does not create the team mailbox; that mailbox must already receive email.
2. Create a sending API key. In Vercel > Project Settings > Environment Variables set RESEND_API_KEY privately.
3. Set APPLICATION_FROM to Unbanz <applications@unbanz.com> using your verified sending domain.
4. Redeploy. The Submit application button posts to /api/application.
5. Submit a real test and verify arrival in team@unbanz.com. Check provider logs for rejection or spam filtering. API acceptance is not proof of inbox delivery.
6. Configure Vercel firewall rate limiting for POST /api/application before running ads. The endpoint includes validation, a honeypot and retry deduplication, but not a distributed rate limiter.
Never paste an API key into frontend JavaScript or commit it to GitHub.

The application is now a two-step onsite form. If the backend is not configured, it honestly reports that online submissions are unavailable and keeps the entered details. There is no email-draft submission fallback. The static ChatGPT preview cannot run the Vercel function. WhatsApp remains available at +19342012490. No application database or payments are included.

## Files
- dist/: frontend, local assets, SEO, sitemap
- api/application.js: server-only email delivery
- tests/application.test.js: mocked delivery/validation tests (sends no real mail)
- .env.example: environment variable names only
- AI_STUDIO_HANDOFF.md: instructions for preserving the design

## Checks
Run node --test tests/application.test.js and node --check dist/app.js.
Static asset, form and accessibility-reference checks passed. Live browser/mobile rendering and real inbox delivery require verification after setup.


## New pages and admin preview
- /unban/, /username/, /ban/: distinct, crawlable service pages with canonical metadata, social previews, internal links and Service schema. Included in sitemap.xml.
- /admin/: visual lead desk preview. Password: preview. Public demo data only; this is NOT authentication. Search, filter, view details and edit demo statuses/notes. Changes live only in memory. Do not add real leads until server-side authentication and access rules are implemented.
- The application collects service, account, context, name, email and optional phone/WhatsApp. No follower package remains.

## Firebase handoff
In AI Studio, preserve the UI. Replace the /api/application integration with a Firebase callable function or protected server endpoint. Validate every field server-side, use App Check/rate controls, and create lead records with a server timestamp and initial New status. Set Firestore rules so visitors cannot read or list leads, and cannot edit arbitrary records. Protect admin with Firebase Authentication plus an explicit admin role; never use the preview password for production. Replace demo records only after authenticated admin reads work. Email notification must run on the server, not expose email credentials in client code. Handle errors without pretending a submission succeeded. Remove the preview gate and demo records when real authentication is ready.

## Phone upload edition
unbanz-phone-upload.zip is a flat, static edition: all fonts, scripts, styles and images are embedded in its HTML files. Upload its extracted files together into the GitHub repository root. Its vercel.json uses output directory . and clean URLs, so unban.html is served at /unban/. It includes the same website, service pages and admin demo, but no running email function. Connect Firebase later. The full source ZIP retains the editable multi-file source and optional Vercel email backend.


## Application redesign and launch artwork
Application buttons now open /apply/ instead of a modal. Desktop shows the complete form in two columns; mobile shows account details then contact details. The /api/application endpoint remains the backend integration point. Static preview and phone-upload edition still require Firebase or another backend before requests can be received.

marketing/ contains three Instagram feed designs, the full-resolution link-preview graphic and captions.txt. These are ready for your review and manual posting; nothing has been posted to Instagram or submitted as an ad.

The optimized link-preview asset is dist/assets/unbanz-share-v2.jpg (1200×628). The public pages use this image in Open Graph/Twitter metadata. It will be accessible to link preview crawlers once unbanz.com is publicly hosted and serving these files. The private ChatGPT preview cannot provide a public crawler preview for the domain.
