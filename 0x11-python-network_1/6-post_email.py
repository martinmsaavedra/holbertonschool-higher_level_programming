#!/usr/bin/python3
'''network module'''
import sys
import requests


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    url = sys.argv[1]
    response = requests.post(url, data)
    print(response.text)
