class Person:

    def __new__(cls, *args, **kwargs):
        print('new called')
        return super().__new__(cls)

    def __init__(self):
        print('init called')


x = Person()

