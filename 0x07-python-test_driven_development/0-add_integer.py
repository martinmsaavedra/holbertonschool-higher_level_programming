#!/usr/bin/python3
"""TDD module"""


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
