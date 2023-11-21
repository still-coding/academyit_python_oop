class Car:
    __car_count = 0
    
    @classmethod
    def __inc_car_count(cls):
        cls.__car_count += 1

    @classmethod
    def __dec_car_count(cls):
        cls.__car_count -= 1

    @classmethod
    def get_car_count(cls):
        return cls.__car_count

    @staticmethod
    def car_details():
        print("This is Car class")


    def __new__(cls):
        cls.__inc_car_count()
        return super().__new__(cls)

    
    def __del__(self):
        self.__dec_car_count()


    def __init__(self, name="Supra A80", make="Toyota", year=1998):
        self.name = name
        self.make = make
        self.year = year
        

    def start(self):
        print("Engine started")


    def stop(self):
        print("Engine turned off")


    def __str__(self):
        return f"{self.make} {self.name} {self.year}"


    def __repr__(self):
        return str(self)


supra = Car()
supra.start() # => Car.start(supra)


# name mangling
# Car._Car__car_count
