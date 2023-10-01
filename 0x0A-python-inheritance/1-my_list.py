#!/usr/bin/python3
"""
this task is about inheriting from another class
"""

class MyList(list):
	"""now here we are initializing the class MyList first"""
    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
    """the crucial part of sorting out the list"""
        sorted_list = sorted(self)
        print(sorted_list)
