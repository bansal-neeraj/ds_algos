import requests

# endpoint = 'http://127.0.0.1:8000/api'
endpoint = 'http://127.0.0.1:8000/api/classlist'

r = requests.get(endpoint)

print(r.json())