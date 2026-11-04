// Read-only IMAP inbox for team@unbanz.com (private /users dashboard only).
// Env (encrypted in Vercel): UNBANZ_MAIL_USER, UNBANZ_MAIL_PASSWORD, UNBANZ_MAIL_HOST (host[:port], default mail.spacemail.com:993, implicit TLS).
// Every mailbox is opened with readOnly:true and bodies are fetched with BODY.PEEK, so nothing is marked read, moved or deleted. No sending.
// GET ?op=folders | ?op=list&folder=INBOX&page=1&size=30&q=term | ?op=msg&folder=INBOX&uid=123 | ?op=export&folder=INBOX&limit=500&since=YYYY-MM-DD
import { ImapFlow } from "imapflow";
import { simpleParser } from "mailparser";
import { json } from "../_lib/auth.mjs";
import { authed } from "../_lib/uauth.mjs";
export const config = { maxDuration: 60 };

function client() {
  const [host, port] = String(process.env.UNBANZ_MAIL_HOST || "mail.spacemail.com:993").split(":");
  return new ImapFlow({ host, port: +port || 993, secure: true, auth: { user: process.env.UNBANZ_MAIL_USER || "team@unbanz.com", pass: process.env.UNBANZ_MAIL_PASSWORD || "" }, logger: false, socketTimeout: 45000, greetingTimeout: 15000, connectionTimeout: 15000 });
}
const addr = (a) => (a && a.length ? a.map((x) => (x.name ? `${x.name} <${x.address || ""}>` : x.address || "")).join(", ") : "");
const clean = (s) => String(s || "").replace(/\s+/g, " ").trim();
// Strip active content; the browser also renders it in a sandboxed iframe with a strict CSP.
function sanitize(html) {
  return String(html || "")
    .replace(/<(script|style|iframe|object|embed|frame|frameset|applet|meta|link|base|form)\b[\s\S]*?(<\/\1\s*>|$)/gi, (m, t) => (/style/i.test(t) ? m.replace(/@import[^;]*;?/gi, "").replace(/expression\s*\(/gi, "") : ""))
    .replace(/<(script|iframe|object|embed|meta|link|base|form|input|button)\b[^>]*>/gi, "")
    .replace(/\son[a-z]+\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/gi, "")
    .replace(/(href|src|action|formaction|xlink:href)\s*=\s*("|')?\s*(javascript|vbscript|data:text\/html)[^"'\s>]*/gi, "$1=$2#");
}
async function folders(c) {
  const list = await c.list({ statusQuery: { messages: true, unseen: true } });
  return list.filter((f) => !f.flags?.has?.("\\Noselect")).map((f) => ({ path: f.path, name: f.name, special: f.specialUse || "", messages: f.status?.messages ?? null, unseen: f.status?.unseen ?? null }));
}
async function resolveFolder(c, want) {
  if (!want || /^inbox$/i.test(want)) return "INBOX";
  if (want === "\\Sent" || /^sent$/i.test(want)) { const l = await c.list(); const s = l.find((f) => f.specialUse === "\\Sent") || l.find((f) => /sent/i.test(f.path)); return s ? s.path : want; }
  return want;
}
async function snippetOf(c, uid) {
  try {
    const m = await c.fetchOne(String(uid), { source: { start: 0, maxLength: 12000 } }, { uid: true });
    const p = await simpleParser(m.source, { skipImageLinks: true, skipHtmlToText: false });
    return clean(p.text || "").slice(0, 180);
  } catch { return ""; }
}
export default async function handler(req, res) {
  if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
  if (!authed(req, res)) return json(res, 401, { error: "unauthorized" });
  if (!process.env.UNBANZ_MAIL_PASSWORD) return json(res, 503, { error: "mail_not_configured", detail: "UNBANZ_MAIL_PASSWORD is not set in Vercel" });
  const q = new URL(req.url, "http://x").searchParams;
  const op = q.get("op") || "list";
  const c = client();
  try {
    try { await c.connect(); } catch (e) { return json(res, 502, { error: "imap_login_failed", detail: clean(e.responseText || e.message).slice(0, 300), code: e.authenticationFailed ? "AUTHENTICATIONFAILED" : e.code || "" }); }
    if (op === "folders") return json(res, 200, { folders: await folders(c) });
    const folder = await resolveFolder(c, q.get("folder"));
    const lock = await c.getMailboxLock(folder, { readOnly: true });
    try {
      const total = c.mailbox.exists || 0;
      if (op === "msg") {
        const uid = String(+q.get("uid") || 0);
        const m = await c.fetchOne(uid, { uid: true, flags: true, envelope: true, source: true }, { uid: true });
        if (!m) return json(res, 404, { error: "not_found" });
        const p = await simpleParser(m.source);
        return json(res, 200, { folder, uid: m.uid, seen: m.flags?.has("\\Seen") || false, from: addr(p.from?.value), to: addr(p.to?.value), cc: addr(p.cc?.value), replyTo: addr(p.replyTo?.value), subject: p.subject || "", date: p.date || m.envelope?.date || null, text: p.text || "", html: p.html ? sanitize(p.html) : "", attachments: (p.attachments || []).map((a) => ({ filename: a.filename || "", type: a.contentType, size: a.size })) });
      }
      // UIDs newest first (all messages, or SEARCH results).
      const term = clean(q.get("q")).slice(0, 200);
      let uids;
      if (term) uids = (await c.search({ or: [{ subject: term }, { from: term }, { body: term }] }, { uid: true })) || [];
      else uids = total ? (await c.search({ all: true }, { uid: true })) || [] : [];
      if (op === "export" && q.get("since")) { const s = new Date(q.get("since")); if (!isNaN(s)) uids = (await c.search(term ? { since: s, or: [{ subject: term }, { from: term }, { body: term }] } : { since: s }, { uid: true })) || []; }
      uids.sort((a, b) => b - a);
      if (op === "export") {
        const limit = Math.min(2000, Math.max(1, +q.get("limit") || 500));
        const out = [];
        const pick = uids.slice(0, limit);
        if (pick.length) for await (const m of c.fetch(pick.join(","), { uid: true, flags: true, source: true }, { uid: true })) {
          const p = await simpleParser(m.source, { skipImageLinks: true });
          out.push({ uid: m.uid, from: addr(p.from?.value), replyTo: addr(p.replyTo?.value), to: addr(p.to?.value), date: p.date || null, subject: p.subject || "", seen: m.flags?.has("\\Seen") || false, text: (p.text || "").slice(0, 20000) });
        }
        out.sort((a, b) => b.uid - a.uid);
        return json(res, 200, { folder, total, matched: uids.length, exported: out.length, messages: out });
      }
      const size = Math.min(100, Math.max(5, +q.get("size") || 30)), page = Math.max(1, +q.get("page") || 1);
      const pick = uids.slice((page - 1) * size, page * size);
      const rows = [];
      if (pick.length) for await (const m of c.fetch(pick.join(","), { uid: true, flags: true, envelope: true, size: true }, { uid: true })) {
        rows.push({ uid: m.uid, seen: m.flags?.has("\\Seen") || false, from: addr(m.envelope?.from), to: addr(m.envelope?.to), subject: m.envelope?.subject || "", date: m.envelope?.date || null, size: m.size });
      }
      rows.sort((a, b) => b.uid - a.uid);
      if (q.get("snippets") !== "0") for (const r of rows) r.snippet = await snippetOf(c, r.uid);
      return json(res, 200, { folder, total, matched: uids.length, page, size, pages: Math.ceil(uids.length / size), q: term, messages: rows });
    } finally { lock.release(); }
  } catch (e) {
    return json(res, 500, { error: "imap_error", detail: clean(e.responseText || e.message).slice(0, 300) });
  } finally { try { await c.logout(); } catch { try { c.close(); } catch {} } }
}
