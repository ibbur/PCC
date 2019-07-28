# Aaron Frankel 2019-7-27
# The purpose of this file is to learn about using a while loop for
#   working with lists and dictionaires.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print("\n____ Does what you expect to happen occur? ____")

for part in confirmed_users:
    print("Confirmed: ")
    print("\t- " + part)
for part in unconfirmed_users:
    print("Confirmed: ")
    print("\t- " + part)
