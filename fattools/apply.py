import sys
from argparse import ArgumentParser

from cool_printer import cool_printer
from tools import rows_to_columns


def parse_args():
	parser = ArgumentParser(description="apply an operation to a list of numbers.")
	parser.add_argument("expressions", nargs="+", help="expression list for every column. If one spesified it will be applied to all given columns.")
	parser.add_argument("-sep", default=",", help="separator.", required=False)

	return parser.parse_args()


def eval_oper(express, y):
	assert "x" in express, "The operation must contain x, like this '5*x + 1'"
	return eval(express, {"x": y})


def apply(inpt, expressions, sep):

	output = []
	rows = [rows.strip().split(sep) for rows in inpt.readlines()]
	columns = rows_to_columns(rows)

	if len(expressions) < len(columns):
		expressions = [expressions[0] for _ in columns]

	output = []
	for i, column in enumerate(columns):
		#print([datum for datum in column[1:]])
		values = [str(eval_oper(expressions[i], float(datum))) for datum in column[1:]]
		output.append([column[0], *values])

	cool_printer(output)


if __name__ == "__main__":
	args = parse_args()
	apply(sys.stdin, args.expressions, args.sep)
