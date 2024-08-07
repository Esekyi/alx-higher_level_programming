#!/usr/bin/python3
"""Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


if __name__ == "__main__":
    """
    Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
    """
    import requests
    import sys
    letter = sys.argv[1]
    response = requests.post(
        url='http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get(
                'id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
