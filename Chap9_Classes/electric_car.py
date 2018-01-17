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

my_car = Car("Honda", "Accord", 2010)
print(my_car.get_name())
my_car.odometer_reading = 17000
my_car.update_odomter(16100)
my_car.read_odometer()
                  
class ElectricCar(Car):
    """This class provide car detail with electic feature"""
    def __init__(self, make, model, year):
        """Intitialze parent classs"""
        """Intiailize subclass attrribute"""
        super().__init__(make, model, year)
        self.battery_size = 85
        self.range = 240

    def get_battery_size(self):
        print("Battery size "+ str(self.battery_size) + "-KWH battery")

    def get_range(self):
        """Range of Battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can travel upto " + str(range)    
        message += " miles on full charge"
        print(message)


my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_name())
print(my_tesla.get_battery_size())
print(my_tesla.get_range())



