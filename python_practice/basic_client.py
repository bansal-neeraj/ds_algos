import json

import requests

endpoint = 'http://127.0.0.1:8000/expapi/dapi'

# r1 = requests.get(endpoint)
# print(r1.json()['msg'])
get_response = requests.get(endpoint,params={'abc':123},json={'name':'Hello World'})
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)


# end_point2 = "http://localhost:8000/expapi/"
# print(requests.get(end_point2,data={"name":"Neeraj"},params={'abc':123}).url)

# get_response = requests.post(end_point2,json={'name':'abc123'})
