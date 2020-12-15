#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    lists = []
    for i in range(0,2):
        a = tuple_a[i] if len(tuple_a) < 2 else 0
        b = tuple_b[i] if len(tuple_b) < 2 else 0
        x = a + b;
        lists.append(x);
    new_tuple = tuple(lists)
    return new_tuple
