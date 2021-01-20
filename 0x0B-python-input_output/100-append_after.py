#!/usr/bin/python3
'''after party module'''


def append_after(filename="", search_string="", new_string=""):
    '''function that inserts a line of text to a file, after
    each line containing a specific string'''

    input_file = open(filename, mode='r').readlines()
    with open(filename, mode="w") as f:
        for line in input_file:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.close()
