#5-8
usernames = ['ed', 'sam', 'lee', 'zoe', 'ben', 'admin']

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello, {user}, thank you for logging in again.")

# 5-9
usernames = []
if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello, {user}, thank you for logging in again.")
else:
    print(f"We need to find some users!")


# 5-10
current_users = ['ed', 'sam', 'lee', 'zoe', 'ben', 'admin']
new_users = ['jo', 'lala', 'SAM', 'Lee', 'ak']

for new_user in new_users:
    # temp_users = current_users[:]
    temp_users = [current_user.lower() for current_user in current_users]

    if new_user.lower() in temp_users:
        print(f"{new_user} is used.  Please select another.")
    else:
        print(f"{new_user} is available.")

# 5-11
nums = list(range(1,10,1))
print(nums)
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")

test = [11, 'test']
print(test)