# Question :-
""" Write a program to print the multiplication table of a
number entered by the user using for loop."""

number = int(input("Enter the number you want multiplication table of :-\n"))

print("")

for i in range(10):
    i = i + 1
    print(f"{number} X {i} = {number*i}")