# Question :-
"""Create a class of pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog."""

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("The Dog is barking very loudly...")

d = Dog()
d.bark()