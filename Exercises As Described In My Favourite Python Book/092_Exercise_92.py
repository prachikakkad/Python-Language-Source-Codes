# Question :-
""" Start with your work from Exercise 89.Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly."""


from Extra_file_for_Exercise_92 import Admin

user = Admin("Prachi" , "Kakkad" , "4 December , 2007" , 15 , "Upleta")
user_privileges = ["can add post" , "can delete post" , "can ban user"]
user.privileges.privileges = user_privileges
user.privileges.show_privileges()