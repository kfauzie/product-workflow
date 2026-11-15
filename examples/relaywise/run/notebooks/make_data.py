"""FICTIONAL: synthetic data for the Relaywise example. No real company, customer or ticket.

Writes, from a fixed seed so every number can be reproduced:
  data/tickets_monthly.csv   12 months x 10 ticket categories: volume and average handle time
  data/eval_results.csv      shadow-mode evaluation of the AI agent on past tickets, per category
  data/inputs.json           everything the prototype reads (categories, costs, thresholds, an example labelled set)
Run from examples/relaywise/run:  python3 notebooks/make_data.py
"""
import csv, json, random
random.seed(11)
MONTHS = [f'2026-{m:02d}' for m in range(1, 13)]
# category, monthly volume (Dec), handle minutes, eval sample, correct, minor errors, major errors, escalated by the AI
CATS = [
 ('Password and login',      2600,  6, 400, 388,  6, 0,  6),
 ('Order status',            2300,  7, 400, 381, 10, 1,  8),
 ('Billing disputes',        1900, 18, 300, 252, 22, 14, 12),
 ('Shipment exceptions',     1500, 22, 250, 214, 18, 5, 13),
 ('API errors',              1400, 25, 200, 158, 20, 6, 16),
 ('Account changes',         1100,  9, 300, 289,  6, 1,  4),
 ('Integrations setup',       900, 30,  80,  64,  8, 3,  5),
 ('Invoices and receipts',    850,  5, 300, 294,  4, 0,  2),
 ('Contract and pricing',     500, 20,  40,  31,  4, 3,  2),
 ('Data export requests',     450, 12, 120, 112,  5, 1,  2),
]
GROWTH = {'API errors': 0.06}           # API errors grew after a mid-year release
rows = []
for c, vol, h, *_ in CATS:
    for i, m in enumerate(MONTHS):
        g = GROWTH.get(c, 0.01)
        v = round(vol / (1 + g) ** (11 - i) * random.uniform(0.96, 1.04))
        rows.append({'month': m, 'category': c, 'tickets': v, 'avg_handle_min': round(h * random.uniform(0.95, 1.05), 1)})
with open('data/tickets_monthly.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
ev = [{'category': c, 'sample': n, 'correct': k, 'wrong_minor': mi, 'wrong_major': ma, 'escalated': e} for c, _, _, n, k, mi, ma, e in CATS]
with open('data/eval_results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(ev[0])); w.writeheader(); w.writerows(ev)
last = {r['category']: r for r in rows if r['month'] == MONTHS[-1]}
inputs = {
 'label': 'FICTIONAL and SYNTHETIC: Relaywise example, not real data',
 'customer': {'name': 'Pellmore', 'team': 'Support Operations', 'agents': 24, 'month': 'Dec 2026'},
 'costs': {'agent_hour_gbp': 32, 'wrong_minor_gbp': 15, 'wrong_major_gbp': 400, 'review_saves_share': 0.35, 'review_misses_share': 0.1},
 'thresholds': {'auto_min_accuracy_low': 0.95, 'auto_max_major_rate': 0.005, 'min_sample': 100, 'review_min_accuracy_low': 0.80},
 'guardrail': {'window': 50, 'max_reversed': 3},
 'categories': [{'name': c, 'tickets_month': last[c]['tickets'], 'handle_min': last[c]['avg_handle_min'], **{k: v for k, v in e.items() if k != 'category'}} for c, e in zip([x[0] for x in CATS], ev)],
 'example_labelled_set': {'file': 'billing_disputes_labelled_400.csv', 'category': 'Billing disputes', 'sample': 400, 'correct': 386, 'wrong_minor': 9, 'wrong_major': 1, 'escalated': 4,
                          'note': 'After the refund-policy article was added to the knowledge base'},
 'other_teams': [{'name': 'Onboarding team', 'status': 'not started'}, {'name': 'Partner support', 'status': 'not started'}],
}
json.dump(inputs, open('data/inputs.json', 'w'), indent=1)
print('categories', len(CATS), '| Dec tickets', sum(c['tickets_month'] for c in inputs['categories']))
