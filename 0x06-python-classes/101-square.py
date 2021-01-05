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
            if i < self.__size -1:
                squa += '\n'
        if self.__size == 0:
            squa = '\n'
        return squa
