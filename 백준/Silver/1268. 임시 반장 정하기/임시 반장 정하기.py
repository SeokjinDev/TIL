import sys
inp = sys.stdin.readline
t = int(inp())
b = [[*map(int, inp().split())] for _ in range(t)]
f = {i: set() for i in range(t)}
[f[i].add(k) or f[k].add(i) for i in range(t) for j in range(5) for k in range(i+1, t) if b[i][j] == b[k][j]]
cnt = [len(f[i]) for i in range(t)]
print(cnt.index(max(cnt))+1)