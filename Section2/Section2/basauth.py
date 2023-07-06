#!/usr/bin/env python3
import requests

from requests.auth import HTTPBasicAuth

requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'password'))

response = requests.get('https://api.github.com/user', auth=('user', 'password'))

print('Response.status_code:'+ str(response.status_code))
if response.status_code ==200:
    print('Login successfull: ' + response.text)