n = int(input())
ls = sorted([*map(int, input().split())])
ans, res = 2000000001, []
for i in range(n-1):
    now = ls[i]
    s, e = i+1, n-1
    while s <= e:
        mid = (s+e)//2
        nex = ls[mid]
        tem = now+nex
        if abs(tem) < ans:
            ans = abs(tem)
            res = [now, nex]
            if tem == 0: break
        if tem < 0: s=mid+1
        else: e=mid-1
print(res[0], res[1])