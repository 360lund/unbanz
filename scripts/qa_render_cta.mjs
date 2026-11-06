import fs from "fs";
import puppeteer from "/tmp/qa-render/node_modules/puppeteer-core/lib/esm/puppeteer/puppeteer-core.js";

const chrome = "/usr/local/bin/google-chrome";
const base = (process.env.BASE || "http://127.0.0.1:8765").replace(/\/$/, "");
const holds = [
  "instagram-account-recovery-saudi-arabia/",
  "instagram-disabled-saudi-arabia-what-to-do/",
  "instagram-hacked-saudi-arabia-what-to-do/",
  "instagram-suspended-appeal-saudi-arabia/",
  "instagram-username-claim-saudi-arabia/",
  "facebook-account-recovery-saudi-arabia/",
  "facebook-account-disabled-saudi-arabia-what-to-do/",
  "meta-ad-account-disabled-saudi-arabia/",
  "meta-appeal-links-saudi-arabia/",
  "agency-client-account-banned-saudi-arabia/",
  "snapchat-account-locked-saudi-arabia/",
  "snapchat-hacked-saudi-arabia-what-to-do/",
  "white-label-agency-saudi-arabia/",
  "white-label-agency-brazil/",
  "pt-br/white-label-agencias-brasil/",
  "pt-br/falar-com-o-instagram-ou-a-meta-no-brasil/",
  "pt-br/onde-denunciar-golpes-e-crimes-online-no-brasil/",
];
const keep = [
  "contact/",
  "instagram-username-claim/",
  "facebook-account-recovery-canada/",
  "instagram-account-recovery-italy/",
  "services/",
];

const browser = await puppeteer.launch({
  executablePath: chrome,
  headless: true,
  args: ["--no-sandbox", "--disable-gpu"],
});
const fails = [];
const notes = [];

async function audit(page, path, expectWa) {
  const res = await page.goto(base + "/" + path, { waitUntil: "domcontentloaded", timeout: 20000 });
  await new Promise((r) => setTimeout(r, 400));
  const data = await page.evaluate(() => {
    const links = [...document.querySelectorAll("a[href]")].map((a) => a.href);
    const bad = links.filter((h) => /wa\.me|mailto:/i.test(h));
    const imgs = [...document.querySelectorAll("img")].filter((img) => !img.hasAttribute("alt")).map((img) => img.src);
    const unnamed = [...document.querySelectorAll("button, a")].filter((el) => {
      if (el.closest("[hidden]")) return false;
      const style = getComputedStyle(el);
      if (style.display === "none" || style.visibility === "hidden") return false;
      const name = (el.getAttribute("aria-label") || el.textContent || "").trim();
      return !name && el.getClientRects().length;
    }).length;
    return {
      bad,
      h1: document.querySelectorAll("h1").length,
      mobile: !!document.querySelector(".mobile-contact"),
      dialog: !!document.querySelector(".cm-dialog"),
      imgs,
      unnamed,
      overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      title: document.title,
    };
  });
  if (expectWa) {
    if (!data.bad.some((h) => h.includes("wa.me"))) fails.push(path + " rendered without WhatsApp");
    if (!data.bad.some((h) => h.startsWith("mailto:"))) fails.push(path + " rendered without email");
  } else {
    if (data.bad.length) fails.push(path + " rendered enquiry links: " + data.bad.slice(0, 4).join(" | "));
    if (data.mobile) fails.push(path + " rendered sticky contact bar");
  }
  if (data.h1 !== 1) fails.push(path + " h1 count " + data.h1);
  if (data.imgs.length) fails.push(path + " images missing alt " + data.imgs.length);
  if (data.unnamed) notes.push(path + " unnamed controls " + data.unnamed);
  if (data.overflow > 2) fails.push(path + " horizontal overflow " + data.overflow);
  return data;
}

const page = await browser.newPage();
await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 1 });
for (const path of holds) await audit(page, path, false);
for (const path of keep) await audit(page, path, true);
await page.setViewport({ width: 1440, height: 900 });
for (const path of ["instagram-account-recovery-saudi-arabia/", "white-label-agency-brazil/", "contact/", "instagram-username-claim/"]) {
  await audit(page, path, path === "contact/" || path === "instagram-username-claim/");
}

await page.setViewport({ width: 1280, height: 900 });
await page.goto(base + "/contact/", { waitUntil: "domcontentloaded" });
await page.click("a.contact-option");
await page.waitForSelector(".cm-dialog", { timeout: 5000 });
const pills = await page.$$eval(".cm-dialog .cm-pill", (els) => els.map((el) => el.textContent.trim()));
const hear = await page.$("#ubz-hear-wa");
if (!pills.includes("Username claim") || !pills.includes("Ad account")) fails.push("contact WhatsApp picker missing service topics: " + pills.join(","));
if (!hear) fails.push("contact WhatsApp picker missing how-did-you-hear");
notes.push("contact WhatsApp topics: " + pills.join(" | "));

await page.goto(base + "/instagram-username-claim/", { waitUntil: "domcontentloaded" });
await page.click("a.hero-email");
await page.waitForSelector(".mp-dialog", { timeout: 5000 });
await page.waitForSelector("#ubz-hear-mail", { timeout: 3000 });
const mailTopics = await page.$$eval(".mp-dialog .cm-pill", (els) => els.map((el) => el.textContent.trim()));
const mailHear = await page.$("#ubz-hear-mail");
if (!mailTopics.some((t) => /username/i.test(t))) fails.push("email picker missing username topic: " + mailTopics.join(","));
if (!mailHear) fails.push("email picker missing how-did-you-hear");
notes.push("email topics: " + mailTopics.join(" | "));

await page.goto(base + "/instagram-account-recovery-saudi-arabia/", { waitUntil: "domcontentloaded" });
await new Promise((r) => setTimeout(r, 500));
const leaked = await page.evaluate(() => [...document.querySelectorAll("a")].some((a) => /wa\.me|mailto:/i.test(a.href)));
if (leaked) fails.push("Saudi page gained an enquiry link after scripts ran");

await browser.close();
const report = { fails, notes };
fs.writeFileSync("/tmp/qa-render/report.json", JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
if (fails.length) process.exit(1);
