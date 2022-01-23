class Employee:
    company = "Google"

    def showcompany(self):
        print(f"The company name is {self.company}")

class Programmer(Employee):
    language = "Python"

    def showlanguage(self):
        print(f"The language is {self.language}")

e = Employee()
p = Programmer()

print("Call using Employee Class :-")
e.showcompany()

print()

print("Call using Programmer Class :-")
p.showcompany()