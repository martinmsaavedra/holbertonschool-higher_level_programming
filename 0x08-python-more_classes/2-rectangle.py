#!/usr/bin/python3
"""Module about Rectangle Class"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Init constructor"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Width Getter
        """
        return self.__width

    @property
    def height(self):
        """Height Getter
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Width Setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height Setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculates area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculates perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))
