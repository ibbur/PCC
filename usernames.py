# Aron Frankel 2019-7-16
# The purpose of this file is to practise with multiple lists and if statements

users = ['admin', 'aaron', 'jonas', 'barron', 'maggie', 'daisy']

request = 'Aaron'

if request.lower() not in users:
    print("\nYou are not authorized " + request.title() + ".")
else:
    print("\nWelcome back, " + request.title() + ". Access granted.\n")

request = 'Bob'

if request.lower() not in users:
    print("\nYou are not authorized, " + request.title() + ". Get lost!\n")
else:
    print("\nWelcome back, " + request.title() + ". Access granted.\n")

for user in users:
    if user.lower() not in users:
        print("\nYou are not authorized, " + user.title() + ". Get lost!\n")
    elif user.lower() == "admin":
        print("\nWelcome back, " + user.title() + ". Would you like a status report? Perhaps a hooker and blow?\n")
    elif user.lower() == "barron":
        print("\nWelcome back, " + user.title() + ". Access granted and a dog biscuit for you.\n")
    elif user.lower() == "maggie":
        print("\nWelcome back, " + user.title() + ". Access granted and a dog biscuit for you.\n")
    elif user.lower() == "daisy":
        print("\nWelcome back, " + user.title() + ". Access granted and a dog biscuit for you.\n")
    else:
        print("\nWelcome back, " + user.title() + ". Access granted.\n")

del users[:]

if users:
    for user in users:
        print("\nHowdy, " + user.title() + ".")
else:
    print("\nWe need some users!")

print("_____ Check Two Lists _____")

current_users = ['TERRIE', 'jan', 'sarah', 'jason', 'jennifer']
new_users = ['terrie', 'lon', 'Jason', 'martha', 'morty']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("\n" + user.title() + " is not available for use.")
    else:
        print("\n" + user.title() + " is available.")

numbers = list(range(1,11))
print(numbers)

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

numbers = list(range(1,11))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
