# unpack a dictionary using ** while passing in a function.

a = {
    'x':'abc',
    'y':'def'
}


def f1(y,x):
    print(x,y)

f1(**a)