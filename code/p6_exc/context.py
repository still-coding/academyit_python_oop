# f = open("./exc.py", "r")
# for line in f:
#     print(line, end="")


# with open("./exc.py", "r") as f:
#     for line in f:
#         print(line, end="")


class MyContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, trace):
        self.file.close()


# with MyContextManager("./exc.py", "r") as f:
#     for line in f:
#         print(line, end="")

from contextlib import contextmanager
from datetime import datetime

@contextmanager
def timer():
    start = datetime.now()

    yield
    end = datetime.now()
    print(end-start)


with timer():
    print(23 ** 456)
