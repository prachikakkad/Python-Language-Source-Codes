# Question :-
""" Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments. """

def make_shirt(size , text):
    print(f"The size of the shirt is {size}")
    print(f"The text to be printed on the shirt is {text}")

size_of_shirt = input("Enter the size of shirt :-\n")
text_to_print = input("Enter the text to be printed on shirt :-\n")

make_shirt(size_of_shirt , text_to_print)