#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    lists = []
    for i in range(0, 2):
        if len(tuple_a) < 2:
            a = 0
        else:
            a = tuple_a[i]
        if len(tuple_b) < 2:
            b = 0
        else:
            b = tuple_b[i]
        x = a + b
        lists.append(x)
    new_tuple = tuple(lists)
    return new_tuple
