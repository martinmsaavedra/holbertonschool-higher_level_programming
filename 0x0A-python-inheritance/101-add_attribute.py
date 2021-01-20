#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible"""


def add_attribute(object, name, value):
    """Adds a new attribute"""
    if not hasattr(object, 'name'):
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
