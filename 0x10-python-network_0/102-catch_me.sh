#!/bin/bash
# Make a request to cause the server to respond with "You got me!"
curl -s -X PUT -L --data "user_id=98" 0.0.0.0:5000/catch_me

