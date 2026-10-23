"""Generates all static pages from tools/source.md (the skills file, minus excluded items) + tools/content.py.
Run: python3 tools/build.py   (output is committed; hosting needs no build step)
Future: add a 'Passion projects / Skills highlights' tab by appending to TABS and writing its panel in index()."""
from rich import R as RICH
import os, re, html, sys
sys.path.insert(0, os.path.dirname(__file__)); from content import CASES
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
def group(n): return "hertfordshire" if n<=13 else "sheffield-hallam" if n<=19 else "simulations"
GROUPNAME = {"hertfordshire":"University of Hertfordshire · BSc Economics","sheffield-hallam":"Sheffield Hallam University · MSc Sport Business Management","simulations":"Forage job simulation"}
def esc(s): return html.escape(s, quote=False)
def ul(xs, tag="ul"): return f"<{tag}>"+"".join(f"<li>{x}</li>" for x in xs)+f"</{tag}>"
def tags(xs): return '<div class="tags">'+"".join(f"<span>{esc(x)}</span>" for x in xs)+"</div>"
def page(title, body, depth, extra=""):
    p = "../"*depth
    nav = "".join(f'<a href="{p}index.html#{k}">{v}</a>' for k,v in TABS)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | Kiyaga Grace Kiwanuka</title><meta name="description" content="Kiyaga Grace Kiwanuka: portfolio of economics, business and data projects.">
<link rel="stylesheet" href="{p}assets/style.css?v={VER}"></head><body>
<header class="nav"><div class="wrap"><a class="brand" href="{p}index.html">Kiyaga Grace Kiwanuka</a><nav id="tabs">{nav}</nav></div></header>
<main>{body}</main><footer><div class="wrap">© 2026 Kiyaga Grace Kiwanuka · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{LI}">LinkedIn</a></div></footer>{extra}</body></html>"""
TABS = [("about","About"),("hertfordshire","Hertfordshire"),("sheffield-hallam","Sheffield Hallam"),("simulations","Simulations"),("experience","Experience"),("contact","Contact")]
def find_tools(text): 
    out=[]; 
    for t in TOOLS:
        if t.lower() in text.lower() and not any(t.lower() in o.lower() for o in out): out.append(t)
    return out
def _w(t): return set(re.findall(r"[a-z0-9]+", re.sub(r"<[^>]+>","",t).lower()))
STOP=set("a an the and or of to in on for by with from at as is are was were be it its this that these those their his her into than then so such can may how what which who do does across over between before after each".split())
def _near(w,x):
    # near-identical: >60% of the shorter sentence's content words reappear, and at least 4 of them
    cw,cx=w-STOP,x-STOP; o=len(cw&cx)
    return o>=4 and o/max(1,min(len(cw),len(cx)))>0.6
def _ss(t): return [x for x in re.split(r"(?<=[.!?])\s+", re.sub(r"<[^>]+>","",t)) if len(_w(x))>=4]
def _n(t): return " ".join(sorted(_w(t)))
def _dup(t, seen):
    # seen: list of word-sets, one per previously rendered sentence
    for s in _ss(t) or [t]:
        w=_w(s)
        if any(x and _near(w,x) for x in seen): return True
    return False
def _add(seen, t): seen.extend(_w(s) for s in (_ss(t) or [t]))
def CVER():
    import glob
    h=hashlib.md5()
    for f in sorted(glob.glob(os.path.join(R,"projects-detail","*.html"))+glob.glob(os.path.join(R,"projects","*","index.html"))): h.update(open(f,'rb').read())
    return h.hexdigest()[:8]
def detail(it):
    n=it["n"]; ss=sents(it["summary"]); ws=sents(it["why"]); c=CBYSLUG.get(CURATED.get(n,""))
    E = (lambda x: x) if c else esc
    r=RICH.get(n,{})
    ctx=[c["prob"] if c else esc(r["q"])] if (c or r.get("q")) else []
    ctx+= [esc(r["ctx"])] if r.get("ctx") else []
    con=[f"<strong>{esc(a)}</strong>: {esc(b)}" for a,b in r.get("con",[])]
    meth=c["appr"] if c else [esc(x) for x in r["app"]] if r.get("app") else [esc(x) for x in ss[1:]]
    secs = [("overview","Overview","p",[esc(ss[0])]),
            ("context","Context &amp; question","p",ctx),
            ("concepts","Key concepts","ul",con),
            ("method","Methodology &amp; process","ol",[E(x) for x in meth] if c else meth),
            ("tools","Data &amp; tools","tags",find_tools(it["summary"]+" "+it["why"])),
            ("findings","Findings &amp; outcomes","ul",[E(x) for x in c["find"]] if c else [] if r.get("app") else [esc(x) for x in ss[1:]]),
            ("why","Why it matters","p",[esc(x) for x in ws]+[esc(x) for x in r.get("emp",[])]),
            ("skills","Skills gained","tags",it["skills"])]
    seen=[]; out=[]; toc=[]
    for sid,name,kind,items in secs:
        if kind!="tags":
            items=[x for x in items if not _dup(x,seen)]
            for x in items: _add(seen,x)
        if not items: continue
        body = tags(items) if kind=="tags" else ul(items,kind) if kind in("ul","ol") else "".join(f"<p>{x}</p>" for x in items)
        out.append(f'<h2 id="{sid}">{name}</h2>{body}'); toc.append(f'<a href="#{sid}">{name.split(" &amp;")[0].replace("Key concepts","Concepts")}</a>')
    hl = "".join(f"<div>{h}</div>" for h in c["hl"]) if c else ""
    g=group(n); back=f"../index.html#{g}"
    b=f"""<section class="hero small"><div class="wrap"><p class="kicker">{"Technical data project" if n==25 else GROUPNAME[g]}</p><h1>{esc(it['title'])}</h1>{'<div class="stats">'+hl+'</div>' if hl else ''}</div></section>
<article class="wrap case"><nav class="toc">{''.join(toc)}</nav>
{''.join(out)}
<p class="back"><a href="{back}">← Back to {dict(TABS)[g]}</a></p></article>"""
    return page(it["title"], b, 1)
