#!/usr/bin/env bash
# Functional tests for print_fires.py (Assignment 4) - single directory version

set -u -o pipefail

TESTS=0
FAILS=0
CMD=""
OUT=""
STATUS=0

run() {
  CMD="$*"
  OUT="$("$@" 2>&1)"
  STATUS=$?
}

ok_status() {
  TESTS=$((TESTS+1))
  local want="$1"
  if [[ "$STATUS" -eq "$want" ]]; then
    echo "PASS status == $want"
  else
    echo "FAIL status $STATUS != $want :: $CMD :: $OUT"
    FAILS=$((FAILS+1))
  fi
}

ok_eq() {
  TESTS=$((TESTS+1))
  local want="$1"
  if [[ "$OUT" == "$want" ]]; then
    echo "PASS output equals: $want"
  else
    echo "FAIL output mismatch. wanted: [$want] got: [$OUT]"
    FAILS=$((FAILS+1))
  fi
}

ok_has() {
  TESTS=$((TESTS+1))
  local needle="$1"
  if [[ "$OUT" == *"$needle"* ]]; then
    echo "PASS output contains: $needle"
  else
    echo "FAIL missing: $needle :: out: $OUT"
    FAILS=$((FAILS+1))
  fi
}

finish() {
  echo
  echo "Ran $TESTS tests; failures: $FAILS"
  [[ "$FAILS" -eq 0 ]] || exit 1
  exit 0
}

SCRIPT="./print_fires.py"
DATA="./mini_agro.csv"
PY=python3

[[ -f "$SCRIPT" ]] || { echo "FAIL missing $SCRIPT"; exit 1; }
[[ -f "$DATA"   ]] || { echo "FAIL missing $DATA"; exit 1; }

# 1) Raw print (no --op)
run "$PY" "$SCRIPT" --file_name "$DATA" --country "United States of America" --country_column 0 --fires_column 4
ok_status 0
ok_eq "[100, 110, 90]"

# 2) mean
run "$PY" "$SCRIPT" --file_name "$DATA" --country "United States of America" --country_column 0 --fires_column 4 --op mean
ok_status 0
ok_eq "mean = 100.0"

# 3) median
run "$PY" "$SCRIPT" --file_name "$DATA" --country "United States of America" --country_column 0 --fires_column 4 --op median
ok_status 0
ok_eq "median = 100"

# 4) std (population) - just check substring
run "$PY" "$SCRIPT" --file_name "$DATA" --country "United States of America" --country_column 0 --fires_column 4 --op std
ok_status 0
ok_has "standard_deviation = "
ok_has "8.16"   # ≈ 8.1649

# 5) zero matches -> []
run "$PY" "$SCRIPT" --file_name "$DATA" --country "Atlantis" --country_column 0 --fires_column 4
ok_status 0
ok_eq "[]"

# 6) missing file -> exit 2
run "$PY" "$SCRIPT" --file_name "./DOES_NOT_EXIST.csv" --country "United States of America" --country_column 0 --fires_column 4 --op mean
ok_status 2
ok_has "Error:"

# 7) bad column index -> exit 2
run "$PY" "$SCRIPT" --file_name "$DATA" --country "United States of America" --country_column 99 --fires_column 4
ok_status 2
ok_has "Error:"

# 8) non-integer fires value (Canada is N/A) -> exit 2
run "$PY" "$SCRIPT" --file_name "$DATA" --country "Canada" --country_column 0 --fires_column 4 --op mean
ok_status 2
ok_has "Error:"
ok_has "Non-integer"

finish
