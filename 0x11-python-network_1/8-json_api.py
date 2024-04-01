#!/usr/bin/python3
"""
A python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the given letter as a parameter and processes the response.
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        resp_json = response.json()

        if resp_json:
            if "id" in resp_json and "name" in resp_json:
                print(
                      "[{}] {}".format(
                          resp_json["id"], resp_json["name"])
                      )
            else:
                print("Not a valid JSON")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
    except Exception as err:
        print("Error:", err)
