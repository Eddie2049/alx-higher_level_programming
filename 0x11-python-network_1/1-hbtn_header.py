#!/usr/bin/python3
"""
a Python script that takes in a URL, 
sends a request to the URL and displays the value 
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request as req_
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    re_ = req_.Request(url)
    with req_.urlopen(re_) as response:
        x_request_id = dict(response.headers).get("X-Request-Id")
        print(x_request_id)
