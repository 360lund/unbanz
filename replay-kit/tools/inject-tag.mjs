// Adds (or re-points) the recorder <script> tag on every public HTML page.
//   node tools/inject-tag.mjs <siteRoot> <recFile> [--anchor '<regex>'] [--skip dir1,dir2] [--dry]
// The tag goes right after the page's tracker script (anchor), so it loads in the same place/way as the other
// hashed shared scripts. Re-running with a new hashed file updates every reference; old files are left in assets/.
import fs from "node:fs";
import path from "node:path";

const [root, file, ...rest] = process.argv.slice(2);
if (!root || !file) { console.error("usage: inject-tag.mjs <siteRoot> <rec.<hash>.js> [--anchor regex] [--skip a,b] [--dry]"); process.exit(1); }
const opt = (k, d) => { const i = rest.indexOf(k); return i >= 0 ? rest[i + 1] : d; };
const anchor = new RegExp(opt("--anchor", '<script src="/assets/site[a-z-]*\\.[0-9a-f]+\\.js"[^>]*></script>'));
const skip = new Set(["node_modules", ".git", "replay-kit", ...(opt("--skip", "users").split(","))]);
const dry = rest.includes("--dry");
const tag = `<script src="/assets/${file}" defer></script>`;
const existing = /<script src="\/assets\/rec\.[0-9a-f]+\.js" defer><\/script>/;
let added = 0, updated = 0, same = 0, none = [];
(function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.isDirectory()) { if (!skip.has(e.name)) walk(path.join(d, e.name)); continue; }
    if (!e.name.endsWith(".html")) continue;
    const f = path.join(d, e.name); let s = fs.readFileSync(f, "utf8");
    if (existing.test(s)) { const n = s.replace(existing, tag); if (n === s) same++; else { updated++; if (!dry) fs.writeFileSync(f, n); } continue; }
    const m = anchor.exec(s);
    if (!m) { none.push(path.relative(root, f)); continue; }
    s = s.slice(0, m.index + m[0].length) + tag + s.slice(m.index + m[0].length);
    added++; if (!dry) fs.writeFileSync(f, s);
  }
})(path.resolve(root));
console.log(JSON.stringify({ added, updated, same, withoutAnchor: none }));
