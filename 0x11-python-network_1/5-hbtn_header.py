#!/usr/bin/python3
"""Python script, takes in a URL, sends
a request and displays the value of the X-Request-Id"""


if __name__ == "__main__":
    """
    Main Function
    Python script, takes in a URL, sends a request
    and displays the value of the X-Request-Id using requests
    package
    """
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
