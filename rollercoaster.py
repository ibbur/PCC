# Aaron Frankel 2019-7-21
# The purpose of this file is to learn about the int() function

name = raw_input("\nWhat's your name? ")
height = raw_input("\nHow tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride, " + name + "!")
else:
    print("\nYou'll be able to ride when you're a little older, " + name + ".")
