#!/usr/bin/python3
"""
A python script that takes a URL, sends a request to the URL and,
Displays the value of the variable X-Request-Id in the response header
"""


import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException as err:
        print("Error:", err)
