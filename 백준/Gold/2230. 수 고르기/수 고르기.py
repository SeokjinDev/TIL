import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])

s, e = 0, 1
ans = 2000000000
while s < n and e < n:
    t = nums[e] - nums[s]
    if t == m:
        print(m)
        exit()
    if t < m:
        e += 1
    else:
        s += 1
        ans = min(ans, t)
print(ans)