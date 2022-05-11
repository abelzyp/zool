from urllib import request
from urllib import parse

# get请求
# response = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())

# post请求
data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
# print(data)
response2 = request.urlopen('http://httpbin.org/post', data=data)
print(response2.read())
