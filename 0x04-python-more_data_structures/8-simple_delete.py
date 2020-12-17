#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dic = a_dictionary
    new_dic.pop(key, None)
    return new_dic
