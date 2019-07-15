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
