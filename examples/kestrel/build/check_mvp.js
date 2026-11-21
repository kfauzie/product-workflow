// FICTIONAL example (Kestrel and Gusta). Headless check (~5s): page loads, rows expand, overrides work, no errors. Run: node check_mvp.js
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); r.end(b); }); });
(async () => {
  await new Promise(ok => srv.listen(0, ok)); const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  const t = (label, ok) => { console.log((ok ? 'PASS ' : 'FAIL ') + label); if (!ok) errs.push(label); };
  const txt = s => p.textContent(s);
  await p.goto(`http://localhost:${srv.address().port}/build/mvp.html?static=1`); await p.waitForSelector('body[data-ready="1"]');
  t('no top bar', !(await p.$('#topbar')));
  t('the design font is loaded as a web font, not borrowed from the machine', await p.evaluate(async () => { await document.fonts.ready; return [...document.fonts].some(f => f.family.replace(/"/g, '') === 'Inter' && f.status === 'loaded'); }));
  const it = await txt('#intro'), hd = await txt('#header'); t('Kestrel and This page at the top, outside the box', it.includes('An AI agent that answers customer support tickets') && it.indexOf('An AI agent') < it.indexOf("Kestrel's analytics and configuration") && !hd.includes("Kestrel's analytics") && hd.includes('Customer'));
  t('accuracy footnote below the table explains the overrides', (await txt('#measure')).startsWith('* Where Kestrel is in use, accuracy is live') && (await txt('#thAcc')) === 'Accuracy*' && (await txt('#measure')).includes('makes a material change') && (await p.evaluate(() => !!(document.querySelector('#types').compareDocumentPosition(document.querySelector('#measure')) & Node.DOCUMENT_POSITION_FOLLOWING))) && (await txt('#measure')).includes('asks for a human') && (await txt('#measure')).includes('Ticket types with no AI in production are measured on a daily test run of 50 recent tickets') && (await p.title()) === 'Kestrel Dashboard');
  t('the user is named: Hannah Okafor, Head of Customer Support', (await txt('#header')).includes("Hannah Okafor, Gusta's Head of Customer Support"));
  t('impact lines say "tax authority", not HMRC', await p.$$eval('#types tr.row td:nth-child(4) .sub', es => es.length === 16 && es.every(e => !e.textContent.includes('HMRC')) && es.some(e => e.textContent.includes('the tax authority'))));
  t('impact labels say how hard a mistake is to undo; no legend, each row explains itself', (await p.$$eval('select[data-risk="0"] option', os => os.map(o => o.textContent).join('|'))) === 'Easy to fix|Fixable|Hard to undo' && !(await p.$('.impact-key')) && (await txt('tr.row[data-i="0"] .reason')).includes('a wrong answer is easy to fix') && (await txt('#summary')).includes('wrong answers reaching customers that are hard to undo'));
  t('headline', (await txt('#headline')) === 'Monthly projection per current settings');
  t('default: 1 setting override (Update company address moved down to AI-assisted human), tagged, no warning', (await txt('#state')) === '1 setting override' && (await p.inputValue('select[data-i="3"]')) === 'draft' && (await txt('tr.row[data-i="3"]')).includes('Setting overridden') && !(await txt('#types')).includes('Riskier than recommended'));
  t('default projection: 44.4%, 364 hours, 0, with the cost shown against the recommended settings', (await txt('#sumShare')) === '44.4%' && (await txt('#sumHours')) === '364' && (await txt('#sumHigh')) === '0' && (await txt('#summary')).includes('−3.1 points from recommended settings') && (await txt('#summary')).includes('−8 hours from recommended settings'));
  t('static mode: no accuracy change on load', (await p.$$('td.acc-up, td.acc-down')).length === 0);
  t('a blinking live dot on each type measured on live tickets (15), 1-second blink', (await p.$$('td.acc .live-dot')).length === 15 && (await p.evaluate(() => { document.body.classList.remove('static'); const cs = getComputedStyle(document.querySelector('.live-dot')); const ok = cs.animationName === 'blink' && cs.animationDuration === '1s'; document.body.classList.add('static'); return ok; })));
  t('the one test-run type is labelled "based on today\'s test run"', (await p.$$eval('td.acc .sub', es => es.filter(e => e.textContent === "based on today's test run").length)) === 1);
  const chips = () => p.$$eval('tr.row td:nth-child(5) .chip', es => es.map(e => e.textContent).join('|')), chips0 = await chips();
  t('one tick: exactly one accuracy cell changes, with its arrow', (await p.evaluate(() => tick())) && (await p.$$('td.acc-up, td.acc-down')).length === 1 && /[▲▼] [+−]\d/.test(await txt('td.acc-up, td.acc-down')));
  const picks = await p.evaluate(() => { const c = {}; for (let k = 0; k < 400; k++) { const before = liveCorrect.slice(); if (tick()) { const i = liveCorrect.findIndex((v, j) => v !== before[j]); c[i] = (c[i] || 0) + 1; } } return c; });
  t('ticks favour rows higher in the table, and only live types move', (picks[0] || 0) > (picks[11] || 0) && (picks[0] || 0) > (picks[13] || 0) && !picks[15]);
  t('ticks stay within 2 tickets of the 30-day figure and never change a recommendation', (await chips()) === chips0 && (await p.evaluate(() => liveCorrect.every((c, i) => Math.abs(c - D.types[i].correct) <= 2 && c <= D.types[i].tested))));
  t('after ticks, each recommendation reason quotes the same accuracy as its cell', await p.$$eval('tr.row', rs => rs.every(r => { const c = r.querySelector('td.acc').cloneNode(true); c.querySelectorAll('.accd, .sub').forEach(x => x.remove());
    const rs2 = r.querySelector('.reason'); return !rs2 || rs2.textContent.includes(c.textContent.trim()); })));
  await p.evaluate(() => { liveCorrect = D.types.map(t => t.correct); render(); });
  t('no load flash on the hours card', !(await p.getAttribute('#sumHours >> xpath=..', 'class')).includes('flash'));
  t('label says solely by AI', (await txt('#summary')).includes('of tickets handled solely by AI'));
  await p.click('#applyAll');
  t('no badge with recommended settings', !(await p.$('#state')));
  t('recommended settings: 47.5%, 372 hours, 0 high-risk wrong answers', (await txt('#sumShare')) === '47.5%' && (await txt('#sumHours')) === '372' && (await txt('#sumHigh')) === '0');
  t('rules before the table', await p.evaluate(() => !!(document.querySelector('#rules').compareDocumentPosition(document.querySelector('#types')) & Node.DOCUMENT_POSITION_FOLLOWING)));
  await p.waitForTimeout(2400);
  t('16 rows, Password reset expanded by default', (await p.$$('tr.row')).length === 16 && (await p.$$('tr.detail')).length === 1 && (await txt('tr.row.open')).includes('Password reset'));
  const det = await txt('tr.detail');
  t('each expanded row has a Recent tickets heading', det.includes('Recent tickets'));
  t('recent tickets are lines, one per ticket, in four columns: request, reply, rule, evaluation', (await p.$$('tr.detail .exrow:not(.exhdr)')).length === 5 && await p.$eval('tr.detail .exrow[data-ex]', r => [...r.children].map(c => c.className).join('|') === 'exc|exc|exc exrule|exc vline' && !!r.querySelector('.exrule .rule-link') && !!r.querySelector('.vline .pill')));
  t("the grading AI's Wrong tickets come first, with a count in the heading", (await p.$$eval('tr.detail .exrow[data-ex]', es => es.map(e => e.dataset.ex).join(','))) === '0-2,0-4,0-0,0-1,0-3' && (await txt('tr.detail .excount')) === '2 of 5 wrong');
  t('colour sits only on the verdict pill: rows are white, Override verdict is a neutral button', await p.$$eval('tr.detail .exrow[data-ex]', es => es.every(e => getComputedStyle(e).backgroundColor === 'rgba(0, 0, 0, 0)' && e.querySelector('.vtools button').className === 'btn-sm secondary')));
  { const sz = await p.$eval('tr.row[data-i="0"]', r => ['td[data-label="Recommendation"] .ctl', 'select[data-risk]', 'select[data-i]'].map(q => { const b = r.querySelector(q).getBoundingClientRect(); return Math.round(b.width) + 'x' + Math.round(b.height); }));
    t('recommendation, impact and setting controls are the same size', sz[0] === sz[1] && sz[1] === sz[2]); }
  { const ex = '.exrow[data-ex="0-0"]', acc = () => txt('tr.row[data-i="0"] td.acc');
    await p.click(`${ex} .vtools button`);
    t('override pop-up shows what the grading AI said and the change', await p.isVisible('#ovr') && (await txt('#ovr')).includes('The grading AI marked this Correct. Change it to Wrong? It will count in'));
    await p.fill('#ovrReason', 'Missed the 30-minute limit.'); await p.click('#ovrSave');
    t('override flips the verdict, shows the reason, and counts in accuracy', !(await p.$('#ovr')) && (await p.getAttribute(ex, 'class')).includes('ex-no') && (await txt(ex)).includes('Verdict overridden') && (await txt(ex)).includes('Your reason: Missed the 30-minute limit.') && (await txt(ex)).includes('The grading AI marked it Correct') && (await acc()).includes('99.6%'));
    t('the confirmation shows under that ticket\'s verdict', await p.$eval('#toast', el => !!el.closest('.vline')));
    t('Edit and Undo override are small buttons', await p.$eval(`${ex} .vtools`, v => [...v.querySelectorAll('button')].map(b => b.className).join('|')) === 'btn-sm secondary|btn-sm secondary');
    await p.click(`${ex} .vtools button:has-text("Edit")`);
    t('edit opens the pop-up with the reason filled in', (await txt('#ovrTitle')) === 'Edit your override' && (await p.inputValue('#ovrReason')) === 'Missed the 30-minute limit.');
    await p.fill('#ovrReason', 'Left out the 30-minute limit.'); await p.click('#ovrSave');
    t('edited reason replaces the old one; accuracy unchanged', (await txt(ex)).includes('Your reason: Left out the 30-minute limit.') && (await acc()).includes('99.6%'));
    await p.click(`${ex} .vtools button:has-text("Edit")`); await p.fill('#ovrReason', ''); await p.click('#ovrSave');
    t('the reason is removed from Edit (no separate link); the override stays', (await txt(ex)).includes('No reason given.') && (await txt(ex)).includes('Verdict overridden') && !(await txt(ex)).includes('Remove reason'));
    await p.click(`${ex} .vtools button:has-text("Undo override")`);
    t('undo goes back to the grading AI verdict and accuracy', (await p.getAttribute(ex, 'class')).includes('ex-ok') && !(await txt(ex)).includes('Verdict overridden') && (await acc()).includes('99.8%'));
    await p.click('.exrow[data-ex="0-2"] .vtools button'); await p.keyboard.press('Escape');
    t('Escape closes the pop-up without changing anything', !(await p.$('#ovr')) && (await p.getAttribute('.exrow[data-ex="0-2"]', 'class')).includes('ex-no'));
    await p.click('.exrow[data-ex="0-2"] .vtools button'); await p.click('#ovrSave');
    t('Wrong to Correct also works, without a reason', (await p.getAttribute('.exrow[data-ex="0-2"]', 'class')).includes('ex-ok') && (await acc()).includes('100.0%'));
    await p.click('.exrow[data-ex="0-2"] .vtools button:has-text("Undo override")'); }
  t('examples use the four labels', ['Customer request', "Kestrel's reply", 'Customer support rule', 'Evaluation (grading AI)'].every(l => det.includes(l)));
  await p.click('tr.row:has-text("Refund request") .name');
  t('clicking a row expands it, with a Wrong example', (await p.$$('tr.detail')).length === 2 && (await txt('#types')).includes('February was still due'));
  { const open = () => p.$$eval('tr.detail', d => d.length), edge = async q => { const l = p.locator(q); await l.scrollIntoViewIfNeeded(); const b = await l.boundingBox(); await l.click({ position: { x: b.width - 4, y: b.height / 2 } }); };
    const before = await open();
    await edge('tr.row[data-i="1"] td[data-label="Impact if wrong"]'); const a1 = await open();
    await edge('tr.row[data-i="1"] td[data-label="Setting"]'); const a2 = await open();
    t('clicking the empty space beside the Impact or Setting dropdown opens and closes the row, like the rest of it', a1 === before + 1 && a2 === before);
    await p.click('tr.row[data-i="1"] select[data-risk]'); await p.keyboard.press('Escape');
    t('clicking a dropdown itself does not open the row', (await open()) === before); }
  t('each rule ID links to that rule in the playbook, in a new tab', await p.$eval('a.rule-link[href="playbook.html#BILL-2"]', a => a.target === '_blank' && a.textContent === 'BILL-2').catch(() => false));
  t('footnote links to the playbook', (await p.getAttribute('#measure a', 'href')) === 'playbook.html');
  { const q = await b.newPage(); q.on('pageerror', e => errs.push('playbook: ' + e.message));
    await q.goto(`http://localhost:${srv.address().port}/build/playbook.html#BILL-2`); await q.waitForSelector('body[data-ready="1"]');
    const pb = JSON.parse(fs.readFileSync(path.join(root, 'data/support_playbook.json'))), all = pb.sections.flatMap(x => x.rules);
    t('playbook page lists every rule, and opens on the linked rule, highlighted', (await q.$$('.rule')).length === all.length && (await q.textContent('.rule.hit')).includes(all.find(r => r.id === 'BILL-2').rule) && (await q.$eval('.rule.hit', e => e.getBoundingClientRect().top)) < 100);
    const pbody = await q.textContent('body'); t('playbook: no em dashes, never "agent" on its own', !pbody.includes('—') && !/(?<!AI |support |human )\bagents?\b/i.test(pbody));
    await q.close(); }
  await p.selectOption('select[data-i="6"]', 'resolve');
  t('confirmation shows after a setting change', await p.isVisible('#toast.show') && (await txt('#toast')).includes('Saved. Projection updated.'));
  const tb = await p.$eval('#toast', e => e.getBoundingClientRect()), sb = await p.$eval('select[data-i="6"]', e => e.getBoundingClientRect());
  t('confirmation sits right under the changed control, inside its cell', Math.abs(tb.top - sb.bottom) < 12 && Math.abs(tb.left - sb.left) < 4);
  const row = await txt('tr.row[data-i="6"]');
  t('raising AI share flashes green, high-risk wrong answers flash red', (await p.getAttribute('#sumShare >> xpath=..', 'class')).includes('flash-good') && (await p.getAttribute('#sumHigh >> xpath=..', 'class')).includes('flash-bad'));
  t('override shows Overridden and the warning', row.includes('Setting overridden') && row.includes('Riskier than recommended: about 10 wrong answers a month would reach customers unchecked'));
  t('summary updates: 51.4%, 10 high-risk wrong answers', (await txt('#sumShare')) === '51.4%' && (await txt('#sumHigh')) === '10');
  t('dashboard updates: 1 setting override, 10 on High-risk types, deltas shown', (await txt('#state')) === '1 setting override' && (await txt('#sumHigh')) === '10' && (await txt('#summary')).includes('+10 from recommended settings'));
  await p.selectOption('select[data-i="0"]', 'human');
  const row0 = await txt('tr.row[data-i="0"]');
  t('lowering autonomy: Overridden, no warning', row0.includes('Setting overridden') && !row0.includes('Riskier than recommended'));
  await p.click('#applyAll');
  // risk: Password reset Low -> High moves it to AI-assisted human; the setting follows because it was on the recommendation
  await p.selectOption('select[data-risk="0"]', 'High');
  let r0 = await txt('tr.row[data-i="0"]');
  t('confirmation after a risk change names the new recommendation', (await txt('#toast')).includes('Saved. Now recommended: AI-assisted human.'));
  t('impact adjusted: "Impact adjusted" under the impact, recommendation and setting follow', (await txt('tr.row[data-i="0"] td:nth-child(4)')).includes('Impact adjusted') && r0.includes('AI-assisted human') && (await p.inputValue('select[data-i="0"]')) === 'draft' && !r0.includes('Overridden'));
  // an overridden setting does not follow a risk change
  await p.selectOption('select[data-i="1"]', 'human'); await p.selectOption('select[data-risk="1"]', 'High');
  t('overridden setting stays when risk changes', (await p.inputValue('select[data-i="1"]')) === 'human');
  await p.selectOption('select[data-risk="0"]', 'Low'); await p.selectOption('select[data-risk="1"]', 'Low'); await p.click('#applyAll');
  t('back to the original: 47.5%', (await txt('#sumShare')) === '47.5%' && !(await txt('#types')).includes('Impact adjusted'));
  t('confirmation after Apply all', (await txt('#toast')).includes('All recommendations applied'));
  t('Apply all recommendations resets everything', (await txt('#sumShare')) === '47.5%' && !(await txt('#types')).includes('Setting overridden'));
  t('rules are one table with 3 coloured rows', (await p.$$('#rules tr.r-resolve, #rules tr.r-draft, #rules tr.r-human')).length === 3 && (await p.$$('#rules .chip')).length === 3);
  t('setting dropdown is coloured by its value', (await p.getAttribute('select[data-i="0"]', 'class')).split(' ').includes('s-resolve') && (await p.getAttribute('select[data-i="6"]', 'class')).split(' ').includes('s-draft') && (await p.getAttribute('select[data-i="15"]', 'class')).split(' ').includes('s-human'));
  const body = await txt('body');
  t('no em dashes on the page', !body.includes('—'));
  t('never "agent" on its own', !/(?<!AI |support |human )\bagents?\b/i.test(body.replace(/the agent itself/g, '')));
  t('one channel: no labels from other channels', !/Help-centre form|· Email/.test(body));
  // phone: everything fits the screen width; the tables become labelled cards
  { const { devices } = require('playwright'); const mc = await b.newContext({ ...devices['iPhone 13'] }), m = await mc.newPage();
    m.on('pageerror', e => errs.push('phone: ' + e.message));
    await m.goto(`http://localhost:${srv.address().port}/build/mvp.html?static=1`); await m.waitForSelector('body[data-ready="1"]');
    t('phone: no sideways scrolling', (await m.evaluate(() => document.documentElement.scrollWidth)) <= m.viewportSize().width);
    t('phone: table header hidden, each ticket type is a card with labelled fields', !(await m.isVisible('#types tr.hdr')) && (await m.$eval('#types tr.row', r => getComputedStyle(r).display)) === 'grid' && (await m.$eval('#types tr.row td[data-label="Setting"]', td => getComputedStyle(td, '::before').content)) === '"Setting"');
    t('phone: rules stack, with "Recommended when" labelled', !(await m.isVisible('.rules tr.hdr')) && (await m.$eval('.rules td[data-label]', td => getComputedStyle(td, '::before').content)) === '"Recommended when"');
    await m.selectOption('select[data-i="6"]', 'resolve');
    t('phone: settings still work', (await m.textContent('#sumHigh')) === '10');
    await mc.close(); }
  { const tp = await b.newPage({ viewport: { width: 768, height: 1024 } }); await tp.goto(`http://localhost:${srv.address().port}/build/mvp.html?static=1`); await tp.waitForSelector('body[data-ready="1"]');
    t('tablet (768px): no sideways scrolling, cards layout', (await tp.evaluate(() => document.documentElement.scrollWidth)) <= 768 && !(await tp.isVisible('#types tr.hdr'))); await tp.close(); }
  t('desktop keeps the full table with its header row', await p.isVisible('#types tr.hdr') && (await p.$eval('#types tr.row', r => getComputedStyle(r).display)) === 'table-row');
  // embedded on the landing page: on a first, uncached visit with slow data, the frame must fit its content (regression: it once stayed at its starting height)
  { const site = path.resolve(root, '../..'), landing = path.join(site, 'index.html');
    if (fs.existsSync(landing)) {
      const slow = http.createServer((q, r) => { const f = path.join(site, decodeURIComponent(q.url.split('?')[0]));
        const send = () => fs.readFile(f, (e, body) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : f.endsWith('.svg') ? 'image/svg+xml' : 'text/html' }); r.end(body); });
        f.endsWith('.json') ? setTimeout(send, 1500) : send(); });
      await new Promise(ok => slow.listen(0, ok));
      const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }), lp = await ctx.newPage();
      lp.on('pageerror', e => errs.push('landing: ' + e.message));
      await lp.goto(`http://localhost:${slow.address().port}/index.html`);
      const fits = async () => { await lp.waitForTimeout(600); return lp.evaluate(() => { const f = document.getElementById('demo'), d = f.contentDocument;
        return !!d && !!d.body.dataset.ready && Math.abs(f.getBoundingClientRect().height - d.body.getBoundingClientRect().height) <= 2; }); };
      await lp.waitForFunction(() => { const d = document.getElementById('demo').contentDocument; return d && d.body && d.body.dataset.ready === '1'; }, null, { timeout: 15000 });
      t('landing page, fresh and slow first visit: the embedded prototype fits its content', await fits());
      await lp.frameLocator('#demo').locator('tr.row[data-i="6"] .name').click();
      t('landing page: the frame grows when a row opens', await fits());
      await ctx.close(); slow.close(); } }
  console.log(errs.length ? 'ERRORS: ' + errs.join(' | ') : 'All checks pass, no errors'); await b.close(); srv.close(); process.exit(errs.length ? 1 : 0);
})();
