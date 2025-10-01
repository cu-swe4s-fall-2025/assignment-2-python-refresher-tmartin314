#!/usr/bin/env bash
set -u

# Working example
python3 print_fires.py \
  --file_name mini_agro.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 4 \
  --op mean

# Error 1: missing file
python3 print_fires.py \
  --file_name data/DOES_NOT_EXIST.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 4 || echo "Expected failure: missing file"

# Error 2: bad column index
python3 print_fires.py \
  --file_name mini_agro.csv \
  --country "USA" \
  --country_column 99 \
  --fires_column 4 || echo "Expected failure: bad column index"
