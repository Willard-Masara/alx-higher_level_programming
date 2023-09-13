#!/usr/bin/python3
""" this is task 5 on the json file"""
import json


def save_to_json_file(my_obj, filename):
    """writing to json rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
