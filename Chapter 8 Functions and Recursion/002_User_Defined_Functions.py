# With no return value and input
def function():
    print("Prachi")  # function definition


function()  # function call


# With return value and input

def function2(a, b):
    """This is a function which will calculate average of two numbers
this function doesnt work for three numbers"""
    a = 23
    b = 6
    average = (a + b) / 2
    print(average)
    return average


print("Docstring :-")
print(function2.__doc__)

function2(23, 6)