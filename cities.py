# Aaron Frankel 2019-7-22
# The purpose of this file is to learn about using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = raw_input(prompt)

    if city == 'quit':
        print("Bye.\n")
        break
    else:
        print("I'd love to go to " + city.title() + "!")
