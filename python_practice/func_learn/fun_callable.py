from typing import Callable

def hello():
    print('helo')


greet: Callable[[],None] = hello

greet()
