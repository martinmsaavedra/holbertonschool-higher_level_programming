#!/usr/bin/python3
'''script that adds all arguments to a Python list,
and then save them to a file'''
import json
import sys
import os.path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = []
i = 0

filename = "add_item.json"
if os.path.exists(filename):
    data = load_from_json_file(filename)
    for ilem in data:
        args.append(ilem)

    for elem in sys.argv:
        if i is not 0:
            args.append(elem)
        i = + 1
    save_to_json_file(args, filename)

else:
    for elem in sys.argv:
        if i is not 0:
            args.append(elem)
        i = + 1

    save_to_json_file(args, filename)
