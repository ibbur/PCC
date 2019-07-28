# Aaron Frankel 2019-7-27
# The purpose of this file is practise removing items from a list
#   with a while loop

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(sorted(pets))

print("Exterminate the cats:")
while 'cat' in pets:
    pets.remove('cat')

print("\nThe cats should now be exterminated:")
print(sorted(pets))
