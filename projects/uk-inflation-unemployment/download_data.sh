#!/usr/bin/env bash
# Downloads ONS CPIH annual rate (L55O), ONS unemployment rate (MGSX) and BoE Bank Rate
set -e; cd "$(dirname "$0")/data"
curl -sL -A "Mozilla/5.0" -o ons_cpih_l55o.csv "https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l55o/mm23"
curl -sL -A "Mozilla/5.0" -o ons_unemployment_mgsx.csv "https://www.ons.gov.uk/generator?format=csv&uri=/employmentandlabourmarket/peoplenotinwork/unemployment/timeseries/mgsx/lms"
curl -sL -A "Mozilla/5.0" -o boe_bank_rate.csv "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/1995&Dateto=31/Dec/2026&SeriesCodes=IUMABEDR&CSVF=TN&UsingCodes=Y"
