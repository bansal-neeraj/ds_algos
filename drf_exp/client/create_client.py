import requests

# endpoint = 'http://127.0.0.1:8000/api/create'
endpoint = 'http://127.0.0.1:8000/api/classcreate'

data = {
    'title': 'abc class 1',
    'content': 'con1 ',
    'price': 100
}

r = requests.post(endpoint,json=data)

print(r.json())
