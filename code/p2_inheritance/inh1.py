class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


class Desk(Table):
    def area(self):
        return self.width * self.height
