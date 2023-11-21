
# Замыкание
# 1) Вложенная функция
# 2) Возврат п.1
# 3) п.1 должна ссылаться на нелокальное имя

from datetime import datetime

def decorator(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'executiion took {end - start} seconds')
        return result
    return wrapper


@decorator
def f(x):
    return x ** 1234


