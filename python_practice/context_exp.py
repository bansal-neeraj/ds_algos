# How to use context managers , code copied from linkedin

import time
from typing import Type
from typing import Optional
from types import TracebackType



class MyTime:
    def __init__(self):
        print('init called')
        self.start = 0
        self.end = 0

    def __enter__(self):
        print('enter called')
        self.start = time.time()
        self.end = 0.0
        # return lambda: self.end - self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('exit called', self.end - self.start)


# class NewTime:
#     def __init__(self):
#         print('new time initialised')
#
#
# with NewTime() as nw:
#     for i in range(10):
#         print(i)

with MyTime() as t:
    for i in range(100000):
        i += 1
#
print(type(t))
print(id(t))

# print("total time taken",t())




