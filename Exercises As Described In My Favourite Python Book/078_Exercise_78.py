# Question :-
"""Start with the code given here :-
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)

Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you."""

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Prachi', 'Kakkad',
location='Upleta',
field='Coding and Programming',
Date_of_Birth = "4 December , 2007" ,
Dreams = "My dream is to meet my idols.")
print(user_profile)