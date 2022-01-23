# Question :-
""" Write a program to greet all the person names stored in a list1 and which starts with S.
list1 = [“Harry”, “Sohan”, “Sachin”, “Rahul”] """

list1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in list1:
    if name.startswith("S"):
        print("Hello", name)