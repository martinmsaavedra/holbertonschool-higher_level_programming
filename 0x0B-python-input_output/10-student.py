#!/usr/bin/python3
"""Module Documentation"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Constructor method"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Json function"""
        if attrs is not None:
            new_dict = {}
            for obj in attrs:
                if type(obj) != str:
                    return self.__dict__
            for obj in attrs:
                if obj in self.__dict__:
                    new_dict[obj] = self.__dict__[obj]
            return new_dict
        else:
            return self.__dict__
