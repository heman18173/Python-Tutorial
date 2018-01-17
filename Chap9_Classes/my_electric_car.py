from electric_car import Car, ElectricCar
import electric_car
from car import * # This import all class of module car

my_new_e_car = ElectricCar("Toyota", "Prius", "2018")
print(my_new_e_car.get_name())

my_new_car = Car("Maruti", "Swift", "2018")
print(my_new_car.get_name())

my_toyoto = electric_car.ElectricCar("Toyota", "Prius", "2018")
print(my_toyoto.get_name())

my_maruti = electric_car.Car("Maruti", "Swift", "2018")
print(my_maruti.get_name())