#!/bin/bash
# bash script that sends a post request to a URL and displays the reponse in the body.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
