import sys
from argparse import ArgumentParser

from tools import get_rows_list, rows_to_columns
from cool_printer import cool_printer


def parse_args():
	parser = ArgumentParser(description="pop column from csv.")
	parser.add_argument("columns_names", type=str, nargs="+", help="column name to pop.")
	parser.add_argument("-sep", type=str, default=',', help="sperator.")

	return parser.parse_args()


def drop(io_input, columns_names, sep):

	rows_list = get_rows_list(io_input, sep)
	columns = rows_to_columns(rows_list)

	return [column for i, column in enumerate(columns) if not column[0] in columns_names]


if __name__ == "__main__":
	args = parse_args()
	columns = drop(sys.stdin, args.columns_names, args.sep)
	cool_printer(columns)
