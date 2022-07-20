#parent class 1
class vehicle:
    def functioning(self):
        print('vehicles are used for transportation')

#child class 1
class car(vehicle):
    def wheels(self):
        print('a car has 4 wheels')
       
#child class 2
class electric_car(car):
    def speciality(self):
        print('electric car runs on electricity')

electric=electric_car()
electric.speciality()
electric.wheels()
electric.functioning()
