class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}, cuisine type is {self.cuisine_type}.")


    def open_restaurant(self):
        print(f"Restaurant is open.")

my_rest = Restaurant("Maxim's", "Chinese")
print(f"{my_rest.name}, {my_rest.cuisine_type}")
my_rest.open_restaurant()
my_rest.describe_restaurant()

# 9-2
my_rest = Restaurant("New HK", "Tea Restaurant")
my_rest2 = Restaurant("KFC", "Fast food")
my_rest3 = Restaurant("New LULU", "Japanese")
my_rest.describe_restaurant()
my_rest2.describe_restaurant()
my_rest3.describe_restaurant()

# 9-3
class User:
    def __init__(self, first_name, last_name, gender, username):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.username = username

    def describe_user(self):
        print(f"{self.username}, {self.first_name}, {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.username}!")

ed = User('ed', 'ho', 'M', 'HOED')
zoe = User('zoe', 'zhou', 'F', 'ZhoZ')

ed.greet_user()
zoe.greet_user()
ed.describe_user()
zoe.describe_user()