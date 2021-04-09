#!/usr/bin/python3
'''network module'''
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    info = dict(response.info())
print(info['X-Request-Id'])
