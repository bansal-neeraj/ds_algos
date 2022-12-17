from abc import ABC,ABCMeta,abstractmethod


class Person:
    def __new__(cls, *args, **kwargs):
        return cls

    def __init__(self):
        print('init called')




print(type(Person))




