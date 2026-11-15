// FICTIONAL example (Kestrel and Gusta). Checks the numbers, the decision rules and the brief's table. Run: node test_mvp.js
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'mvp.html'), 'utf8');
const m = { exports: {} }; new Function('module', html.split('<script id="calc">')[1].split('</script>')[0])(m); const C = m.exports;
const D = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/ticket_types.json'))); const n = D.test_tickets_per_type;
let fail = 0; const t = (name, ok, got) => { if (!ok) fail++; if (!ok || got !== undefined) console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${got !== undefined ? ': ' + got : ''}`); };
// the table from the brief: name, tickets, correct, risk, recommendation
const BRIEF = [['Password reset',468,50,'Low','resolve'],["Can't log in",268,49,'Low','resolve'],['Missing payslip',342,50,'Low','resolve'],['Update company address',97,50,'Medium','resolve'],
  ['Add a new employee',251,48,'Medium','draft'],['Change bank details',154,49,'High','draft'],['Refund request',121,46,'High','human'],['Payroll run failed',189,45,'High','human'],
  ['Tax form question',298,47,'High','human'],['Cancel subscription',88,50,'High','draft'],['Change pay date',132,47,'High','human'],['Invoice question',177,49,'Low','resolve'],
  ['Holiday pay calculation',170,43,'Medium','human'],['Export payroll report',131,50,'Low','resolve'],['Pension deduction question',96,44,'Medium','human']];
BRIEF.forEach(([name, tk, k, risk, rec], i) => { const x = D.types[i];
  t(`${name}: data matches the brief`, x.name === name && x.tickets === tk && x.correct === k && x.risk === risk);
  t(`${name}: rules give the brief's recommendation`, C.recommend(x, n) === rec);
  t(`${name}: 3 examples with message, proposal, rule and verdict`, x.examples.length === 3 && x.examples.every(e => e.message && e.proposed && e.rule && e.verdict_reason));
  if (k < n) t(`${name}: below 100% so at least one Wrong example`, x.examples.some(e => !e.correct));
  else t(`${name}: 50/50 so every example is Correct`, x.examples.every(e => e.correct)); });
const rec = D.types.map(x => C.recommend(x, n)), s = C.summary(D, rec);
t('tickets a month', s.all === 2982, s.all);
t('handled by AI: 49.7%', (s.aiShare * 100).toFixed(1) === '49.7', (s.aiShare * 100).toFixed(2));
t('hours saved: 1,483 × 8 min + 493 × 4 min = 231', Math.round(s.hours) === 231 && s.ai === 1483 && s.assisted === 493, s.hours.toFixed(1));
t('wrong answers: 268 × 2% + 177 × 2% = 8.9', Math.abs(s.wrong - 8.9) < 0.001, s.wrong.toFixed(2));
// overriding Refund request to AI: more autonomy, so a warning, and the numbers move
const o = rec.slice(); o[6] = 'resolve'; const so = C.summary(D, o);
t('override Refund request to AI is above recommended', C.aboveRecommended(D.types[6], n, 'resolve'));
t('override adds 121 AI tickets and 9.7 wrong answers', so.ai === 1604 && Math.abs(so.wrong - (8.9 + 121 * 0.08)) < 0.001, `${so.ai}, ${so.wrong.toFixed(2)}`);
t('lowering autonomy is not a warning', !C.aboveRecommended(D.types[0], n, 'human'));
const text = JSON.stringify(D) + html;
t('no em dashes', !text.includes('—'));
t('never "agent" on its own', !/(?<!AI |support )\bagents?\b/i.test(text.replace(/the agent itself/g, '')));
console.log(fail ? `${fail} FAILED` : 'All tests pass'); process.exit(fail ? 1 : 0);
