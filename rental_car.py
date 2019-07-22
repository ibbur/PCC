# Aaron Frankel 2019-7-21
# The purpose of this file is to learn about working with

name = raw_input("\nWhat's your name? ")
car = raw_input("\nWhat kind of rental car would you like? ")

print("\nLet me see if I can find you a " + car + ", " + name + ".")

seating = raw_input("\nHow many people will be joing you for dinner " +
    name + "? ")
seating = int(seating)
seating += 1
if seating >= 8:
    print(str(seating) + " total. There will be a short wait for a table, " +
    name + ".")
else:
    print(str(seating) + ".Your table is read, " + name
    + ". Vallet will park your " + car + ".")
