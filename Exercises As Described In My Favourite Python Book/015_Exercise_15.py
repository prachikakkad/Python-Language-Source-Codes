# Question :-
""" You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
•	 Start with your program from Exercise 14. Add a print statement at the end of your program stating the name of the guest who can't make it.
•	 Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still in your list."""

guest = ["Uncle" , "Aunty" , "Brother"]

print(f"Hello {guest[0]} , you are invited on a dinner tonight at our house with {guest[1]} and {guest[2]}.")

print(f"Hello {guest[1]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[2]}.")

print(f"Hello {guest[2]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[1]}.")

print(f"{guest[0]} can't make it.")

guest[0] = "Sister"

print(f"Hello {guest[0]} , you are invited on a dinner tonight at our house with {guest[1]} and {guest[2]}.")

print(f"Hello {guest[1]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[2]}.")

print(f"Hello {guest[2]} , you are invited on a dinner tonight at our house with {guest[0]} and {guest[1]}.")