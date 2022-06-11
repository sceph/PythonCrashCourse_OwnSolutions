# Restaurant - 02 - Try It Yourself

# Class - Start
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Method - 01 --> Name of Restaurant
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is the name")
    
    # Method - 02 --> Open / Closed - Restaurant
    def open_restaurant(self):
        print()





# Create 3 different instances - then call them with the describe_restaurant method
restaurant_01 = Restaurant('no clue - dinner', 'BURGER')
restaurant_02 = Restaurant('betch - restaurant', 'FISH N CHIPS')
restaurant_03 = Restaurant('macrest', 'MACCES')



# Printing - Restaurant Types (Names in particular)
print("The first name of the Restaurant-List is: " + restaurant_01.restaurant_name.title() + ".")
print("The second name of the Restaurant-List is: " + restaurant_02.restaurant_name.title() + ".")
print("The third name of the Restaurant-List is: " + restaurant_03.restaurant_name.title() + ".")

# Executing previous created methods
describe_restaurant()
