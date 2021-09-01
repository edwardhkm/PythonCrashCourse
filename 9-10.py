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
lottery_items = [0,1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd', 'e']
lottery_items2 = [0,1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd', 'e']
for item in lottery_items2:
    print(item)
print(f"Random choice is: {choice(lottery_items2)}")

lottery = ""
for x in range(4):
    lottery += str(choice(lottery_items2))
print(f"The lottery ticket is: {lottery}")

# 9-15
my_ticket = '1234'
not_win = True
not_win_count = 0
while not_win:
    for x in range(4):
        lottery += str(choice(lottery_items2))
    if lottery != my_ticket:
        not_win_count += 1
    else:
        print(f"total number of try: {not_win_count}")
        not_win = False



