# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)
# # print("----")
# print(contents.rstrip())
# print("----")

# filename = 'pi_digits.txt'
filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))
# print(f"{pi_string[:20]}")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")
