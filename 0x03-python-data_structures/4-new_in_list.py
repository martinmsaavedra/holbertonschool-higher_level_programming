#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcp = list.copy(my_list)
    if idx < 0:
        return listcp
    elif idx > len(my_list) - 1:
        return listcp
    else:
        listcp[idx] = element
        return listcp
