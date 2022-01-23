# Question :-
"""Write a program to find out whether a given post is
talking about “Harry” or not."""

text = '''Harry Potter In the past couple years, there has been a growing phenomenon in the world of children's 
literature, this phenomenon is Harry Potter. J.K. Rowlings series of novels about a young wizard and his years at "
Hogwarts School of Warding and Witchcraft," has become one of the most successful children's book series of 
all time. '''
name = "harry"
if name.lower() in text.lower():
    print("They are talking about Harry")
else:
    print("They are talking about someone else")