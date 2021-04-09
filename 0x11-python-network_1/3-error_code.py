#!/usr/bin/python3
'''network modules'''
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
        print(html)
    except urllib.error.HTTPError as e:
        print("Error code:", str(e.code))
