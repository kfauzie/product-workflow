// FICTIONAL example (Palmer). Headless check (~5s): page loads, example panel works, no errors. Run: node check_mvp.js
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); r.end(b); }); });
(async () => {
  await new Promise(ok => srv.listen(0, ok)); const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  const t = (label, ok) => { console.log((ok ? 'PASS ' : 'FAIL ') + label); if (!ok) errs.push(label); };
  await p.goto(`http://localhost:${srv.address().port}/build/mvp.html`); await p.waitForSelector('body[data-ready="1"]');
  t('page title line', (await p.textContent('.title')) === 'AI Support Agent · Analytics · Palmer');
  t('header names the customer and channels', (await p.textContent('#hCustomer')).includes('in-app chat, email and the help-centre form'));
  t('summary: 49.7% handled by AI', (await p.textContent('#sumShare')) === '49.7%');
  t('summary: 198 hours saved', (await p.textContent('#sumHours')) === '198');
  t('summary: 9 wrong answers, on Low-cost tickets', (await p.textContent('#sumWrong')) === '9' && (await p.textContent('#summary')).includes('Low-cost'));
  t('rules shown before the table', await p.evaluate(() => document.querySelector('.rules').compareDocumentPosition(document.querySelector('#types')) & Node.DOCUMENT_POSITION_FOLLOWING));
  t('15 rows', (await p.$$('tr.row')).length === 15);
  t('example panel open on Refund request', (await p.textContent('#exTitle')).includes('Refund request') && (await p.$$('.exbox')).length === 3);
  t('examples show channel, rule and verdict', (await p.textContent('#examples')).includes('Playbook rule') && (await p.textContent('#examples')).includes('Grading AI verdict') && (await p.textContent('#examples')).includes('Email'));
  await p.click('tr.row:has-text("Payroll run failed")');
  t('clicking a row swaps the panel', (await p.textContent('#exTitle')).includes('Payroll run failed'));
  const body = await p.textContent('body');
  t('no em dashes on the page', !body.includes('—'));
  t('never "agent" on its own', !/(?<!AI |support )\bagent\b/i.test(body.replace(/AI Support Agent/g, '')));
  console.log(errs.length ? 'ERRORS: ' + errs.join(' | ') : 'All checks pass, no errors'); await b.close(); srv.close(); process.exit(errs.length ? 1 : 0);
})();
