#!/usr/bin/python3
'''network module'''
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status')as response:
   html = response.read()
print("Body response:\n\t- type: {}\n\t- content: {}\n\t -utf8 content: {}".format(type(html), html, html.decode()))
