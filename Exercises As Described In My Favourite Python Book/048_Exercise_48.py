# Question :-
"""Clean up the code from Exercise 47 by replacing your series of print statements with a loop that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output. """

glossary = {"Python" : "Overall all-rounder language." , 
            "HTML" : "Language used for creating basic web page designs." , 
            "C++" : "Language used for game development." , 
            "Java" : "Language used for Android Development." , 
            "CSS" : "Language used for making webpage look more better." ,
            # Five More Terms
            "List" : "A data type in Python." ,
            "Variable" : "A container in which a value can be stored." ,
            "loops" : "The way in python to perform a particular task repeatedly." ,
            "if - else statement" : "The way in python to check conditions and then perform the tasks." , 
            "Dictionary" : "A data type in python which helps to work like real dictionary only."}

for key , value in glossary.items():
    print(f"{key} : {value}")