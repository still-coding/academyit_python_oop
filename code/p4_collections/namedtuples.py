from collections import namedtuple

# до
point = (1, 3)

print(point[0])
print(point[1])

print(point)



# после
Point = namedtuple('Point', ('x', 'y'))

p = Point(x=1, y=3)

print(f"{p.x=}")
print(f"{p.y=}")

