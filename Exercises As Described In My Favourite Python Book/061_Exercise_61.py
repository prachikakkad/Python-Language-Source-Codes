# Question :-
"""Write different versions of either Exercise 59 or Exercise 60 that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value."""

prompt = "What topping would you like to have on your pizza ? \nEnter 'quit' when you are finished :- \n"

# Version 1 :-

active = True

while active == True:
    topping = input(prompt)
    if topping != "quit":
        print(f"I will add {topping} to your pizza.")
    
    else:
        break

# Version 2 :-

active = True

while active:
    topping = input(prompt)
    if topping != "quit":
        print(f"I will add {topping} to your pizza.")
    
    else:
        break

# Version 3 :-

while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"I will add {topping} to your pizza.")
    
    elif topping == "quit":
        break