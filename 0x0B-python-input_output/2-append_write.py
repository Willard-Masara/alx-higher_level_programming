#!/usr/bin/python3
"""now we append to the file"""


def append_write(filename="", text=""):
    """this is how to append"""
     with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
