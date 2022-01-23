class Employee:
    company = "Google"
    salary = 1000000
    
    def getSalary(self):
        print(f"Prachi's salary is {self.salary}")

Prachi = Employee()
Employee.getSalary(Prachi) # is same as Prachi.getSalary()