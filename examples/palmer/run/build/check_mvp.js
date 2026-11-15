// FICTIONAL example (Palmer). Headless check (~5s): page loads, a row opens, no errors. Run: node check_mvp.js
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); r.end(b); }); });
(async () => {
  await new Promise(ok => srv.listen(0, ok)); const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  const t = (label, ok) => { console.log((ok ? 'PASS ' : 'FAIL ') + label); if (!ok) errs.push(label); };
  await p.goto(`http://localhost:${srv.address().port}/build/mvp.html`); await p.waitForSelector('body[data-ready="1"]');
  t('context line names Palmer', (await p.textContent('#context')).startsWith('Palmer is a fictional payroll software company'));
  t('summary: 49.7% resolved alone', (await p.textContent('#sumShare')) === '49.7%');
  t('summary: 198 hours saved', (await p.textContent('#sumHours')) === '198');
  t('summary: 9 wrong answers', (await p.textContent('#sumWrong')) === '9');
  t('15 rows', (await p.$$('tr.row')).length === 15);
  await p.click('tr.row:has-text("Refund request")');
  t('row opens with 3 examples', (await p.$$('.exbox')).length === 3);
  t('a wrong example explains why', (await p.textContent('tr.detail')).includes('✗ Wrong'));
  t('no em dashes on the page', !(await p.textContent('body')).includes('—'));
  console.log(errs.length ? 'ERRORS: ' + errs.join(' | ') : 'All checks pass, no errors'); await b.close(); srv.close(); process.exit(errs.length ? 1 : 0);
})();
