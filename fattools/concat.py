import sys
from argparse import ArgumentParser

from get_columns import get_columns
from cool_printer import cool_printer


def parse_args():
	parser = ArgumentParser(description="concatenate two files.")
	parser.add_argument("file_names", type=str, help="csv file columns columns", nargs="+")
	parser.add_argument("-sep", type=str, help="seperator", default=",", required=False)

	return parser.parse_args()


def concat(file_names, sep):

	concat_columns = []
	for f_name in file_names:
		columns = get_columns(f_name, None, sep)
		concat_columns.extend(columns)

	return concat_columns


if __name__ == "__main__":
	args = parse_args()
	columns = concat(args.file_names, args.sep)
	cool_printer(columns)
