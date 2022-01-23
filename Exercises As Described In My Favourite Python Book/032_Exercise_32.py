# Question :-
"""Start with your program from Exercise 22. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message , My friend's favorite pizzas are :- , and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list. """

fav_pizza = ["Cheese Burst Pizza"  , "Mexican Pizza" , "Pepperoni Pizza"]
for pizza in fav_pizza:
    print(pizza)

for pizza in fav_pizza:
    print(f"I like {pizza}")

print('I really like :-\nCheese Burst Pizza\nMexican Pizza\nPepperoni Pizza\nI really love eating Pizza !')

friend_pizzas = fav_pizza[:]

fav_pizza.append("Sicilian Pizza")
friend_pizzas.append("Greek Pizza")

print()

print("My Favourite Pizzas are :-")
for name in fav_pizza:
    print(name)

print()

print("My Friend's Favourite Pizzas are :-")
for name in friend_pizzas:
    print(name)