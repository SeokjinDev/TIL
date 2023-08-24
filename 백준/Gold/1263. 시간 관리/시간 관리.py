n = int(input())
li = sorted([[*map(int, input().split())] for _ in range(n)], reverse=True, key=lambda x: x[1])
c = 1000000
for i in range(n):
    t, s = li[i]
    c = min(c, s)
    c = c - t
if c < 0:
    print(-1)
else:
    print(c)