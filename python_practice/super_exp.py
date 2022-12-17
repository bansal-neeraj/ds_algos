class Root:
    def f(self):
        print("root")


class A(Root):
    def f1(self):
        print("calss A")
        # super().f()


class B(Root):
    def f(self):
        print('class B')


class C(A,B):
    def f(self):
        print('class C')
        super().f()


c_obj = C()

c_obj.f()

print(C.__mro__)