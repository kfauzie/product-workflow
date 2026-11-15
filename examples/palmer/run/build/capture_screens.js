// FICTIONAL example (Palmer). Saves the page, and the page with one row open, to ../design/. Run: node capture_screens.js [scale]
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..'), scale = +(process.argv[2] || 2);
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); r.end(b); }); });
(async () => {
  await new Promise(ok => srv.listen(0, ok)); const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: scale });
  await p.goto(`http://localhost:${srv.address().port}/build/mvp.html`); await p.waitForSelector('body[data-ready="1"]');
  await p.screenshot({ path: path.join(root, 'design', '1-overview.png'), fullPage: true });
  await p.click('tr.row:has-text("Payroll run failed")');
  await p.screenshot({ path: path.join(root, 'design', '2-row-open.png'), fullPage: true });
  console.log('saved 2 screens'); await b.close(); srv.close();
})();
