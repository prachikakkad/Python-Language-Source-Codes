# Question :-
"""Write a python function to print the multiplication table of a
given number."""

number = int(input("Enter the number you want multiplication table of :-\n"))

print("")


def multiplication(number):
    for i in range(10):
        i = i + 1
        print(f"{number} X {i} = {number * i}")

multiplication(number)