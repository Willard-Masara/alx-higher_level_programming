#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    status_code = response.status_code

    if status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {status_code}")

