visits = ['hk', 'sydney', 'japan', 'thailand', 'usa']
print(visits)
print(sorted(visits))
print(visits)
print(sorted(visits, reverse=True))
print(visits)
visits.reverse()
print(visits)
visits.reverse()
print(visits)
visits.sort()
print(visits)
visits.sort(reverse=True)
print(visits)

# 3-9
guests = ['jo', 'jj', 'ee', 'dd']
print(guests)
print(f"number of guest is {len(guests)}.")

def createFunction():
    guests = ['jo', 'jj', 'ee', 'dd']
    guests.append("oo")
    print(guests)

createFunction()