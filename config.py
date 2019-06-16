#!/usr/bin/env python3

import json
from argparse import ArgumentParser


def parse_args():
	parser = ArgumentParser(description="Configure 'fat_config.json' file.")
	parser.add_argument("python_inter_name", type=str, help="Python interpreter name.")
	parser.add_argument("source_code_path", type=str, help="fattools tools source code path.")

	return parser.parse_args()


def config(python_int, source_path):

	with open("fat_config.json", "r") as config_json:
		config_dict = json.loads(config_json.read())
		config_dict["python_interpreter_name"] = python_int
		config_dict["source_code_path"] = source_path

	with open("fat_config.json", "w", encoding="utf-8") as config_file:
		json.dump(config_dict, config_file, indent=4)


if __name__ == "__main__":
	args = parse_args()
	config(args.python_inter_name, args.source_code_path)
