# Question :-
""" Start with Exercise 48 , where you used a standard dictionary to represent a glossary. Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary. """

from collections import OrderedDict

glossary = OrderedDict()

glossary["Python"] = "Overall all-rounder language."
glossary["HTML"] = "Language used for creating basic web page designs."
glossary["C++"] = "Language used for game development."
glossary["Java"] = "Language used for Android Development."
glossary["CSS"] = "Language used for making webpage look more better."
glossary["List"] = "A data type in Python."
glossary["Variable"] = "A container in which a value can be stored."
glossary["loops"] = "The way in python to perform a particular task repeatedly."
glossary["if - else statement"] = "The way in python to check conditions and then perform the tasks."
glossary["Dictionary"] = "A data type in python which helps to work like real dictionary only."

for word , meaning in glossary.items():
    print(f"{word} : {meaning}")