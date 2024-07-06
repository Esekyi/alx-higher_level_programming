#!/usr/bin/python3
"""Python script, takes in a URL, sends a request
and displays the body of the response in utf-8"""


if __name__ == "__main__":
    """
    Main Function
    Python script, takes in a URL, sends a request
    and displays the body of the response in utf-8
    """
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
