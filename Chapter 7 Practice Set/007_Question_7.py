# Question :-
"""Write a program to print the multiplication table of n
using for loop in reversed order."""

number = int(input("Enter the number you want multiplication table of in reversed order :-\n"))

print("")

for i in range(11, 1, -1):
    i = i - 1
    print(f"{number} X {i} = {number * i}")
