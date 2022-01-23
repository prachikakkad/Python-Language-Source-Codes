class Programmer:

    company = "Microsoft"
    salary = 1000000

    @classmethod
    def changeDetails(cls , sal , company):
        cls.salary = sal
        cls.company = company

p = Programmer()
print(f"Before Change :- {p.salary} , {p.company}")
p.changeDetails(5000000 , "Google")
print(f"After Change :- {p.salary} , {p.company}")