#!/usr/bin/python3
"""
Python script, takes in a URL and email, sends
a POST request and displays the body of the response in utf-8
"""


if __name__ == "__main__":
    """
    Main Function
    Python script, takes in a URL and email, sends a POST request
    and displays the body of the response in utf-8
    """
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data.encode('ascii')
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        # print(html.decode('utf-8'))
        print("Your email is: {}".format(values['email']))
