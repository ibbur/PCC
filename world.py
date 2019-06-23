# Aaron Frankel 2019-6-23
# The purpose of this file is to exercise sorting lists

places = ['costa rica', 'aruba', 'alaska', 'israel', 'germany' ]
print("Here are our places to visit:")
print(places)

print("\nLet's sort the list...")
print("Here's the list sorted alphabetically:")
print(sorted(places))
print("\nHere is the list again to show the sort is not permanently:")
print(places)

print("\nWe will now sort the list in reverse order temporarily...")
print(sorted(places, reverse=True))
print("The list order to show not permanet:")
print(places)

print("\nWe will now sort the list in reverse order permanently...")
places.reverse()
print("Here is the list reversed:")
print(places)

print("\nLet's reverse the list again to put it back in original order...")
places.reverse()
print("Here is the list:")
print(places)

print("\nWe will now sort the list alphabetically and permanently...")
places.sort()
print("Here's the sorted list:")
print(places)

print("\nLast action.")
print("We will now sort the list in reverse alphabetical order...")
places.sort(reverse=True)
print("Here's the list:")
print(places)
