import sys
input = sys.stdin.readline
n, m = map(int, input().split())
jud = [int(input()) for _ in range(n)]
s, e = 0, jud[0]*m
while s <= e:
    mid = (s+e)//2
    t = sum([mid//jud[i] for i in range(n)])
    if t < m:
        s = mid+1
    else:
        e = mid-1
print(s)