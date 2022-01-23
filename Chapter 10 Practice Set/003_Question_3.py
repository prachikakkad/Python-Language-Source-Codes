# Question :-
"""Create a class with a class attribute a; create an object from it and set a directly using object. a = 0 Does this change the class attribute ?"""
# Answer :- 
# No , it will not change the class attribute. Instead , it will create a new instance attribute

class check:
    a = 0

obj = check()
obj.a = 6
print(obj.a)
print(check.a)