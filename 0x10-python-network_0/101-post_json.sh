#!/bin/bash
# sends a JSON POST request with file content to a URL, displays response body
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
