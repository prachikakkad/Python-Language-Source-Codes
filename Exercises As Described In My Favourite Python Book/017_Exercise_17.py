# Question :-
""" You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
•	Start with your program from Exercise 16. Add a new line that prints a message saying that you can invite only two people for dinner.
•	Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
•	Print a message to each of the two people still on your list, letting them know they're still invited.
•	Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program."""


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

print("I am really sorry but now I can invite only two people for dinner because my new dinner table won't arrive on time due to some circumstances.")

var1_Mama = guest.pop(1)
print(f"Sorry {var1_Mama} , I am not able to invite you at dinner.")

var2_Aunty = guest.pop(1)
print(f"Sorry {var2_Aunty} , I am not able to invite you at dinner.")

var3_Nani = guest.pop(1)
print(f"Sorry {var3_Nani} , I am not able to invite you at dinner.")

var4_Friennd = guest.pop(2)
print(f"Sorry {var4_Friennd} , I am not able to invite you at dinner.")

print(f"{guest[0]} , You are still invited for dinner at our home tonight.")
print(f"{guest[1]} , You are still invited for dinner at our home tonight.")

del guest[0]
del guest[0]

print(guest)