# Question :-
""" Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message."""

def make_shirt(size = "large" , text = "I love Python"):
    print(f"The size of the shirt is {size}.")
    print(f"The text to be printed on the shirt is {text}")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')