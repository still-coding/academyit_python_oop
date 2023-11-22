class A:
    def __init__(self, value):
        self.value = value

class B(A):
    def __new__(cls):
        return A(42)

b = B()
print(b.value)
