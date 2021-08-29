# 6-4
programming_words = {'for': 'for loop', 'in': 'in for loop', 'print': 'printing', 'if': 'if-else', 'elif': 'else-if'}
for k, v in programming_words.items():
    print(f"{k}, {v}")



# 6-5
rivers = {'nile': 'egypt', 'china': 'yellow river', 'america': 'missisipi'}
for k, v in rivers.items():
    print(f"The {v} runs through {k}")
for k in rivers.keys():
    print(k)
for v in rivers.values():
    print(v)

# 6-6

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for k, v in favorite_languages.items():
    print(f"{k}:{v}")

# 6-7
Zoe = {'lastname':'Zhou', 'firstname':'Zoe', 'city':'Sydney',
       'title': 'Data engineer', 'company': 'CBA'}
ed = {'lastname':'Ho', 'firstname':'Edward', 'city':'Sydney',
      'title': 'Data Analyst', 'company': 'NESA'}
lee = {'lastname':'Adamson', 'firstname':'Lee', 'city':'Sydney',
       'title': 'Data Analyst', 'company': 'MQ'}

people = [ed, lee, Zoe]

for human in people:
    print(f"{human}")

# 6-8 Pets
dog = {'name': 'on dog dog', 'owner': 'ed' }
cat = {'name': 'on 99', 'owner': '4'}
pets = [dog, cat]
for pet in pets:
    print(f"{pet}")

# 6-9 Favorite Places
favorite_places = {'jo': ['tokyo', 'hk', 'sydney'],
                   'ed': ['chatswood', 'lai chi kok', 'shatin'],
                   'baobao': ['willoughby', 'tong chung', 'mong kok'],
                   }
for name, places in favorite_places.items():
    print(f"{name} favorite places are:")
    for place in places:
        print(f"\t{place}")

# 6-11
print("question 6-11")
cities = {'hk': {'population': 7000000, 'language': 'cantonese'},
          'tokyo': {'population': 10000000, 'language': 'japanese'},
          'sydney': {'population': 5000000, 'language': 'english'},
          }
for city, facts in cities.items():
    print(f"{city.title()}")
    for fact, value in facts.items():
        print(f"\t{fact}: {value}")