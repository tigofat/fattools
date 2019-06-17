import os
import sys
from argparse import ArgumentParser

from cool_printer import cool_printer
from tools import rows_to_columns


def parse_args():
	parser = ArgumentParser(description="")
	parser.add_argument("file_name", type=str, help="csv file name.")
	parser.add_argument("-c", "--columns", type=str, nargs="+", help="columns' names to get.", required=False)
	parser.add_argument("-sep", type=str, default=",", help="separator.", required=False)

	return parser.parse_args()


def get_columns(file_name, column_names, separator):

	assert os.path.isfile(file_name), f"{file_name} does not exist."

	with open(file_name, "r") as f:

		csv_column_names = f.readline().strip().split(separator)

		if not column_names: column_names = csv_column_names

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

		return columns


if __name__ == "__main__":
	args = parse_args()
	columns = get_columns(args.file_name, args.columns, args.sep)
	cool_printer(columns)
