# Question :-
"""You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•  Start with your program from Exercise 14 or Exercise 15. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•  Use insert() to add one new guest to the beginning of your list.
•  Use insert() to add one new guest to the middle of your list.
•  Use append() to add one new guest to the end of your list.
•  Print a new set of invitation messages, one for each person in your list"""

guest = ["Uncle" , "Aunty" , "Brother"]

print(f"Hello {guest[0]} , you are invited on a dinner tonight at our house with {guest[1]} and {guest[2]}.")

print(f"Hello {guest[1]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[2]}.")

print(f"Hello {guest[2]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[1]}.")

print(f"{guest[0]} can't make it.")

guest[0] = "Sister"

print(f"Hello {guest[0]} , you are invited on a dinner tonight at our house with {guest[1]} and {guest[2]}.")

print(f"Hello {guest[1]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[2]}.")

print(f"Hello {guest[2]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[1]}.")

print("Now I have found a bigger dinner table.")

guest.insert(-2 , "Mama")
guest.insert(-1 , "Nani")
guest.append("Friend")

print(f"Hello {guest[0]} , you are invited on a dinner tonight at our house with {guest[1]} , {guest[2]} , {guest[-1]} , {guest[-2]} and {guest[3]}.")

print(f"Hello {guest[1]} , you are invited on a dinner tonight at our house with {guest[0]} , {guest[2]} , {guest[-1]} , {guest[-2]} and {guest[3]}.")

print(f"Hello {guest[2]} , you are invited on a dinner tonight at our house with {guest[0]} , {guest[1]} , {guest[-1]} , {guest[-2]} and {guest[3]}.")

print(f"Hello {guest[-1]} , you are invited on a dinner tonight at our house with {guest[0]} , {guest[1]} , {guest[2]} , {guest[-2]} and {guest[3]}.")

print(f"Hello {guest[-2]} , you are invited on a dinner tonight at our house with {guest[0]} , {guest[1]} , {guest[-1]} , {guest[2]} and {guest[3]}.")

print(f"Hello {guest[3]} , you are invited on a dinner tonight at our house with {guest[0]} , {guest[1]} , {guest[-1]} , {guest[-2]} and {guest[2]}.")

