class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...")
    

p = Person()
e = Employee()
pr = Programmer()