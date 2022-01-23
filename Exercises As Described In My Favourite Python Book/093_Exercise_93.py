# Question :-
""" Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file , create an Admin instance and call show_privileges() to show that everything is still working correctly."""

from Extra_file_for_Exercise_93_02 import Admin

user = Admin("Prachi" , "Kakkad" , "4 December , 2007" , 15 , "Upleta")
user_privileges = ["can add post" , "can delete post" , "can ban user"]
user.privileges.privileges = user_privileges
user.privileges.show_privileges()