# Question :-
""" You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests. Have at least one True and one False result for each of the following:
•	 Tests for equality and inequality with strings
•	 Tests using the lower() function
•	 Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list """

string_1 = "Naveen Kumar"
string_2 = "Naveen kumar"
print(string_1 == string_2)

print(string_1.lower() == string_2.lower())

number_1 = 21
number_2 = 15

print(number_1 == number_2)
print(number_1 != number_2)
print(number_1 > number_2)
print(number_1 < number_2)
print(number_1 >= number_2)
print(number_1 <= number_2)

list = ["Naveen Kumar" , "Prachi Kakkad"]
print("Papa" not in list)
print("Naveen Kumar" in list)