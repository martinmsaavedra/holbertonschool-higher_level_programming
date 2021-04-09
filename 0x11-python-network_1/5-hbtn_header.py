#!/usr/bin/python3
'''network module'''
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get['x-request-id'])
