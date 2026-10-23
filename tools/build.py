"""Generates all static pages from tools/source.md (the skills file, minus excluded items) + tools/content.py.
Run: python3 tools/build.py   (output is committed; hosting needs no build step)
Future: add a 'Passion projects / Skills highlights' tab by appending to TABS and writing its panel in index()."""
import os, re, html, sys
sys.path.insert(0, os.path.dirname(__file__)); from content import CASES, NEW
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL="kiyagagrace460@gmail.com"; LI="https://www.linkedin.com/in/kiyagakiwanuka"
import hashlib
VER = hashlib.md5((open(os.path.join(R,"assets","style.css")).read()+open(os.path.join(R,"assets","app.js")).read()).encode()).hexdigest()[:8]
MODAL_CSS = open(os.path.join(R,"tools","modal.css")).read().replace("\n"," ")
SRC = open(os.path.join(R,"tools","source.md")).read()
CURATED = dict(zip([19,1,3,14,18,25,2], ["sharks-feasibility","uk-housing-econometrics","portfolio-optimisation","everton-financials","fsa-fan-research","bi-pipeline","remote-work-london"]))
CBYSLUG = {c["slug"]:c for c in CASES}
SHORT = {1:"Housing market econometrics",2:"Remote work in Greater London",3:"Portfolio investment & risk",4:"Classical vs neo-classical trade theory",5:"AI and the demand for labour",6:"Global value chains",7:"Macroeconomic performance",8:"Inflation shocks & central banks",9:"Cost-of-living crisis briefing",10:"Political economy of climate change",11:"State investment banks",12:"Infant industry protection",13:"Neoclassical economics & water",14:"Everton FC financial performance",15:"Forest Green Rovers strategy",16:"Chief People Officer perspective",17:"Johari Window leadership",18:"FSA non-league fan research",19:"Sheffield Sharks feasibility study",20:"BCG: Data for Decision Makers",21:"Deloitte: Data Analytics",22:"Tata: Data Visualisation",23:"BCG: Strategy Consulting",25:"Data analytics & BI pipeline"}
TOOLS = ["MySQL Workbench","Excel Solver","Excel","Pivot Tables","Power BI","PowerBI","Tableau","Office for National Statistics (ONS)","ONS Census 2021","Bank of England","Companies House","Sport England","matrix algebra","efficient frontier","Sharpe Ratio","PESTEL","Porter's Five Forces","VRIO","Segmentation, Targeting, and Positioning (STP)","AIDA model","Technology Acceptance Model","Phillips Curve","Task-Based Model","argument map","Johari Window","Goleman’s Emotional Intelligence framework","Emotional Intelligence (EI) models","Ricardian","Heckscher-Ohlin","smile curve","weighted multi-criteria decision analysis","contribution-margin model","ROCE","Current Ratio","Gearing","regression","econometric modeling","thematic analysis","survey"]
def parse():
    items = {}
    for m in re.finditer(r"### (\d+)\. (.+?)\n(.*?)(?=\n### |\n---|\Z)", SRC, re.S):
        n = int(m.group(1)); body = m.group(3)
        g = lambda k: (re.search(r"\*\*"+k+r"\*\*:\s*(.+)", body) or [None,""])[1].strip()
        items[n] = dict(n=n, title=m.group(2).strip(), summary=g("Summary of Project"), why=g("Why the Project is Useful and Relevant"), skills=[s.strip() for s in re.split(r",\s*(?![^()]*\))", g("Skills Gained").rstrip(".")) if s.strip()])
    return items
def sents(t): return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"])", t) if s.strip()]
ITEMS = parse()
def slug(n): return CURATED.get(n) or re.sub(r"[^a-z0-9]+","-", SHORT[n].lower()).strip("-")
def group(n): return "hertfordshire" if n<=13 else "sheffield-hallam" if n<=19 else "simulations" if n<=23 else "data"
GROUPNAME = {"hertfordshire":"University of Hertfordshire · BSc Economics","sheffield-hallam":"Sheffield Hallam University · MSc Sport Business Management","simulations":"Forage job simulation","data":"Technical data project"}
def esc(s): return html.escape(s, quote=False)
def ul(xs, tag="ul"): return f"<{tag}>"+"".join(f"<li>{x}</li>" for x in xs)+f"</{tag}>"
def tags(xs): return '<div class="tags">'+"".join(f"<span>{esc(x)}</span>" for x in xs)+"</div>"
def page(title, body, depth, extra=""):
    p = "../"*depth
    nav = "".join(f'<a href="{p}index.html#{k}">{v}</a>' for k,v in TABS)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | Kiyaga Grace Kiwanuka</title><meta name="description" content="Kiyaga Grace Kiwanuka: data, business and economic analyst portfolio.">
