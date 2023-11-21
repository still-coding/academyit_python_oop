# class ИмяКласса:
#     поле1 = значение1
#     поле2 = значение2
#     ...

#     def метод1():
#         блок1


#     def метод2():
#         блок2

#     ...



class Car:
    car_count = 0
    
    def __new__(cls):
        cls.car_count += 1
        return super().__new__(cls)

    
    def __del__(self):
        self.__class__.car_count -= 1


    def __init__(self, name="Supra A80", make="Toyota", year=1998):
        self.name = name
        self.make = make
        self.year = year
        

    def start(self):
        print("Engine started")


    def stop(self):
        print("Engine turned off")



supra = Car()
supra.start() # => Car.start(supra)



