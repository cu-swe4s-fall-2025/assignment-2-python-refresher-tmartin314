import csv

def get_column(file_name, query_column, query_value, result_column):
    f = open(file_name,'r', encoding="utf-8")
    results = []
    for line in f:
        line = line.strip()
        row = line.split(',')
        if line[query_column] == query_value:
            results.append(row[result_column])
    f.close()
    return results
