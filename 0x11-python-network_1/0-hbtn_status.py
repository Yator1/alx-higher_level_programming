#!/usr/bin/python3

"""
This module consists a script that
fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as resp:
        body = resp.read()

        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode("utf-8")))
