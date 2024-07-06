#!/usr/bin/python3
"""Python script, takes in a URL and email, sends
a POST request and displays the body of the response in utf-8"""


if __name__ == "__main__":
    """
    Main Function
    Python script, takes in a URL and email, sends a POST request
    and displays the body of the response in utf-8
    """
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url=url, data={'email': email})
    print(response.text)
