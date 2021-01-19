#!/usr/bin/python3


def inherits_from(obj, a_class):
    if obj.__class__ == a_class:
        return False
    else:
        return True
