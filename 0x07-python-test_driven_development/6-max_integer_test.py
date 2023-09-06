#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """the task is to find the max int among a list of ints"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
