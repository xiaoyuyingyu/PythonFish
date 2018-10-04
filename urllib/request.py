import urllib.request
from urllib import request,parse
request = urllib.request.Request('https://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))