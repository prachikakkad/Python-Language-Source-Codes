# Question :-
""" Write a program that prompts the user for their name. When they respond , write their name to a file."""

while True:
    ask = input("Enter your name :-\n")
    with open("Extra_file_for_Exercise_99.txt" , "w") as mode:
        mode.write(ask)