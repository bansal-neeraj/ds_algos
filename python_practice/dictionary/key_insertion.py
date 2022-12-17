"""
key insertion and deletion are NOT allowed while dictionary is being iterated
"""

a = {
    1:'abc',
    2:'def'
}

for k,v in a.items():
    print(k,v)
    # a.pop(1)

print(dir(dict))
print(help(dict.pop))