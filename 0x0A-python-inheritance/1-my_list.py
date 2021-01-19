#!/usr/bin/python3
''' module with Mylist class'''


class MyList(list):
    def print_sorted(self):
        ''' print and sort the list'''
        print(sorted(self))
