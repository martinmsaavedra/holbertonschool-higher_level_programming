#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl 35.231.45.150:5000 -sI | grep "Content-Length" | cut -d " " -f2
