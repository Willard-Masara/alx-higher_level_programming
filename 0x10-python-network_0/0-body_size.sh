#!/bin/bash
# takes in a url, sends request there and displays body of resp
curl -s "$1" | wc -c
