#!/usr/bin/python3
"""this is task 0-- opening a file"""


def read_file(filename=""):
    """use resad to print file output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
