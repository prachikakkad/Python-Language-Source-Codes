# Question :-
"""Working with the program of Exercises 14 , use len() to print a message indicating the number of people you are inviting to dinner."""

guest = ["Uncle" , "Aunty" , "Brother"]

print(f"Hello {guest[0]} , you are invited on a dinner tonight at our house with {guest[1]}.")

print(f"Hello {guest[1]} , you are invited on a dinner tonight at our house with {guest[0]}.")

print(f"Hello {guest[2]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[1]}.")

print(f"{len(guest)} people are invited on a dinner tonight at our house.")