"""
*args - arguments are recved as tuple by a function
**kwargs - arguments received as dictionary in the function
* can be used to unpack map , range, list , tuple
** - used to unpack dictionary
"""
from typing import Any


def f1(*args):
    print(args)
    print(type(args))


x, y, z = 2,10,20
f1(x,y,z)

n = 300

f1(x,y,z,n)

# unpack a list and send it to function
def unpack(a,b):
    print(a)
    print(b)


a_liast = ['apple','orange']

unpack(*a_liast)

# **kwargs


def func(**kwargs: Any) -> None:
    print(kwargs)
    print(type(kwargs))


func(a='India',b='Mumbai',c='Delhi')

# unpacking map iterartor
print('map')

a = [1,2,3,4,5]


def exp_map(x):
    return x*x

m = map(exp_map,a)
print(type(m))
print(*m)

# range object unpacking
print('range object unpacking')
print(*range(10))

# special unpacking

a, *_, b = [10,20,30,40]

print(f'{a=}')
print(f'{_=}')
print(f'{b=}')

# ############ using args and kwargs together #######################


def my_product(product: str,*args:Any, **kwargs: Any) -> None:
    print(f'{product=}')
    print(f'{args=}')
    print(f'{kwargs=}')


my_product('sneakers','black','white','red',brand='Nike',size=10,in_stock=False)


# ############ dictionary unpacking and kwargs #######################

my_dict = {
    'name': 'Neeraj',
    'age': 47,
    'language': 'Python'
}

print('#'*20,'dictionary unpacking')


def my_func(**kwargs):
    print(kwargs)


my_func(**my_dict)