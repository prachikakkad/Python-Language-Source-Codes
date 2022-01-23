# Question :-
"""Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways."""

class Train:

    def __init__(self , name , status , fare):
        self.name = name
        self.status = status
        self.fare = fare

    def booking(self):
        if self.status > 0:
            print(f"Congratulations ! Your seat is booked ! Your seat number is {self.status}")
            self.status = self.status - 1
        else: 
            print("Sorry ! The train is full !")

    def seats(self):
        print(f"The name of Train is {self.name}")
        print(f"The Number of seats available are {self.status} ")

    def fareInfo(self):
        print(f"The price of the seat of this train is {self.fare}")

a = Train("Rajdhani Express" , 230 , 100)
a.booking()
a.seats()
a.fareInfo()