# Question :-
""" Using the Restaurant class of Exercise 85 , store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance , and call all the methods of Restaurant class  to show that the import statement is working properly."""

from Extra_file_for_Exercise_91 import Restaurant

# Other way to import the module
from Extra_file_for_Exercise_91 import *

restaurant =  Restaurant("Dominoz" , "Pizza")
restaurant.describe_restaurant()