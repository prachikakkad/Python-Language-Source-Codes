# Question :-
""" An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 84 or Exercise 86. Add an attribute , privileges , that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator's set of privileges. Create an instance of Admin , and call your method. """

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
    def __init__(self, first_name, last_name, Date_of_birth, age, city_or_town):
        super().__init__(first_name, last_name, Date_of_birth, age, city_or_town)
        self.privileges = []

    def show_privileges(self):
        print("Privileges of an administrator are :-")
        for self.privilege in self.privileges:
            print(f" - {self.privilege}")

user = Admin("Prachi" , "Kakkad" , "4 December , 2007" , 15 , "Upleta")
user.describe_user()

user.privileges = ["can add post" , "can delete post" , "can ban user"]
user.show_privileges()