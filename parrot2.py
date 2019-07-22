prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = raw_input(prompt)
    if message.lower() == 'quit':
        print("Quitting. Y'all come back now, ya hear. Bye.")
    else:
        print("\n" + message.title())
