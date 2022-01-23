# Question :-
"""Write a program to calculate the factorial of a given
number using for loop."""

number = int(input("Enter a number :-\n"))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f"The factorial of {number} is {factorial}")
