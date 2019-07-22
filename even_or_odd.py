# Aaron Frankel 2019-7-21
# The purpose of this file is to learn about the modulo operator (%)

#
# 

number = raw_input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
