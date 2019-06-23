    # Aaron Frankel 2019-6-22
    # The purpose of this file is to learn more about working with lists
    # This set of exercises focus on organization of lists
    # I will print messages often instead of commenting code
    # I like the way printing messages breaks up the text in Terminal
    # However, I do get the point about comminting code
    # But it is redundant when printing messages to the terminal

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nOur new list...")
print(cars)
sorting = "Doing the sorting thing... "
print(sorting)
cars.sort()
print(cars)

print("\nWe will now sort in reverse order using an argument with sort(). ")
print("It is important to capitalize true in reverse=True.")
print(sorting)
cars.sort(reverse=True)
print(cars)

print("\nWe will now return the list to the original order for the exercise.")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print("\nWe will now use the sorted() method to temporarily sort the list.")
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print("\nWe will now use sorted, but reverse the order")
print("\nHere's the original list:")
print(cars)
print("\nHere's the reverse sorted list:")
# The damn author didn't show the code for reversing the sorted() functions.
# It is not the same for the sorted() function as it is for the sort() method.
# Thankfully, the answer was a quick search away.
print(sorted(cars, reverse=True))
print("\nHere's the original list again:")
print(cars)

print("\nI'm getting hungry. This is unrelated to the exercise.")

print("\nWe will now use the reverse() method to reverse the list item order.")
print("Here is the current order:")
print(cars)
print(sorting)
cars.reverse()
print("\nHere is the reversed order:")
print(cars)

print("\nWe will now reverse the order back to the original.")
print(sorting)
cars.reverse()
print("Here is the resorted list:")
print(cars)

print("\nNow let's use the len() function.")
# The damn author didn't include the print code and I had to go look it up.
# Perhaps he thinks I now know enough to know how to form this without telling.
print(len(cars))
