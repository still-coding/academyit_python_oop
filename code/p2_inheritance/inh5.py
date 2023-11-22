class Device:
    def turn_on(self):
        print('turned on')
    def turn_off(self):
        print('turned off')

class Phone(Device):
    def call(self, number):
        print('calling', number)

    def ring(self):
        print('Ring-ring!')


class Camera(Device):
    def make_photo(self):
        print('click')

class SmartPhone(Phone, Camera):
    pass

s = SmartPhone()

