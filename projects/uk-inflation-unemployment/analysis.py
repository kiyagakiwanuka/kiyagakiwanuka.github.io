"""UK inflation, unemployment and Bank Rate: a Phillips-curve and policy-reaction check.
Sources: ONS CPIH annual rate (L55O, MM23), ONS unemployment rate 16+ SA (MGSX, LMS), BoE Bank Rate (IUMABEDR)."""
import pandas as pd, numpy as np, re, os, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = os.path.join(os.path.dirname(__file__), "data"); C = os.path.join(os.path.dirname(__file__), "charts")
def ons_monthly(path, name):
    raw = pd.read_csv(path, header=None, names=["k","v"])
    m = raw[raw.k.str.match(r"^\d{4} [A-Z]{3}$", na=False)].copy()
    m["month"] = pd.to_datetime(m.k, format="%Y %b").dt.to_period("M")
    return m.set_index("month").v.astype(float).rename(name)
cpih = ons_monthly(f"{D}/ons_cpih_l55o.csv","cpih"); un = ons_monthly(f"{D}/ons_unemployment_mgsx.csv","unemployment")
br = pd.read_csv(f"{D}/boe_bank_rate.csv"); br.index = pd.to_datetime(br.DATE, format="%d %b %Y").dt.to_period("M"); br = br.IUMABEDR.rename("bank_rate")
df = pd.concat([cpih, un, br], axis=1).dropna(); df.to_csv(f"{D}/uk_macro_clean.csv")
out = [f"Common monthly sample: {df.index[0]} to {df.index[-1]} (n={len(df)})"]
out.append(f"Peak CPIH: {df.cpih.max():.1f}% in {df.cpih.idxmax()}; latest CPIH {df.cpih.iloc[-1]:.1f}%, unemployment {df.unemployment.iloc[-1]:.1f}%, Bank Rate {df.bank_rate.iloc[-1]:.2f}% ({df.index[-1]})")
out.append(f"Peak unemployment in sample: {df.unemployment.max():.1f}% in {df.unemployment.idxmax()}; low: {df.unemployment.min():.1f}% in {df.unemployment.idxmin()}")
for a,b in [("1995-01","2007-12"),("2008-01","2019-12"),("2020-01",str(df.index[-1]))]:
    s = df.loc[a:b]; slope = np.polyfit(s.unemployment, s.cpih, 1)[0]
    out.append(f"{a[:4]}-{b[:4]}: corr(unemployment, CPIH)={s.unemployment.corr(s.cpih):.2f}, slope={slope:.2f} pp inflation per pp unemployment")
lags = {l: df.cpih.corr(df.bank_rate.shift(-l)) for l in range(0,25,3)}
best = max(lags, key=lags.get); out.append("Corr(CPIH today, Bank Rate l months later): " + ", ".join(f"{l}m={v:.2f}" for l,v in lags.items()) + f" -> strongest at {best}m")
hi = df[df.cpih>2].loc["2021":]; out.append(f"Post-2021: CPIH first above 2% in {hi.index[0]}; first Bank Rate rise month " + str(df.loc["2021":][df.bank_rate.loc['2021':].diff()>0].index[0]))
open(os.path.join(os.path.dirname(__file__),"results.txt"),"w").write("\n".join(out)); print("\n".join(out))
fig, ax = plt.subplots(figsize=(10,5)); t = df.index.to_timestamp()
for col,c,l in [("cpih","#c0504d","CPIH inflation, annual %"),("unemployment","#1f4e79","Unemployment rate %"),("bank_rate","#7f7f7f","Bank Rate %")]: ax.plot(t, df[col], color=c, label=l)
ax.axhline(2, ls="--", color="#c0504d", lw=.7); ax.legend(); ax.set_title("UK inflation, unemployment and Bank Rate"); fig.text(0.01,0.01,"Source: ONS (L55O, MGSX); Bank of England (IUMABEDR)",fontsize=8); fig.tight_layout(); fig.savefig(f"{C}/macro_timeseries.png", dpi=130)
fig, ax = plt.subplots(figsize=(7,5))
for (a,b),c in zip([("1995","2007"),("2008","2019"),("2020","2030")],["#1f4e79","#9bbb59","#c0504d"]):
    s = df.loc[a:b]; ax.scatter(s.unemployment, s.cpih, s=10, color=c, label=f"{a}-{min(int(b),df.index[-1].year)}")
ax.set_xlabel("Unemployment rate %"); ax.set_ylabel("CPIH inflation %"); ax.legend(); ax.set_title("UK Phillips curve by era"); fig.tight_layout(); fig.savefig(f"{C}/phillips_curve.png", dpi=130)
