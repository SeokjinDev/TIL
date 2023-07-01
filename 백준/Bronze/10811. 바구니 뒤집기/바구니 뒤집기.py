n, m = map(int, input().split())
buckets = [*range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    buckets[s:e+1] = buckets[e:s-1:-1]
print(*buckets[1:])