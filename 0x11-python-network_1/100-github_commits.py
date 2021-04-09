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
    for elem in list_commits:
        sha = elem.get('parents')[0].get('sha')
        name = elem.get('commit').get('author').get('name')
        print(sha, name)
