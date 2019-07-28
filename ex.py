prompt = "Let's make a pizza. Enter toppings. Enter done when complete."
prompt += "\nToppings: "

active = True
while active:
    toppings = raw_input(prompt)

    if toppings.lower() == "done":
        print("Rodger dodger. Making the pizza.")
        active = False
        break
    else:
        print("Adding " + toppings.lower() + " to your weird pizza.")

print("\nWhile looping with lists ____ ")

list_one = ['dog','cat','bird']
list_two = []

while list_one:
    item = list_one.pop()

    print("Moving item " + item)
    list_two.append(item)

print("Items from list two:")
for item in list_two:
    print("\t- " + item)
