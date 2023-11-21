class A:
    # конструктор
    def __new__(cls):
        print("Object created")
        return super().__new__(cls)


    def __init__(self):
        print("Object initialized")

    # деструктор
    def __del__(self):
        print("Object deleted")

