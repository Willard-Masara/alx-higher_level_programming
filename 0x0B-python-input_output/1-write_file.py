#!/usr/bin/python3
""" this is taks 1"""

def write_file(filename="", text=""):
	"""opeing with write permissions"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            num_characters_written = file.write(text)
            return num_characters_written
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")
        return 0
