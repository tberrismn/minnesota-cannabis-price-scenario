"""Shared loaders: harmonize, deflate, index. All paths relative to code/."""
import csv, json, math, os
HERE=os.path.dirname(os.path.abspath(__file__)); DATA=os.path.join(HERE,'..','data')
LAUNCH={'MA':'2018-11','MI':'2019-12','IL':'2020-01','CT':'2023-01','OH':'2024-08','MN':'2025-09'}
G_PER_OZ=28.349523125; G_PER_LB=453.59237
def rd(name): return list(csv.DictReader(open(os.path.join(DATA,name))))
def msl(state,period):
    y,m=map(int,period[:7].split('-')); ly,lm=map(int,LAUNCH[state].split('-')); return (y-ly)*12+m-lm
def add_months(period,k):
    y,m=map(int,period.split('-')); t=y*12+m-1+k; return f'{t//12:04d}-{t%12+1:02d}'
def cpi_table():
    c={r['month']:float(r['cpi']) for r in rd('cpi_midwest_CUUR0200SA0.csv') if r['cpi']}
    # missing months (Oct 2025: BLS did not publish) use the mean of adjacent published months
    ms=sorted(c); out=dict(c); filled=[]
    for i in range(len(ms)-1):
        a,b=ms[i],ms[i+1]; k=1
        while add_months(a,k)<b:
            out[add_months(a,k)]=(c[a]+c[b])/2; filled.append(add_months(a,k)); k+=1
    base=max(c)  # latest published month; target is 2026-09
    return out,base,filled
CPI,CPI_BASE_MONTH,CPI_FILLED=cpi_table()
def real(v,period): return v*CPI[CPI_BASE_MONTH]/CPI[period]
EXCLUDE={'MA':['2020-04']}  # COVID closure of adult-use retail (2020-03-24 to 2020-05-25); price not comparable
def primary_series():
    """Nominal USD/g, one primary retail flower series per analog state: {state:{period:value}}"""
    S={}
    S['MA']={r['period']:float(r['value']) for r in rd('prices_MA.csv') if r['period_type']=='month' and r['market']=='adult_use' and r['unit']=='usd_per_gram'}
    S['MI']={r['period']:float(r['value'])/G_PER_OZ for r in rd('prices_MI.csv') if r['period_type']=='month' and r['market']=='adult_use' and r['metric']=='weighted_avg'}
    S['IL']={r['period']:float(r['value']) for r in rd('prices_IL.csv') if r['period_type']=='month' and r['market']=='adult_use' and r['category']=='flower' and r['period']<'2025-06'}
    S['CT']={r['period']:float(r['value']) for r in rd('prices_CT.csv') if r['period_type']=='month'}
    sup={(r['period'],r['variable']):float(r['value']) for r in rd('supply_OH.csv') if r['period_type']=='month'}
    S['OH']={p:sup[(p,'flower_sales_usd_adult_use')]/sup[(p,'flower_sold_lbs_adult_use')]/G_PER_LB for (p,v) in sup if v=='flower_sold_lbs_adult_use' and p>='2024-08'}
    for st,ps in EXCLUDE.items():
        for p in ps: S[st].pop(p,None)
    return S
def index_series(nom):
    """Real (base-month dollars) series and index with mean(months 0..2)=100."""
    out={}
    for st,s in nom.items():
        r={p:real(v,p) for p,v in s.items() if p in CPI}
        base=[r[add_months(LAUNCH[st],k)] for k in range(3)]
        b=sum(base)/3
        out[st]={msl(st,p):(p,s[p],r[p],100*r[p]/b) for p in sorted(r)}
    return out
def pop21(state,year):
    P={}
    for r in rd('pop21.csv'): P.setdefault(r['state'],{})[int(r['year'])]=float(r['pop21'])
    ys=sorted(P[state]); y=min(max(year,ys[0]),ys[-1])
    if y not in P[state]:  # 2020 gap: use prior published year
        y=max(k for k in ys if k<=y)
    return P[state][y]
def flower_grams_sold():
    """Monthly legal flower grams sold (adult-use + medical) for states that publish weight."""
    out={}
    spec={'MI':[('flower_sold_lbs_adult_use',G_PER_LB),('flower_sold_lbs_medical',G_PER_LB)],
          'MA':[('flower_sold_grams_adult_use',1),('flower_sold_grams_medical',1)],
          'OH':[('flower_sold_lbs_adult_use',G_PER_LB),('flower_sold_lbs_medical',G_PER_LB)]}
    for st,vs in spec.items():
        d={}
        for r in rd(f'supply_{st}.csv'):
            if r['period_type']!='month': continue
            for v,k in vs:
                if r['variable']==v: d.setdefault(r['period'],{})[v]=float(r['value'])*k
        out[st]={p:sum(x.values()) for p,x in d.items() if len(x)==len(vs)}
    return out
def per_adult(st,g):
    return {p:v/pop21(st,int(p[:4])) for p,v in g.items()}
def trailing(d,k=3):
    ps=sorted(d); out={}
    for i,p in enumerate(ps):
        if i>=k-1 and all(add_months(ps[i-j],0)==add_months(p,-j) for j in range(k)): out[p]=sum(d[ps[i-j]] for j in range(k))/k
    return out
