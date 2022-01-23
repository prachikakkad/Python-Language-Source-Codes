class Person:
    country = "India"

    def takeBreath1(self):
        print("Class Person")

class Employee(Person):
    company = "Honda"
    
    def takeBreath2(self):
        print("Class Employee")

class Programmer(Employee):
    company = "Fiverr"
    
    def takeBreath3(self):
        print("Class Programmer")

p = Person()
e = Employee()
pr = Programmer()

p.takeBreath1()
e.takeBreath2()
pr.takeBreath3()

p.takeBreath1()

e.takeBreath2()
e.takeBreath1()

pr.takeBreath3()
pr.takeBreath2()
pr.takeBreath1()