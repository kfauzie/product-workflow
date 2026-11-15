"""FICTIONAL example: numbers quoted in the run documents. Run from examples/relaywise/run."""
import csv, json
t = list(csv.DictReader(open('data/tickets_monthly.csv'))); ev = {r['category']: r for r in csv.DictReader(open('data/eval_results.csv'))}
dec = {r['category']: int(r['tickets']) for r in t if r['month'] == '2026-12'}; jan = {r['category']: int(r['tickets']) for r in t if r['month'] == '2026-01'}
hm = {r['category']: float(r['avg_handle_min']) for r in t if r['month'] == '2026-12'}
tot = sum(dec.values()); top3 = sorted(dec, key=dec.get)[-3:]
print('Dec tickets', tot, '| top 3', top3, round(sum(dec[c] for c in top3)/tot*100), '%')
mins = {c: dec[c]*hm[c] for c in dec}; print('agent time share, top 3 by minutes', sorted(mins, key=mins.get)[-3:], round(sum(sorted(mins.values())[-3:])/sum(mins.values())*100), '%')
print('API errors Jan->Dec', jan['API errors'], '->', dec['API errors'], round((dec['API errors']/jan['API errors']-1)*100), '%; all others', round((sum(dec[c] for c in dec if c!='API errors')/sum(jan[c] for c in jan if c!='API errors')-1)*100), '%')
for c, r in ev.items():
    n = int(r['sample']); a = n-int(r['escalated'])
    if c in ('Billing disputes','Contract and pricing','Integrations setup'): print(c, 'sample', n, 'acc', round(int(r['correct'])/a*100,1), 'major', round(int(r['wrong_major'])/a*100,1))
print('total checked', sum(int(r['sample']) for r in ev.values()))
