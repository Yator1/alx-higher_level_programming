#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
It manage urllib.error.HTTPError exceptions and print: Error code: the code
"""


import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))