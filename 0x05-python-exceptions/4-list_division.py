#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    print("wrong type")
                    result_list.append(0)
                elif my_list_2[i] == 0:
                    print("division by 0")
                    result_list.append(0)
                else:
                    result_list.append(my_list_1[i] / my_list_2[i])
            except IndexError:
                print("out of range")
                result_list.append(0)
    except TypeError:
        print("out of range")
    finally:
        return (result_list)
