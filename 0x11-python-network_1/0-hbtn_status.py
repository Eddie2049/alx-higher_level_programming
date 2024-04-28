#!/usr/bin/python3

import urllib.request as req_

url_ = 'https://alx-intranet.hbtn.io/status'

with req_.urlopen(url_) as response:
    res_ = response.read()
    utf8_content = res_.decode('utf-8')

print("Body response:")
print("\t- type:", type(res_))
print("\t- content:", res_)
print("\t- utf8 content:", utf8_content)
