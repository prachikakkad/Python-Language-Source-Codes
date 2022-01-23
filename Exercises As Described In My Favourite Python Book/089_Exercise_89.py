# Question :-
""" First copy the program of Exercise 88  in this program. Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 88. Move the show_privileges() method to this class from Admin class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges. """

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

class Admin(User):
    def __init__(self , first_name , last_name , Date_of_birth , age , city_or_town):
        super().__init__(first_name, last_name, Date_of_birth , age , city_or_town)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("Privileges of this administrator are :-")
            for privilege in self.privileges:
                print("- " + privilege)


user = Admin("Prachi" , "Kakkad" , "4 December , 2007" , 15 , "Upleta")
user.describe_user()

user.privileges.show_privileges()

user_privileges = ["can add post" , "can delete post" , "can ban user"]
user.privileges.privileges = user_privileges
user.privileges.show_privileges()