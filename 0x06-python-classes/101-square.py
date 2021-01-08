#!/usr/bin/python3
"""Define a Square Class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position
        self.__size = size

    def __str__(self):
        """print an square"""
        string = ""
        if self.__size > 0:
            for x in range(self.__position[1]):
                string += "\n"
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    string += " "
                for j in range(self.__size):
                    string += "#"
                if i < self.__size - 1:
                    string += "\n"
        return string

    def area(self):
        """Method to calculate the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns size of square"""
        return self.__size

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @size.setter
    def size(self, value=0):
        """Defines size of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Defines position of square"""
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def my_print(self):
        """print an square"""
        if self.__size == 0:
            print()
            return
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i < self.__size - 1:
                print()
