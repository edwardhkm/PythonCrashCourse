# 6-1
Zoe = {'lastname':'Zhou', 'firstname':'Zoe', 'city':'Sydney',
       'title':'Data engineer', 'company': 'CBA'}
print(Zoe)

for att in Zoe:
    print(f"{att}")

# 6-2
favorite_nums = {'zoe':1, 'ed':8, 'lee':9, 'ben':10, 'jo':11}
for num in favorite_nums:
    val = favorite_nums.get(num)
    print(f"{num}, {val}")

# 6-3
programming_words = {'for':'for', 'in': 'in', 'print':'printing', 'if':'if', 'else':'else'}
for word in programming_words:
    print(f"{word} = {programming_words.get(word)}.")

