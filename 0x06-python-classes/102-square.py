#!/usr/bin/python3
"""Square with area and size setter"""


class Square:
    """Square class"""
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

    @property
    def size(self):
        """Returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines size of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __gt__(self, Square):
        """compare object if is greater than"""
        return self.area() > Square.area()

    def __lt__(self, Square):
        """compare object if is less than"""
        return self.area() < Square.area()

    def __ge__(self, Square):
        """compare object if is greater or equal than"""
        return self.area() >= Square.area()

    def __le__(self, Square):
        """compare object if is lower or equal than"""
        return self.area() <= Square.area()

    def __eq__(self, Square):
        """compare object if is equal than"""
        return self.area() == Square.area()

    def __ne__(self, Square):
        """compare object if is not equal than"""
        return self.area() != Square.area()
