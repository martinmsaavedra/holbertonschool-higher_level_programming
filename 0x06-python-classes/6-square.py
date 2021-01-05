#!/usr/bin/python3
"""Square class with area, print and str methods"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Square constructor"""
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Defines position of square"""
        if type(position) != tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    def my_print(self):
        """Prints Square"""
        if self.__size == 0:
            print()
        else:
            for b in range(self.position[1]):
                print()
            for m in range(self.__size):
                for a in range(self.position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
