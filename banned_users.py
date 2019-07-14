# Aaron Frankel 2019-7-7
# The purpose of this file is to lear about the keyword not
#     and boolean expressions.

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")

print("\n_____ Boolean Test _____")
car = 'subaru'
print("Is car == 'subaru'? I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict fales.")
print(car == 'audi')

print("\n_____ My Boolean Test _____")

Truck = 'Avalanche'
SUV = 'XC90'
House = 'Glen Dell'
Pistol = 'G19'
Rifle = 'LMT MWS'
print("Is your truck an Avalanche? I predict yes.")
print(Truck == 'Avalanche')
print("Is Jen's SUV an XC90? I prerdict yes.")
print(SUV == 'XC90')
print("Is your mid-century on Glen Dell? I predict yes.")
print(House == "Glen Dell")
print("Is your EDC carry a G19? I predict yes.")
print(Pistol == 'G19')
print("Is your rifle a LMT MWS? I predict yes.")
print(Rifle == 'LMT MWS')

print("Is your truck a F150? I predict no.")
print(Truck == 'F150')
print("Is Jen's Volvo a XC60? I predict no.")
print(SUV == 'XC60')
print("Is Fort GDC on Woodhead? I predict no.")
print(House == 'Woodhead')
print("Is your daily carry a Nighthawk? I predict no.")
print(Pistol == 'Nighthawk')
print("Is your rifle a LaRue? I predict no.")
print(Rifle == 'LaRue')


dogs = ['barron','maggie','daisy']
print("\nIs the first dog in the list named Barron? I predict true.")
print(dogs[0] == 'barron')
print("Is the second dog in the list Maggie or Daisy? I predict true.")
print(dogs[1] == 'maggie') or (dogs[1] == 'daisy')
print("Is Barron in the list? I predict yes.")
print('barron' in dogs)
print("Is Daisy in the list? I predict yes.")
print('daisy' in dogs)
print("Is Maggie in the list? I predict yes.")
print('maggie' in dogs)

print("\nIs Maggie not in the list? I predict no.")
if 'maggie' not in dogs:
    print('True')
else:
    print('False')
print("Is George the ferret in the dogs list? I predict no.")
print('george' in dogs)
print("Are George the ferret and Mike the lizzard in the list? I predict no.")
print('george' in dogs) and ('mike' in dogs)
print("Are George the ferret or Mike the lizzard in the list? I predict no.")
print('george' in dogs) or ('mike' in dogs)

print("\n")
