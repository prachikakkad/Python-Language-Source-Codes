# Question :-
""" A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the change.
•	 The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu. """

menu = ("Chapati" , "sev-tomato sabzi" , "Bajra roti" , "Dal" , "Rice")
for items in menu:
    print(items)

# menu[0] = "Roti" --> throws an error

menu = ("Chapati" , "Undhiyu" , "Upma" , "Dal" , "Rice")
for items in menu:
    print(items)