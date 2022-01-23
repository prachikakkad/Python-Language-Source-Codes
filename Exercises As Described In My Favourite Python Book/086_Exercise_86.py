# Question :-
""" Add an attribute called login_attempts to your User class from Exercise 84. Write a method called increment_ login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_ attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0. """

class User:
    def __init__(self , first_name , last_name , Date_of_birth , age , city_or_town):
        self.first_name = first_name
        self.last_name = last_name
        self.Date_of_birth = Date_of_birth
        self.age = age
        self.city_or_town = city_or_town
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name of the user is {self.first_name} {self.last_name}.")
        print(f"The birth date of user is {self.Date_of_birth}.")
        print(f"The age of user is {self.age}")
        print(f"The user live in {self.city_or_town}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} , How are you ?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user_1 = User("Prachi" , "Kakkad" , "4 December , 2007" , 15 , "Upleta")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(str(user_1.login_attempts))

print("Reseting login attempts...")
user_1.reset_login_attempts()
print(str(user_1.login_attempts))