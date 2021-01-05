#!/usr/bin/python3
"""Square class with area and print"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Square constructor"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines size of square"""
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        """Prints Square"""
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
