# Aaron Frankel 2019-7-18
# The purpose of this file is to learn about nesting

alien_0 = {'color': 'green', 'points': 5,}
alien_1 = {'color': 'yellow', 'points': 10,}
alien_2 = {'color': 'red', 'points': 15,}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\nMaking aliens...")
# Make an empty list for storying aliens.
aliens = []

# Make 30 greens aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens " + str(len(aliens)))

print("\nLevel 2...")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# Just showing a elif
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print("...")

print("\nLevel 3...")

for alien in aliens[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print("...")
