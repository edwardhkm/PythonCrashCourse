# 9-1, 9-4
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 9-4

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}, cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Restaurant is open.")

    def set_number_served(self, num_customers):
        self.number_served = num_customers

    def increment_number_served(self, increase_customer):
        self.number_served += increase_customer


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

# 9-3, 9-5
class User:
    def __init__(self, first_name, last_name, gender, username):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.username}, {self.first_name}, {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.username}!")

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

ed = User('ed', 'ho', 'M', 'HOED')
zoe = User('zoe', 'zhou', 'F', 'ZhoZ')

ed.greet_user()
zoe.greet_user()
ed.describe_user()
zoe.describe_user()

ben = User('ben', 'turner', 'M', 'bent')
ben.increment_login_attempts()
ben.increment_login_attempts()
ben.increment_login_attempts()
print(f"Ben's login attempts: {ben.login_attempts}.")
ben.reset_login_attempts()
print(f"Now reset Ben's login attempts, and it becomes {ben.login_attempts}.")


# 9-4
restaurant = Restaurant('OldMac', 'fast food')
print(f"Number of customer served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number of customer served: {restaurant.number_served}")
restaurant.set_number_served(20)
print(f"Number of customer served: {restaurant.number_served}")
restaurant.increment_number_served(30)
print(f"Number of customer served: {restaurant.number_served}")


# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def get_flavors(self):
        print(f"Flavors: {self.flavors}")


flavors = ['choco', 'vanilla']
ic = IceCreamStand('bao', 'ice cream stand')
ic.flavors = flavors
ic.get_flavors()

# 9-7, 9-8
class Privileges:
    def __init__(self, privileges):
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")

class Admin(User):
    def __init__(self, first, last, gender, username):
        super().__init__(first, last, gender, username)
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        pp = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges(pp)

    # def show_privileges(self):
    #     print(f"Admin privileges: {self.privileges}")

admin = Admin('aa', 'bbc', 'M', 'adminn')
admin.privileges.show_privileges()
admin.describe_user()