# Question :-
"""Write a program to find the greatest of four
numbers entered by the user."""

a = input("Enter First Number :-\n")
b = input("Enter Second Number :-\n")
c = input("Enter Third Number :-\n")
d = input("Enter Forth Number :-\n")

if a > b and a > c and a > d:
    print("The Greatest number among all is :-", a)
elif b > a and b > c and b > d:
    print("The Greatest number among all is :-", b)
elif c > a and c > b and c > d:
    print("The Greatest number among all is :-", c)
elif d > a and d > b and d > c:
    print("The Greatest number among all is :-", d)
else:
    print("Enter VALID Values ! This values are INVALID ! All the numbers must be DIFFERENT from each other.")