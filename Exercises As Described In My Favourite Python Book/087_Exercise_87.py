# Question :-
""" An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 82 or Exercise 85. Either version of the class will work ; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand , and call this method."""

class Restaurant:

    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.cuisine_type} is the speciality of {self.restaurant_name} !")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is Open ! Come on ! Come inside and enjoy the tasty meal !")

class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavours = ["vanilla" , "chocolate" , "butter scotch"]

    def display(self):
        print("Following flavours are availabe :-")
        for self.flavour in self.flavours:
            print(f"- {self.flavour}")

ice_cream = IceCreamStand()
ice_cream.display()