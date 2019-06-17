from argparse import ArgumentParser

from get_columns import get_columns
from tools import get_rows_list, rows_to_columns
from cool_printer import cool_printer


def parse_args():
	parser = ArgumentParser(description="append one csv to another csv.")
	parser.add_argument("append_to", type=str, help="csv to append to(or csv to append with depending if a stream comes to a file ('sys.stdin' is empty)).")
	parser.add_argument("append_with", type=str, help="csv to append with.")
	parser.add_argument("-sep", type=str, default=',', help="sperator.")

	return parser.parse_args()


def replace(append_to, append_with, sep):
	append_to_columns = get_columns(append_to, None, sep)
	append_with_columns = get_columns(append_with, None, sep)

	for i, append_with in enumerate(append_with_columns):
		append_to_columns[i].extend(append_with[1:])

	return append_to_columns


if __name__ == "__main__":
	args = parse_args()
	columns = replace(args.append_to, args.append_with, args.sep)
	cool_printer(columns)
