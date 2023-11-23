from collections import ChainMap

d1 = {'a': 1, 'b': 2, 'c': 2}
d2 = {'c': 1, 'e': 3, 'f': 1}

c = ChainMap(d1, d2)

print(c)

print(c['a'])
print(c['c'])
print(c['e'])

d1['x'] = 1
print(c)

print(c.new_child({1: 2}))

print(list(c.keys()))
print(list(c.values()))