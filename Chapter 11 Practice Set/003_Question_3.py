# Question :-
"""Create a class Employee and add salary and increment properties to it. Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary."""

class Employee:
    salary = 1000000
    increment = 100000

    @property
    def Salary_After_Increment(self):
        return self.salary + self.increment
    
    @Salary_After_Increment.setter
    def Salary_After_Increment(self, value):
        self.increment = value - self.salary


e = Employee()
print(e.salary)
print(e.increment)
print(e.Salary_After_Increment)

e.salary = 5000000
e.increment = 100000

print()

print(e.salary)
print(e.increment)
print(e.Salary_After_Increment)