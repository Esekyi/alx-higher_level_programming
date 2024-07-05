#!/bin/bash
# bash script that makes a request to a sandbox url, causes the server to respond with a message, "	You got me!"
curl -sL -X PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: School"