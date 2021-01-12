#!/usr/bin/python3
"""TDD Module"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if type(text) == str:
        for letter in text:
            if letter == "." or letter == "?" or letter == ":":
                print(letter, end="")
                print("\n")
            else:
                print(letter, end="")
    else:
        raise TypeError("text must be a string")
