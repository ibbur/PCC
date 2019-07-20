# Aaron Frankel 2019-7-17
# The purpose of this file is to learn about looping through a dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key.title() + "\nValue: " + value.title())

# Revisiting per page 111 of PCC

user_1 = {
    'username': 'nasty',
    'first': 'jannet',
    'last': 'jackson',
    }
user_2 = {
    'username': 'johnp',
    'first': 'johnny',
    'last': 'paradise',
    }
user_3 = {
    'username': 'themclovin',
    'first': 'Sam',
    'last': 'mclovin'
}

users = [user_0, user_1, user_2, user_3,]

for user in users:
    print(user)
