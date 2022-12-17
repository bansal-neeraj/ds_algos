"""
checking what datatype of keys a dictinary can have , as per python doc any immutable type
a dictiony keys can be any of the following immutable data types

string
int
float
tuple - (if they contain immutable datatypes)
frozenset
datetime objcect  - as it is also immutable
Boolean
empty string

NOT ALLOWED AS KEYS A- because they are mutable

sets
list
dictionaries

"""

import datetime

d1 = datetime.date(2021,1,1)
print(d1)

print(d1)

fs = frozenset([1,2,3])
b = True
x = 45


a = {
    d1:'abc',
    fs:'ef',
    b:'123',
    x:96,
    'False':100,
    '':500
}

# a.clear()
b = {
    'a': [1,2,3],
    'b':[4,5,6],
    'c':[7,8,9,10,11,12,13]
}
cont_list = []
print('id',id(cont_list))
for x in b.values():
    cont_list += x


print(cont_list)
print('id',id(cont_list))
x_list = [1,2,3]
for i in x_list:
    print(i,x_list.index(i))

for index,j in enumerate(a.values(),start=1):
    print(index,j)


# new code to test dictiony creation with two new keys at a time

print('*'*10)
x1 = {}
d1 = datetime.date(2021,1,1)

option_type = True
opp_option_type = False


x1[d1] = {}
x1[d1][option_type] = 57.4
x1[d1][opp_option_type] = 30


print(x1.keys())

# creata a copy of dictionary anfd then modify the copy

n1 = {1:'abc'}

n2 = n1

n2[1] = 'def'
print(n1)
print(n2)

