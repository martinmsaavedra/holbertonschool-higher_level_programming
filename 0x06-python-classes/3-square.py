#!/usr/bin/python3
"""Square with area method"""


class Square:
    """"Square class"""
    def __init__(self, size=0):
        """Square constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size
