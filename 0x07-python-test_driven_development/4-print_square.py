#!/usr/bin/python3
"""Print Square Module"""


def print_square(size):
    """
    Prints the Square of length size with the character #
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size >= 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    else:
        raise ValueError("size must be >= 0")