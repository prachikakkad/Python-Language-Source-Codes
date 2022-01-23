class Employee:
    company = "Facebook"
    salary = 5600
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self , value):
        self.salarybonus = value - self.salary

e = Employee()
print(f"Total Before Change:- {e.totalSalary}")
print(f"Salary Before Change :- {e.salary}")
print(f"Bonus Before Change :- {e.salarybonus}")
e.salary = 6000
e.salarybonus = 4000
print(f"Total After Change:- {e.totalSalary}")
print(f"Salary After Change :- {e.salary}")
print(f"Bonus After Change :- {e.salarybonus}")
