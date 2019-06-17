import sys
from argparse import ArgumentParser

from cool_printer import cool_printer
from tools import rows_to_columns, get_rows_list


def parse_args():
	parser = ArgumentParser(description="apply an operation to a list of numbers.")
	parser.add_argument("expressions", nargs="+", help="expression list for every column. If one spesified it will be applied to all given columns.")
	parser.add_argument("-sep", default=",", help="separator.", required=False)

	return parser.parse_args()


def eval_oper(express, y):
	assert "x" in express, "The operation must contain x, like this '5*x + 1'"
	return eval(express, {"x": y})


def apply_oper(io_inpt, expressions, sep):

	rows = get_rows_list(io_inpt, sep)
	columns = rows_to_columns(rows)

	if len(expressions) < len(columns):
		expressions = [expressions[0] for _ in columns]

	for i, column in enumerate(columns):
		for j in range(len(column)):
			if j == 0:
				continue
			columns[i][j] = str(eval_oper(expressions[i], float(column[j])))

	return columns


if __name__ == "__main__":
	args = parse_args()
	columns = apply_oper(sys.stdin, args.expressions, args.sep)
	cool_printer(columns)
