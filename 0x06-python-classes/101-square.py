#!/usr/bin/python3
"""Square Class with area, print and str methods"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if len(position) == 2:
            if type(position[0]) != int\
               or type(position[1]) != int or type(position) != tuple:
                raise TypeError("position must be a tuple of \
                2 positive integers")
            if type(position[0]) is int and type(position[1]) is int:
                if int(position[0]) < 0 or int(position[1]) < 0:
                    raise TypeError("position must be a tuple of \
                    2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2:
            if value[0] < 0 or value[1] < 0 or type(value[0]) != int or\
               type(value[1]) != int or type(value) != tuple:
                raise TypeError("position must be a tuple of \
                2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def __str__(self):
        """Prints Square"""
        squa = ""
        for b in range(self.position[1]):
            squa += '\n'
        for i in range(self.__size):
            for a in range(self.position[0]):
                squa += " "
            for m in range(self.__size):
                squa += "#"
            if i < (self.__size - 1):
                squa += '\n'
        if self.__size == 0:
            squa = '\n'
        return squa
