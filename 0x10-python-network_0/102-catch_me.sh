#!/bin/bash
# makes a request to "0.0.0.0:5000/catch_me" causing the server to respond "You got me!"
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool" | sed -n '/You got me!/,$p'
