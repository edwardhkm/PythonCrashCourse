# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


active = True
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while active:
    message =  input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
# while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

