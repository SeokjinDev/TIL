n, m = map(int, input().split())
ns = sorted([*map(int, input().split())])
ans = []
def dfs(x, l, r):
    global ans
    if l == 0:
        ans.append(r)
        return
    for i in range(x, n):
        dfs(i, l-1, r+[ns[i]])
dfs(0, m, [])
for an in ans:
    for a in an: print(a, end=' ')
    print()