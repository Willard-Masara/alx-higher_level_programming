#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_value = my_list[0]
    for number in my_list:
        if number > max_value:
            max_value = number

    return max_value

numbers = [10, 5, 25, 8, 30]
result = max_integer(numbers)
print(result)

empty_list = []
result_empty = max_integer(empty_list)
print(result_empty)

