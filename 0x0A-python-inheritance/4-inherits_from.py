#!/usr/bin/python3
"""
to check is the obj inherits from subclass
"""
def inherits_from(obj, a_class):
	"""the use of the fucntion subclass, crucial """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
