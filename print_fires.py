#!/usr/bin/env python3
import argparse
import sys

from my_utils import get_column, mean, median, standard_deviation

def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter a CSV and optionally compute a statistic on the results."
    )
    parser.add_argument("--file_name", required=True, help="Path to the CSV file")
    parser.add_argument("--country", required=True, help="Query value for the country (string match)")
    parser.add_argument("--country_column", type=int, required=True, help="Zero-based column index for country")
    parser.add_argument("--fires_column", type=int, required=True, help="Zero-based column index for the numeric values")
    parser.add_argument(
        "--op",
        choices=["mean", "median", "std", "stdev", "standard-deviation", "standard_deviation"],
        help="Optional operation to perform on returned values"
    )
    return parser.parse_args()

def to_int_list(values):
    """Convert list of strings/ints to list of ints with a helpful error."""
    ints = []
    for i, v in enumerate(values):
        try:
            ints.append(int(v))
        except (TypeError, ValueError):
            raise ValueError(
                f"Non-integer value at position {i}: {v!r}. "
                "Ensure the fires column contains integers."
            )
    return ints

def main():
    args = parse_args()

    # Fetch the values using your util
    try:
        values = get_column(
            file_name=args.file_name,
            query_column=args.country,
            query_value=args.country_column,
            fires_column=args.fires_column,
        )
    except (FileNotFoundError, OSError, IndexError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    if args.op is None:
        # No operation requested: print values as before
        print(values)
        return

    # Map --op to the right function
    op = args.op
    if op in ("std", "stdev", "standard-deviation", "standard_deviation"):
        op_func = standard_deviation
        op_label = "standard_deviation"
    elif op == "mean":
        op_func = mean
        op_label = "mean"
    else:  # "median"
        op_func = median
        op_label = "median"

    # If get_column already returns ints this is a no-op; else convert
    try:
        int_values = to_int_list(values)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    result = op_func(int_values)
    print(f"{op_label} = {result}")

if __name__ == "__main__":
    main()
