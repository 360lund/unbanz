// node build.mjs -> ../../assets/adrec.<hash>.js (recorder, ad visitors only) and ../../assets/adrv.<hash>.js (private viewer)
import esbuild from "esbuild"; import fs from "node:fs"; import path from "node:path"; import crypto from "node:crypto"; import zlib from "node:zlib"; import { fileURLToPath } from "node:url";
const here = path.dirname(fileURLToPath(import.meta.url)), out = path.resolve(here, "../../assets");
const slim = { name: "slim", setup(b) { b.onLoad({ filter: /@rrweb[\\/]record[\\/]dist[\\/]record\.js$/ }, (a) => { let s = fs.readFileSync(a.path, "utf8"); s = s.replace(/^const jsContent = .*$/m, 'const jsContent = "";'); const a1 = s.indexOf("function variableListFor("), a2 = s.indexOf("class StylesheetManager {"); if (a1 < 0 || a2 < 0) throw new Error("rrweb layout changed"); s = s.slice(0, a1) + "class CanvasManager { constructor() {} reset() {} freeze() {} unfreeze() {} lock() {} unlock() {} addWindow() {} addShadowRoot() {} resetShadowRoots() {} }\n" + s.slice(a2); return { contents: s, loader: "js" }; }); } };
const res = {};
for (const [name, entry] of [["adrec", "src/recorder.js"], ["adrv", "src/viewer.js"]]) {
  const r = await esbuild.build({ entryPoints: [path.join(here, entry)], bundle: true, minify: true, format: "iife", target: "es2018", write: false, legalComments: "none", plugins: [slim], loader: { ".css": "text" } });
  const code = r.outputFiles[0].contents, hash = crypto.createHash("sha256").update(code).digest("hex").slice(0, 12), file = `${name}.${hash}.js`;
  fs.writeFileSync(path.join(out, file), code); res[name] = file;
  console.log(file, code.length, "B", zlib.gzipSync(code).length, "B gz");
}
fs.writeFileSync(path.join(here, "dist.json"), JSON.stringify(res) + "\n");
