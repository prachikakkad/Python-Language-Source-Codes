class Employee:
	company = "Google" 	# Specific to each class
Prachi = Employee()	# Object instantiation
print(Employee.company) # Prints Google as the company variable of class Employee is initialized to Google
Employee.company = "YouTube" # changing class attribute
print(Employee.company) # Prints YouTube as the company variable of class Employee is changed from Google to YouTube during the program