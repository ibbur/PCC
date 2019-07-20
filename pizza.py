# Aaron Frankel 2019-6-25
# The purpose of this file is to learn about the for loop

pizzas = ['pepporoni', 'deep dish', 'starburt']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print("\nI enjoy " + pizza + " pizza.")

print("\n" + pizzas[0].title() + " is great. The classic I grew up with.")
print(pizzas[1].title() + " is my favorite style now. Regular is ok. I'm just not a fan of thin crust.")
print(pizzas[2].title() + " is my all time favorite pizza. I could eat it every day.")

print("\nJennifer really loves pizza. She might like it more than I do!")

print("\n")

friend_pizzas = pizzas[:-1]
friend_pizzas.append('chicken')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# Added 2019-7-18 per page 111 of PCC
# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
    }

# Summarize the order.
print("\nYou ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t-" + topping)
