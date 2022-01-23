# Question :-
""" Ask the user for a number , and then report whether the number is a multiple of 10 or not. """

ask = input("Enter a number :-\n")
ask = int(ask)

if ask % 10 == 0:
    print(f"{ask} is the multiple of 10.")

else:
    print(f"{ask} is not the multiple of 10.")
