def rows_to_columns(data):
	columns = [[] for _ in range(len(data[0]))]
	for row in data:
		for i, datum in enumerate(row):
			columns[i].append(datum)

	return columns
