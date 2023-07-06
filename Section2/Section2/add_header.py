#!/usr/bin/env python3
from urllib.request import Request

USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20'
URL = 'http://youtube.com'

def add_header():
    headers = {'Accept-Language': 'n1', 'User-agent': USER_AGENT}
    request = Request(URL, headers=headers)
    print("Request headers: ")
    for key, value in request.header_items():
        print ("%s: %s" %(key, value))

if __name__ == '__main__':
    add_header()