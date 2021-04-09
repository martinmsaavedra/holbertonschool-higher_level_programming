#!/usr/bin/python3
'''network module'''
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status')as response:
    html = response.read().decode('utf-8')
print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(html), html))
