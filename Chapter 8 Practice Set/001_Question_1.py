# Question :-
"""Write a program using the functions to find the
greatest of three numbers."""


def function(a, b, c, d):
    """This function finds the greatest number among all four numbers"""
    if a > b and a > c and a > d:
        print(f"{a} is greatest among all !")
    elif b > a and b > c and b > d:
        print(f"{b} is greatest among all !")
    elif c > a and c > b and c > d:
        print(f"{c} is greatest among all !")
    elif d > a and d > b and d > c:
        print(f"{d} is greatest among all !")
    else:
        print("Enter VALID Numbers ! There Numbers are INVALID ! All the numbers must be DIFFERENT from each other !")


# print(function.__doc__)

num1 = int(input("Enter first number :-\n"))
num2 = int(input("Enter second number :-\n"))
num3 = int(input("Enter third number :-\n"))
num4 = int(input("Enter forth number :-\n"))

function(num1, num2, num3, num4)