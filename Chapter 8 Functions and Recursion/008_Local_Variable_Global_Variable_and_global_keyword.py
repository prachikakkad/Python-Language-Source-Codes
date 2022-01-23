x = 23  # global variable


def addition():
    a = 10  # local variable cannot be accessed outside the function
    b = 20
    add = a + b
    print(add)


# print(a)  # this gives an error


def print_Number():
    # x = x + 1 # cause an error
    print(x)


print_Number()