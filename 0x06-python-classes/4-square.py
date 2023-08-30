#!/usr/bin/python3
"""tssk 4-square.py"""


class Square:
    def __init__(self, size=0):
        self.size = size  # Use the setter method to set the size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
