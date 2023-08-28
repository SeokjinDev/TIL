n, m = map(int, input().split())
ns = sorted([*map(int, input().split())])
ans = []
def dfs(l, r):
    global ans
    if l == 0:
        ans.append(r)
        return
    for i in range(0, n):
        if ns[i] not in r:
            dfs(l-1, r+[ns[i]])
dfs(m, [])
for an in ans:
    for a in an: print(a, end=' ')
    print()