"""Generates the static HTML pages. Run: python3 tools/build.py (output is committed; no build step needed for hosting)."""
import os, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL="kiyagagrace460@gmail.com"; LI="https://www.linkedin.com/in/kiyagakiwanuka"
def page(title, body, depth):
    p = "../"*depth
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Kiyaga Grace Kiwanuka</title><meta name="description" content="Kiyaga Grace Kiwanuka: data, business and economic analyst portfolio.">
<link rel="stylesheet" href="{p}assets/style.css"></head><body>
<header class="nav"><div class="wrap"><a class="brand" href="{p}index.html">Kiyaga Grace Kiwanuka</a>
<nav><a href="{p}index.html#projects">Projects</a><a href="{p}index.html#skills">Skills</a><a href="{p}index.html#experience">Experience</a><a href="{p}index.html#contact">Contact</a></nav></div></header>
<main>{body}</main><footer><div class="wrap">© 2026 Kiyaga Grace Kiwanuka · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{LI}">LinkedIn</a></div></footer></body></html>"""
def ul(xs): return "<ul>"+"".join(f"<li>{x}</li>" for x in xs)+"</ul>"
def tags(xs): return '<div class="tags">'+"".join(f"<span>{html.escape(x)}</span>" for x in xs)+"</div>"

CASES = [
 dict(slug="sharks-feasibility", t="Feasibility Study: Over-40s Basketball Programme, B. Braun Sheffield Sharks", org="MSc Sport Business Management · Sheffield Hallam University · Sole consultant", kicker="Primary research · break-even modelling · decision analysis",
  hl=["97 eligible survey responses","Break-even tested at 6 price points × 2 cost scenarios","20,000 randomised reweightings in sensitivity test"],
  prob="A Super League Basketball club asked whether it could sustainably run a weekly recreational session for adults over 40, and whether to fund it through a Sport England grant or through participant fees.",
  appr=["Designed and distributed a primary survey (97 eligible responses) and interviewed the founder of the only comparable provider in Sheffield.","Benchmarked court hire, sessional coaching and affiliation costs across the city.","Sized the addressable market from ONS Census 2021 data.","Traced the club's corporate structure through Companies House filings to establish which entity could apply for public money.","Built a contribution-margin model testing break-even across six price points and two cost scenarios.","Ranked the two funding pathways with weighted multi-criteria decision analysis, stress-tested against 20,000 randomised reweightings of the criteria."],
  find=["The survey reached lapsed and current players, not the inactive adults Sport England funds: 85.6% had played basketball before and only 6.2% recorded a week without a single 30-minute bout of activity.","This contradicted the premise of the brief. The sampling limitation became the basis of the recommendation: launch commercially for the audience the evidence found, and defer the grant application to year two once a running pilot can evidence the reach a funder scores against.","Delivered a 6,000-word report with a costed launch plan, a risk register and a staged measurement framework."],
  sk=["Survey design","Semi-structured interviews","Financial modelling","Break-even analysis","Multi-criteria decision analysis","Sensitivity testing","Companies House due diligence","ONS Census 2021","Consultancy reporting"]),
 dict(slug="uk-housing-econometrics", t="Econometric Analysis of UK Housing Market Determinants", org="BSc Economics · University of Hertfordshire", kicker="Time-series regression · ONS & Bank of England data",
  hl=["Quarterly data, 2005–2019","Regression model explaining 95% of price variation","Multicollinearity & heteroskedasticity tests"],
  prob="What drives UK house prices? The project tested how population density, interest rates and housing supply affect UK real estate prices.",
  appr=["Assembled quarter-by-quarter data from the Office for National Statistics (ONS) and the Bank of England, 2005–2019.","Estimated a time-series OLS regression of house prices on population density, interest rates and housing supply.","Tested model reliability by checking for multicollinearity and heteroskedasticity, and assessed statistical significance of each determinant."],
  find=["The regression model explained 95% of the variation in prices.","Shows how external shifts such as interest rate changes feed into asset values through supply-and-demand equilibrium."],
  sk=["OLS regression","Significance testing","Diagnostic testing","Time-series data","Macroeconomic analysis","Quantitative research"]),
 dict(slug="portfolio-optimisation", t="Portfolio Investment & Risk Management", org="BSc Economics · Techniques of Economic Analysis · University of Hertfordshire", kicker="Modern Portfolio Theory · matrix algebra · Excel Solver",
  hl=["5 stocks: Netflix, Amazon, Google, NVIDIA, RIO","2014–2018 returns","Efficient frontier with 10 allocations + Sharpe maximisation"],
  prob="How should capital be allocated across five major company shares to get the best risk-adjusted return?",
  appr=["Collected share data for Netflix, Amazon, Google, NVIDIA and RIO from 2014 to 2018.","Used matrix algebra to calculate the return and risk of an equally weighted portfolio.","Constructed an efficient frontier from 10 different allocation weights.","Used Excel Solver (linear programming) to find the allocation that maximises the Sharpe Ratio."],
  find=["Visualised the risk/return trade-off across allocations with the efficient frontier.","Identified the Sharpe-maximising allocation as the optimal risk-adjusted portfolio."],
  sk=["Financial modelling","Excel Solver","Linear programming","Matrix algebra","Modern Portfolio Theory","Risk-return analysis"]),
 dict(slug="everton-financials", t="Business & Financial Performance Report: Everton FC", org="MSc Sport Business Management · Sheffield Hallam University", kicker="Corporate financial analysis · ratios · benchmarking",
  hl=["Five-year review, 2020–2025","ROCE, Current Ratio, Gearing","4,000-word corporate report"],
  prob="How financially healthy and structurally stable is Everton FC, given ownership changes, stadium construction and Premier League Profit & Sustainability Rules (PSR)?",
  appr=["Analysed five years of financial performance (2020–2025).","Calculated and benchmarked ratios including ROCE, Current Ratio and Gearing.","Evaluated ownership transitions, matchday ticket price inelasticity and wage-to-turnover trajectories.","Assessed capital efficiency relating to the new stadium construction."],
  find=["Exposed core operating losses in the club's business.","Set out how competitive spending must be balanced with financial discipline under PSR, and how stadium commercialisation and private equity takeovers affect sustainability."],
  sk=["Ratio analysis","Financial statement analysis","Corporate benchmarking","Applied economic theory","Data visualisation","Strategic reporting"]),
 dict(slug="fsa-fan-research", t="Non-League Football Marketing & Communication: \"Who's Your Real Team?\"", org="MSc Sport Business Management · Consulting report for the Football Supporters' Association · Lead Operations", kicker="Mixed-methods research · digital audits · thematic coding",
  hl=["12 regional clubs audited","Face-to-face interviews with fans & volunteers","Best Practice Toolkit for club executives"],
  prob="Why does online reach at non-league clubs fail to convert into gate attendance, and what low-cost actions can close that gap?",
  appr=["Ran primary face-to-face qualitative interviews with fans and volunteers.","Carried out cross-platform digital audits across twelve regional clubs.","Deep-dived the operations of Worsbrough Bridge AFC, Maltby Main FC and Penistone Church FC to isolate the \"digital-to-physical action gap\".","Thematically coded Sheffield FC primary data into themes such as \"Grassroots Intimacy\" vs \"Professional Disillusionment\", using the AIDA model and Technology Acceptance Model, and integrated it with quantitative ground-experience scores."],
  find=["Identified where online reach fails to convert into attendance.","Delivered a low-cost Best Practice Toolkit: brand perception audits, mobile-first design optimisation and tactical scheduling to attract disillusioned Football League fans."],
  sk=["Qualitative interviewing","Thematic analysis & coding","Digital audit","Conversion analysis","AIDA / TAM frameworks","Strategic consulting"]),
 dict(slug="bi-pipeline", t="Enterprise Data Analytics & BI Pipeline", org="Self-directed technical project", kicker="SQL · Excel · Power BI · Tableau",
  hl=["MySQL Workbench queries & joins","Excel pivot tables & descriptive stats","Dashboards in Power BI and Tableau"],
  prob="Corporate data often sits in relational databases while decisions are made from dashboards. This project built an end-to-end workflow connecting the two, simulating real corporate lifecycle challenges.",
  appr=["Built relational database queries in MySQL Workbench, joining multi-layered tables to extract clean datasets.","Processed and transformed messy corporate records in Excel using dynamic Pivot Tables, logical conditions and descriptive statistics.","Modelled data connections across platforms and deployed interactive dashboards in Power BI and Tableau."],
  find=["A repeatable pipeline from database back-end to front-end business reporting.","Keeps conclusions grounded in statistical validity rather than visual bias."],
  sk=["SQL (MySQL)","Joins & RDBMS","Data cleansing / ETL","Excel Pivot Tables","Power BI","Tableau","Descriptive statistics"]),
 dict(slug="remote-work-london", t="Socioeconomic Dynamics of Remote Work in Greater London", org="BSc Economics · University of Hertfordshire", kicker="Econometric modelling · labour market analysis",
  hl=["1% more overcrowding → 1.59% lower likelihood of WFH","Education a key facilitator of flexible work"],
  prob="What determines who can work from home in Greater London? The project examined the role of housing conditions and education levels.",
  appr=["Built an econometric model of the likelihood of working from home.","Interpreted coefficients on home overcrowding and education."],
  find=["For every 1% increase in home overcrowding, the likelihood of working from home decreased by 1.59%.","Education was identified as a key facilitator of flexible roles.","The physical home environment matters as much as individual skills, with implications for HR strategy, urban planning and social policy."],
  sk=["Econometric modelling","Coefficient interpretation","Labour market analysis","Analytical writing"]),
]
NEW = [
 dict(slug="uk-house-prices-interest-rates", t="UK House Prices vs Bank Rate (2005–2026)", kicker="Python · pandas · statsmodels · Land Registry & BoE data",
  q="How closely do UK house prices respond to Bank of England rate changes, and with what lag?", charts=["price_vs_bank_rate.png","growth_vs_rate_change.png"], files=["analysis.py","download_data.sh","results.txt","data/uk_hpi_bankrate_clean.csv"]),
 dict(slug="uk-inflation-unemployment", t="UK Inflation, Unemployment & Bank Rate (1995–2026)", kicker="Python · ONS time series · Phillips curve",
  q="Does the UK Phillips curve still hold, and how fast does the Bank of England react to inflation?", charts=["macro_timeseries.png","phillips_curve.png"], files=["analysis.py","download_data.sh","results.txt","data/uk_macro_clean.csv"]),
 dict(slug="uk-regional-housing-sql", t="Regional House Prices with SQL (2016–2026)", kicker="SQL · SQLite · CTEs & self-joins · Land Registry data",
  q="Which regions and property types gained most in a decade, and where are prices still below their 2022–23 peak?", charts=["regional_growth.png","flat_vs_detached.png"], files=["queries.sql","load_and_run.py","results.md","data/regional_hpi_clean.csv"]),
]
OTHER = [("Comparative Evaluation of Classical and Neo-Classical Trade Theories","Ricardian vs Heckscher-Ohlin models, Leontief Paradox, H-O-V extension."),
("AI and the Demand for Labour","Acemoglu–Restrepo task-based model: displacement, productivity and reinstatement effects; argument map."),
("Global Value Chains & Developing Economies","Trade in tasks, the smile curve, middle-income trap, FDI and COVID-19 shocks."),
("Macroeconomic Performance: Indicators & Trends","Real GDP growth, unemployment, inflation; cross-economy comparison; Phillips Curve trade-offs."),
("Inflation Shocks and Institutional Responses","Central bank responses to inflation and their effect on employment and income inequality."),
("Economic Policy & the Cost-of-Living Crisis","Junior-economist briefing for the Secretary of State; energy producers' financial data 2014–2023 and windfall taxes."),
("Political Economy of Climate Change","Climate justice in Bangladesh and Tuvalu; loss-and-damage framework; climate migration costs."),
("Economic Justifications for State Investment Banks","Market failures, countercyclical lending and the entrepreneurial state."),
("Infant Industry Protection","UK, USA, Germany, Japan; trade policy vs GDP growth, 1960–80 protection vs 1980–2000 liberalisation."),
("Neoclassical Economics in the Water Sector","Privatisation, pricing and deregulation; efficiency vs equity trade-off."),
("Strategic & Marketing Plan: Forest Green Rovers F.C.","PESTEL, Porter's Five Forces, VRIO audit and STP marketing plan."),
("Leadership & Organisational Development","Inclusive culture, Emotional Intelligence models and multi-generational workforce dynamics."),
("Leadership Potential: Johari Window","Self vs peer perception, Goleman EI framework, personal development plan.")]
FORAGE = [("BCG","Data for Decision Makers","Interpreted simulated customer behaviour data in Excel to assess conversion across audiences and channels for a consumer goods client."),
("Deloitte Australia","Data Analytics","Classified raw corporate records in Excel and built an interactive Tableau dashboard; data modelling and forensic technology."),
("Tata Consultancy Services","Data Visualisation","Cleaned retail revenue data and built executive-ready visuals in Tableau/Power BI; drafted strategic questions for client meetings."),
("BCG","Introduction to Strategy Consulting","Structured creative thinking and brainstorming on revenue optimisation and repositioning for a luxury clothing brand.")]

