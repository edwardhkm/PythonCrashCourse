"""A set of classes used to represent gas and electric cars."""
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        :param mileage:
        :return:
        """
        if self.odometer_readiing < mileage:
            self.odometer_readiing = mileage
        else:
            print(f"You cannot roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_readiing += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    # 9-9 new method
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        """Electric car don't have gas tanks."""
        print("This car doesn't need a gas tank!")
