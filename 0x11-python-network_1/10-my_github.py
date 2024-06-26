#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(
            url, auth=(username, access_token)
            )
        if response.status_code == 200:
            data = response.json()
            user_id = data["id"]
            print(f"{user_id}")
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
