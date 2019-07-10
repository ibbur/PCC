# Aaron Frankel 2019-7-9
# The purpose of this file is to work with conditional tests

desk = ['imac','speakers','bunnies','picture','vape','costers']
computer = 'Apple'
user = 'aaron'
ring_holder = 'bunnies'
bedrooms = '3'
sqft = '3400'

if ring_holder != 'one bunny':
    print("\nIt's two " + ring_holder + " kissing. How cute!")

print("\nIs your computer an Apple iMac? I predict yes.")
print(computer.lower() == 'apple')

print("\nIs your name Aaron? I predict true.")
print(user.lower() == 'aaron')

print("\nYour name is not Bob. I predict true.")
print(user.lower() != 'bob')

print("\nYour name is Bob. I predict false.")
print(user.lower() == 'bob')

print("\n")
print(bedrooms == '3')
print(bedrooms != '2')
print(sqft == '3400')
print(sqft != '3300')
print(bedrooms >= '3')
print(bedrooms <= '4') or (sqft <= '3500')
print(bedrooms >= '2') and (sqft >= '3400')

if ring_holder in desk:
    print("\nThe " + ring_holder.lower() + " ring holder is in the list.\n")

if user not in desk:
    print(user.title() + " is not on the list. You're not sitting on the desk.")
