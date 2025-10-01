import csv

def get_column(file_name, query_column, query_value, fires_column):
    """
    Return a list of INTEGERS from 'fires_column' for rows where row[query_value] == query_column.
    Raises FileNotFoundError, OSError, IndexError, ValueError on problems.
    """
    results = []
    with open(file_name, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for lineno, row in enumerate(reader, start=1):
            if query_value >= len(row) or fires_column >= len(row):
                raise IndexError(f"Column out of range at line {lineno}. Row has {len(row)} columns.")
            if row[query_value] == query_column:
                try:
                    results.append(int(row[fires_column]))
                except (TypeError, ValueError):
                    raise ValueError(f"Non-integer in fires_column at line {lineno}: {row[fires_column]!r}")
    return results

def mean(arr):
    if not arr:
        return None
    return sum(arr) / len(arr)

def median(arr):
    if not arr:
        return None
    s = sorted(arr)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]

def standard_deviation(arr):
    if not arr:
        return None
    m = mean(arr)
    var = sum((x - m) ** 2 for x in arr) / len(arr)
    return var ** 0.5
