from random import randint, choice
print(randint(1, 6))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# 9-13
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        side = randint(1, self.sides)
        return side

die_6 = Die(6)
print(die_6.roll_die())

# 9-14
