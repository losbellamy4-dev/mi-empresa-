// guia_*.html → guia_*.pdf (A4). Uso: node pdf.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const l of ['es', 'en']) {
    await p.goto('file://' + path.join(__dirname, `guia_${l}.html`), { waitUntil: 'networkidle' }).catch(() => {});
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: path.join(__dirname, `guia_${l}.pdf`), format: 'A4', printBackground: true, preferCSSPageSize: true });
    console.log(`guia_${l}.pdf`);
  }
  await b.close();
})();
