# Aaron Frankel 2019-7-14
# The purpose of this file is to learn about if-elif-else statements

print("\n____ If-elif-else Statements ____")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# More concise to set just he price inside the if-elif-else chain
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("\nYour admission cost is $" + str(price) + ".")

# Using multiple if-elif-else statements
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")

# Using all elif statements instead of ending the test with an else
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")
