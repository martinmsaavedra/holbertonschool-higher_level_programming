#!/usr/bin/pyhton3
def complex_delete(a_dictionary, value):
    for key, value2 in list(a_dictionary.items()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
