#!/usr/bin/env python3
import requests
from requests.auth import HTTPDigestAuth

url = 'http://httpbin.org/digest-auth/auth/user/pass'

resource = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
print('Response.status_code:' + str(resource.status_code))
if resource.status_code == 200:
    print('Login successful: '+str(resource.json()))