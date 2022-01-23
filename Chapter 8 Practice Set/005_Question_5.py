# Question :-
""" Write a python function that converts inches to centimetres."""
# Formula :-
# x inches * 2.54


def converter(inch):
    if inch == 0:
        return 0
    else:
        return inch * 2.54


inches = int(input("Enter the number but don't enter the decimal !\n"))

print(converter(inches))