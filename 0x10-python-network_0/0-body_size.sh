#!/bin/bash
# bash script that takes in a URL, sends a request to that URL, and displays the size of the body in the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f 2
