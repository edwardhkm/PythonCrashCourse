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
