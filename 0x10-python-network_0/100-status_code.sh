#!/bin/bash
#sends a request to a URL passed as an argument, and displays only the status code of the response
if [ $(curl -s -o /dev/null -I -w "%{http_code}" $1) -eq "200" ]; then curl $1; fi
