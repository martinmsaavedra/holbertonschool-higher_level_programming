#!/usr/bin/python3
'''network module'''
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    info = response.getheader('X-Request-Id')
print(info)
