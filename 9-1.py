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