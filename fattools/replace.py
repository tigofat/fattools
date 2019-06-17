import sys
from argparse import ArgumentParser

from get_columns import get_columns
from tools import get_rows_list, rows_to_columns
from cool_printer import cool_printer


def parse_args():
	parser = ArgumentParser(description="replace values in csv.")
	parser.add_argument("replace", type=str, help="item that will be replaced.")
	parser.add_argument("replace_with", type=str, help="item to replace with.")
	parser.add_argument("-sep", type=str, help="separator.", required=False)

	return parser.parse_args()


def replace(inpt, replace, replace_with, sep):

	rows_list = get_rows_list(inpt, sep)
	columns = rows_to_columns(rows_list)

	for i, column in enumerate(columns):
		for j in range(len(column)):
			if j == 0:
				continue
			columns[i][j] = columns[i][j].replace(replace, replace_with)

	return columns


if __name__ == "__main__":
	args = parse_args()
	columns = replace(sys.stdin, args.replace, args.replace_with, args.sep)
	cool_printer(columns)
