#!/usr/bin/python3
# task 13


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    lines = []
    with op   lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines[i:i + 1] = [lines[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
