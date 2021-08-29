# 7-1
car = input("What kind of car you like? ")
print(f"Let me see if I can find you a {car}")

# 7-2
num_people = int(input("How many people you have today? "))
if num_people >= 8:
    print(f"You have to wait.")
else:
    print(f"Your table is ready.")

# 7-3
num = int(input("Give me a number: "))
if num % 10 == 0:
    print(f"It is divisible by 10.")
else:
    print(f"It cannot divisible by 10.")

# 7-4
active = True
while active:
    topping = input("Please input topping(Type quit to exit): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Topping is: {topping}")

# 7-5
active = True
while active:
    age = input("What is your age? ")
    if age != 'quit':
        if int(age) < 3:
            print(f"Ticket is free.")
        elif int(age) < 12:
            print(f"Ticket is 10.")
        else:
            print(f"Ticket is 15")
    else:
        break

# 7-8
sandwich_orders = ['egg', 'becon', 'mixed', 'ham']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich made.")

# 7-9
finished_sandwiches = []
sandwich_orders = ['egg', 'becon', 'mixed', 'ham', 'pastrami', 'pastrami', 'pastrami']
print("Running out of pastrami sandwich.  Please remove them.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich made.")