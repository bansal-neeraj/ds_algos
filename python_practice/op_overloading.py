"""
operator overloading and
dunder methods are called implicitly and NOT explicitly

"""


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"x is {self.x} and y is {self.y}"

    def __del__(self):
        print('objects is being deconstructed')

    def __call__(self, *args, **kwargs):
        print('object was called')


v1 = Vector(10, 20)
v2 = Vector(40, 50)

v3 = v1 + v2
print(v3)
v3()