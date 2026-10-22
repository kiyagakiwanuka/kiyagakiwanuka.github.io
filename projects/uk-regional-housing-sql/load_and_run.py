"""Load HM Land Registry UK HPI into SQLite, run queries.sql, save outputs and charts."""
import pandas as pd, sqlite3, os, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
B = os.path.dirname(os.path.abspath(__file__)); D, C = f"{B}/data", f"{B}/charts"
REG = ["North East","North West","Yorkshire and The Humber","East Midlands","West Midlands","East of England","London","South East","South West","Wales","Scotland","Northern Ireland"]
raw = pd.read_csv(f"{D}/uk_hpi_full.csv", usecols=["Date","RegionName","AveragePrice","SalesVolume","DetachedPrice","FlatPrice"])
df = raw[raw.RegionName.isin(REG+["England","United Kingdom"])].copy()
df["date"] = pd.to_datetime(df.Date, dayfirst=True).dt.strftime("%Y-%m-%d")
df = df.rename(columns={"RegionName":"region","AveragePrice":"avg_price","SalesVolume":"sales_volume","DetachedPrice":"detached_price","FlatPrice":"flat_price"})[["date","region","avg_price","sales_volume","detached_price","flat_price"]]
df.to_csv(f"{D}/regional_hpi_clean.csv", index=False)
con = sqlite3.connect(":memory:"); df.to_sql("hpi", con, index=False); pd.DataFrame({"region":REG}).to_sql("regions", con, index=False)
qs = [q.strip() for q in open(f"{B}/queries.sql").read().split(";") if "SELECT" in q]
res = []
with open(f"{B}/results.md","w") as f:
    for i,q in enumerate(qs,1):
        r = pd.read_sql(q, con); res.append(r); f.write(f"## Q{i}\n\n{r.to_markdown(index=False)}\n\n"); print(f"Q{i}\n", r.to_string(index=False))
r = res[0].sort_values("growth_pct"); fig, ax = plt.subplots(figsize=(9,5.5)); ax.barh(r.region, r.growth_pct, color="#1f4e79")
ax.set_xlabel("Average price growth over 10 years (%)"); ax.set_title("10-year house price growth by UK region / nation"); fig.text(.01,.01,"Source: HM Land Registry UK HPI",fontsize=8); fig.tight_layout(); fig.savefig(f"{C}/regional_growth.png", dpi=130)
r = res[1].set_index("region").sort_values("flat_growth_pct"); ax = r.plot.barh(figsize=(9,5.5), color=["#c0504d","#1f4e79"]); ax.set_xlabel("10-year growth (%)"); ax.set_title("Flats vs detached houses: 10-year price growth"); plt.tight_layout(); plt.savefig(f"{C}/flat_vs_detached.png", dpi=130)
