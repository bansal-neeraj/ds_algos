# to create a copy of a object and then modify the copy
import copy

class A:
    def __init__(self,x):
        self.x = x
        self.y = {1:10}


obj1 = A(10)
obj2 = copy.deepcopy(obj1)
obj2.x = 34

print(obj1.x,obj1.y)
print(obj2.x,obj2.y)

obj2.y[1] = 9

print(obj1.x,obj1.y)
print(obj2.x,obj2.y)


print(id(obj1))
print(id(obj2))