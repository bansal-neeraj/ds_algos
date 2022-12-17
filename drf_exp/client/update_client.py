import requests

endpoint = 'http://127.0.0.1:8000/api/classupdate/1'

data = {
    'title': 'Cars 2',
    'content': 'con4',
    # 'price': 400
}

r = requests.put(endpoint,json=data)

print(r.json())
