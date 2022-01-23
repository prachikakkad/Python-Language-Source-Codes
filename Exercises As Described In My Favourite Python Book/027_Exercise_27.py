# Question :-
""" Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number. """

numbers = [value + 0 for value in range(1 , 21 , 2)]
for num in numbers:
    print(num)