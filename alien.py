# Aaron Frankel 2019-7-17
# The purpose of this file is to learn the basics of dictionaries

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + "!")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x_position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
alien_0['color'] = 'green'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\nNext x-position: " + str(alien_0['x_position']) + "\n")

print("\n")
print(alien_0)

print("\n")
alien_0['points'] = 5
print(alien_0)

print("\n")
del alien_0['points']
print(alien_0)
