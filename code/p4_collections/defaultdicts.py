from collections import defaultdict

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# print(d['a'])
# print(d['x'])
# d['x'] = 0

# default_d = defaultdict(int, d)

# print(default_d)

# print(default_d['a'])
# print(default_d['x'])
# print(default_d)




lst = list(range(10)) + [3, 5, 6, 3, 8]
print(lst)

# d = {}
# for i in lst:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


d = defaultdict(int)
for i in lst:
    d[i] += 1
print(d)

