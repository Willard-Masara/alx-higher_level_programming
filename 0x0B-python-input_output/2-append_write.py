#!/usr/bin/python3
"""task 2 appending to the file"""

def append_write(filename="", text=""):
	"""these are the basics of file input"""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            num_characters_added = file.write(text)
            return num_characters_added
    except Exception as e:
        print(f"Error appending to file '{filename}': {e}")
        return 0
