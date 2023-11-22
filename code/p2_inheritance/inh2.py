class Super:
    def method(self):
        print('super method')

# 1) Наследование
class Inheritor(Super):
    pass

# i = Inheritor()
# i.method()

# 2) Замещение

class Replacer(Super):
    def method(self):
        print('replacer method')

# r = Replacer()
# r.method()


# 3) Расширение

class Extender(Super):
    def method(self):
        print('extender method begins')
        super().method()
        print('extender method ends')

# e = Extender()
# e.method()


