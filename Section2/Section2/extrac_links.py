#!/usr/bin/env python3
from html.parser import HTMLParser
import urllib.request

class pyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag == "a"):
            for a in attrs:
                if (a[0] == 'href'):
                    link = a[1]
                    if (link.find('http') >= 0):
                        print(link)
                        newParse = pyParser()
                        newParse.feed(link)
url = "http://youtube.com"
request = urllib.request.urlopen(url)
parser = pyParser()
parser.feed(request.read().decode('utf-8'))