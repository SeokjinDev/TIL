n, m = map(int, input().split())
ans = []
def dfs(x, l, r):
    global ans
    if l == 0:
        ans.append(r)
        return
    for i in range(x, n+1):
        dfs(i, l-1, r+[i])
dfs(1, m, [])
for an in ans:
    for a in an: print(a, end=' ')
    print()