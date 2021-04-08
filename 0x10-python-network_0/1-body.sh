#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ $(curl -s -o /dev/null -I -w "%{http_code}" $1) -eq "200" ]; then curl $1; fi
