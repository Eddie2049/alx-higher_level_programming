#!/usr/bin/python3
import urllib.request as req_
import sys

url = sys.argv[1]

with req_.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
