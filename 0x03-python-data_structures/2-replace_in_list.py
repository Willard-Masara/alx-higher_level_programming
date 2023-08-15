#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

my_list = [10, 20, 30, 40, 50]
replace_in_list(my_list, 2, 35)
print(my_list)  
