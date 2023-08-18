import sys
for _ in range(int(input())):
    n, k = map(int, input().split())
    ns = sorted([*map(int, sys.stdin.readline().split())])
    c = 0
    cn = 200000000
    for i in range(n):
        s, e = i+1, n-1
        while s <= e:
            mid = (s+e)//2
            x = ns[i]+ns[mid]
            if x > k:
                e = mid-1
            else:
                s = mid+1
            if abs(k-x) == cn:
                c += 1
            elif abs(k-x) < cn:
                cn = abs(k-x)
                c = 1
    print(c)