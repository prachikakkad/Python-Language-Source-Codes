# Question :-
""" Write a function to calculate Fibonacci series till n numbers using recursion.
1 , 1 , 2 , 3 , 5 , 8 , 13 ……"""


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter the will which you want fibonacci series :-\n"))

print(fibonacci(number))