// Vercel Routing Middleware (no framework, Web API only).
// GEO-BLOCK DISABLED. Previously blocked visitors from a country list
// with a small self-contained 403 page. Every other request (including
// requests with no country header) passes through untouched, so static
// files, vercel.json headers, redirects and the 404 page behave as before.

// The owner is in Pakistan: the private /users dashboard and its data API stay reachable from PK only.
const OWNER_COUNTRY = 'PK';
const OWNER_PATHS = /^\/(?:users\/?|api\/users\/.*|assets\/.*)$/i;

const BLOCK_PAGE = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Unavailable in your region | Unbanz</title><style>html,body{margin:0;height:100%}body{display:flex;align-items:center;justify-content:center;padding:24px;box-sizing:border-box;background:#f7fafc;color:#25415d;font-family:'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;text-align:center}main{max-width:420px}.w{font-size:28px;font-weight:700;letter-spacing:-.04em;margin:0 0 20px}h1{font-size:22px;font-weight:400;letter-spacing:-.02em;line-height:1.3;margin:0}</style></head><body><main><p class="w">unbanz.</p><h1>unbanz.com isn’t available in your region.</h1></main></body></html>`;

export const config = {
  // Run on every path, including /assets/*, so nothing is served to blocked regions.
  matcher: '/(.*)',
};

// Known AI assistants and search crawlers: their fetchers can sit in (or be geolocated to)
// blocked regions, so they are never geo-blocked. Human visitors are unaffected.
const BOT_UA = /(ChatGPT-User|OAI-SearchBot|GPTBot|PerplexityBot|Perplexity-User|ClaudeBot|Claude-User|Claude-SearchBot|anthropic-ai|Google-Extended|Googlebot|Google-InspectionTool|GoogleOther|Storebot-Google|bingbot|BingPreview|msnbot|adidxbot|Applebot|DuckDuckBot|DuckAssistBot|YandexBot|Amazonbot|meta-externalagent|meta-externalfetcher|facebookexternalhit|MistralAI-User|cohere-ai|YouBot|PhindBot|xAI|Grok|Bravebot|CCBot|Diffbot)/i;

// TEMP PAUSE (3h, Nov 4 2026): every page except the homepage returns 503 + Retry-After.
// 503 tells search engines/AI crawlers "temporary, come back" (no deindexing). Revert this commit to undo.
const PAUSE = true;
const PAUSE_ALLOW = /^\/(?:index\.html|robots\.txt|sitemap[^/]*\.xml|llms(?:-full)?\.txt|favicon\.ico|apple-touch-icon\.png|site\.webmanifest|[0-9a-f]{32}\.txt|assets\/.*|api\/.*)$/i;
const STATIC_EXT = /\.(?:css|js|mjs|map|png|jpe?g|gif|webp|avif|svg|ico|woff2?|ttf|otf|eot|json|webmanifest)$/i;
const PAUSE_PAGE = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Temporarily unavailable | Unbanz</title></head><body style="font-family:Arial,sans-serif;text-align:center;padding:48px 20px;color:#25415d"><h1>This page is temporarily unavailable</h1><p>Please check back shortly. Meanwhile visit the <a href="/">Unbanz homepage</a> or message us on <a href="https://wa.me/19342012490">WhatsApp</a>.</p></body></html>`;
const SHORT = { '/testimonials': '/reviews/', '/review': '/reviews/' };

export default function middleware(request) {
  const path = new URL(request.url).pathname.replace(/\/+$/, '') || '/';
  if (SHORT[path]) {
    return new Response(null, { status: 301, headers: { Location: new URL(SHORT[path], request.url).toString(), 'Cache-Control': 'public, max-age=3600' } });
  }
  const raw = new URL(request.url).pathname;
  if (PAUSE && path !== '/' && !PAUSE_ALLOW.test(raw) && !STATIC_EXT.test(raw)) {
    return new Response(PAUSE_PAGE, { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8', 'Retry-After': '10800', 'Cache-Control': 'no-store' } });
  }
  // Geo-block disabled 2026-10-23: all countries and paths pass through.
  return;
}
