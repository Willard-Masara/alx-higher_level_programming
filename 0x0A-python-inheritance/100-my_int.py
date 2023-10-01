#!/usr/bin/python3
"""
a bit of trickey here, customising the behaviour of operators
"""
class MyInt(int):
    def __eq__(self, other):
        """Override the equality operator (==) to return the opposite result"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to return the opposite result"""
        return super().__eq__(other)
