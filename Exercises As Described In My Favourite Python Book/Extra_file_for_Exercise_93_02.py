from Extra_file_for_Exercise_93_01 import User

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