// Mail for the private /users dashboard (team@unbanz.com and any mailbox connected in the UI).
// Auth: the existing /users session (cookie or X-Users-Token). POSTs also need same-origin + X-Ubz-Csrf: 1 (CSRF).
// Credentials connected in the UI live in Postgres; the password is AES-256-GCM encrypted (key = HKDF of USERS_SESSION_SECRET),
// never returned to the client and never logged. Env fallback: UNBANZ_MAIL_USER / UNBANZ_MAIL_PASSWORD / UNBANZ_MAIL_HOST.
// Reads use readOnly mailboxes + BODY.PEEK, so opening mail never marks it read. Writes only happen on explicit actions.
// GET  op=boxes | folders | list (folder, page, size, q) | msg (folder, uid) | export (folder, since, limit) | blocks | audit
// POST op=connect | disconnect | flag (seen) | move (to: archive|trash|inbox|junk|<path>) | delete (permanent, Trash only)
//      | block / unblock (pattern) | send (to, cc, bcc, subject, text, html, inReplyTo, references, attachments[{filename,type,data(base64)}])
import crypto from "node:crypto";
import { ImapFlow } from "imapflow";
import { simpleParser } from "mailparser";
import nodemailer from "nodemailer";
import MailComposer from "nodemailer/lib/mail-composer/index.js";
import { json, sameOrigin, readJson } from "../_lib/auth.mjs";
import { sql } from "../_lib/db.mjs";
import { authed } from "../_lib/uauth.mjs";
import { limit, audit, auditList } from "../_lib/guard.mjs";
import { geoLabels } from "../_lib/geo.mjs";
export const config = { maxDuration: 60, api: { bodyParser: false } };

const key = () => Buffer.from(crypto.hkdfSync("sha256", process.env.USERS_SESSION_SECRET || "", "unbanz-mail", "mailbox-password-v1", 32));
const enc = (t) => { const iv = crypto.randomBytes(12), c = crypto.createCipheriv("aes-256-gcm", key(), iv); const d = Buffer.concat([c.update(String(t), "utf8"), c.final()]); return ["g1", iv.toString("base64"), c.getAuthTag().toString("base64"), d.toString("base64")].join("."); };
const dec = (s) => { const [, iv, tag, d] = String(s).split("."); const c = crypto.createDecipheriv("aes-256-gcm", key(), Buffer.from(iv, "base64")); c.setAuthTag(Buffer.from(tag, "base64")); return Buffer.concat([c.update(Buffer.from(d, "base64")), c.final()]).toString("utf8"); };
let migrated;
const migrate = () => (migrated ||= Promise.all([
  sql(`create table if not exists mailboxes (id serial primary key, email text unique not null, imap_host text not null, imap_port int not null, smtp_host text, smtp_port int, pass_enc text not null, created_at timestamptz default now(), updated_at timestamptz default now())`),
  sql(`create table if not exists mail_blocks (id serial primary key, mailbox text not null, pattern text not null, created_at timestamptz default now(), unique (mailbox, pattern))`),
]).catch((e) => { migrated = null; throw e; }));
const envBox = () => { const [h, p] = String(process.env.UNBANZ_MAIL_HOST || "mail.spacemail.com:993").split(":"); return process.env.UNBANZ_MAIL_PASSWORD ? { id: "env", email: process.env.UNBANZ_MAIL_USER || "team@unbanz.com", imap_host: h, imap_port: +p || 993, smtp_host: h, smtp_port: 465, pass: process.env.UNBANZ_MAIL_PASSWORD, source: "env" } : null; };
async function boxes() { await migrate(); return sql(`select id, email, imap_host, imap_port, smtp_host, smtp_port, updated_at from mailboxes order by id`); }
async function getBox(id) {
  await migrate();
  const r = id && id !== "env" ? await sql(`select * from mailboxes where id = $1`, [+id || 0]) : id === "env" ? [] : await sql(`select * from mailboxes order by id limit 1`);
  if (r[0]) return { ...r[0], pass: dec(r[0].pass_enc), source: "db" };
  return envBox();
}
const client = (b) => new ImapFlow({ host: b.imap_host, port: +b.imap_port || 993, secure: true, auth: { user: b.email, pass: b.pass }, logger: false, socketTimeout: 45000, greetingTimeout: 15000, connectionTimeout: 15000 });
const loginErr = (e) => ({ error: "imap_login_failed", code: e.authenticationFailed ? "AUTHENTICATIONFAILED" : e.code || "", detail: String(e.responseText || e.message || "").replace(/\s+/g, " ").trim().slice(0, 300), hint: e.authenticationFailed ? "Wrong email/password, or IMAP access is disabled for this mailbox (Spacemail Manager or Webmail > Settings > IMAP/SMTP/POP3)." : "Could not reach the IMAP server; check host and port (Spacemail: mail.spacemail.com, 993 SSL)." });

