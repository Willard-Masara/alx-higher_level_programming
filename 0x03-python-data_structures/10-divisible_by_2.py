#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = divisible_by_2(numbers)
print(result)

