# Question :-
""" Write a python program using the functions to convert
Celsius to Fahrenheit."""


# Formula :-
# (var°C × 9/5) + 32 = 32

def converter(number):
    result = number * 1.8 + 32

    print(f"{celsius} in fahrenheit is {result}")


celsius = int(input("Enter temperature in celsius and please don't enter it in decimal :-\n"))

converter(celsius)
