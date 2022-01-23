# Question :-
""" Wrap your code from Exercise 102 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number."""

while True:
    try:
        ask_1 =  int(input("Enter first number :-\n"))
        ask_2 =  int(input("Enter second number :-\n"))

    except ValueError:
        print("Please enter a number not anyting else !")

    else:
        print(f"The sum of {ask_1} and {ask_2} :- {ask_1 + ask_2}")