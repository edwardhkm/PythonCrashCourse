# 8-12
def accept_sandwiches(*sandwich_items):
    print(sandwich_items)

accept_sandwiches('ham', 'egg', 'vege', 'burger', 'leg ham')
accept_sandwiches('vege', 'sadin', 'becon')
accept_sandwiches('mayo', 'jam')

# 8-13 User profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('ed', 'ho', language = 'python', location = 'hk', gender = 'male', body = 'fat')

print(user_profile)

# 8-14 Cars
def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car_spec = make_car('honda', 'crx', cylinda=4, gas_type='unlead', doors = 2)
print(car_spec)


