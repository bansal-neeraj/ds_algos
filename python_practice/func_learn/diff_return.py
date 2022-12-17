"""
function return 1 or more than 1 value
"""

def f1(x):

    if x == 1:
        return -1

    else:
        return [2, 3]


y = f1(1)

z = f1(2)

print(y,type(y))
print(z,type(z))

# What is the output of the following Python code?
a = {'name' : 'abc'}
b = a
c = a.copy()
a['name'] = 'xyz'
print(b['name'],c['name'])