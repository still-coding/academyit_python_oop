from contextlib import contextmanager
from datetime import datetime

@contextmanager
def timer():
    start = datetime.now()

    yield
    end = datetime.now()
    print(end - start)


def test_search(search_func):
    print(f"Testing {search_func.__name__}:", end=' ')
    lst = list(range(100000000))
    to_find = 50000001
    with timer():
        index = search_func(lst, to_find)
    assert index == to_find
    print('Success!')


def linear_search(seq, val):
    for i, elem in enumerate(seq):
        if elem == val:
            return i
    return None


def recursive_binary_search(seq, val):
    def binary_search(seq, val, left, right):
        if left <= right:
            mid = (left + right) // 2
            if seq[mid] == val:
                return mid
            if seq[mid] < val:
                return binary_search(seq, val, mid + 1, right)
            return binary_search(seq, val, left, mid - 1)
        return None
    return binary_search(seq, val, 0, len(seq) - 1)


def iterative_binary_search(seq, val):
    left = 0
    right = len(seq) - 1
    while left <= right:
        mid = (left + right) // 2
        if seq[mid] == val:
            return mid
        if seq[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == '__main__':
    test_search(linear_search)
    test_search(recursive_binary_search)
    test_search(iterative_binary_search)
    