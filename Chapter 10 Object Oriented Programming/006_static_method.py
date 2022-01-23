class Employee:
    company = "Google"
    salary = 1000000
    
    def getSalary(self):
        print(f"Prachi's salary is {self.salary}")
    
    @staticmethod  
    def greet(): # Here I used static method because I don't wanted to use self in this function
        print("Hello dear !")


Prachi = Employee()
Employee.getSalary(Prachi) # is same as Prachi.getSalary()
Prachi.greet()