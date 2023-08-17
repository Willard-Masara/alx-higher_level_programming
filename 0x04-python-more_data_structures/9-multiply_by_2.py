#!/usr/bin/python3
# task 9


def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()

    new_values = list(map(lambda x: x * 2, new_dir.values()))
    new_keys = list(new_dir.keys())
    
    for i in range(len(new_keys)):
        new_dir[new_keys[i]] = new_values[i]

    return new_dir
