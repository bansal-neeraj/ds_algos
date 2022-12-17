class A:
    # __slots__ = ('x','y')
    v = 10

    def __init__(self):
        self.x = 10
        self.y = 20


x = A()
x.z = 54
print(x.x)
print(x.y)

abc = A()
abc.x = 123
abc.y = 245

print(abc.x)
print(abc.y)
# print(x.__dict__)