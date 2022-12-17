import string

print(string.punctuation)
print(type(string.punctuation))

v = ','

x = any(v in p for p in string.punctuation)
print(x)
y = [v in p for p in string.punctuation]
print(y)