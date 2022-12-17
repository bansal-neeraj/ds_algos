from abc import ABC,abstractmethod


class MyBase(ABC):


    @abstractmethod
    def f1(self):
        print('abc method')

    def f2(self):
        print('non abc method')


class MyChild(MyBase):

    def __init__(self):
        self.type = 1

    def f1(self):
        super().f1()
        super(MyChild, self).f2()
        print(self.type)



m1 = MyChild()

m1.f1()