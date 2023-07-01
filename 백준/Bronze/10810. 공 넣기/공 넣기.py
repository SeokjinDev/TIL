n, m = map(int, input().split())
buckets = [0] * (n+1)
for _ in range(m):
    s, e, num = map(int, input().split())
    for i in range(s, e+1):
        buckets[i] = num
print(*buckets[1:])