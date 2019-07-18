# Aaron Frankel 2019-7-17
# The purpose of this file is to learn about looping through a dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key.title())
    print("Value: " + value.title())
