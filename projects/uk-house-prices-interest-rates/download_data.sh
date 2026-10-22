#!/usr/bin/env bash
# Downloads raw public data (UK HM Land Registry UK HPI, Bank of England Bank Rate)
set -e; cd "$(dirname "$0")/data"
curl -sL -o uk_hpi_full.csv "https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2026-07.csv"
curl -sL -A "Mozilla/5.0" -o boe_bank_rate.csv "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/1995&Dateto=31/Dec/2026&SeriesCodes=IUMABEDR&CSVF=TN&UsingCodes=Y"
