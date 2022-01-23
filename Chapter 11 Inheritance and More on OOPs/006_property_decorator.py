class Employee:
    company = "Facebook"
    salary = 5600
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus


e = Employee()
print(f"Total :- {e.totalSalary}")
print(f"Salary :- {e.salary}")
print(f"Bonus :- {e.salarybonus}")