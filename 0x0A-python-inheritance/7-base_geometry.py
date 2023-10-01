#!/usr/bin/python3
"""
now we have two methods in the class
"""
class BaseGeometry:
 """ the class"""
    def area(self):
    """the first method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
    """the second method that raise error if name is not int """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

