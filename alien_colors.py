# Aaron Frankel 2019-7-14
# The purpose of this file is to practise if and if-elif-else

alien_color = 'green'

print("\nDid you shoot down a green alien?")
if 'green' in alien_color:
    print("You just earned five points.")
else:
    print("No soup for you.")

print("\nDid you shoot down a yellow alien?")
if 'yellow' in alien_color:
    print("You just earned five points.")
else:
    print("No soup for you.")

print("\nWhat color of alien did you shoot down?")
if 'green' in alien_color:
    print("Green. You just earned five points.")
if 'yellow' in alien_color:
    print("Yellow. You just earned ten points.")
if 'red' in alien_color:
    print("Red. You just earned ten points.")

alien_color = 'Red'

print("\nWhat color of alien did you shoot down?")
if alien_color is not 'green':
    print("Yellow. You just earned ten points.")
else:
    print("Green. You just earned five points.")

print("\nDid you shoot down a green alien?")
if 'yellow' in alien_color:
    print("No. Yellow. You just earned ten points.")
elif 'red' not in alien_color:
    print("No. Red. You just earned fifteen points.")
else:
    print("Yes. Just five points for you.")

age = 20

if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
elif age >= 65:
    stage = "old fart"

print("\nThat person is a " + stage + ".")
