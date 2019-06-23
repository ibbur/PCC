    # Aaron Frankel 2019-6-22
    # The purpose of this file is to exercies my list skills to this point.
    # This is the second version of the file so I can practice again.
    # I will print extra messages instead of using commints.

guests = ['dad', 'pappaw', 'ben']
    # It's too bad guests=guests.title() doesn't work. It would elliminate bloat.
print(guests)

invitation = ", please join us for a small dinner party. "
print("\n" + guests[0].title() + invitation)
print("\n" + guests[1].title() + invitation)
print("\n" + guests[2].title() + invitation)

print("\n" + guests[2].title() + " will not be able to make it. A new guest will be invited.")
guests[2] = ('morty')
print("\nA guest has changed. " + guests[2].title() + " is now being invited.")
print("\n" + guests[2].title() + invitation)
may = " may join us."
print("\n" + guests[0].title() + invitation + guests[2].title() + may)
print("\n" + guests[1].title() + invitation + guests[2].title() + may)

print("\nWe just received word from the book author we're getting more seats.")
print("We will now add to the list and invite more guests!")

guests.insert(3, 'shausha')
guests.insert(4, 'gemmaw')
guests.append('joe')
print("\nThe list now consists of...")
print(guests)
print("We will now invite the new additions to the list.")

print("\n" + guests[3].title() + invitation)
print("\n" + guests[4].title() + invitation)
print("\n" + guests[5].title() + invitation)
newthree = (guests[3].title() + ", " + guests[4].title() + ", and " + guests[5].title() + ". ")
print("\n" + guests[0].title() + ", we're also inviting " + newthree)

# The next two lines are added per exercise 3-9.
print("\n______How many guests are on the list?______")
print(len(guests))

print("\nThe author informed us we've lost four of our six seats.")
sorry = ", the jerk author took away seats. We'll rechedule a new party soon. "
popped = guests.pop()
print("\n" + popped.title() + sorry)
print(guests)
popped = guests.pop()
print("\n" + popped.title() + sorry)
print(guests)
popped = guests.pop()
print("\n" + popped.title() + sorry)
print(guests)
popped = guests.pop()
print("\n" + popped.title() + sorry)
print(guests)

print("\n" + guests[0].title() + " and " + guests[1].title() + ", you are still invited.")

print("\nThe shady author cancelled our party. Shame. Removing all guests.")
del guests[1]
del guests[0]
print(guests)
