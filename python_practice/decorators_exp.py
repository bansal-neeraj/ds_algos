import time


def my_decorator(func):
    def inner_func(*args,**kwargs):
        start = time.perf_counter()
        print(f'{func.__name__=}')
        r1 = func(*args,**kwargs)
        end = time.perf_counter()
        print(end -start)
        return r1
    return inner_func

@my_decorator
def add_two(n1,n2):
    return n1 + n2


x = add_two(10,20)

print(x)
