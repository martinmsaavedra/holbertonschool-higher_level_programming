#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""

import json
import sys
import os.path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = []
i = 0
for x in sys.argv:
    if i is not 0:
        my_list.append(x)
    i += 1
filename = "add_item.json"
try:
    data = load_from_json_file(filename)
    my_list = data + my_list
except:
    save_to_json_file(my_list, filename)
else:
    save_to_json_file(my_list, filename)