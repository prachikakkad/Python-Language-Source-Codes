# Question :-
""" Start with your class from Exercise 82. Create three different instances from the class, and call describe_restaurant() for each instance."""

class Restaurant:

    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.cuisine_type} is the speciality of {self.restaurant_name} !")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is Open ! Come on ! Come inside and enjoy the tasty meal !")

retaurant_1 = Restaurant("Amidhara" , "Punjabi")
retaurant_1.describe_restaurant()

retaurant_2 = Restaurant("Green Village" , "Sizzler")
retaurant_2.describe_restaurant()

retaurant_3 = Restaurant("Dominoz" , "Pizza")
retaurant_3.describe_restaurant()