# Question :-
"""Create a class programmer for storing information of a few programmers working at Microsoft."""

class Programmer:
    company = "Microsoft"

    def __init__(self , name , salary , software , mobile_number):
        self.name = name
        self.salary = salary
        self.software = software
        self.mobile_number = mobile_number

    def Information(self):
        print(f"The name of {self.company} Programmer is {self.name}.\nThe salary of Programmer is {self.salary}.\nThe software in which Programmer works is {self.software}.\nThe mobile number of Programmer is {self.mobile_number}")
        print("\n")
        

Prachi = Programmer("Prachi" , 1000000 , "Visual Studio Code" , 9426253654)


Shreeja = Programmer("Shreeja" , 100000 , "Microsoft Word" , 7309258722)


Harry = Programmer("Harry" , 10000 , "Microsoft Power Point" , 5968568963)


Tejal = Programmer("Tejal" , 1000 , "Microsoft Edge" , 4515842635)


Rohan = Programmer("Rohan" , 100 , "Microsoft Store" , 8963215647)
 
 
Prachi.Information()
Shreeja.Information()
Harry.Information()
Tejal.Information()
Rohan.Information()