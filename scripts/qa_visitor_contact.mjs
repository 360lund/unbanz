import puppeteer from "/tmp/qa-render/node_modules/puppeteer-core/lib/esm/puppeteer/puppeteer-core.js";

const base = "http://127.0.0.1:8765";
const browser = await puppeteer.launch({
  executablePath: "/usr/local/bin/google-chrome",
  headless: true,
  args: ["--no-sandbox", "--disable-gpu"],
});
const page = await browser.newPage();
let country = "";
await page.setRequestInterception(true);
page.on("request", (req) => {
  if (req.url().includes("/api/geo")) {
    req.respond({
      status: 200,
      contentType: "application/json",
      headers: { "Cache-Control": "private, no-store" },
      body: JSON.stringify({ c: country }),
    });
  } else req.continue();
});

async function check(code, path, expectBoth) {
  country = code;
  await page.goto(base + path, { waitUntil: "domcontentloaded" });
  await page.evaluate(() => sessionStorage.clear());
  await page.reload({ waitUntil: "domcontentloaded" });
  await page.waitForFunction(() => document.documentElement.getAttribute("data-contact"), { timeout: 8000 });
  await new Promise((r) => setTimeout(r, 200));
  const data = await page.evaluate(() => {
    const visible = (sel) => [...document.querySelectorAll(sel)].filter((el) => {
      const s = getComputedStyle(el);
      return s.display !== "none" && s.visibility !== "hidden" && el.getClientRects().length;
    });
    const mail = document.querySelector(".mobile-contact a[href^='mailto:']");
    const box = mail ? mail.getBoundingClientRect() : null;
    return {
      mode: document.documentElement.getAttribute("data-contact"),
      wa: visible("a[href*='wa.me']").length,
      mail: visible("a[href^='mailto:']").length,
      emailH: box ? Math.round(box.height) : 0,
      emailW: box ? Math.round(box.width) : 0,
    };
  });
  const fails = [];
  if (expectBoth && data.mode !== "both") fails.push("mode " + data.mode);
  if (!expectBoth && data.mode !== "email") fails.push("mode " + data.mode);
  if (expectBoth && data.wa < 1) fails.push("missing visible WhatsApp");
  if (!expectBoth && data.wa > 0) fails.push("WhatsApp leaked " + data.wa);
  if (data.mail < 1) fails.push("missing visible email");
  if (data.emailH && data.emailH < 48) fails.push("email height " + data.emailH);
  if (data.emailW && data.emailW < 120) fails.push("email width " + data.emailW);
  return { code, path, expectBoth, data, fails };
}

const cases = [
  ["US", "/contact/", true],
  ["CA", "/services/", true],
  ["GB", "/instagram-username-claim/", true],
  ["FR", "/contact/", true],
  ["NL", "/contact/", true],
  ["AE", "/contact/", true],
  ["IT", "/instagram-account-recovery-italy/", true],
  ["BR", "/contact/", false],
  ["MX", "/services/", false],
  ["SA", "/instagram-account-recovery-saudi-arabia/", false],
  ["AF", "/contact/", false],
  ["IR", "/username/", false],
  ["IQ", "/pricing/", false],
  ["ID", "/ad-account-recovery/", false],
  ["DE", "/contact/", false],
  ["", "/contact/", false],
  ["", "/best-username-claim-service-usa/", true],
  ["", "/instagram-account-recovery-saudi-arabia/", false],
];
const fails = [];
await page.setViewport({ width: 390, height: 844 });
for (const [code, path, both] of cases) {
  const row = await check(code, path, both);
  console.log(JSON.stringify(row));
  if (row.fails.length) fails.push(code + " " + path + " " + row.fails.join("; "));
}
await page.setViewport({ width: 390, height: 844 });
country = "BR";
await page.goto(base + "/contact/", { waitUntil: "domcontentloaded" });
await page.evaluate(() => sessionStorage.clear());
await page.reload({ waitUntil: "domcontentloaded" });
await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
await page.waitForSelector(".mobile-contact.is-visible", { timeout: 5000 });
await new Promise((r) => setTimeout(r, 600));
await page.screenshot({ path: "/opt/cursor/artifacts/after/email-bar-br.png" });
await page.click(".mobile-contact a[href^='mailto:']");
await page.waitForSelector(".mp-dialog", { timeout: 5000 });
const topics = await page.$$eval(".mp-dialog .cm-pill", (els) => els.map((el) => el.textContent.trim()));
if (!topics.some((t) => /username/i.test(t))) fails.push("email picker topics " + topics.join(","));
console.log("picker", topics.join(" | "));
await browser.close();
if (fails.length) {
  console.log("FAILURES");
  fails.forEach((f) => console.log(" *", f));
  process.exit(1);
}
console.log("OK");
