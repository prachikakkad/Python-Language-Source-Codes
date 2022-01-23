# Calculating Factorial using Iteration
def factorial_iterative(n):
    fac1 = 1
    for i in range(n):
        fac1 = fac1 * (i + 1)
    return fac1


number1 = int(input("Enter a number :-\n"))

factorial_iterative(number1)

print(f"The factorial of {number1} is {factorial_iterative(number1)}")


# Calculating Factorial using Recursion

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number2 = int(input("Enter a number :-\n"))

factorial_recursive(number2)

print(f"The factorial of {number2} is {factorial_recursive(number2)}")
