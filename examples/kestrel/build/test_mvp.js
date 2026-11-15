// FICTIONAL example (Kestrel and Gusta). Checks the numbers, the decision rules and the brief's table. Run: node test_mvp.js
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'mvp.html'), 'utf8');
const m = { exports: {} }; new Function('module', html.split('<script id="calc">')[1].split('</script>')[0])(m); const C = m.exports;
const D = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/ticket_types.json'))); const n = 0;
let fail = 0; const t = (name, ok, got) => { if (!ok) fail++; if (!ok || got !== undefined) console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${got !== undefined ? ': ' + got : ''}`); };
// the table from the brief: name, tickets, correct, risk, recommendation
const BRIEF = [['Password reset',468,468,467,'Low','resolve'],["Can't log in",268,268,263,'Low','resolve'],['Missing payslip',342,342,340,'Low','resolve'],['Update company address',97,97,96,'Medium','resolve'],['Add a new employee',251,251,242,'Medium','draft'],['Change bank details',154,154,152,'High','draft'],['Refund request',121,50,46,'High','human'],['Payroll run failed',189,50,45,'High','human'],['Tax form question',298,50,47,'High','human'],['Cancel subscription',88,88,87,'High','draft'],['Change pay date',132,50,47,'High','human'],['Invoice question',177,177,174,'Low','resolve'],['Holiday pay calculation',170,50,43,'Medium','human'],['Export payroll report',131,131,129,'Low','resolve'],['Pension deduction question',96,50,44,'Medium','human']];
BRIEF.forEach(([name, tk, tested, k, risk, rec], i) => { const x = D.types[i];
  t(`${name}: data matches; tested on all 30-day tickets if Kestrel is used, else 50`, x.name === name && x.tickets === tk && x.tested === (rec === 'human' ? 50 : tk) && x.tested === tested && x.correct === k && x.risk === risk);
  t(`${name}: reason quotes the live accuracy`, x.reason.includes((k / tested * 100).toFixed(tested === 50 ? 0 : 1) + '%'));
  t(`${name}: rules give the brief's recommendation`, C.recommend(x, n) === rec);
  t(`${name}: 3 examples with message, proposal, rule and verdict`, x.examples.length === 3 && x.examples.every(e => e.message && e.proposed && e.rule && e.verdict_reason));
  if (k < tested) t(`${name}: below 100% so at least one Wrong example`, x.examples.some(e => !e.correct)); });
const rec = D.types.map(x => C.recommend(x, n)), s = C.summary(D, rec);
t('tickets a month', s.all === 2982, s.all);
t('handled by AI: 49.7%', (s.aiShare * 100).toFixed(1) === '49.7', (s.aiShare * 100).toFixed(2));
t('hours saved: 1,483 × 10 min + 493 × 5 min = 288', Math.round(s.hours) === 288 && s.ai === 1483 && s.assisted === 493, s.hours.toFixed(1));
t('wrong answers on AI-handled types: 1 + 5 + 2 + 1 + 3 + 2 = 14', Math.abs(s.wrong - 14) < 1e-9, s.wrong.toFixed(2));
// overriding Refund request to AI: more autonomy, so a warning, and the numbers move
const o = rec.slice(); o[6] = 'resolve'; const so = C.summary(D, o);
t('override Refund request to AI is above recommended', C.aboveRecommended(D.types[6], n, 'resolve'));
t('override adds 121 AI tickets', so.ai === 1604, so.ai);
t('recommended settings: 0 wrong answers on High-risk types', s.wrongHigh === 0, s.wrongHigh);
t('Refund request on AI: wrong answers on High-risk types = 121 × 8% = 9.7', Math.abs(so.wrongHigh - 121 * 4 / 50) < 1e-9, so.wrongHigh.toFixed(2));
t('lowering autonomy is not a warning', !C.aboveRecommended(D.types[0], n, 'human'));
const text = JSON.stringify(D) + html;
t('no em dashes', !text.includes('—'));
t('never "agent" on its own', !/(?<!AI |support |human )\bagents?\b/i.test(text.replace(/the agent itself/g, '')));
console.log(fail ? `${fail} FAILED` : 'All tests pass'); process.exit(fail ? 1 : 0);