def case_page(c):
    b = f"""<section class="hero small"><div class="wrap"><p class="kicker">{c['kicker']}</p><h1>{c['t']}</h1><p class="sub">{c['org']}</p>
<div class="stats">{''.join(f'<div>{h}</div>' for h in c['hl'])}</div></div></section>
<article class="wrap case"><h2>Problem</h2><p>{c['prob']}</p><h2>Approach</h2>{ul(c['appr'])}<h2>Findings</h2>{ul(c['find'])}<h2>Skills</h2>{tags(c['sk'])}
<p class="back"><a href="../index.html#projects">← Back to all projects</a></p></article>"""
    return page(c['t'], b, 1)
def md_findings(slug):
    txt = open(f"{R}/projects/{slug}/README.md").read()
    sec = txt.split("## Findings")[1].split("**Limitations")[0]; lines=[l[2:] for l in sec.splitlines() if l.startswith("- ")]
    lim = txt.split("**Limitations:**")[1].split("\n")[0].strip(); data = txt.split("**Data")[1].split("\n")[0].split(":**",1)[1].strip()
    meth = txt.split("**Method")[1].split("\n")[0].split(":**",1)[1].strip()
    import re; f = lambda s: re.sub(r"`([^`]+)`", r"<code>\1</code>", re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s))
    return [f(l) for l in lines], f(lim), f(data), f(meth)
