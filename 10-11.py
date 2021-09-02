import json

filename = "favorite_numbers.json"
num = input("What is your favourite num? ")
with open(filename, 'w') as f:
    f.write(num)


