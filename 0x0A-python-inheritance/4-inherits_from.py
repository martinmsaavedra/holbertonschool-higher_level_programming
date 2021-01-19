#!/usr/bin/python3
'''inhertis_from module'''


def inherits_from(obj, a_class):
    '''inherits_from function'''

    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
