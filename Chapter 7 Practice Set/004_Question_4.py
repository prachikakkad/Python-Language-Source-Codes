# Question :-
"""Write a program to find whether a given number is
prime or not."""

number = int(input("Enter a number :-\n"))
prime = True

for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print("This is a prime number.")
else:
    print("This is not a prime number.")
