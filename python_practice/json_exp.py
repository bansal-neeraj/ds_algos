import json

a = 10

b = {
    'name':'Neeraj',
    'age':46
}


json_data = json.dumps(b)

print(type(b))

print(json_data)
print(type(json_data))

parsed_data = json.loads(json_data)

print(parsed_data)
print(type(json_data))

