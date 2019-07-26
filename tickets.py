# Aaron Frankel 2019-7-25
# The purpose of this file is to work with while loops

prompt = "Enter your age for ticket pricing. Enter '0' when satisfied."
prompt += " Age? "

active = True
while active:
    age = raw_input(prompt)
    if age.lower() == "done":
        print("Bye.")
        active = False
        break
    age = int(age)

    if age <= 3:
        print("Tickets for age 3 and under are FREE.")
    elif age <= 12:
        print("Tickets for age 4 - 12 are $10.")
    elif age <= 64:
        print("Ticket prices for age 13 - 64 are $15.")
    elif age > 64:
        print("Senior ticket prices are $5.")
