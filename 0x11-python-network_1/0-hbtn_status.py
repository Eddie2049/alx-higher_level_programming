#!/usr/bin/python3
import urllib.request as req_

url_ = 'https://alx-intranet.hbtn.io/status'

with req_.request.urlopen(url_) as response:
    res_ = response.read().decode('utf-8')

print("- res_ response:")
print("\t- type:", type(res_))
print("\t- content:", res_)
