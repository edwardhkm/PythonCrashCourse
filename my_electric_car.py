from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# print(my_tesla.battery.battery_size)
my_tesla.battery.get_range()