#!/usr/bin/python3
'''network module'''


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        http = response.getheader('X-Request-Id')
    print(http)
