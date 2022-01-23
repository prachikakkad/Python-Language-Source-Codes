# Question :-
"""Write a python function to remove a given word from a list and strip
it at the same time."""


def remove_and_split(string, word):
    new_string = string.replace(word, "")
    return new_string.strip()


this = "   Prachi is a good girl   "
n = remove_and_split(this, "Prachi")
print(n)
# print(this)
# print(this.strip())
