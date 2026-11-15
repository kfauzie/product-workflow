"""FICTIONAL: generates the synthetic data for the Corvane example. No real company, customer or asset.

Writes, from a fixed seed so every number in the example can be reproduced:
  data/sites.json            the 14 sites x 4 scenarios x 12 years, in the shape the prototype reads
  data/sites.csv             the same as a wide export (<hazard>_<scenario>_<year>_<metric>), for tools/lens.py
  data/synthetic_inputs.json deal inputs, EBITDA by site, past deals, premium assumptions, an example policy, defences
Run from examples/corvane/run:  python3 notebooks/make_data.py
"""
import json, random
random.seed(7)
H = ['River Flood','Surface Flood','Coastal Flood','Subsidence','Landslide','Wildfires','Storms','Tropical Cyclones','Hail','Extreme Heat Days','Drought']
DAMAGE = H[:9]
SCEN = ['ssp126','ssp245','ssp370','ssp585']
YEARS = [2020,2025,2030,2035,2040,2045,2050,2060,2070,2080,2090,2100]
GROWTH = {'ssp126':0.002,'ssp245':0.004,'ssp370':0.006,'ssp585':0.009}   # yearly rise in expected loss after 2020
UNITS = {'River Flood':'maximum depth (m)','Surface Flood':'maximum depth (m)','Coastal Flood':'maximum depth (m)','Subsidence':'indicator [0,2]',
         'Storms':'3s gust wind speed (km/h)','Hail':'diameter (mm)'}
# id, street, city, country, type, use, floors, rebuild cost, base expected loss a year by hazard (2020)
SITES = [
 ('S01','Quay Street','Port Avelin','Norland','OFFICE','commercial',28, 900e6, {'Coastal Flood':6.4e6,'Hail':0.30e6,'Surface Flood':0.12e6}),
 ('S02','Mill Lane','Kessford','Norland','PARKING','commercial',4, 38e6, {'River Flood':1.05e6,'Surface Flood':0.02e6,'Subsidence':0.03e6}),
 ('S03','Station Road','Brenholt','Vestmark','HIGH_ST','commercial',12, 210e6, {'Subsidence':0.85e6,'Storms':0.03e6,'Hail':0.02e6}),
 ('S04','Canal Walk','Orsay Vale','Vestmark','SINGLE_RES','residential',3, 2.1e6, {'River Flood':0.21e6,'Subsidence':0.01e6}),
 ('S05','Harbour Row','Tamberly','Norland','OFFICE','commercial',6, 16e6, {'Surface Flood':0.05e6,'Storms':0.01e6}),
 ('S06','King Street','Fennick','Ostria','OFFICE','commercial',9, 44e6, {'Hail':0.07e6,'Storms':0.02e6}),
 ('S07','Park Avenue','Corrow','Ostria','MANUFACTURING','industrial',4, 19e6, {'Subsidence':0.09e6,'Hail':0.02e6}),
 ('S08','Bridge End','Halvik','Vestmark','TRANSPORT','infrastructure',5, 3.4e6, {'Surface Flood':0.02e6}),
 ('S09','Market Square','Marisport','Ostria','HIGH_ST','commercial',2, 4.0e6, {'Hail':0.015e6}),
 ('S10','Elm Road','Eldwin','Norland','OFFICE','commercial',18, 72e6, {'Storms':0.02e6,'Surface Flood':0.01e6}),
 ('S11','Union Place','Sunmere','Calvia','MIXED_USE','mixed_use',22, 30e6, {'Hail':0.004e6}),
 ('S12','Hill Crescent','Rothwick','Calvia','OFFICE','commercial',14, 95e6, {'Storms':0.006e6}),
 ('S13','Dock Road','Port Avelin','Norland','TRANSPORT','infrastructure',3, 2.6e6, {'Surface Flood':0.014e6}),
 ('S14','West Gate','Calloway Ridge','Calvia','OFFICE','commercial',30, 120e6, {}),
]
SEV = {'Coastal Flood':1.6,'River Flood':1.9,'Surface Flood':0.3,'Subsidence':1.2,'Storms':140.0,'Hail':32.0}
def grade_pct(p):  # overall grade from damage as a share of rebuild cost (as the product does)
    for g,t in (('A',.01),('B',.05),('C',.08),('D',.11),('E',.15),('F',.20)):
        if p < t: return g
    return 'G'
