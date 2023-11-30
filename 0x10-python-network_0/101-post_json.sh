#!/bin/bash
# sends a JSON post TO A URL, disp the resp
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
