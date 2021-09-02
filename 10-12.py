import json
import os.path

filename = "favorite_numbers.json"
if not os.path.isfile(filename):
    num = input("What is your favourite num? ")
    with open(filename, 'w') as f:
        f.write(num)
else:
    with open(filename) as f:
        contents = f.read()
        print(f"I know your favorite number! It's {contents}.")