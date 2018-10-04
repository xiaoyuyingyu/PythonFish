import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get',timeout=10)
print(response.read())