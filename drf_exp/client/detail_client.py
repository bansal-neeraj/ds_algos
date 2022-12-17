import requests

# endpoint = 'http://127.0.0.1:8000/api/2'
endpoint = 'http://127.0.0.1:8000/api/classdetail/10'

r = requests.get(endpoint)
print(r.json())