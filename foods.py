# Aaron Frankel 2019-7-5
# The purpose of this file is to learn about copying a list.

print("\n")

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

print("My favorite foods using a for loop are are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods using a for loop are are:")
for food in friend_foods:
    print(food)

print("\n")
print("\n")
print("\n")
