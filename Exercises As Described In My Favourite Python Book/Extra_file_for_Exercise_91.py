class Restaurant:

    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.cuisine_type} is the speciality of {self.restaurant_name} !")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is Open ! Come on ! Come inside and enjoy the tasty meal !")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served