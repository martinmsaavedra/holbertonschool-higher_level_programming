#!/usr/bin/python3


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Square constructor"""
        try:
            int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
            self.__position = position
        except TypeError:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Defines position of square"""
        try:
            int(value[0])
            int(value[1])
            if value[0] < 0 or value[1] < 0:
                raise Error("Negative value")
        except (TypeError, ValueError, Error):
            raise TypeError("position must be a tuple of 2 positive integers")

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
        try:
            int(value)
        except:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints Square"""
        for b in range(self.position[1]):
            print()
        for m in range(self.__size):
            for a in range(self.position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
