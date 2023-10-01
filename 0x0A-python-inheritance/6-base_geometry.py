#!/usr/bin/python3
"""
this task brings back try except raise exception
"""
class BaseGeometry:
	"""this is the base class"""
    def area(self):
    """raise exception with message area not implemented if area() not used"""
        raise Exception("area() is not implemented")

