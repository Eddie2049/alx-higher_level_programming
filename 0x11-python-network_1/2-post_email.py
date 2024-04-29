#!/usr/bin/python3
"""
 a Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys

if len(sys.argv) != 3:
    print("bug.. : python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# encode the email as a URL parameter
data_ = urllib.parse.urlencode({'email': email})
# encode the data as UTF-8
data_ = data_.encode('utf-8')

# send a POST request to the URL with the email parameter
with urllib.request.urlopen(url, data_) as response:
    # Read and decode the response body
    res_ = response.read().decode('utf-8')
    print(res_)
