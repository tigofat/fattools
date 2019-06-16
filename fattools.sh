#!/bin/bash

# get the running file dir
running_file_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ -z "$1" ]; then
	config_json_name=$running_file_path"/fat_config.json"
else
	config_json_name=$1
fi

function get_json_value() {
	echo $(python3 -c "
import json
with open('$config_json_name') as file:
	print(json.load(file)[$1])")
}

python_inter_name=$(get_json_value "'python_interpreter_name'")
source_code_path=$(get_json_value "'source_code_path'")

alias get_columns="$python_inter_name $source_code_path'/get_columns.py'"
alias apply="$python_inter_name $source_code_path'/apply.py'"
echo "Welcome to fattools."
