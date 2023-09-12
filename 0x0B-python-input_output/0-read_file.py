#!/usr/bin/python3
# this is task 0


def read_file(filename=""):
	"""oepning a file in pythin"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
