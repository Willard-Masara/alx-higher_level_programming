#!/usr/bin/python3
"""after opening the file we write to it"""


def write_file(filename="", text=""):
    """open the file with write permissions"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
