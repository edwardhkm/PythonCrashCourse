# 3-4
guests = ['jo', 'jj', 'ee', 'dd']
print(f"Please come to dinner, {guests[1].title()}")

# 3-5
not_come = guests.pop(0)
print(f"{not_come} one is not coming over.")
guests.insert(0, "kk")
print(f"{guests} are all coming")

# 3-6
print(guests)
guests.insert(0, "yy")
guests.insert(3, "nn")
guests.append("ll")
print(f"{guests} are all coming")

# 3-7
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
print(f"only {guests} are allow to come")
del guests[0]
del guests[0]
print(f"my guest list is {guests}")