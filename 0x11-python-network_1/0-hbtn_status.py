#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""


if __name__ == "__main__":
    import urllib.request

    """
    Main Function
    Python script that fetches https://alx-intranet.hbtn.io/status
    using the urllib package
    """
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
