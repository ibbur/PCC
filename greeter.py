# Aaron Frankel 2019-7-20
# The purpose of this file is to learn about the input() fuction
# I'll use raw_input() since I'm running Python 2.7 and not 3

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = raw_input(prompt)
print("\nHello, " + name + "!")

age = raw_input("How old are you " + name + "? ")
age = int(age)
print(age >= 18)
