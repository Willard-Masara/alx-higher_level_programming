#!/usr/bin/ptyhon3
# task 6


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    
    for key in sorted_keys:
        print(key, ":", a_dictionary[key])

