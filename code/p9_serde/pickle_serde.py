import pickle
# import dill as pickle

class MyClass:
    __my_lambda = staticmethod(lambda x: x * x + 1)

    def __init__(self):
        self.a_number = 35
        self.a_string = "hey"
        self.a_list = [1, 2, 3]
        self.a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
        self.a_tuple = (22, 23)
        self.a_lambda = self.__my_lambda

    def print_attrs(self):
        for attr in self.__dict__:
            if attr.startswith("a_"):
                print(self.__dict__[attr])

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['a_lambda']
        return attributes
    
    def __setstate__(self, state):
        self.__dict__ = state
        self.a_lambda = self.__my_lambda

    
mc = MyClass()
mc_pickled = pickle.dumps(mc)
mc_unpickled = pickle.loads(mc_pickled)
mc_unpickled.print_attrs()
print(mc_unpickled.a_lambda(2))