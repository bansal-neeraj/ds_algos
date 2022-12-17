"""
Monkey Patching - to change class attributes during run time
"""


class MyData:
    def __init__(self,x):
        self.x= x

    def f1(self):
        print('f1 called')

    def f2(self):
        self.f1()


def monkey_code(self):
    print("monkey called")


x = MyData(12)
x.f2()

MyData.f1 = monkey_code

y = MyData(15)
y.f1()

