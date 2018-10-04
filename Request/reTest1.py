import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789') # 设置了一个cookie
resp = s.get('http://httpbin.org/cookies')
print(resp.text)
'''
import json

response = requests.get('http://httpbin.org/get')
print(response.text)
print(response.json())
print(json.load(response.text))
print(type(response.json()))
'''

'''
data = {
    'name' : 'Jack',
    'age' : 20
}
response = requests.get('http://httpbin.org/get',params=data)

print(response.text)

'''

'''
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
'''
