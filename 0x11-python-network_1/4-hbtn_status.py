#!/usr/bin/python3
'''network module'''


import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\t- type: {}\t- content: {}'.
          format(type(response.text), response.text))
