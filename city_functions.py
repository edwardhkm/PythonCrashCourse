def city_country(city, country, population=0):
    if population:
        full_name = f"{city}, {country} - population {population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()