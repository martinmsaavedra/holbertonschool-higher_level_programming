#!/usr/bin/python3
'''network module'''
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) is 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    response = requests.post(url, data)
    try:
        if len(response.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response.json().
                                   get('id'), response.json().get('name')))
    except ValueError:
        print("Not a valid JSON")
