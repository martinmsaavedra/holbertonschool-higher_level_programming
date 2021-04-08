#!/usr/bin/python3
'''  finds a peak in a list of unsorted integers. '''
def find_peak(list_of_integers):
    ''' finds a peak in a list '''
    if not list_of_integers:
        return None
    if len(list_of_integers) == 2:
        return None
    for i in range(1, len(list_of_integers) - 1):
        numbers = list_of_integers[i]
        nei_1 = list_of_integers[i - 1]
        nei_2 = list_of_integers[i + 1]
        if numbers >= nei_1 and numbers >= nei_2:
            peak = numbers
    return numbers
