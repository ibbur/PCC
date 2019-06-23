# Aaron Frankel 2019-6-23
# The purpose of this file is to exercise sorting lists

places = ['costa rica', 'aruba', 'alaska', 'israel', 'germany' ]
print("Here are our places to visit:")
print(places)

print("Let's sort the list...")
print("Here's the list sorted alphabetically:")
print(sorted(places))
print("\nHere is the list again to show the sort is not permanent:")
print(places)

print("\nWe will now sort the list in reverse order temporarily...")
print(sorted(places, reverse=True))