def card(href, title, text, sk):
    sl = href.split("/")[-1].replace(".html","") if href.startswith("projects-detail") else href.split("/")[1]
    return f'<a class="card" data-slug="{sl}" href="{href}"><h3>{esc(title)}</h3><p>{esc(text)}</p>{tags(sk[:3])}</a>'
def oneline(it):
    s=sents(it["summary"])[0]; return s if len(s)<150 else s[:147].rsplit(" ",1)[0]+"…"
def grid(ns): return '<div class="grid">'+"".join(card(f"projects-detail/{slug(n)}.html", ITEMS[n]["title"], oneline(ITEMS[n]), ITEMS[n]["skills"]) for n in ns)+"</div>"
def index():
    sk=[("Tools",["SQL (MySQL)","Excel (Pivot Tables, Solver)","Power BI","Tableau"]),("Methods",["OLS regression & diagnostics","Time-series analysis","Financial ratio analysis","Break-even modelling","Portfolio optimisation","Multi-criteria decision analysis"]),("Research",["Survey design","Interviews & thematic coding","Market sizing (ONS Census)","Companies House due diligence","Policy & executive briefings"])]
    panels = {
     "about": f"""<div class="about"><div><p class="lead">Economics and sport business graduate who turns public and primary data into clear, decision-ready recommendations using SQL, Excel, Power BI, Tableau and econometrics.</p>
<p class="sub">BSc Economics, University of Hertfordshire · MSc Sport Business Management, Sheffield Hallam University</p>
<div class="cta"><a class="btn" href="#sheffield-hallam">Consulting projects</a><a class="btn ghost" href="#hertfordshire">Economics projects</a><a class="btn ghost" href="mailto:{EMAIL}">Email</a><a class="btn ghost" href="{LI}">LinkedIn</a></div></div>
<div class="skills">{''.join(f'<div class="skillcol"><h3>{a}</h3>{tags(b)}</div>' for a,b in sk)}</div></div>""",
     "hertfordshire": f"<h2>University of Hertfordshire <span>BSc Economics</span></h2>{grid(range(1,14))}",
     "sheffield-hallam": f"<h2>Sheffield Hallam University <span>MSc Sport Business Management</span></h2>{grid(range(14,20))}",
     "simulations": f"<h2>Forage job simulations</h2>{grid(range(20,24))}<h2>Technical project</h2>{grid([25])}",
     "experience": f"""<h2>Experience</h2><div class="job"><h3>Bartender · The Forum, Hertfordshire, UK</h3><p class="sub">Aug 2023 – Jan 2025</p>{ul(["<strong>Financial accountability:</strong> managed daily cash and digital transactions with 100% accuracy, maintaining strict bank-out procedures.","<strong>Customer excellence:</strong> delivered high-quality service in a high-volume setting, ensuring order accuracy during peak periods.","<strong>Team collaboration:</strong> partnered with a multicultural team to streamline bar operations, reducing waiting times.","<strong>Conflict resolution:</strong> handled complex customer inquiries and maintained a safe, professional environment."])}</div>
<div class="job"><h3>Education</h3>{ul(["MSc Sport Business Management, Sheffield Hallam University","BSc Economics, University of Hertfordshire"])}</div>""",
     "contact": f"""<h2>Contact</h2><p>Get in touch by email or LinkedIn.</p><div class="cta"><a class="btn solid" href="mailto:{EMAIL}">{EMAIL}</a><a class="btn solid ghostl" href="{LI}">linkedin.com/in/kiyagakiwanuka</a></div>"""}
    body = "<div class='wrap panels'>"+"".join(f'<section id="tab-{k}" data-tab="{k}" class="panel">{panels[k]}</section>' for k,_ in TABS)+"</div>"
    js = """<style>"""+MODAL_CSS+"""</style><div id="pm" class="pm" data-v="@@CVER@@" aria-hidden="true" hidden><div class="pm-backdrop"></div><div class="pm-dialog" role="dialog" aria-modal="true" aria-labelledby="pm-title"><button class="pm-close" type="button" aria-label="Close project details">×</button><div class="pm-body" tabindex="-1"></div></div></div><script src="assets/app.js?v="""+VER+""""></script>"""
    hero = f'<section class="hero tiny"><div class="wrap"><p class="kicker">Economics · Business · Data</p><h1>Kiyaga Grace Kiwanuka</h1></div></section>'
    return page("Portfolio", hero+body, 0, js)
os.makedirs(f"{R}/projects-detail", exist_ok=True)
for f in os.listdir(f"{R}/projects-detail"): os.remove(f"{R}/projects-detail/{f}")
for n,it in ITEMS.items(): open(f"{R}/projects-detail/{slug(n)}.html","w").write(detail(it))
open(f"{R}/index.html","w").write(index().replace("@@CVER@@",CVER()))
print("built", len(ITEMS), "detail pages")
