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

def mean(arr):
    return sum(arr) / len(arr)

def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        return mid(sorted_arr)

def std(arr):
    m = mean(arr)
    variance = sum((x - m) ** 2 for x in arr) / len(arr)
    return variance ** 0.5
