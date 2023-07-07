from itertools import combinations
n, s = map(int, input().split())
nums = [*map(int, input().split())]

count = 0
for i in range(n):
    for j in combinations(nums, i+1):
        if sum(j) == s:
            count += 1
print(count)