const addr = (a) => (a && a.length ? a.map((x) => (x.name ? `${x.name} <${x.address || ""}>` : x.address || "")).join(", ") : "");
const clean = (s) => String(s || "").replace(/\s+/g, " ").trim();
const EMAIL = /^[^@\s<>,;"]+@[^@\s<>,;"]+\.[^@\s<>,;"]+$/;
const emails = (v) => { const l = (Array.isArray(v) ? v : String(v || "").split(/[,;]/)).map((x) => String(x).trim()).filter(Boolean).map((x) => (x.match(/<([^>]+)>/) || [, x])[1].trim()); if (l.length > 50 || l.some((x) => !EMAIL.test(x) || x.length > 254)) throw new Error("invalid_address"); return l; };
const PATH = (s) => { s = String(s || ""); if (!s || s.length > 200 || /[\r\n\0]/.test(s)) throw new Error("invalid_folder"); return s; };
const UID = (v) => { const n = +v; if (!Number.isInteger(n) || n < 1) throw new Error("invalid_uid"); return n; };
const UIDS = (v) => { const l = (Array.isArray(v) ? v : [v]).map(UID); if (!l.length || l.length > 500) throw new Error("invalid_uid"); return l; };

// Server-side HTML clean-up; the browser additionally renders it in a sandboxed iframe (no scripts) with a CSP that blocks remote images unless asked.
function sanitize(html) {
  return String(html || "")
    .replace(/<!--[\s\S]*?-->/g, "")
    .replace(/<(script|iframe|object|embed|frame|frameset|applet|noscript|template|svg|math)\b[\s\S]*?(<\/\1\s*>|$)/gi, "")
    .replace(/<\/?(script|iframe|object|embed|meta|link|base|form|input|button|textarea|select|frame|frameset)\b[^>]*>/gi, "")
    .replace(/\son[a-z]+\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/gi, "")
    .replace(/\s(srcdoc|formaction|action|ping)\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/gi, "")
    .replace(/(href|src|background|xlink:href)\s*=\s*(["']?)\s*(javascript|vbscript|data:(?!image\/(png|gif|jpe?g|webp)))[^"'\s>]*/gi, "$1=$2#")
    .replace(/@import[^;]*;?/gi, "").replace(/expression\s*\(/gi, "(");
}
async function specialPath(c, use, rx, create) {
  const l = await c.list();
  const f = l.find((x) => x.specialUse === use) || l.find((x) => rx.test(x.name) || rx.test(x.path));
  if (f) return f.path;
  if (create) { await c.mailboxCreate(create).catch(() => {}); return create; }
  return null;
}
const ROLES = [["inbox", null, /^inbox$/i], ["sent", "\\Sent", /^(sent|sent items|sent mail|sent messages)$/i], ["drafts", "\\Drafts", /^drafts?$/i], ["trash", "\\Trash", /^(trash|deleted|deleted items|deleted messages|bin)$/i], ["junk", "\\Junk", /^(junk|spam|junk e-?mail|bulk)$/i], ["archive", "\\Archive", /^archives?$/i]];
const roleOf = (f, taken) => { if (/^inbox$/i.test(f.path)) return "inbox"; for (const [r, use] of ROLES) if (use && f.specialUse === use && !taken.has(r)) return r; for (const [r, , rx] of ROLES) if (!taken.has(r) && (rx.test(f.name) || rx.test(f.path.split(f.delimiter || "/").pop()))) return r; return "custom"; };
async function resolveFolder(c, want) {
  if (!want || /^inbox$/i.test(want)) return "INBOX";
  if (/^sent$/i.test(want)) return (await specialPath(c, "\\Sent", /^sent/i)) || want;
  return PATH(want);
}
// In-instance cache for list pages (warm lambdas reuse it); any write on the mailbox clears it.
const CACHE = new Map(), TTL = 20000;
const ckey = (b, ...k) => `${b.email}|${k.join("|")}`;
const cget = (k) => { const v = CACHE.get(k); return v && Date.now() - v.t < TTL ? v.d : null; };
const cset = (k, d) => { if (CACHE.size > 200) CACHE.clear(); CACHE.set(k, { t: Date.now(), d }); };
const cdrop = (b) => { for (const k of CACHE.keys()) if (k.startsWith(b.email + "|")) CACHE.delete(k); };

async function blocksFor(b) { await migrate(); return (await sql(`select pattern from mail_blocks where mailbox = $1 order by pattern`, [b.email])).map((r) => r.pattern); }
// Auto-filter: messages in INBOX from blocked senders/domains are moved to Junk (never deleted).
async function autoFilter(c, b) {
  let pats = []; try { pats = await blocksFor(b); } catch { return 0; }
  if (!pats.length) return 0;
  const lock = await c.getMailboxLock("INBOX");
  let moved = 0;
  try {
    const junk = await specialPath(c, "\\Junk", /^(junk|spam)/i, "Junk");
    for (const p of pats) {
      const u = (await c.search({ from: p }, { uid: true })) || [];
      if (u.length) { await c.messageMove(u.join(","), junk, { uid: true }); moved += u.length; }
    }
  } finally { lock.release(); }
  return moved;
}

async function list(c, b, q) {
  if (q.get("folder") === "__blocked") return blockedList(c, b, q);
  const folder = await resolveFolder(c, q.get("folder"));
  const term = clean(q.get("q")).slice(0, 200);
  const size = Math.min(100, Math.max(5, +q.get("size") || 40)), page = Math.max(1, +q.get("page") || 1);
  const k = ckey(b, "list", folder, term, page, size);
  if (q.get("fresh") !== "1") { const hit = cget(k); if (hit) return { ...hit, cached: true }; }
  let filtered = 0;
  if (folder === "INBOX" && page === 1) filtered = await autoFilter(c, b).catch(() => 0);
  const lock = await c.getMailboxLock(folder, { readOnly: true });
  try {
    const total = c.mailbox.exists || 0;
    let uids = term ? (await c.search({ or: [{ subject: term }, { from: term }, { to: term }, { body: term }] }, { uid: true })) || [] : total ? (await c.search({ all: true }, { uid: true })) || [] : [];
    uids.sort((x, y) => y - x);
    const pick = uids.slice((page - 1) * size, page * size), rows = await rowsFor(c, folder, pick);
    rows.sort((x, y) => y.uid - x.uid);
    const d = { folder, total, unseen: null, matched: uids.length, page, size, pages: Math.ceil(uids.length / size), q: term, filtered, messages: rows };
    cset(k, d);
    return d;
  } finally { lock.release(); }
}
async function message(c, folder, uid) {
  const lock = await c.getMailboxLock(folder, { readOnly: true });
  try {
    const m = await c.fetchOne(String(uid), { uid: true, flags: true, envelope: true, source: true }, { uid: true });
    if (!m) return null;
    const p = await simpleParser(m.source);
    const cids = {};
    for (const a of p.attachments || []) if (a.cid && /^image\//.test(a.contentType) && a.size < 400000) cids[a.cid] = `data:${a.contentType};base64,${a.content.toString("base64")}`;
    let html = p.html ? sanitize(p.html) : "";
    html = html.replace(/cid:([^"'\s)>]+)/gi, (x, id) => cids[id] || x);
    let geo = null; try { geo = (await geoLabels([{ raw: m.source.toString("utf8", 0, Math.min(m.source.length, 65536)), fromAddr: p.from?.value?.[0]?.address || "" }]))[0]; } catch {}
    return { geo, folder, uid: m.uid, seen: m.flags?.has("\\Seen") || false, from: addr(p.from?.value), fromAddr: p.from?.value?.[0]?.address || "", to: addr(p.to?.value), cc: addr(p.cc?.value), replyTo: addr(p.replyTo?.value), subject: p.subject || "", date: p.date || m.envelope?.date || null, messageId: p.messageId || "", references: [].concat(p.references || []).join(" "), text: p.text || "", html, remote: /<img[^>]+src\s*=\s*["']?https?:/i.test(html) || /url\(\s*["']?https?:/i.test(html), attachments: (p.attachments || []).filter((a) => !a.cid || !cids[a.cid]).map((a) => ({ filename: a.filename || "", type: a.contentType, size: a.size })) };
  } finally { lock.release(); }
}
async function exportMail(c, folder, q) {
  const lock = await c.getMailboxLock(folder, { readOnly: true });
  try {
    const total = c.mailbox.exists || 0, s = q.get("since") ? new Date(q.get("since")) : null;
    let uids = total ? (await c.search(s && !isNaN(s) ? { since: s } : { all: true }, { uid: true })) || [] : [];
    uids.sort((a, b) => b - a);
    const pick = uids.slice(0, Math.min(2000, Math.max(1, +q.get("limit") || 500))), out = [];
    if (pick.length) for await (const m of c.fetch(pick.join(","), { uid: true, flags: true, source: true }, { uid: true })) {
      const p = await simpleParser(m.source, { skipImageLinks: true });
      out.push({ uid: m.uid, from: addr(p.from?.value), replyTo: addr(p.replyTo?.value), to: addr(p.to?.value), cc: addr(p.cc?.value), date: p.date || null, subject: p.subject || "", messageId: p.messageId || "", inReplyTo: p.inReplyTo || "", seen: m.flags?.has("\\Seen") || false, answered: m.flags?.has("\\Answered") || false, text: (p.text || "").slice(0, 20000), _raw: m.source.toString("utf8", 0, Math.min(m.source.length, 65536)), _fa: p.from?.value?.[0]?.address || "" });
    }
    try { const g = await geoLabels(out.map((x) => ({ raw: x._raw, fromAddr: x._fa }))); out.forEach((x, i) => (x.geo = g[i])); } catch {}
    out.forEach((x) => { delete x._raw; delete x._fa; });
    out.sort((a, b) => b.uid - a.uid);
    return { folder, total, matched: uids.length, exported: out.length, messages: out };
  } finally { lock.release(); }
}

async function folders(c, b) {
  const l = (await c.list({ statusQuery: { messages: true, unseen: true } })).filter((f) => !f.flags?.has?.("\\Noselect"));
  const taken = new Set(), out = [];
  // special-use flags win over names
  for (const f of [...l].sort((x, y) => (y.specialUse ? 1 : 0) - (x.specialUse ? 1 : 0))) { const role = roleOf(f, taken); if (role !== "custom") taken.add(role); out.push({ path: f.path, name: f.name, special: f.specialUse || "", role, messages: f.status?.messages ?? null, unseen: f.status?.unseen ?? null }); }
  const order = ["inbox", "sent", "drafts", "archive", "junk", "trash", "custom"];
  out.sort((x, y) => order.indexOf(x.role) - order.indexOf(y.role) || x.path.localeCompare(y.path));
  let blocked = { messages: 0, unseen: 0 };
  try { const r = await blockedAll(c, b, ""); blocked = { messages: r.length, unseen: r.filter((x) => !x.seen).length }; } catch {}
  return { folders: out, blocked };
}
const fromQuery = (pats) => (pats.length === 1 ? { from: pats[0] } : { or: pats.map((p) => ({ from: p })) });
// Every message from a blocked sender, in any folder. Returns rows with their own folder.
async function blockedAll(c, b, term) {
  const pats = (await blocksFor(b)).slice(0, 40);
  if (!pats.length) return [];
  const k = ckey(b, "blockedAll", term), hit = cget(k); if (hit) return hit;
  const l = (await c.list()).filter((f) => !f.flags?.has?.("\\Noselect"));
  const rows = [];
  for (const f of l) {
    const lock = await c.getMailboxLock(f.path, { readOnly: true });
    try {
      if (!c.mailbox.exists) continue;
      const qy = fromQuery(pats); const u = (await c.search(term ? { ...qy, text: term } : qy, { uid: true })) || [];
      if (!u.length) continue;
      for await (const m of c.fetch(u.slice(-1500).join(","), { uid: true, flags: true, envelope: true, internalDate: true }, { uid: true })) rows.push({ folder: f.path, uid: m.uid, seen: m.flags?.has("\\Seen") || false, t: +new Date(m.envelope?.date || m.internalDate || 0) });
    } finally { lock.release(); }
    if (rows.length > 5000) break;
  }
  rows.sort((x, y) => y.t - x.t);
  cset(k, rows); return rows;
}
async function rowsFor(c, folder, uids) {
  const rows = [], items = [];
  if (!uids.length) return rows;
  for await (const m of c.fetch(uids.join(","), { uid: true, flags: true, envelope: true, size: true, headers: true, source: { start: 0, maxLength: 8000 } }, { uid: true })) {
    let snippet = "";
    try { const p = await simpleParser(m.source, { skipImageLinks: true }); snippet = clean(p.text || "").slice(0, 160); } catch {}
    const fromAddr = m.envelope?.from?.[0]?.address || "";
    rows.push({ folder, uid: m.uid, seen: m.flags?.has("\\Seen") || false, flagged: m.flags?.has("\\Flagged") || false, answered: m.flags?.has("\\Answered") || false, from: addr(m.envelope?.from), fromAddr, to: addr(m.envelope?.to), subject: m.envelope?.subject || "", date: m.envelope?.date || null, size: m.size, snippet });
    items.push({ raw: m.headers ? m.headers.toString("utf8") : "", fromAddr });
  }
  try { const g = await geoLabels(items); rows.forEach((r, i) => (r.geo = g[i])); } catch {}
  return rows;
}
async function blockedList(c, b, q) {
  const term = clean(q.get("q")).slice(0, 200);
  const size = Math.min(100, Math.max(5, +q.get("size") || 40)), page = Math.max(1, +q.get("page") || 1);
  const all = await blockedAll(c, b, term), pick = all.slice((page - 1) * size, page * size), out = [];
  const by = {}; for (const r of pick) (by[r.folder] ||= []).push(r.uid);
  for (const [f, u] of Object.entries(by)) { const lock = await c.getMailboxLock(f, { readOnly: true }); try { out.push(...(await rowsFor(c, f, u))); } finally { lock.release(); } }
  const pos = new Map(pick.map((r, i) => [r.folder + "|" + r.uid, i])); out.sort((x, y) => pos.get(x.folder + "|" + x.uid) - pos.get(y.folder + "|" + y.uid));
  return { folder: "__blocked", total: all.length, matched: all.length, page, size, pages: Math.ceil(all.length / size), q: term, filtered: 0, messages: out };
}

async function post(req, res, b, box) {
  const op = String(b.op || "");
  if (op === "connect") {
    if (!(await limit(req, "mail-connect", 10, 3600))) return json(res, 429, { error: "rate_limited" });
    const email = String(b.email || "").trim().toLowerCase(), pass = String(b.password || "");
    const imap_host = String(b.imap_host || "mail.spacemail.com").trim(), imap_port = +b.imap_port || 993, smtp_host = String(b.smtp_host || "mail.spacemail.com").trim(), smtp_port = +b.smtp_port || 465;
    const HOST = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/i;
    if (!EMAIL.test(email) || !pass || pass.length > 512 || !HOST.test(imap_host) || !HOST.test(smtp_host) || ![993, 143].includes(imap_port) && !(imap_port > 0 && imap_port < 65536) || !(smtp_port > 0 && smtp_port < 65536)) return json(res, 400, { error: "invalid_input" });
    const c = client({ email, pass, imap_host, imap_port });
    try { await c.connect(); } catch (e) { await audit(req, "mail-connect", email, false, e.authenticationFailed ? "auth failed" : e.code || ""); return json(res, 400, loginErr(e)); } finally { try { await c.logout(); } catch { try { c.close(); } catch {} } }
    await migrate();
    await sql(`insert into mailboxes (email, imap_host, imap_port, smtp_host, smtp_port, pass_enc) values ($1,$2,$3,$4,$5,$6) on conflict (email) do update set imap_host = excluded.imap_host, imap_port = excluded.imap_port, smtp_host = excluded.smtp_host, smtp_port = excluded.smtp_port, pass_enc = excluded.pass_enc, updated_at = now()`, [email, imap_host, imap_port, smtp_host, smtp_port, enc(pass)]);
    await audit(req, "mail-connect", email, true);
    return json(res, 200, { ok: true, mailboxes: await boxes() });
  }
  if (op === "disconnect") { await migrate(); await sql(`delete from mailboxes where id = $1`, [+b.id || 0]); await audit(req, "mail-disconnect", String(b.id), true); return json(res, 200, { ok: true, mailboxes: await boxes() }); }
  if (!box) return json(res, 503, { error: "mail_not_configured" });
  if (op === "block" || op === "unblock") {
    const p = String(b.pattern || "").trim().toLowerCase();
    if (!/^(@?[a-z0-9.-]+\.[a-z]{2,}|[^@\s<>]+@[a-z0-9.-]+\.[a-z]{2,})$/i.test(p) || p.length > 254) return json(res, 400, { error: "invalid_pattern" });
    await migrate();
    if (op === "block") await sql(`insert into mail_blocks (mailbox, pattern) values ($1,$2) on conflict do nothing`, [box.email, p]);
    else await sql(`delete from mail_blocks where mailbox = $1 and pattern = $2`, [box.email, p]);
    cdrop(box); await audit(req, "mail-" + op, `${box.email} ${p}`, true);
    let moved = 0;
    if (op === "block") { const c = client(box); try { await c.connect(); moved = await autoFilter(c, box); } catch {} finally { try { await c.logout(); } catch {} } }
    return json(res, 200, { ok: true, moved, blocks: await blocksFor(box) });
  }
  if (op === "send") return send(req, res, b, box);
  if (!["flag", "move", "delete"].includes(op)) return json(res, 400, { error: "bad_op" });
  const uids = UIDS(b.uids ?? b.uid);
  const c = client(box);
  try {
    try { await c.connect(); } catch (e) { return json(res, 502, loginErr(e)); }
    const folder = await resolveFolder(c, b.folder);
    const lock = await c.getMailboxLock(folder);
    try {
      const set = uids.join(",");
      let out = { ok: true };
      if (op === "flag") {
        const fl = b.flag === "flagged" ? "\\Flagged" : "\\Seen";
        if (b.value) await c.messageFlagsAdd(set, [fl], { uid: true }); else await c.messageFlagsRemove(set, [fl], { uid: true });
      } else if (op === "move") {
        const t = String(b.to || "");
        const dest = t === "archive" ? await specialPath(c, "\\Archive", /^archive/i, "Archive") : t === "trash" ? await specialPath(c, "\\Trash", /^(trash|deleted)/i, "Trash") : t === "junk" ? await specialPath(c, "\\Junk", /^(junk|spam)/i, "Junk") : t === "inbox" ? "INBOX" : PATH(t);
        if (dest === folder) return json(res, 400, { error: "same_folder" });
        const r = await c.messageMove(set, dest, { uid: true });
        out = { ok: true, dest, uidMap: r && r.uidMap ? Object.fromEntries(r.uidMap) : null };
      } else {
        // Permanent delete only from Trash/Junk; elsewhere 'delete' means move to Trash (undoable).
        const trash = await specialPath(c, "\\Trash", /^(trash|deleted)/i, "Trash");
        const junk = await specialPath(c, "\\Junk", /^(junk|spam)/i, null);
        if (folder !== trash && folder !== junk) { const r = await c.messageMove(set, trash, { uid: true }); out = { ok: true, dest: trash, uidMap: r && r.uidMap ? Object.fromEntries(r.uidMap) : null }; }
        else { await c.messageDelete(set, { uid: true }); out = { ok: true, permanent: true }; }
      }
      cdrop(box); await audit(req, "mail-" + op, `${box.email} ${folder} ${set}`.slice(0, 200), true, op === "move" ? String(b.to) : op === "flag" ? `${b.flag || "seen"}=${!!b.value}` : "");
      return json(res, 200, out);
    } finally { lock.release(); }
  } finally { try { await c.logout(); } catch { try { c.close(); } catch {} } }
}

async function send(req, res, b, box) {
  if (!(await limit(req, "mail-send", 30, 3600))) return json(res, 429, { error: "rate_limited" });
  const to = emails(b.to), cc = emails(b.cc), bcc = emails(b.bcc);
  if (!to.length && !cc.length && !bcc.length) return json(res, 400, { error: "no_recipients" });
  const subject = String(b.subject || "").replace(/[\r\n]+/g, " ").slice(0, 300), text = String(b.text || "").slice(0, 200000);
  const att = Array.isArray(b.attachments) ? b.attachments.slice(0, 10) : [];
  let bytes = 0;
  const attachments = att.map((a) => { const content = Buffer.from(String(a.data || ""), "base64"); bytes += content.length; return { filename: String(a.filename || "file").replace(/[\r\n"\\/]/g, "_").slice(0, 120), contentType: /^[\w.+-]+\/[\w.+-]+$/.test(a.type || "") ? a.type : "application/octet-stream", content }; });
  if (bytes > 3 * 1024 * 1024) return json(res, 413, { error: "attachments_too_large", max: "3 MB total" });
  const ref = (v) => String(v || "").replace(/[\r\n]+/g, " ").slice(0, 2000);
  const mail = { from: box.email, to, cc, bcc, subject, text, attachments, inReplyTo: ref(b.inReplyTo) || undefined, references: ref(b.references) || undefined };
  if (b.dry === true) return json(res, 200, { ok: true, dry: true, to, cc, bcc, subject, bytes });
  const raw = await new MailComposer({ ...mail, bcc: undefined }).compile().build();
  const tx = nodemailer.createTransport({ host: box.smtp_host || box.imap_host, port: +box.smtp_port || 465, secure: (+box.smtp_port || 465) === 465, auth: { user: box.email, pass: box.pass }, connectionTimeout: 15000, socketTimeout: 30000 });
  let info;
  try { info = await tx.sendMail({ envelope: { from: box.email, to: [...to, ...cc, ...bcc] }, raw }); }
  catch (e) { await audit(req, "mail-send", box.email, false, String(e.code || e.responseCode || "")); return json(res, 502, { error: "smtp_failed", detail: String(e.response || e.message || "").replace(/\s+/g, " ").slice(0, 300) }); }
  // Copy to Sent (IMAP APPEND) and mark the original answered.
  let saved = false;
  const c = client(box);
  try {
    await c.connect();
    const sent = await specialPath(c, "\\Sent", /^sent/i, "Sent");
    await c.append(sent, raw, ["\\Seen"]); saved = true;
    if (b.replyUid && b.replyFolder) { const l = await c.getMailboxLock(PATH(b.replyFolder)); try { await c.messageFlagsAdd(String(UID(b.replyUid)), ["\\Answered"], { uid: true }); } finally { l.release(); } }
  } catch {} finally { try { await c.logout(); } catch {} }
  cdrop(box); await audit(req, "mail-send", `${box.email} -> ${[...to, ...cc].join(",")}`.slice(0, 200), true, `${subject.slice(0, 80)} | ${attachments.length} att`);
  return json(res, 200, { ok: true, messageId: info.messageId, savedToSent: saved });
}

export default async function handler(req, res) {
  if (!authed(req, res)) return json(res, 401, { error: "unauthorized" });
  try {
    if (req.method === "POST") {
      // CSRF: same-origin Origin header required, plus a custom header a cross-site form cannot set.
      if (!req.headers.origin || !sameOrigin(req) || req.headers["x-ubz-csrf"] !== "1") return json(res, 403, { error: "forbidden" });
      if (!(await limit(req, "mail-post", 120, 60))) return json(res, 429, { error: "rate_limited" });
      let b; try { b = await readJson(req, 4.3 * 1024 * 1024); } catch { return json(res, 400, { error: "bad_request" }); }
      if (!b || typeof b !== "object") return json(res, 400, { error: "bad_request" });
      let box = null; if (!["connect", "disconnect"].includes(b.op)) { try { box = await getBox(b.mb); } catch { box = envBox(); } }
      return await post(req, res, b, box);
    }
    if (req.method !== "GET") return json(res, 405, { error: "method_not_allowed" });
    if (!(await limit(req, "mail-get", 300, 60))) return json(res, 429, { error: "rate_limited" });
    const q = new URL(req.url, "http://x").searchParams;
    const op = q.get("op") || "list";
    if (op === "audit") return json(res, 200, { audit: await auditList(150) });
    let box; try { box = await getBox(q.get("mb")); } catch { box = envBox(); }
    if (op === "boxes") { let l = []; try { l = await boxes(); } catch {} const e = envBox(); return json(res, 200, { mailboxes: l.length ? l : e ? [{ id: "env", email: e.email, imap_host: e.imap_host, imap_port: e.imap_port, source: "env" }] : [] }); }
    if (!box) return json(res, 503, { error: "mail_not_configured", detail: "No mailbox connected. Use Connect mailbox." });
    if (op === "blocks") return json(res, 200, { blocks: await blocksFor(box) });
    const c = client(box);
    try {
      try { await c.connect(); } catch (e) { return json(res, 502, { ...loginErr(e), mailbox: box.email }); }
      if (op === "folders") return json(res, 200, { mailbox: box.email, ...(await folders(c, box)) });
      if (op === "list") return json(res, 200, { mailbox: box.email, ...(await list(c, box, q)) });
      const folder = await resolveFolder(c, q.get("folder"));
      if (op === "msg") { const m = await message(c, folder, UID(q.get("uid"))); return m ? json(res, 200, m) : json(res, 404, { error: "not_found" }); }
      if (op === "export") { await audit(req, "mail-export", `${box.email} ${folder}`, true); return json(res, 200, await exportMail(c, folder, q)); }
      return json(res, 400, { error: "bad_op" });
    } finally { try { await c.logout(); } catch { try { c.close(); } catch {} } }
  } catch (e) {
    const m = String(e && e.message || "");
    if (/^invalid_/.test(m)) return json(res, 400, { error: m });
    return json(res, 500, { error: "server_error", detail: String(e.responseText || "").slice(0, 200) });
  }
}
