#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(0, 2):
       for j in range(0, 2):
            if i == j:
                new_tuple += tuple_a[i] + tuple_b[j]
    return new_tuple
