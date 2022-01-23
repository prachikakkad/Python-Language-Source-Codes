class Dunder_Methods:

    def __init__(self , num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __len__(self):
        return 10

DM = Dunder_Methods(10)
print(f"Value in the form of String is :- {DM.__str__()}")
print(f"Length is :- {DM.__len__()}")