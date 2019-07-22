# Aaron Frankel 2019-7-20
# The purpose of this file is to learn about input()

# message = raw_input("Tell me something, and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
# while message != 'quit':
#     message = raw_input(prompt)
#     if message.lower() == 'quit':
#         print("Quitting. Y'all come back now, ya hear. Bye.")
#     else:
#         print("\n" + message.title())

active = True
while active:
    message= raw_input(prompt)

    if message.lower() == 'quit':
        active = False
    else:
        print(message.title())
