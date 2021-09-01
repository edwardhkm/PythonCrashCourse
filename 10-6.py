# 10-6
# x = input("Please input x: ")
# y = input("Please input y: ")
#
# try:
#     val = int(x)+int(y)
# except ValueError:
#     print("Either x or y is not a number.")

# 10-7
# active = True
# while active:
#     x = input("Please input x: ")
#     y = input("Please input y: ")
#
#     try:
#         val = int(x) + int(y)
#     except ValueError:
#         print("Either x or y is not a number.")
#     else:
#         print(f"x+y is {int(x)+int(y)}")

# 10-8
filenames = ['cats.txt','dogs.txt', 'pigs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.readlines()
            print(f"{filename} contains {contents}")
    except FileNotFoundError:
        # print(f"{filename} not found.") # 10-8
        pass # 10-9

# 10-10
filename = 'alice.txt'
with open(filename) as f:
    contents = f.read()
    num_words = contents.lower().count('the ')
    print(f"'the ' count is {num_words}.")

