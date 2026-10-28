// Builds the two browser bundles into ../assets (override with OUT=dir) under content-hashed names:
//   rec.<hash>.js   recorder for public pages (vendored rrweb record, slimmed, MIT)   -> must stay < 25KB gzipped
//   rpv.<hash>.js   dashboard Replays list + player (loads only on the dashboard)
// Old hashed files are kept (cached pages may still reference them).  Usage: node build.mjs [rec|rpv|all]
import esbuild from "esbuild";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import zlib from "node:zlib";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.resolve(here, process.env.OUT || "../assets");
const which = process.argv[2] || "all";
fs.mkdirSync(out, { recursive: true });

// rrweb's record bundle carries canvas recording + an inline web worker we do not use (~4KB gz). Strip them.
const slim = {
  name: "slim-rrweb-record",
  setup(b) {
    b.onLoad({ filter: /@rrweb[\\/]record[\\/]dist[\\/]record\.js$/ }, (a) => {
      let s = fs.readFileSync(a.path, "utf8");
      s = s.replace(/^const jsContent = .*$/m, 'const jsContent = "";');
      const a1 = s.indexOf("function variableListFor("), a2 = s.indexOf("class StylesheetManager {");
      if (a1 < 0 || a2 < 0) throw new Error("rrweb layout changed: cannot slim canvas code");
      s = s.slice(0, a1) + "class CanvasManager { constructor() {} reset() {} freeze() {} unfreeze() {} lock() {} unlock() {} addWindow() {} addShadowRoot() {} resetShadowRoots() {} }\n" + s.slice(a2);
      return { contents: s, loader: "js" };
    });
  },
};

async function bundle(name, entry, extra = {}) {
  const r = await esbuild.build({ entryPoints: [path.join(here, entry)], bundle: true, minify: true, format: "iife", target: "es2018", write: false, legalComments: "none", plugins: [slim], ...extra });
  const code = r.outputFiles[0].contents;
  const hash = crypto.createHash("sha256").update(code).digest("hex").slice(0, 12);
  const file = `${name}.${hash}.js`;
  fs.writeFileSync(path.join(out, file), code);
  const gz = zlib.gzipSync(code, { level: 9 }).length;
  console.log(`${file}  ${code.length} B  ${gz} B gz`);
  return { file, gz };
}

if (which === "all" || which === "rec") {
  const r = await bundle("rec", "src/recorder.js");
  if (r.gz > 25 * 1024) { console.error("recorder exceeds 25KB gzipped"); process.exit(1); }
  fs.writeFileSync(path.join(here, "dist-rec.txt"), r.file + "\n");
}
if ((which === "all" || which === "rpv") && fs.existsSync(path.join(here, "src/player.js"))) {
  const r = await bundle("rpv", "src/player.js", { loader: { ".css": "text" } });
  fs.writeFileSync(path.join(here, "dist-rpv.txt"), r.file + "\n");
}
