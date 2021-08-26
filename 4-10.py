# 4-10
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(f"The first 3 items in the list are : {my_foods[:3]}")

print(f"Three items from the middle of the list are: {my_foods[3:]}")
print(f"The last three items in the list are: {my_foods[-3:]}")

# 4-11
pizzas = ['Hawaii', "Meat lover", "Vege", "tradition", "BBQ Meats Deluxe", "Garlic Chicken"]
friend_pizzas = pizzas[:]
pizzas.append("Alo")
friend_pizzas.append("Bacon")
print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(f'\t{pizza}')
print(f'My friend favorite pizzas are:')
for pizza in friend_pizzas:
    print(f'\t{pizza}')

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append("ice cream")
for food in my_foods:
    print(food)
print("\n")
for food in friend_foods:
    print(food)
