"""Python script, takes in a URL and email, sends
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