def new_page(n):
    fs, lim, data, meth = md_findings(n['slug'])
    imgs = "".join(f'<figure><img src="charts/{c}" alt="{c[:-4].replace("_"," ")} chart"></figure>' for c in n['charts'])
    links = " · ".join(f'<a href="{f}">{f}</a>' for f in n['files'])
    b = f"""<section class="hero small"><div class="wrap"><p class="kicker">New hands-on project · {n['kicker']}</p><h1>{n['t']}</h1><p class="sub">{n['q']}</p></div></section>
<article class="wrap case"><h2>Problem</h2><p>{n['q']}</p><h2>Data</h2><p>{data}</p><h2>Approach</h2><p>{meth}</p><h2>Findings</h2>{ul(fs)}{imgs}
<h2>Limitations</h2><p>{lim}</p><h2>Code &amp; data</h2><p>{links} · <a href="README.md">README</a></p>
<p class="back"><a href="../../index.html#projects">← Back to all projects</a></p></article>"""
    return page(n['t'], b, 2)
def card(href, kicker, title, text, img=None):
    im = f'<img src="{img}" alt="" loading="lazy">' if img else ""
    return f'<a class="card" href="{href}">{im}<p class="kicker">{kicker}</p><h3>{title}</h3><p>{text}</p><span class="more">Read case study →</span></a>'
