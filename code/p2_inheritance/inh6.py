class A:
    def method(self):
        print("method A")

class B:
    def method(self):
        print("method B")


class C(A, B):
    pass


class D(C):
    pass
