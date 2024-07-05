#!/bin/bash
# bash script, sends a request to given URL and displays the status code of its response
curl -s -o /dev/null -w "%{http_code}" "$1"
