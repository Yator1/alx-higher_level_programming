#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
Print: Error code: followed by the value of the HTTP status code
"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    status = response.status_code

    if status >= 400:
        print(f"Error code: {status}")
    else:
        print(response.text)
