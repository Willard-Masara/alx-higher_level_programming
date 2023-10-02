#!/usr/bin/python3
""" Defines an object atribute function """

def lookup(obj):
	""" this function returns the attributes of the object"""
    check = dir(obj)
    return check
