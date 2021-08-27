cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print("\nThis is the original list")
print(cars)
print("\nThis is reverse sorted()")
print(sorted(cars, reverse=True))
print("\nThis is car list")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print(len(cars))


cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "Audi"
print(car.lower())
print(car)

