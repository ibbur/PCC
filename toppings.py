# Aaron Frankel 2019-7-6
# The purpose of this file is to learn and practise inequalities

requested_toppings = ['mushrooms', 'extra cheese']

if requested_toppings != 'anchovies':
    print("Hold the anchovies!\n")

# Page 87 of Python Crash Course returns to the file
# What follows is for learning about if-elif-else statements

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")

# The following stops after the first condition is met because
# we use an if-elif-else chain
# This is interest. I thought it only did this if there is an else block.
# But it does it regardless.

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making the pizza.\n")

# The following was added on 2019-7-16
# The purpose is to work with if statements and lists

# let's look at how you can watch for special values in a list and handle those values appropriately.

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nHello. Finished making your pizza.\n")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now. No peppers for you!")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza.\n")

# Checking to see if a list is empty
# Instead of jumping into a for loop, we do a quick check. When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to fales.
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?\n")

# Using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!\n")
