#!/usr/bin/python3
'''JSON module'''
import json


def load_from_json_file(filename):
    '''function that creates an Object from a “JSON file”'''
    with open(filename) as f:
        data = json.load(f)
    return data
