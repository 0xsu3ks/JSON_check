import json
import sys

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False

file_path = sys.argv[1]

try:
    with open(file_path, "r") as file:
        json_data = file.read()
        if is_valid_json(json_data):
            print("The JSON is valid.")
        else:
            print("The JSON is not valid.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")
