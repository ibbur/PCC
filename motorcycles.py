    # Aaron Frankel 2019-6-20
    # The purpose of this file is to learn how to modify lists.
    # I'm trying to get better about commentting my code.

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

    # Here we'll learn how to modify a list item.
    # This will change a list item at a specific position.
motorcycles[0] = 'ducati'
print(motorcycles)

    # Here we'll learn how to append a list.
    # This will add the appended item to the end of the list.
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

motorcycles=[]
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

    # Here we'll learn how to add an item to a list at a specific position.
    # This will use the list made in lines 16 - 20

motorcycles.insert(0, 'ducati')
print(motorcycles)

    # Here we'll learn how to remove an item from a list.
    # We'll use the del statement because the position is known.
    # We'll use the existing list.
del motorcycles[0]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

    # Here we'll rebuild the list to follow the exercise and for extra practise
motorcycles.insert(0, 'honda')
print(motorcycles)

    # Here we'll remove an item from another position
del motorcycles[1]
print(motorcycles)

    # Add it all back again
motorcycles.insert(1, 'yamaha')
print(motorcycles)

    # Here we'll learn to use the pop method
    # This first line pops the item out and stores the popped item in a variable.
    # The pop method removes the last item in the list.
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print("Put the popped item back in. ---")
    # Put the popped item back
motorcycles.insert(2, 'suzuki')
print(motorcycles)

last_owned = motorcycles.pop()
print ("The last motorcycle I owned was a " + last_owned.title() + ".")
print(motorcycles)

print("Put the popped item back in... again. --- ")
motorcycles.insert(2, 'susuki')
print(motorcycles)

    # You can use pop() to remove an item in a list at any positing by including the index of the item you want to remove in parentheses.

first_owned = motorcycles.pop(0)
print ('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

print("Put the popped item back in. --- ")
motorcycles.insert(0, 'honda')
print(motorcycles)

print("Add ducati back in for the exercise.")
motorcycles.append('ducati')

print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
