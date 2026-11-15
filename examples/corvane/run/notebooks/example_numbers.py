"""FICTIONAL example: the numbers quoted in the run documents. Run from examples/corvane/run."""
import json
d = json.load(open('data/sites.json')); S = json.load(open('data/synthetic_inputs.json'))
def yr(site, sc, y, defended=False):
    ys = sorted(int(k) for k in site['risk'][sc]); lo = max(k for k in ys if k <= y); hi = min(k for k in ys if k >= y)
    def tot(k):
        r = site['risk'][sc][str(k)]; return r['loss'] - (r['hazards']['Coastal Flood']['loss'] or 0 if defended else 0)
    return tot(lo) if lo == hi else tot(lo) + (tot(hi) - tot(lo)) * (y - lo) / (hi - lo)
hold = range(2026, 2032)
a30 = {s['id']: s['risk']['ssp245']['2030']['loss'] for s in d['sites']}; t30 = sum(a30.values())
top = max(a30, key=a30.get); ts = next(s for s in d['sites'] if s['id'] == top)
print('2030 middle: total AAL', round(t30/1e6, 2), 'top', ts['city'], ts['type'], round(a30[top]/t30*100), '%', 'coastal of top', round(ts['risk']['ssp245']['2030']['hazards']['Coastal Flood']['loss']/a30[top]*100), '%')
print('top 3 share', round(sum(sorted(a30.values())[-3:])/t30*100), '%', '| grade of top', ts['risk']['ssp245']['2030']['grade'], 'loss_pct', round(ts['risk']['ssp245']['2030']['loss_pct']*100, 2))
print('sites graded A', sum(1 for s in d['sites'] if s['risk']['ssp245']['2030']['grade'] == 'A'), 'of', len(d['sites']))
print('2025->2035 change', round((sum(s['risk']['ssp245']['2035']['loss'] for s in d['sites'])/sum(s['risk']['ssp245']['2025']['loss'] for s in d['sites'])-1)*100, 1), '%')
u = sum(yr(s, 'ssp245', y) for s in d['sites'] for y in hold); df = sum(yr(s, 'ssp245', y, True) for s in d['sites'] for y in hold)
print('hold 2026-31 undefended', round(u/1e6, 1), 'defended', round(df/1e6, 1), 'EV share', round(u/S['deal']['ev']*100), round(df/S['deal']['ev']*100))
print('rebuild total', round(sum(s['replacement_cost'] for s in d['sites'])/1e6), 'm vs EV', S['deal']['ev']/1e6)
