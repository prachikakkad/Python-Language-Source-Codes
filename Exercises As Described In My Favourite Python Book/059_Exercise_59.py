# Question :-
""" Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping , print a message saying you'll add that topping to their pizza. """

prompt = "What topping would you like to have on your pizza ? \nEnter 'quit' when you are finished :- \n"

while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"I will add {topping} to your pizza.")
    else:
        break