# Aaron Frankel 2019-6-23
# The purpose of this file is to demonstrate each function learned in lists

list=['apple', 'speakers', 'mouse', 'keyboard', 'rabbit', 'picture','scale','book', 'camera','coaster','water']
print(list)

print("\nUse the sorted function...")
print(sorted(list))

print("\nuse the sorted function in reverse...")
print(sorted(list, reverse=True))

print("\nShow list...")
print(list)

print("\nUse the sort method...")
list.sort()
print(list)

print("\nReverse the sort method...")
list.sort(reverse=True)
print(list)

print("\nShow the first item in the list...")
print(list[0].title() + " is the first item in the list.")

print("\nAdd to the end of the list...")
list.append('cable')
print(list)

print("\nAdd to the second location in the list.")
list.insert(1, 'phone')
print(list)

print("\nModify the first item in the list.")
list[0] = 'bottle'
print(list)

print("\nDelete the first item in the list.")
del list[0]
print(list)

print("\nPop an item from the list, show the popped item, and show the list.")
popped = list.pop()
print(popped.title() + " was popped.")

print("\nPop off an item at a specific index.")
popped = list.pop(1)
print(popped.title() + " was popped off.")

print("\nRemove an item you don't konw the position of.")
list.remove('mouse')
print(list)
print("Mouse was removed.")

print("\nSort the list.")
list.sort()
print(list)

print("\nHow many items are in the list now?")
print(len(list))

print("\nWe will now clear some of the list.")
del list[0]
list.remove('coaster')
list.remove('phone')
list.remove('rabbit')
print(list)
print("\nThere are this many items in the list now:")
print(len(list))

list.insert(4, "rabbit")

print("\nWrite a statement about each item remaining on the list.")
print(list)
print("A " + list[0] + " is sitting to my right.")
print("A " + list[1] + " is on the shelf.")
print("A " + list[2] + " is what I use to enter text and commands.")
print("A " + list[3] + " of Jen and I sits in front of my iMac.")
print("A " + list[4] + " holds my ring and sits next to the " + list[3] + ".")
print("An Arch " + list[5] + " rests in front of me.")

print("\nLet's clear the list using all the functions and methods.")
del list[0]
print(list)
del list[1]
print(list)
list.pop()
print(list)
list.remove("picture")
print(list)
list.pop(1)
print(list)
del list[0]
print("\nAll gone...")
print(list)
