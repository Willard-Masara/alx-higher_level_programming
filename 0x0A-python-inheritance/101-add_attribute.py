#!/usr/bin/python3
"""
this task is about replacing try,except
"""

def add_attribute(obj, attr_name, attr_value):
	"""these fucntions are powerful, this hasattr and setattr"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
