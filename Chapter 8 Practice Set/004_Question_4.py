# Question :-
"""	Write a python function to print the first n lines of the following pattern
***
**      For n = 3 (It is an example of 3 lines)
* """

number = int(input("Enter a number :-\n"))


def function(num):
    for i in range(number):
        print("*" * (number - i))


function(number)
