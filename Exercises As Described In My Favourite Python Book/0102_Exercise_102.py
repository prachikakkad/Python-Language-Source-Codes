# Question :-
""" One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you'll get a TypeError. Write a program that prompts for two numbers. Add them together and print the result. Catch the TypeError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number."""

try:
    ask_1 =  int(input("Enter first number :-\n"))
    ask_2 =  int(input("Enter second number :-\n"))

except ValueError:
    print("Please enter a number not anyting else !")

else:
    print(f"The sum of {ask_1} and {ask_2} :- {ask_1 + ask_2}")