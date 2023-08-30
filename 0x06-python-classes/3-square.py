#!/usr/bin/python3
""" task 3-square.py"""


class Square:
    """fr the sqaure"""

    def __init__(self, size=0):
        """initialisation of the attreibutes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """fore the area of the sqaure"""
        return self.__size ** 2
