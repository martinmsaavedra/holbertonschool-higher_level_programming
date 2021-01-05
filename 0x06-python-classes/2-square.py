#!/usr/bin/python3

class Square:
    """Square class"""
    def __init__(self, size=0):
        """Square constructor"""
        try:
            int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
