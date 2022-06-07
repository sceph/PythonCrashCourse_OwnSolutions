# Try It Yourself --> Restaurant

# Class Restaurant
class Restaurant():

# Init Method
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


   # Method 1 --> Descirbes the restaurant.
    def describe_restaurant():
        print(self.restaurant_name.title() + " Cuisine de la Beste")
    # Method 2 --> Name of the Restaurant.
    def open_restaurant(self):
        print(self.cuisine_type.title() + " Bolognese")

     


restaurant_01 = Restaurant('Kei Plan', 'open')

print("The Restaurant's name is " + restaurant_01.restaurant_name.title() + ".")
print("The Restaurant is currently: " + restaurant_01.cuisine_type.title() + ".") 
