def get_column(file_name, query_column, query_value, result_column):
    f = open(file_name,'r', encoding="utf-8")
    results = []
    for line in f:
        line = line.strip()
        row = line.split(',')
        if row[query_value] == query_column:
            results.append(row[result_column])
        else:
            results.append(1)
    f.close()
    return results
