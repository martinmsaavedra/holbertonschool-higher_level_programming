#!/usr/bin/python3
''' BaseGeometry class module'''

BaseGeometry = __import__('6-base_geometry').BaseGeometry

class BaseGeometry:
    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
