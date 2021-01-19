#!/usr/bin/python3
''' module with Mylist class'''


class MyList(list):
    '''MyList Class'''

    def print_sorted(self):
        ''' print and sort the list'''
        print(sorted(self))
