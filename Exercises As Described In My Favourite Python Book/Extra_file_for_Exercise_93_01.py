class User:
    def __init__(self , first_name , last_name , Date_of_birth , age , city_or_town):
        self.first_name = first_name
        self.last_name = last_name
        self.Date_of_birth = Date_of_birth
        self.age = age
        self.city_or_town = city_or_town

    def describe_user(self):
        print(f"Name of the user is {self.first_name} {self.last_name}.")
        print(f"The birth date of user is {self.Date_of_birth}.")
        print(f"The age of user is {self.age}")
        print(f"The user live in {self.city_or_town}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} , How are you ?")