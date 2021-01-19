#!/usr/bin/python3
''' BaseGeometry class module'''


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        '''return area of geometry'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
        return ("[Square] {}/{}".format(self.__size, self.__size))
