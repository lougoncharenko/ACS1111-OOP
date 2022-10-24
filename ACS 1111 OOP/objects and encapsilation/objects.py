class Car:
    def __init__(self, name, year, model):
        self.name = name
        self.year = year
        self.model = model

    def honk(self):
        print ('honk, honk')


#object is the instance of a class
my_car = Car ('Tesla', 2020, 'Model X')
my_car.honk()

mom_car = Car('Toyota', 2016, 'Camry')
mom_car.honk()

sis_car = Car('Honda', 2015, 'Civic')
sis_car.honk()


#encapsulation
# bundles related data and functionality together

