// Read-only IMAP inbox for team@unbanz.com (private /users dashboard only).
// Env (encrypted in Vercel): UNBANZ_MAIL_USER, UNBANZ_MAIL_PASSWORD, UNBANZ_MAIL_HOST (host[:port], default mail.spacemail.com:993, implicit TLS).
// Every mailbox is opened with readOnly:true and bodies are fetched with BODY.PEEK, so nothing is marked read, moved or deleted. No sending.
// GET ?op=folders | ?op=list&folder=INBOX&page=1&size=30&q=term | ?op=msg&folder=INBOX&uid=123 | ?op=export&folder=INBOX&limit=500&since=YYYY-MM-DD
import { ImapFlow } from "imapflow";
import { simpleParser } from "mailparser";
import crypto from "node:crypto";
import { json, sameOrigin, readJson } from "../_lib/auth.mjs";
import { sql } from "../_lib/db.mjs";
import { authed } from "../_lib/uauth.mjs";
export const config = { maxDuration: 60 };

// Mailbox credentials entered in the dashboard are stored in Postgres, the password encrypted with AES-256-GCM
// (key = HKDF-SHA256 of the server-only USERS_SESSION_SECRET). The password is never returned or logged.
const key = () => Buffer.from(crypto.hkdfSync("sha256", process.env.USERS_SESSION_SECRET || "", "unbanz-mail", "mailbox-password-v1", 32));
const enc = (t) => { const iv = crypto.randomBytes(12), c = crypto.createCipheriv("aes-256-gcm", key(), iv); const d = Buffer.concat([c.update(String(t), "utf8"), c.final()]); return ["g1", iv.toString("base64"), c.getAuthTag().toString("base64"), d.toString("base64")].join("."); };
const dec = (s) => { const [, iv, tag, d] = String(s).split("."); const c = crypto.createDecipheriv("aes-256-gcm", key(), Buffer.from(iv, "base64")); c.setAuthTag(Buffer.from(tag, "base64")); return Buffer.concat([c.update(Buffer.from(d, "base64")), c.final()]).toString("utf8"); };
let migrated;
const migrate = () => (migrated ||= sql(`create table if not exists mailboxes (id serial primary key, email text unique not null, imap_host text not null, imap_port int not null, smtp_host text, smtp_port int, pass_enc text not null, created_at timestamptz default now(), updated_at timestamptz default now())`).catch((e) => { migrated = null; throw e; }));
const envBox = () => { const [h, p] = String(process.env.UNBANZ_MAIL_HOST || "mail.spacemail.com:993").split(":"); return process.env.UNBANZ_MAIL_PASSWORD ? { id: "env", email: process.env.UNBANZ_MAIL_USER || "team@unbanz.com", imap_host: h, imap_port: +p || 993, pass: process.env.UNBANZ_MAIL_PASSWORD, source: "env" } : null; };
async function boxes() { await migrate(); return sql(`select id, email, imap_host, imap_port, smtp_host, smtp_port, updated_at from mailboxes order by id`); }
async function getBox(id) {
  await migrate();
  const r = id && id !== "env" ? await sql(`select * from mailboxes where id = $1`, [+id || 0]) : await sql(`select * from mailboxes order by id limit 1`);
  if (r[0]) return { ...r[0], pass: dec(r[0].pass_enc), source: "db" };
  return envBox();
}
function client(b) {
  return new ImapFlow({ host: b.imap_host, port: +b.imap_port || 993, secure: true, auth: { user: b.email, pass: b.pass }, logger: false, socketTimeout: 45000, greetingTimeout: 15000, connectionTimeout: 15000 });
}
const loginErr = (e) => { const d = String(e.responseText || e.message || "").replace(/\s+/g, " ").trim().slice(0, 300); return { error: "imap_login_failed", code: e.authenticationFailed ? "AUTHENTICATIONFAILED" : e.code || "", detail: d, hint: e.authenticationFailed ? "Wrong email/password, or IMAP access is disabled for this mailbox (Spacemail Manager or Webmail > Settings > IMAP/SMTP/POP3)." : "Could not reach the IMAP server; check host and port (Spacemail: mail.spacemail.com, 993 SSL)." }; };
async function manage(req, res) {
  if (!sameOrigin(req)) return json(res, 403, { error: "forbidden" });
  let b; try { b = await readJson(req, 4000); } catch { return json(res, 400, { error: "bad_request" }); }
  await migrate();
  if (b.op === "disconnect") { await sql(`delete from mailboxes where id = $1`, [+b.id || 0]); return json(res, 200, { ok: true, mailboxes: await boxes() }); }
  if (b.op !== "connect") return json(res, 400, { error: "bad_op" });
  const email = String(b.email || "").trim().toLowerCase(), pass = String(b.password || "");
  const imap_host = String(b.imap_host || "mail.spacemail.com").trim(), imap_port = +b.imap_port || 993, smtp_host = String(b.smtp_host || "mail.spacemail.com").trim(), smtp_port = +b.smtp_port || 465;
  if (!/^[^@\s]+@[^@\s]+$/.test(email) || !pass || !/^[a-z0-9.-]+$/i.test(imap_host)) return json(res, 400, { error: "invalid_input" });
  const c = client({ email, pass, imap_host, imap_port });
  try { await c.connect(); } catch (e) { return json(res, 400, loginErr(e)); } finally { try { await c.logout(); } catch { try { c.close(); } catch {} } }
  await sql(`insert into mailboxes (email, imap_host, imap_port, smtp_host, smtp_port, pass_enc) values ($1,$2,$3,$4,$5,$6) on conflict (email) do update set imap_host = excluded.imap_host, imap_port = excluded.imap_port, smtp_host = excluded.smtp_host, smtp_port = excluded.smtp_port, pass_enc = excluded.pass_enc, updated_at = now()`, [email, imap_host, imap_port, smtp_host, smtp_port, enc(pass)]);
  return json(res, 200, { ok: true, mailboxes: await boxes() });
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
  if (!authed(req, res)) return json(res, 401, { error: "unauthorized" });
  if (req.method === "POST") { try { return await manage(req, res); } catch { return json(res, 500, { error: "server_error" }); } }
  if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
  const q = new URL(req.url, "http://x").searchParams;
  const op = q.get("op") || "list";
  let box; try { box = await getBox(q.get("mb")); } catch { box = envBox(); }
  if (op === "boxes") { let l = []; try { l = await boxes(); } catch {} const e = envBox(); return json(res, 200, { mailboxes: l.length ? l : e ? [{ id: "env", email: e.email, imap_host: e.imap_host, imap_port: e.imap_port, source: "env" }] : [] }); }
  if (!box) return json(res, 503, { error: "mail_not_configured", detail: "No mailbox connected. Use Connect mailbox." });
  const c = client(box);
  try {
    try { await c.connect(); } catch (e) { return json(res, 502, { ...loginErr(e), mailbox: box.email }); }
    if (op === "folders") return json(res, 200, { mailbox: box.email, folders: await folders(c) });
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
