# Question :-
"""Write a program to find the sum of first n natural
numbers using a while loop."""

number = int(input("Enter the number :-\n"))
addition = 0

while number > 0:
    addition = addition + number
    number = number - 1

print("The sum of first", number, "Natural Numbers is", addition)