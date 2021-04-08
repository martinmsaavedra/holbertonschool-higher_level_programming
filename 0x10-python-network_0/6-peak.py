#!/usr/bin/python3
'''  finds a peak in a list of unsorted integers. '''


def find_peak(list_of_integers):
    ''' finds a peak in a list '''
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    mid_size = int(len(list_of_integers) / 2)
    middle = list_of_integers[mid_size]
    if middle > list_of_integers[mid_size - 1]\
       and middle > list_of_integers[mid_size + 1]:
        return middle
    elif middle < list_of_integers[mid_size - 1]:
        return find_peak(list_of_integers[:mid_size])
    else:
        return find_peak(list_of_integers[mid_size + 1:])
