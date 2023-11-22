# 1) Позиционные
def f(a, b, c):
    pass
f(1, 2, 3)


# 2) Ключевые аргументы
def f(a, b, c):
    pass
f(a=1, b=2, c=3)

# 3) Стандартные
def f(a, b=2, c=3):
    pass

# 4) Сбор переменного числа аргументов
def f(*args): # собираем в кортеж (позиционные)
    pass
def f(**kwargs): # собираем в словарь (ключевые)
    pass

