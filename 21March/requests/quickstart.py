import requests
from PIL import Image
from io import BytesIO
import json


# r = requests.get('https://api.github.com/events')
# print(r.text)

# r = requests.post('http://httpbin.org/post', data={'key': 'value'})
# r = requests.put('http://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

# print(r.text)

# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get("http://httpbin.org/get", params=payload)

# r = requests.get('https://api.github.com/events')


# i = Image.open(BytesIO(r.content))
# print(r.status_code)

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)

# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# payload = (('key1', 'value1'), ('key2', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

# url = 'https://api.github.coom/some/endpoint'
# payload = {'some', 'data'}
#
# r = requests.post(url, data=json.dumps(payload))

# r = requests.post(url, json=payload)
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
#
# r = requests.get(url, cookies=cookies)
#
# print(r.text)

r = requests.get('http://github.com')

print(r.url)
print(r.status_code)
print(r.history)




