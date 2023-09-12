#!/usr/bin/python3

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    # Check if add_item.json exists, and load its content if it does.
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    # Add command-line arguments to the list.
    arguments = sys.argv[1:]
    existing_list.extend(arguments)

    # Save the updated list to add_item.json.
    save_to_json_file(existing_list, "add_item.json")

if __name__ == "__main__":
    main()
