# Creating a Car-Class - Working with Classes and Instances

class Car():
    """ A simple attempt to represend a car. """
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage. """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

# Print the 'make', 'model' and 'year' of a car
my_new_car = Car('vw', 'golf', 2012)
print(my_new_car.get_descriptive_name())

# Printing the odometer statement
# my_new_car.read_odometer()

# Modifying the attribute's Value --> Directly
my_new_car.odometer_reading = 231874 
my_new_car.read_odometer()