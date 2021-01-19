#!/usr/bin/python3
''' BaseGeometry class module'''

BaseGeometry = __import__('9-rectangle.py').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class'''

    def __init__(self, width, height):
        '''Constructor function'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Returns area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''prints object description'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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
