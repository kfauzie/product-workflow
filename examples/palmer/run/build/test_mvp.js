// FICTIONAL example (Palmer). Checks the numbers and the decision rules. Run: node test_mvp.js
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'mvp.html'), 'utf8');
const m = { exports: {} }; new Function('module', html.split('<script id="calc">')[1].split('</script>')[0])(m); const C = m.exports;
const D = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/ticket_types.json'))); const n = D.test_tickets_per_type;
let fail = 0; const t = (name, ok, got) => { if (!ok) fail++; console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${got !== undefined ? ': ' + got : ''}`); };
const s = C.summary(D);
t('15 ticket types', D.types.length === 15, D.types.length);
t('tickets sum to about 3,000', s.all > 2900 && s.all < 3100, s.all);
t('resolved alone: 49.7%', Math.abs(s.aloneShare * 100 - 49.73) < 0.05, (s.aloneShare * 100).toFixed(2));
t('hours saved: 198', Math.round(s.hours) === 198, s.hours.toFixed(1));
t('wrong answers reaching customers under 10', s.wrong < 10, s.wrong.toFixed(2));
// every row follows the rules as written
for (const x of D.types) {
  const a = x.correct / n, r = C.recommend(x, n);
  if (r === 'resolve') t(`${x.name}: resolve alone has 98%+ and Low/Medium cost`, a >= 0.98 && x.cost !== 'High');
  if (r === 'draft') t(`${x.name}: draft has 90%+ (98%+ if it moves money)`, a >= 0.90 && (!x.moves_money || a >= 0.98));
  if (r === 'human') t(`${x.name}: human only is under 90%, or moves money under 98%`, a < 0.90 || (x.moves_money && a < 0.98));
  t(`${x.name}: 3 examples`, x.examples.length === 3);
  if (x.correct === n) t(`${x.name}: 50/50 so every example is correct`, x.examples.every(e => e.correct));
  t(`${x.name}: wrong examples explain why`, x.examples.every(e => e.correct || e.note.length > 10));
}
t('no type that moves money resolves alone', D.types.every(x => !(x.moves_money && C.recommend(x, n) === 'resolve')));
console.log(fail ? `${fail} FAILED` : 'All tests pass'); process.exit(fail ? 1 : 0);
