name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is you first name? "

name = input(prompt)
print(f"Hello, {name}!")

age = int(input("How old are you? "))
#print(type(age))
if age > 18:
    msg = "You are adult."
else:
    msg = "You are kid."
print(msg)