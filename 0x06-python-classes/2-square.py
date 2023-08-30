#!/usr/bin/python3
"""Continuing with 1-square.py"""


class Square:
    """for the class square"""

    def __init__(self, size=0):
        """ this is to initialsie a square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
