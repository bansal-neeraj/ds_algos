import requests

endpoint = 'http://127.0.0.1:8000/api/classdelete/4'

r = requests.delete(endpoint)

print(r.status_code)