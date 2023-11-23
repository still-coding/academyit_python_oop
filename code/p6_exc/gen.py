def f():
    n = 1
    while True:
        yield n
        n += 1


g = (i for i in range(5))
