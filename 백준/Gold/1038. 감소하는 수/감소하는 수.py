from itertools import combinations
n = int(input())
nums = []
for i in range(10):
    for c in combinations(range(10), i+1):
        c = map(str, sorted([*c], reverse=True))
        c = int("".join(c))
        nums.append(c)
nums.sort()
try:
    print(nums[n])
except:
    print(-1)