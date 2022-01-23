class Employee:

    def details(self):
        company = "Google"
        name = "Prachi"
        print("detail function :-")
        print(company)
        print(name)

class Programmer:

    def name(self):
        name = "Coder"
        print("name function :-")
        print(name)

class Manager(Employee , Programmer):

    def full_name(self):
        full_name = "Prachi Kakkad"
        print("full_name function :-")
        print(full_name)

m = Manager()

m.details()
print()

m.name()
print()

m.full_name()
print()