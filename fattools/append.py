from argparse import ArgumentParser

from get_columns import get_columns
from tools import get_rows_list, rows_to_columns
from cool_printer import cool_printer


def parse_args():
	parser = ArgumentParser(description="append one csv to another csv.")
	parser.add_argument("csv_files_names", type=str, nargs="+", help="list of csv files' name.")
	parser.add_argument("-sep", type=str, default=',', help="sperator.")

	return parser.parse_args()


def replace(csv_files_names, sep):
	files_columns = [get_columns(f_name, None, sep) for f_name in csv_files_names]

	columns = []
	for i, column in enumerate(files_columns):
		columns.extend(column)

	return columns


if __name__ == "__main__":
	args = parse_args()
	columns = replace(args.csv_files_names, args.sep)
	cool_printer(columns)
