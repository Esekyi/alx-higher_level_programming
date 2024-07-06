"""Python script, takes in a URL, sends a request
and displays the body of the response in utf-8
"""


if __name__ == "__main__":
    """
    Main Function
    Python script, takes in a URL, sends a request
    and displays the body of the response in utf-8
    """
    import urllib.request
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
