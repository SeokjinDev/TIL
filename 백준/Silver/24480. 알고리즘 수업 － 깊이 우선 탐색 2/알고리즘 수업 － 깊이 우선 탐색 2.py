import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)
idx = 1
def dfs(r):
    global visited, graph, idx
    visited[r] = idx
    idx += 1
    for g in sorted(graph[r], reverse=True):
        if visited[g] == 0:
            dfs(g)
    return

dfs(r)
for i in visited[1:]:
    print(i)