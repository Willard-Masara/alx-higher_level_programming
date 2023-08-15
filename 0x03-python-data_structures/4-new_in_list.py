#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list.insert(idx, element)
    for val in my_list:
        if val < 0 or val >= len(my_list):
            return my_list[:]
    return my_list[:]


original_list = [10, 20, 30, 40, 50]
new_list = new_in_list(original_list, 2, 35)
print(original_list)
print(new_list) 

