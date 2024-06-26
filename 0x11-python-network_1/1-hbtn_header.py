#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL,
Displays the value of the X-Request-Id variable found in the header
of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(f"{x_request_id}")
