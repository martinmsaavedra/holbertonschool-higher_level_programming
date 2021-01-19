#!/usr/bin/python3
''' BaseGeometry class module'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Returns area of rectangle'''
        return super().area()

    def __str__(self):
        '''prints object description'''
        return super().__str__()
