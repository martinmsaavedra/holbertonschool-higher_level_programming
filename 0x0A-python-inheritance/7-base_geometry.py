#!/usr/bin/python3
''' BaseGeometry class module'''


if __name__ == "__main__":
    """Test cases"""
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")


class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''return area of geometry'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
