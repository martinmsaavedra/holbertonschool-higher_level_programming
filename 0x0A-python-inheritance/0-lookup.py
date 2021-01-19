#!/usr/bin/python3
''' Module with lookup function'''


def lookup(obj):
    """
    Return list with dictionary of the class
    """
    return list(dir(obj))
