#!/usr/bin/python3
# task 3


def new_in_list(my_list, idx, element):
    my_list.insert(idx, element)
    for val in my_list:
        if val < 0 or val >= len(my_list):
            return my_list[:]
    return my_list[:]
