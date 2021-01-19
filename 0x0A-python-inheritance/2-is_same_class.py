#!/usr/bin/python3
''' module with is_same_class function'''


def is_same_class(obj, a_class):
    """ Returns  True if object is exactly an instance of the specified class
    otherwise returns False """
    if obj.__class__ == a_class:
        return True
    else:
        return False
