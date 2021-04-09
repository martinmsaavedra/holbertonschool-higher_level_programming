#!/usr/bin/python3
'''network module'''
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    response = requests.get(url)
    list_commits = response.json()
    for index, elem in enumerate(list_commits):
        if index <= 9:
            sha = elem.get('sha')
            name = elem.get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
        else:
            break
