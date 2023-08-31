n, m = map(int, input().split())
ns = sorted([*map(int, input().split())])
ans = {}
def dfs(l, sequence, tmp):
    global ans
    if l == 0:
        seq = ' '.join(map(str, sequence))
        if ans.get(seq) is None:
            ans[seq] = 1
        return
    for i in range(n):
        if i not in tmp:
            dfs(l-1, sequence+[ns[i]], tmp+[i])
for i in range(n):
    dfs(m, [], [])
for a in ans.keys():
    print(a)