#!/usr/bin/python3


def inherits_from(obj, a_class):
    if issubclass(obj.__class__, a_class) == True:
        if isinstance(obj.__class__, a_class) == True:
            return False
    else:    
        return issubclass(obj.__class__, a_class)