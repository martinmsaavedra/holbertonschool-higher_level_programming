#!/usr/bin/python3
'''network module'''
import sys
import urllib.request
from urllib import parse


if __name__ == "__main__":
    args = {'email': sys.argv[2]}
    data = parse.urlencode(args).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        html = response.read().decode('utf-8')
    print(html)
