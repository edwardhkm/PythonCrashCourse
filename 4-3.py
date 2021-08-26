# 4-3
for num in range(1,21):
    print(num)

# 4-4
# for num in range(1, 1_000_001):
#     print(num)

# 4-5
nums = [num for num in range(1, 1000000)]
print(min(nums))
print(max(nums))
print(sum(nums))

# 4-6
odd_nums = list(range(1, 21, 2))
for num in odd_nums:
    print(num)

print(odd_nums)

# 4-7
m3 = [num * 3 for num in range(1,11)]
for m in m3:
    print(m)

# 4-8
cubes = [num ** 3 for num in range(1,11)]
for m in cubes:
    print(m)

# 4-9
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)