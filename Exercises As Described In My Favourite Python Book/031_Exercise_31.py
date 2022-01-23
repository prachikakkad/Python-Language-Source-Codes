# Question :-
""" Using one of the programs you wrote , add several lines to the end of the program that do the following:
•	 Print the message, The first three items in the list are :- Then use a slice to print the first three items from that program's list.
•	 Print the message, Three items from the middle of the list are :- Use a slice to print three items from the middle of the list.
•	 Print the message, The last three items in the list are :- Use a slice to print the last three items in the list. """

names = ["Prachi" , "Naveen" , "Shreeja" , "Rahul" ,  "Saumya" , "Siddharth" , "Karan"]

print(f"The first three items in the list are :- {names[:3]}")
print(f"The three items in the middle of the list are :- {names[1:4]}")
print(f"The three items at the end of the list are :- {names[4:7]}")