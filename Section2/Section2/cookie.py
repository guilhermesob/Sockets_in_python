import http.cookiejar
import urllib
import urllib.request

URL = input("Write a URL: ")
def extract():
    cookie_j = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_j))
    resp = opener.open(URL)
    for cookie in cookie_j:
        print("Cookie: %s --> %s" % (cookie.name, cookie.value))
    print("Headers: %s" % resp.headers)

if __name__ == "__main__":
    extract()