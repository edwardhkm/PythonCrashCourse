import json
filename = "favorite_numbers.json"
with open(filename) as f:
    contents = f.read()
    print(f"I know your favorite number! It's {contents}.")