# Question :-
"""Write a class calculator capable of finding square, cube, and the square root of a number."""

class calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"The square of {self.number} is {self.number * self.number}")

    def squareroot(self):
        print(f"The square root of {self.number} is {self.number ** 0.5}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number * self.number * self.number}")

    @staticmethod
    def greet():
        print("Hello User !")

calculator.greet()

number = int(input("Enter a number and this program will find square , square root and cube for you of that number :- \n"))

num = calculator(number)

num.square()

num.squareroot()

num.cube()