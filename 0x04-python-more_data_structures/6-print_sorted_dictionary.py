#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for par in sorted(a_dictionary):
        print("{}: {}".format(par, a_dictionary.get(par)))
