players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:3])

print(players[1:4])
print(players[1:5])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[0::2])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
