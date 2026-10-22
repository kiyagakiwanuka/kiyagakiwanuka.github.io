-- Regional house price analysis (SQLite). Table hpi built by load_and_run.py from HM Land Registry UK HPI.
-- Q1: average price by English region + nations, latest month vs 10 years earlier
WITH latest AS (SELECT MAX(date) d FROM hpi)
SELECT a.region, ROUND(b.avg_price) AS price_10y_ago, ROUND(a.avg_price) AS price_latest,
       ROUND(100.0*(1.0*a.avg_price/b.avg_price-1),1) AS growth_pct
FROM hpi a JOIN hpi b ON a.region=b.region AND b.date=date((SELECT d FROM latest),'-10 years')
WHERE a.date=(SELECT d FROM latest) AND a.region IN (SELECT region FROM regions)
ORDER BY growth_pct DESC;
-- Q2: flat vs detached price growth over the same 10 years, by region
WITH latest AS (SELECT MAX(date) d FROM hpi)
SELECT a.region, ROUND(100.0*(1.0*a.flat_price/b.flat_price-1),1) AS flat_growth_pct,
       ROUND(100.0*(1.0*a.detached_price/b.detached_price-1),1) AS detached_growth_pct
FROM hpi a JOIN hpi b ON a.region=b.region AND b.date=date((SELECT d FROM latest),'-10 years')
WHERE a.date=(SELECT d FROM latest) AND a.region IN (SELECT region FROM regions)
ORDER BY flat_growth_pct;
-- Q3: peak-to-latest change after the 2022-23 rate rises
SELECT h.region, p.peak_date, ROUND(p.peak) AS peak_price, ROUND(h.avg_price) AS latest_price,
       ROUND(100.0*(1.0*h.avg_price/p.peak-1),1) AS change_from_peak_pct
FROM hpi h JOIN (SELECT region, MAX(avg_price) peak,
     (SELECT date FROM hpi x WHERE x.region=y.region AND x.date BETWEEN '2022-01-01' AND '2023-12-31' ORDER BY avg_price DESC LIMIT 1) peak_date
     FROM hpi y WHERE date BETWEEN '2022-01-01' AND '2023-12-31' GROUP BY region) p ON h.region=p.region
WHERE h.date=(SELECT MAX(date) FROM hpi) AND h.region IN (SELECT region FROM regions)
ORDER BY change_from_peak_pct;
-- Q4: annual recorded sales volume, England (complete years only)
SELECT strftime('%Y',date) AS yr, SUM(sales_volume) AS sales FROM hpi
WHERE region='England' AND date BETWEEN '2015-01-01' AND '2024-12-31' GROUP BY yr ORDER BY yr;
