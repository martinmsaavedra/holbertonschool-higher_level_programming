#!/usr/bin/python3

class Square:
    """Square class"""
    def __init__(self, size):
        """Square constructor"""
        try:
            int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns area of square"""
        return  self.__size * self.__size

    @property
    def size(self):
        """Returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines size of square"""
        try:
            int(value)
        except:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
