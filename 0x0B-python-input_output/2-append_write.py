#!/usr/bin/python3
'''write and append a text in a file module'''


def append_write(filename="", text=""):
    '''Write a function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added'''
    with open(filename, mode="a", encoding="utf-8") as f:
        lenght = f.write(text)
    return lenght
