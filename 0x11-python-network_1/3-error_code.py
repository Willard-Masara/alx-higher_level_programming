#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}"
