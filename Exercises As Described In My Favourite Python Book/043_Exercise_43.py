# Question :-
"""Do the following to create a program that simulates how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted."""

current_users = ["naveen_kumar_goyat" , "prachi_kakkad" , "shreeja_shukla" , "rahul_vaidya" , "siddharth_shukla"]

new_users = ["naveen_kumar_goyat" , "prachi_kakkad" , "technical_duo" , "bro_sis" , "family_life"]

current_users_lower = [user.lower() for user in current_users]

for users in new_users:
    if  users.lower() in current_users_lower:
        print(f"{users} have to enter a new username. This username is not available.")
    
    else:
        print(f"{users} is a VALID username. It is available.")