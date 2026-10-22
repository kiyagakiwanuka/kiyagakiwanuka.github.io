"""UK house prices vs Bank of England Bank Rate (2005 onwards).
Sources: HM Land Registry UK HPI full file; BoE series IUMABEDR (monthly average Bank Rate)."""
import pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, statsmodels.formula.api as smf, os
D = os.path.join(os.path.dirname(__file__), "data"); C = os.path.join(os.path.dirname(__file__), "charts")
hpi = pd.read_csv(f"{D}/uk_hpi_full.csv", usecols=["Date","RegionName","AveragePrice","Index","SalesVolume"])
uk = hpi[hpi.RegionName=="United Kingdom"].copy()
uk["Date"] = pd.to_datetime(uk.Date, dayfirst=True); uk = uk.sort_values("Date")
uk["month"] = uk.Date.dt.to_period("M")
br = pd.read_csv(f"{D}/boe_bank_rate.csv"); br["month"] = pd.to_datetime(br.DATE, format="%d %b %Y").dt.to_period("M")
br = br.rename(columns={"IUMABEDR":"bank_rate"})[["month","bank_rate"]]
df = uk.merge(br, on="month").set_index("month")
df["hpi_yoy"] = df.AveragePrice.pct_change(12)*100
df["rate_chg_12m"] = df.bank_rate.diff(12)
df["rate_chg_12m_lag12"] = df.rate_chg_12m.shift(12)
df = df[df.index >= pd.Period("2005-01","M")]
df[["AveragePrice","Index","SalesVolume","bank_rate","hpi_yoy","rate_chg_12m"]].to_csv(f"{D}/uk_hpi_bankrate_clean.csv")
out = []
first, last = df.iloc[0], df.dropna(subset=["AveragePrice"]).iloc[-1]
out.append(f"Period: {df.index[0]} to {last.name}")
out.append(f"UK average price: £{first.AveragePrice:,.0f} -> £{last.AveragePrice:,.0f} ({(last.AveragePrice/first.AveragePrice-1)*100:.1f}% nominal)")
pk = df.AveragePrice.idxmax(); out.append(f"Peak average price: £{df.AveragePrice.max():,.0f} in {pk}")
out.append(f"Max YoY growth: {df.hpi_yoy.max():.1f}% ({df.hpi_yoy.idxmax()}); min YoY: {df.hpi_yoy.min():.1f}% ({df.hpi_yoy.idxmin()})")
for lag in [0,6,12,18,24]:
    out.append(f"Corr(HPI YoY, 12m change in Bank Rate lagged {lag}m) = {df.hpi_yoy.corr(df.rate_chg_12m.shift(lag)):.2f}")
m = smf.ols("hpi_yoy ~ rate_chg_12m_lag12", data=df.dropna(subset=["hpi_yoy","rate_chg_12m_lag12"])).fit(cov_type="HAC", cov_kwds={"maxlags":12})
out.append(f"OLS hpi_yoy ~ rate_chg_12m_lag12 (HAC SE): coef={m.params.iloc[1]:.2f} pp per 1pp rate change, p={m.pvalues.iloc[1]:.3f}, R2={m.rsquared:.2f}, n={int(m.nobs)}")
# 2022-23 tightening episode
tight = df.loc["2021-12":"2023-08"]
out.append(f"Tightening Dec-2021->Aug-2023: Bank Rate {tight.bank_rate.iloc[0]:.2f}% -> {tight.bank_rate.iloc[-1]:.2f}%")
sv = df.SalesVolume.dropna(); s22, s23 = sv.loc["2022"].sum(), sv.loc["2023"].sum()
out.append(f"Recorded sales volume 2022: {s22:,.0f}; 2023: {s23:,.0f} ({(s23/s22-1)*100:.1f}%) [recent months subject to revision]")
open(os.path.join(os.path.dirname(__file__),"results.txt"),"w").write("\n".join(out)+"\n\n"+m.summary().as_text()); print("\n".join(out))
fig, ax = plt.subplots(figsize=(10,5)); ax.plot(df.index.to_timestamp(), df.AveragePrice/1000, color="#1f4e79"); ax.set_ylabel("UK average price (£000)", color="#1f4e79")
ax2 = ax.twinx(); ax2.plot(df.index.to_timestamp(), df.bank_rate, color="#c0504d"); ax2.set_ylabel("Bank Rate (%)", color="#c0504d")
ax.set_title("UK average house price vs Bank of England Bank Rate"); fig.text(0.01,0.01,"Source: HM Land Registry UK HPI; Bank of England (IUMABEDR)",fontsize=8); fig.tight_layout(); fig.savefig(f"{C}/price_vs_bank_rate.png", dpi=130)
fig, ax = plt.subplots(figsize=(10,5)); ax.plot(df.index.to_timestamp(), df.hpi_yoy, label="House price growth, YoY %", color="#1f4e79")
ax.plot(df.index.to_timestamp(), df.rate_chg_12m_lag12, label="12m change in Bank Rate (pp), lagged 12m", color="#c0504d"); ax.axhline(0,color="grey",lw=.7); ax.legend(); ax.set_title("House price growth vs lagged change in Bank Rate")
fig.text(0.01,0.01,"Source: HM Land Registry UK HPI; Bank of England",fontsize=8); fig.tight_layout(); fig.savefig(f"{C}/growth_vs_rate_change.png", dpi=130)