<link rel="stylesheet" href="{p}assets/style.css?v={VER}"></head><body>
<header class="nav"><div class="wrap"><a class="brand" href="{p}index.html">Kiyaga Grace Kiwanuka</a><nav id="tabs">{nav}</nav></div></header>
<main>{body}</main><footer><div class="wrap">© 2026 Kiyaga Grace Kiwanuka · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{LI}">LinkedIn</a></div></footer>{extra}</body></html>"""
TABS = [("about","About"),("hertfordshire","Hertfordshire"),("sheffield-hallam","Sheffield Hallam"),("data","Data projects"),("simulations","Simulations"),("experience","Experience"),("contact","Contact")]
def find_tools(text): 
    out=[]; 
    for t in TOOLS:
        if t.lower() in text.lower() and not any(t.lower() in o.lower() for o in out): out.append(t)
    return out
def _w(t): return set(re.findall(r"[a-z0-9]+", re.sub(r"<[^>]+>","",t).lower()))
def _dup(t, seen): 
    w=_w(t)
    return any(len(w & x)/max(1,min(len(w),len(x)))>0.6 for x in seen if x)
def detail(it):
    n=it["n"]; ss=sents(it["summary"]); ws=sents(it["why"]); c=CBYSLUG.get(CURATED.get(n,""))
    E = (lambda x: x) if c else esc
    secs = [("overview","Overview","p",[esc(ss[0])]),
            ("context","Context &amp; question","p",[c["prob"]] if c else []),
            ("method","Methodology &amp; process","ol",[E(x) for x in (c["appr"] if c else ss[1:])]),
            ("tools","Data &amp; tools","tags",find_tools(it["summary"]+" "+it["why"])),
            ("findings","Findings &amp; outcomes","ul",[E(x) for x in (c["find"] if c else ws[:1])]),
            ("why","Why it matters","p",[esc(x) for x in (ws if c else ws[1:])]),
            ("skills","Skills gained","tags",it["skills"])]
    seen=[]; out=[]; toc=[]
    for sid,name,kind,items in secs:
        if kind!="tags":
            items=[x for x in items if not _dup(x,seen)]; seen+= [_w(x) for x in items]
        if not items: continue
        body = tags(items) if kind=="tags" else ul(items,kind) if kind in("ul","ol") else "".join(f"<p>{x}</p>" for x in items)
        out.append(f'<h2 id="{sid}">{name}</h2>{body}'); toc.append(f'<a href="#{sid}">{name.split(" &amp;")[0]}</a>')
    hl = "".join(f"<div>{h}</div>" for h in c["hl"]) if c else ""
    g=group(n); back=f"../index.html#{g}"
    b=f"""<section class="hero small"><div class="wrap"><p class="kicker">{GROUPNAME[g]}</p><h1>{esc(it['title'])}</h1>{'<div class="stats">'+hl+'</div>' if hl else ''}</div></section>
<article class="wrap case"><nav class="toc">{''.join(toc)}</nav>
{''.join(out)}
<p class="back"><a href="{back}">← Back to {dict(TABS)[g]}</a></p></article>"""
    return page(it["title"], b, 1)
def md_parts(slug):
    t=open(f"{R}/projects/{slug}/README.md").read()
    f=lambda s: re.sub(r"`([^`]+)`", r"<code>\1</code>", re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s))
    fs=[f(l[2:]) for l in t.split("## Findings")[1].split("**Limitations")[0].splitlines() if l.startswith("- ")]
    one=lambda k: f(t.split(k)[1].split("\n")[0].split(":**",1)[1].strip())
    return fs, one("**Limitations"), one("**Data"), one("**Method")
