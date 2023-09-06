#!/usr/bin/python3
"""this is task 0"""

def add_integer(a, b=98):
    """Check if a and b are integers or floats"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    """Cast a and b to integers if they are floats"""
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    """Perform the addition and return the result as an integer"""
    result = a + b
    return int(result)
