class Animal:
    pass


class Mammal(Animal):
    pass

class Reptile(Animal):
    pass

class Cat(Mammal):
    def __init__(self, name=None):
        self.name = name

    def make_sound(self):
        return f'{self.name} says "meow"' if self.name else 'meow'


class Snake(Reptile):
    def make_sound(self):
        return 'shhhhh'


boris = Cat("Boris")
print(boris.make_sound())

snake = Snake()
print(snake.make_sound())

