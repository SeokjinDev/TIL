n, m = map(int, input().split())
ns = sorted([*map(int, input().split())])
ans = {}
def dfs(start, l, seq):
    if l == 0:
        s = ' '.join(map(str, seq))
        if ans.get(s) is None:
            ans[s] = 1
        return
    for i in range(start, n):
        dfs(i, l-1, seq+[ns[i]])
for i in range(n):
    dfs(i, m, [])
for a in ans.keys():
    print(a)