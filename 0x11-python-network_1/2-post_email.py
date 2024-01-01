#!/user/bin/python3
"""
this script sends a POST request, aslo displays the body of response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as resp:
        body = resp.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)

