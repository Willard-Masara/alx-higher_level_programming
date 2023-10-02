#!/usr/bin/python3
"""
to demonstrate if its an instance of a clss
"""

def is_same_class(obj, a_class):
	"""isinstance should be followed by parenthesis!"""
    if isinstance(obj, a_class):
    """return true in that case or false as may be"""
        return True
    else:
        return False