def grade_h(loss, cost):
    p = loss/cost if cost else 0
    return 'A' if p < .0005 else 'B' if p < .002 else 'C' if p < .004 else 'D' if p < .006 else 'E' if p < .008 else 'F'
sites, rows = [], []
for sid, street, city, country, typ, use, floors, cost, base in SITES:
    lat, lon = round(random.uniform(40, 60), 5), round(random.uniform(-8, 25), 5)
    s = {'id':sid,'street':street,'city':city,'postcode':None,'region':None,'country':country,'lat':lat,'lon':lon,'use':use,'type':typ,
         'age':'post-1985','floors':floors,'replacement_cost':int(cost),'area_m2':None,'risk':{}}
    row = {'site_id':sid,'city':city,'country':country,'asset_type':typ,'property_value_gbp':int(cost)}
    for sc in SCEN:
        s['risk'][sc] = {}
        for y in YEARS:
            f = (1 + GROWTH[sc]) ** (y - 2020)
            hz, tot = {}, 0
            for h in H:
                loss = round(base.get(h, 0) * f) if h in DAMAGE else None
                if loss: tot += loss
                hz[h] = {'grade': grade_h(loss or 0, cost) if h in DAMAGE else 'A', 'loss': loss, 'sev': SEV.get(h) if loss else (0 if h in DAMAGE else None)}
            s['risk'][sc][str(y)] = {'grade': grade_pct(tot/cost), 'loss': int(tot), 'loss_pct': tot/cost, 'hazards': hz}
            if y in (2030, 2050):
                for h in DAMAGE:
                    k = h.lower().replace(' ', '_'); l = hz[h]['loss'] or 0
                    row[f'{k}_{sc}_{y}_loss_gbp'] = l; row[f'{k}_{sc}_{y}_damage_pct'] = l / cost * 100; row[f'{k}_{sc}_{y}_rating'] = hz[h]['grade']
    sites.append(s); rows.append(row)
meta = {'scenarios':SCEN,'years':YEARS,'hazards':H,'severity_units':UNITS,'currency':'GBP','flood_defences':'Undefended','source':'Riskline export (FICTIONAL)'}
json.dump({'meta':meta,'sites':sites}, open('data/sites.json','w'), separators=(',',':'))
import csv
with open('data/sites.csv','w',newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
total_ebitda = 45_000_000                     # assumed: EV £360m at 8x EBITDA
w8 = {s['id']: s['replacement_cost'] ** 0.5 for s in sites if s['id'] != 'S01'}
ebitda = {'S01': 9_000_000}
for k, v in w8.items(): ebitda[k] = round((total_ebitda - 9_000_000) * v / sum(w8.values()), -4)
ebitda['S02'] += total_ebitda - sum(ebitda.values())
inputs = {
 'label': 'FICTIONAL and SYNTHETIC: Corvane example, not real data',
 'deal': {'name':'Project Lantern','company':'Lantern Group','ev':360_000_000,'hold_years':6,'hold_start':2026,'ic_date':'10 Dec 2026'},
 'ebitda_by_site': ebitda,
 'past_deals_aal_pct_ebitda': [0.3,0.8,1.1,1.6,2.2,2.7,3.1,3.9,5.2,6.8,10.4],
 'premium': {'loading_low':1.5,'loading_high':2.0,'after_claim_low':1.25,'after_claim_high':2.0,'yearly_rise':0.05,'after_claim':0.5,'claim_year':2028},
 'example_policy': {'file':'quay_street_flood_policy.pdf','site':'S01','hazard':'Coastal Flood','covers_flood':True,'limit_per_event':40_000_000,
                    'excess_per_event':1_000_000,'valid_until':'31 Mar 2028','last_covered_year':2027,'pages':{'covers':3,'limit':5,'excess':5,'valid':1}},
 'other_deals': [{'name':'Project Beacon','status':'IC in 6 weeks','dot':'green'},{'name':'Project Ember','status':'not started','dot':'grey'}],
 'defences': {'S01': {'status':'Suggested from public sources · to verify','items':[
    {'what':'Port Avelin tidal barrier','who':"The city's harbour authority",'standard':'Design standard: to verify with the authority'},
    {'what':'Quay Street sea wall','who':'Regional government coastal programme','standard':'Protection level at this site: to verify'}]}},
}
json.dump(inputs, open('data/synthetic_inputs.json','w'), indent=1)
print('sites', len(sites), '| EBITDA', sum(ebitda.values()))
