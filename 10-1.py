# 10-1
filename = "learning_python.txt"
with open(filename) as file_object:
    ppp = file_object.read()

print(ppp)
print("-----")
with open(filename) as f_object:
    for ll in f_object:
        print(ll.rstrip())
print("-----")
with open(filename) as f_object:
    lll = f_object.readlines()

for ll in lll:
    print(ll.strip())

print("--- 10-2 ---")
# 10-2
message = "I really like dogs."
message.replace('dog', 'cat')
file_name = "learning_python.txt"
with open(file_name) as f_object:
    lines = f_object.readlines()
    for line in lines:
        print("-- Original line --")
        print(line)
        print("-- Replace with Java --")
        msg = line.replace('Python', 'Java').strip()
        print(msg)
        print("--- Replace with Java in single line...")
        print(line.strip().replace('Python', 'Java'))
        # print(line)


# 10-3
filename = "guestname.txt"
with open(filename, 'w') as f_object:
    active = True
    while active:
        guest_name = input("Input guest name(press q to quit): ")
        if guest_name != 'q':
            f_object.write(f"{guest_name}\n")
        else:
            active = False

# 10-4
filename = "guest_book.txt"
print("Please sign guest book.\n")
with open(filename, 'w') as f_object:
    active = True
    while active:
        guest_name = input("Input guest name(press q to quit): ")
        if guest_name != 'q':
            print(f"Greeting, {guest_name}!")
            f_object.write(f"{guest_name}\n")
        else:
            active = False

# 10-5
active = True
print(f"Please write reason why you love programming.")
filename = "programming_poll.txt"
with open(filename, 'w') as f_object:
    while active:
        response = input("Your reason: ")
        if response != 'q':
            f_object.write(f"{response}\n")
        else:
            active = False