def index():
    feat = "".join(card(f"case-studies/{c['slug']}.html", c['kicker'], c['t'], c['hl'][0]) for c in CASES)
    newc = "".join(card(f"projects/{n['slug']}/index.html", n['kicker'], n['t'], n['q'], f"projects/{n['slug']}/charts/{n['charts'][0]}") for n in NEW)
    oth = "".join(f'<div class="mini"><h4>{t}</h4><p>{d}</p></div>' for t,d in OTHER)
    fg = "".join(f'<div class="mini"><p class="kicker">{a}</p><h4>{b}</h4><p>{d}</p></div>' for a,b,d in FORAGE)
    sk = [("Tools","SQL (MySQL, SQLite)","Excel (Pivot Tables, Solver)","Power BI","Tableau","Python (pandas, statsmodels, matplotlib)"),
          ("Quantitative methods","OLS regression & diagnostics","Time-series analysis","Financial ratio analysis","Break-even & contribution-margin modelling","Portfolio optimisation (MPT)","Multi-criteria decision analysis & sensitivity testing"),
          ("Research & communication","Survey design","Interviews & thematic coding","Market sizing (ONS Census)","Companies House due diligence","Executive & policy briefings","Consultancy reports")]
    skh = "".join(f'<div class="skillcol"><h3>{s[0]}</h3>{tags(s[1:])}</div>' for s in sk)
    b = f"""<section class="hero"><div class="wrap"><p class="kicker">Data · Business · Economic · Financial Analyst</p><h1>Kiyaga Grace Kiwanuka</h1>
<p class="lead">Economics and sport business graduate who turns public and primary data into clear, decision-ready recommendations using SQL, Excel, Power BI, Tableau and econometrics.</p>
<p class="sub">BSc Economics, University of Hertfordshire · MSc Sport Business Management, Sheffield Hallam University</p>
<div class="cta"><a class="btn" href="#projects">View projects</a><a class="btn ghost" href="mailto:{EMAIL}">Email me</a><a class="btn ghost" href="{LI}">LinkedIn</a></div></div></section>
<section id="skills" class="wrap"><h2>Skills</h2><div class="skills">{skh}</div></section>
<section id="projects" class="wrap"><h2>Featured projects</h2><p class="intro">Case studies from university and consulting work, written as Problem → Approach → Findings → Skills.</p><div class="grid">{feat}</div>
<h2 class="mt">Hands-on data projects</h2><p class="intro">Reproducible analyses on real UK public data, with code, cleaned data and charts.</p><div class="grid">{newc}</div></section>
<section class="wrap"><h2>Forage job simulations</h2><div class="minigrid">{fg}</div></section>
<section class="wrap"><h2>Other academic work</h2><div class="minigrid">{oth}</div></section>
<section id="experience" class="wrap"><h2>Experience</h2><div class="job"><h3>Bartender · The Forum, Hertfordshire, UK</h3><p class="sub">Aug 2023 – Jan 2025</p>
{ul(["Managed daily cash and digital transactions with 100% accuracy, following strict bank-out procedures.","Delivered accurate, high-quality service in a high-volume setting during peak periods.","Worked with a multicultural team to streamline bar operations, reducing waiting times.","Handled complex customer enquiries and maintained a safe, professional environment."])}</div>
<div class="job"><h3>Education</h3>{ul(["MSc Sport Business Management, Sheffield Hallam University","BSc Economics, University of Hertfordshire"])}</div></section>
<section id="contact" class="wrap contact"><h2>Contact</h2><p>Open to data, business, economic and financial analyst roles.</p>
<div class="cta"><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a><a class="btn ghost" href="{LI}">linkedin.com/in/kiyagakiwanuka</a></div></section>"""
    return page("Analyst Portfolio", b, 0)
os.makedirs(f"{R}/case-studies", exist_ok=True)
open(f"{R}/index.html","w").write(index())
for c in CASES: open(f"{R}/case-studies/{c['slug']}.html","w").write(case_page(c))
for n in NEW: open(f"{R}/projects/{n['slug']}/index.html","w").write(new_page(n))
print("built")
