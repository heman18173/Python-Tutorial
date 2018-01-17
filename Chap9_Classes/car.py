class Car():
    """This is simple car class"""
    def __init__(self, make, model, year):
        """Initailze attribute"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_name(self):
        print("Car is " + str(self.year) + " " + self.make + "  " + self.model)    

    def read_odometer(self):
        """ Print odometer """
        print("This car milage is " + str(self.odometer_reading))    

    def update_odomter(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back odometer...")

#my_car = Car("Honda", "Accord", 2010)
#print(my_car.get_name())
#my_car.odometer_reading = 17000
#my_car.update_odomter(16100)
#my_car.read_odometer()
                  
            