DATA_EXTRA = {
 "uk-house-prices-interest-rates": dict(steps=["Downloaded the HM Land Registry UK HPI full file and the Bank of England monthly average Bank Rate (IUMABEDR) with <code>download_data.sh</code>.","Filtered the HPI to the United Kingdom series and merged it with Bank Rate by month (Jan 2005 – Jul 2026).","Computed year-on-year house price growth and the 12-month change in Bank Rate.","Measured cross-correlations at 0, 6, 12, 18 and 24-month lags.","Estimated an OLS regression of price growth on the 12-month-lagged rate change with Newey-West (HAC) standard errors.","Examined the 2021–23 tightening episode and annual sales volumes; produced charts with matplotlib."], tools=["Python","pandas","statsmodels","matplotlib","HM Land Registry UK HPI","Bank of England IUMABEDR"], why="Interest-rate sensitivity of asset prices matters for lenders, housebuilders, investors and policy teams; this shows why naive correlations mislead and how lag structure changes the conclusion.", skills=["Time-series analysis","Regression (OLS, HAC errors)","Data cleaning & merging","Data visualisation","Reproducible analysis"]),
 "uk-inflation-unemployment": dict(steps=["Downloaded ONS CPIH annual rate (L55O), ONS unemployment rate (MGSX) and Bank of England Bank Rate.","Parsed the ONS time-series CSV format to extract monthly observations and aligned all three series (Jan 1995 – Jul 2026, 379 months).","Split the sample into eras (1995–2007, 2008–2019, 2020–2026) and computed correlations and linear slopes of inflation on unemployment.","Computed correlations between inflation and Bank Rate 0–24 months later to gauge the policy reaction lag.","Visualised the series and an era-coloured Phillips curve scatter."], tools=["Python","pandas","numpy","matplotlib","ONS (L55O, MGSX)","Bank of England IUMABEDR"], why="Reading the inflation–labour market relationship correctly is central to macro, rates and economic-research roles; the analysis shows the trade-off is unstable across eras.", skills=["Macroeconomic analysis","Time-series data handling","Correlation analysis","Data visualisation"]),
 "uk-regional-housing-sql": dict(steps=["Downloaded the HM Land Registry UK HPI full file.","Filtered to the 9 English regions plus Wales, Scotland and Northern Ireland, and loaded the cleaned table into SQLite with Python.","Wrote SQL (CTEs, self-joins on date offsets, correlated subqueries, aggregation) to compare 10-year growth, flats vs detached homes, change from the 2022–23 peak, and annual sales volumes.","Exported query results to <code>results.md</code> and charted them with matplotlib."], tools=["SQL","SQLite","Python","pandas","matplotlib","HM Land Registry UK HPI"], why="Regional and property-type differences drive lending, investment and housing-policy decisions; the project shows SQL used to answer business questions end to end.", skills=["SQL (CTEs, joins, subqueries)","Data cleaning","Regional analysis","Data visualisation"]),
}
def data_page(nw):
    fs, lim, data, meth = md_parts(nw["slug"]); x=DATA_EXTRA[nw["slug"]]
    imgs="".join(f'<figure><img src="charts/{c}" alt="{c[:-4].replace("_"," ")} chart"></figure>' for c in nw["charts"])
    links=" · ".join(f'<a href="{f}">{f}</a>' for f in nw["files"]+["README.md"])
    b=f"""<section class="hero small"><div class="wrap"><p class="kicker">Hands-on data project · {nw['kicker']}</p><h1>{nw['t']}</h1></div></section>
<article class="wrap case"><nav class="toc"><a href="#overview">Overview</a><a href="#method">Method</a><a href="#tools">Data &amp; tools</a><a href="#findings">Findings</a><a href="#why">Why it matters</a><a href="#skills">Skills</a></nav>
<h2 id="overview">Overview</h2><p>{meth}</p><h2 id="context">Context &amp; question</h2><p>{nw['q']}</p>
<h2 id="method">Methodology &amp; process</h2>{ul(x['steps'],'ol')}<h2 id="tools">Data &amp; tools</h2><p>{data}</p>{tags(x['tools'])}
<h2 id="findings">Findings &amp; outcomes</h2>{ul(fs)}{imgs}<p><strong>Limitations:</strong> {lim}</p>
<h2 id="why">Why it matters</h2><p>{x['why']}</p><h2 id="skills">Skills gained</h2>{tags(x['skills'])}
<h2>Code &amp; data</h2><p>{links}</p><p class="back"><a href="../../index.html#data">← Back to Data projects</a></p></article>"""
    return page(nw["t"], b, 2)
def card(href, title, text, sk):
    sl = href.split("/")[-1].replace(".html","") if href.startswith("projects-detail") else href.split("/")[1]
    return f'<a class="card" data-slug="{sl}" href="{href}"><h3>{esc(title)}</h3><p>{esc(text)}</p>{tags(sk[:3])}</a>'
def oneline(it):
    s=sents(it["summary"])[0]; return s if len(s)<150 else s[:147].rsplit(" ",1)[0]+"…"
