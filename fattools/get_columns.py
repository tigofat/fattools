import os
import sys
from argparse import ArgumentParser

from cool_printer import cool_printer
from tools import rows_to_columns


def parse_args():
	parser = ArgumentParser(description="")
	parser.add_argument("file_name", type=str, help="csv file name.")
	parser.add_argument("column_names", type=str, nargs="+", help="column or row names to get.")
	parser.add_argument("-sep", type=str, default=",", help="Separator.")

	return parser.parse_args()


def get_column(file_name, column_names, separator):

	assert os.path.isfile(file_name), f"{file_name} does not exist."

	with open(file_name, "r") as f:

		csv_column_names = f.readline().strip().split(separator)

		indices = []
		for name in column_names:
			try:
				indices.append(csv_column_names.index(name))
			except ValueError:
				raise Exception(f"'{name}' column does not exist.")

		value_rows = [[line.strip().split(separator)[i] for i in indices]
						for line in f.readlines()]

		rows = [column_names, *value_rows]
		columns = rows_to_columns(rows)

		cool_printer(columns)


if __name__ == "__main__":
	args = parse_args()
	get_column(args.file_name, args.column_names, args.sep)
