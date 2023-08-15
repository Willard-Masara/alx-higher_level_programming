#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list

original_list = [10, 20, 30, 40, 50]
new_list = delete_at(original_list, 2)
print(original_list)
print(new_list)