def grid(ns): return '<div class="grid">'+"".join(card(f"projects-detail/{slug(n)}.html", ITEMS[n]["title"], oneline(ITEMS[n]), ITEMS[n]["skills"]) for n in ns)+"</div>"
def index():
    datac = "".join(card(f"projects/{nw['slug']}/index.html", nw['t'], nw['q'], DATA_EXTRA[nw['slug']]['tools'][:3]) for nw in NEW) + card(f"projects-detail/{slug(25)}.html", ITEMS[25]["title"], oneline(ITEMS[25]), ITEMS[25]["skills"])
    sk=[("Tools",["SQL (MySQL, SQLite)","Excel (Pivot Tables, Solver)","Power BI","Tableau","Python (pandas, statsmodels)"]),("Methods",["OLS regression & diagnostics","Time-series analysis","Financial ratio analysis","Break-even modelling","Portfolio optimisation","Multi-criteria decision analysis"]),("Research",["Survey design","Interviews & thematic coding","Market sizing (ONS Census)","Companies House due diligence","Policy & executive briefings"])]
    panels = {
     "about": f"""<div class="about"><div><p class="lead">Economics and sport business graduate who turns public and primary data into clear, decision-ready recommendations using SQL, Excel, Power BI, Tableau and econometrics. Targeting data, business, economic and financial analyst roles.</p>
<p class="sub">BSc Economics, University of Hertfordshire · MSc Sport Business Management, Sheffield Hallam University</p>
<div class="cta"><a class="btn" href="#sheffield-hallam">Consulting projects</a><a class="btn ghost" href="#data">Data projects</a><a class="btn ghost" href="mailto:{EMAIL}">Email</a><a class="btn ghost" href="{LI}">LinkedIn</a></div></div>
<div class="skills">{''.join(f'<div class="skillcol"><h3>{a}</h3>{tags(b)}</div>' for a,b in sk)}</div></div>""",
     "hertfordshire": f"<h2>University of Hertfordshire <span>BSc Economics</span></h2>{grid(range(1,14))}",
     "sheffield-hallam": f"<h2>Sheffield Hallam University <span>MSc Sport Business Management</span></h2>{grid(range(14,20))}",
     "data": f"<h2>Data projects <span>SQL · Python · BI on real UK public data</span></h2><div class='grid'>{datac}</div>",
     "simulations": f"<h2>Forage job simulations</h2>{grid(range(20,24))}",
     "experience": f"""<h2>Experience</h2><div class="job"><h3>Bartender · The Forum, Hertfordshire, UK</h3><p class="sub">Aug 2023 – Jan 2025</p>{ul(["<strong>Financial accountability:</strong> managed daily cash and digital transactions with 100% accuracy, maintaining strict bank-out procedures.","<strong>Customer excellence:</strong> delivered high-quality service in a high-volume setting, ensuring order accuracy during peak periods.","<strong>Team collaboration:</strong> partnered with a multicultural team to streamline bar operations, reducing waiting times.","<strong>Conflict resolution:</strong> handled complex customer inquiries and maintained a safe, professional environment."])}</div>
<div class="job"><h3>Education</h3>{ul(["MSc Sport Business Management, Sheffield Hallam University","BSc Economics, University of Hertfordshire"])}</div>""",
     "contact": f"""<h2>Contact</h2><p>Open to data, business, economic and financial analyst roles.</p><div class="cta"><a class="btn solid" href="mailto:{EMAIL}">{EMAIL}</a><a class="btn solid ghostl" href="{LI}">linkedin.com/in/kiyagakiwanuka</a></div>"""}
    body = "<div class='wrap panels'>"+"".join(f'<section id="tab-{k}" data-tab="{k}" class="panel">{panels[k]}</section>' for k,_ in TABS)+"</div>"
    js = """<style>"""+MODAL_CSS+"""</style><div id="pm" class="pm" aria-hidden="true" hidden><div class="pm-backdrop"></div><div class="pm-dialog" role="dialog" aria-modal="true" aria-labelledby="pm-title"><button class="pm-close" type="button" aria-label="Close project details">×</button><div class="pm-body" tabindex="-1"></div></div></div><script src="assets/app.js?v="""+VER+""""></script>"""
    hero = f'<section class="hero tiny"><div class="wrap"><p class="kicker">Data · Business · Economic · Financial Analyst</p><h1>Kiyaga Grace Kiwanuka</h1></div></section>'
    return page("Analyst Portfolio", hero+body, 0, js)
os.makedirs(f"{R}/projects-detail", exist_ok=True)
for f in os.listdir(f"{R}/projects-detail"): os.remove(f"{R}/projects-detail/{f}")
for n,it in ITEMS.items(): open(f"{R}/projects-detail/{slug(n)}.html","w").write(detail(it))
for nw in NEW: open(f"{R}/projects/{nw['slug']}/index.html","w").write(data_page(nw))
open(f"{R}/index.html","w").write(index())
print("built", len(ITEMS), "detail pages")
