import sys


def fill_all(data, maxes):
	for row in zip(*data):
		print(','.join(row))


def fill_all_struct(data, maxes):
	for row in zip(*data):
		for i, datum in enumerate(row):
			left_spaces = ' ' * (maxes[i] - len(datum))
			min_left_spaces = "  "
			print(f"{left_spaces}{datum}", end=min_left_spaces)
		print()


def fill_shortened_struct(data, maxes):
	if len(data[0]) <= 100:
		fill_all(data)
		return

	shortened_data = [[*column[:15], '...', *column[-15:]] for column in data]

	fill_all_struct(shortened_data, maxes)


def select_mode():
	return {
		True: fill_shortened_struct,
		False: fill_all
	}.get(sys.stdout.isatty())


def cool_printer(columns):
	if len(columns) == 0:
		return

	printer_func = select_mode()
	maxes = [len(max(column, key=lambda x: len(x)))
			for column in columns]
	printer_func(columns, maxes)
