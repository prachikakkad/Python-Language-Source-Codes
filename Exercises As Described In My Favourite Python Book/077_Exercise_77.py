# Question :-
""" Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time."""

def accept(*items):
    for item in items:
        print(f"Adding {item} into sandwich.")
    print("Your sandwich is ready !")

accept("Cheese" , "Sauces" , "Vegetables" , "Butter")
accept("Cheese" , "Sauces" ,  "Butter" , "Green peas" , "Ketch up")
accept("Cheese" , "Vegetables" , "Butter")
