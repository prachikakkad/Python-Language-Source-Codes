# Question :-
"""Write a program that finds out whether a given name
is present in a list or not."""

List = ["Prachi", "Amit", "Avani"]

name = input("Enter a Name :-\n")

if name in List:
    print("It is there in the list !")
elif name not in List:
    print("It is not there in the list !")