# Question :-
""" Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users , and call both methods for each user."""

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

user_1 = User("Prachi" , "Kakkad" , "4 December , 2007" , 15 , "Upleta")
user_1.describe_user()
user_1.greet_user()

user_2 = User("Naveen" , "Goyat" , "14 February , 2000" , 21 , "Bhiwani")
user_2.describe_user()
user_2.greet_user()

user_3 = User("Shreeja" , "Shukla" , "23 November , 2008" , 14 , "Kanpur")
user_3.describe_user()
user_3.greet_user()