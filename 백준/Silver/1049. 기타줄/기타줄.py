from math import inf
n, m = map(int, input().split())
six, one = inf, inf
for _ in range(m):
    s, o = map(int, input().split())
    if six > s: six = s
    if one > o: one = o
ans = 0
ans += (n // 6) * min(six, 6*one)
ans += min(six, (n%6)*one)
print(ans)