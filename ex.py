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
