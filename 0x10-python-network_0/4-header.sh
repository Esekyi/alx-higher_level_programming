#!/bin/bash
# bash script written to display the body of the response of a request to a given URL
curl -s "$1" -X GET -H "X-School-User-Id: 98"
