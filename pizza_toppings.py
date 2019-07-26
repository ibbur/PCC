# Aaron Frankel 2019-7-25
# The purpose of this file is to work with while loops

prompt = "Enter a topping. Enter 'done' when finished."
prompt += "\nTopping: "

active = True
while active:
    topping = raw_input(prompt)

    if topping.lower() == 'done':
        print("Got it. We'll start making the pizza with your selections.")
        active = False
        break
    else:
        print("Adding " + topping.lower() + " to your order.")
