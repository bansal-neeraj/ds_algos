# Magic functions

class MyClass:

    def __init__(self,x):
        self.x = x

    def __eq__(self, other):
        print ('magic function called')
        return self.x == other.x


ob1 = MyClass(10)
obj2 = MyClass(20)

print(ob1 == obj2)