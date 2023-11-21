class Number:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.val + other.val)
        return self
            # raise TypeError('Other must be a Number')


# a + b => a.__add__(b) => Number.__add__(a, b)

class MyList(list):
    def __getitem__(self, key):
        if key == 0:
            raise IndexError('key must be non non-zero')
        if key > 0:
            key -= 1
        return super().__getitem__(key)


